#coding=utf-8

#初始化
from leap import *
from leap.message_def import *
from leap.ittimsg_def import *
from leap.command_def import *
from leap.leapmessage_def import *
from leap.func import *
buf_size = 4096

#建立连接
le = leap("192.168.137.99", "7897")

while True:
    #接收消息
    message_id, ue_id, length, msg = le.recv(buf_size)
    
    #改变流程
    if message_id == LEAP_ITTI_MSG:
        le.hold(True)
    
    #用户自定义
    elif message_id == LEAP_INITIAL_NAS_DATA:
        nas_msg = le.nas_message_decode(msg)     
        message_type = nas_msg.contents.header.message_type
        if message_type == ATTACH_REQUEST:
            imsi = pointer(nas_msg.contents.attach_request.oldgutiorimsi.imsi)
            ppstruct(imsi)
    
    else:
        le.exit_loop()
