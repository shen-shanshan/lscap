# -*- coding:UTF-8 -*-

"""
说明：
1.本文件为从客户端发送到服务端的 leap_command 的定义
"""

from ctypes import *

# 指令类型
EXIT_LOOP = -1
# HOLD_FALSE = 0
# HOLD_TRUE = 1
IMSI_CATCHING = 1
# GET_EMM_SECURITY_CONTEXT = 2
# GET_EMM_PROC_COMMON_GET_ARGS = 3
SET_AND_SEND_ATTACH_REJECT = 4
# NAS_ITTI_DL_DATA = 5
# NAS_ITTI_PLAIN_MSG = 6
# NAS_PROC_ESTABLISH_IND = 7
# NAS_INITIAL_ATTACH_PROC = 8
SET_AND_SEND_AUTHENTICATION_REJECT = 9
SEND_NETWORK_INITIATED_DETACH_REQUEST = 10
AUTH_SYNC_FAILURE_ATTACK = 11
# PAGING_CHANNEL_HIJACKING = 12
STEALTHY_KICKING_OFF_ATTACK = 13
SET_AND_SEND_TAU_REJECT = 14
SET_AND_SEND_IDENTITY_REQUEST = 15


# 指令格式
class leap_command_t(Structure):

    def __str__(self):
        s = []
        for k in self._fields_:
            if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
                s.append("\"%s\":%s" % (k[0], getattr(self, k[0])))
            else:
                s.append("\"%s\":\"%s\"" % (k[0], getattr(self, k[0])))
        return '{%s}' % (','.join([i for i in s]))

    _fields_ = [
        ('command_id', c_ubyte),
        ('ue_id', c_ubyte),
        ('cause', c_ubyte),
        ('length', c_ubyte),
    ]
