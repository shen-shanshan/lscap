#ifndef SRSEPC_TCPSERVER_H
#define SRSEPC_TCPSERVER_H

#include "srsepc/hdr/mme/nas.h"
#include "srsepc/hdr/mme/s1ap.h"
#include "srsran/interfaces/epc_interfaces.h"

typedef signed   char int8_t_leap;
typedef unsigned char uint8_t_leap;

namespace srsepc {

  #define buf_size 4096

  // message id
  #define LEAP_ITTI_MSG                   0
  #define LEAP_INITIAL_NAS_DATA           1
  #define LEAP_EMM_SECURITY_CTX           2
  #define LEAP_EMM_PROC_COMMON_GET_ARGS   3
  #define LEAP_EMM_SAP_MSG                4
  #define LEAP_SEC_MODE_COMMAND_NAS_DATA  5
  #define LEAP_SECURITY_MODE_COMMAND      6
  #define LEAP_WAIT_COMMAND               7
  #define LEAP_AUTH_FAILURE               8
  #define LEAP_ATTACH_COMPLETE            9
  #define LEAP_TAU_REQUEST               10

  // command id
  #define EXIT_LEAP_LOOP                        -1
  #define HOLD_FALSE                             0
  #define HOLD_TRUE                              1
  #define GET_EMM_SECURITY_CONTEXT               2
  #define GET_EMM_PROC_COMMON_GET_ARGS           3
  #define SET_AND_SEND_ATTACH_REJECT             4 // dos attack
  #define NAS_ITTI_DL_DATA                       5
  #define NAS_ITTI_PLAIN_MSG                     6
  #define NAS_PROC_ESTABLISH_IND                 7
  #define NAS_INITIAL_ATTACH_PROC                8
  #define SET_AND_SEND_AUTHENTICATION_REJECT     9 // numb attack
  #define SEND_NETWORK_INITIATED_DETACH_REQUEST 10 // detach/downgrade attack
  #define AUTH_SYNC_FAILURE_ATTACK              11 // auth sync failure attack
  #define PAGING_CHANNEL_HIJACKING              12 // paging channel hijacking attack
  #define STEALTHY_KICKING_OFF_ATTACK           13 // stealthy kicking-off attack
  #define SET_AND_SEND_TAU_REJECT               14 // dos attack
  #define SET_AND_SEND_IDENTITY_REQUEST         15 // imsi catching

  // functions
  int   leap_send_only(int assocfd, uint8_t_leap message_id, uint8_t_leap ue_id, char* sendBuf, int size);
  int   leap_send(int assocfd, uint8_t_leap message_id, uint8_t_leap ue_id, char* sendBuf, int size);
  int   leap_recv_only(int assocfd, char* recvBuf, int size, int flag);
  int   leap_recv(int assocfd, char* recvBuf, int size, int flag);
  int   leap_loop();
  int   leap_wait_command();
  void* _leap_wait_command(void* p);
  void  tcp_init();
  void* tcpproc(void* p);
  void* communicate_with_client(void* arg);

  typedef struct {
    int8_t_leap  command_id;
    uint8_t_leap ue_id;
    uint8_t_leap cause;
    uint8_t_leap length;
    char         message[0];
  } leap_command_t;

  typedef struct {
    uint8_t_leap message_id;
    uint8_t_leap ue_id;
    uint8_t_leap length;
    char         message[0];
  } leap_message_t;

  typedef struct leap_info_s {
    // message id
    int leap_message_id;

    // s1ap_nas_transport.cc 
    // handle_initial_ue_message():
    char*                   leap_nas_msg;
    int                     leap_nas_msg_size;
    int                     leap_enb_ue_s1ap_id;
    struct sctp_sndrcvinfo* leap_enb_sri;
    nas_init_t              leap_m_nas_init;
    nas_if_t                leap_m_nas_if;
    uint64_t                leap_imsi;
    uint8_t                 leap_eps_bearer_id;

    // nas.cc
    // handle_imsi_attach_request_unknown_ue():
    nas*                    leap_nas_ctx;
    s1ap_interface_nas*     leap_s1ap;
  } leap_info_t;

} // namespace srsepc
#endif // SRSEPC_TCPSERVER_H