  //Python take over
  char tcp_msg[] = "ATTACH_REQUEST from imei:";
  strcat(tcp_msg,itoa(ue_id));
  send(accsocfd,tcp_msg,strlen(tcp_msg),0); //change to strlen()?
  recv(accsocfd, recvBuf, 100, 0);
  if(!strcmp("1",recvBuf)){   //if python take over, break.
    ue_ctx.emm_cause = EMM_CAUSE_IMEI_NOT_ACCEPTED;  //change to custom configure later
    rc = _emm_attach_reject (&ue_ctx);
    OAILOG_FUNC_RETURN (LOG_NAS_EMM, rc);
  }