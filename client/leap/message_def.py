# -*- coding: utf-8 -*-
# 3gpp 24.301


#==============================================================================
# 9 General message format and information elements coding
#==============================================================================

#------------------------------------------------------------------------------
# 9.2 Protocol discriminator
#------------------------------------------------------------------------------

# 9.3.1 Security header type
SECURITY_HEADER_TYPE_NOT_PROTECTED                    = 0b0000
SECURITY_HEADER_TYPE_INTEGRITY_PROTECTED              = 0b0001
SECURITY_HEADER_TYPE_INTEGRITY_PROTECTED_CYPHERED     = 0b0010
SECURITY_HEADER_TYPE_INTEGRITY_PROTECTED_NEW          = 0b0011
SECURITY_HEADER_TYPE_INTEGRITY_PROTECTED_CYPHERED_NEW = 0b0100
SECURITY_HEADER_TYPE_SERVICE_REQUEST                  = 0b1100
SECURITY_HEADER_TYPE_RESERVED1                        = 0b1101
SECURITY_HEADER_TYPE_RESERVED2                        = 0b1110
SECURITY_HEADER_TYPE_RESERVED3                        = 0b1111

# 9.3.2 EPS bearer identity
# see 24.007

#------------------------------------------------------------------------------
# 9.8 Message type
#------------------------------------------------------------------------------
# Table 9.8.1: Message types for EPS mobility management
# Message identifiers for EPS Mobility Management     #
ATTACH_REQUEST                                       = 0b01000001 # 65 = 0x41 #
ATTACH_ACCEPT                                        = 0b01000010 # 66 = 0x42 #
ATTACH_COMPLETE                                      = 0b01000011 # 67 = 0x43 #
ATTACH_REJECT                                        = 0b01000100 # 68 = 0x44 #
DETACH_REQUEST                                       = 0b01000101 # 69 = 0x45 #
DETACH_ACCEPT                                        = 0b01000110 # 70 = 0x46 #
TRACKING_AREA_UPDATE_REQUEST                         = 0b01001000 # 72 = 0x48 #
TRACKING_AREA_UPDATE_ACCEPT                          = 0b01001001 # 73 = 0x49 #
TRACKING_AREA_UPDATE_COMPLETE                        = 0b01001010 # 74 = 0x4a #
TRACKING_AREA_UPDATE_REJECT                          = 0b01001011 # 75 = 0x4b #
EXTENDED_SERVICE_REQUEST                             = 0b01001100 # 76 = 0x4c #
SERVICE_REJECT                                       = 0b01001110 # 78 = 0x4e #
GUTI_REALLOCATION_COMMAND                            = 0b01010000 # 80 = 0x50 #
GUTI_REALLOCATION_COMPLETE                           = 0b01010001 # 81 = 0x51 #
AUTHENTICATION_REQUEST                               = 0b01010010 # 82 = 0x52 #
AUTHENTICATION_RESPONSE                              = 0b01010011 # 83 = 0x53 #
AUTHENTICATION_REJECT                                = 0b01010100 # 84 = 0x54 #
AUTHENTICATION_FAILURE                               = 0b01011100 # 92 = 0x5c #
IDENTITY_REQUEST                                     = 0b01010101 # 85 = 0x55 #
IDENTITY_RESPONSE                                    = 0b01010110 # 86 = 0x56 #
SECURITY_MODE_COMMAND                                = 0b01011101 # 93 = 0x5d #
SECURITY_MODE_COMPLETE                               = 0b01011110 # 94 = 0x5e #
SECURITY_MODE_REJECT                                 = 0b01011111 # 95 = 0x5f #
EMM_STATUS                                           = 0b01100000 # 96 = 0x60 #
EMM_INFORMATION                                      = 0b01100001 # 97 = 0x61 #
DOWNLINK_NAS_TRANSPORT                               = 0b01100010 # 98 = 0x62 #
UPLINK_NAS_TRANSPORT                                 = 0b01100011 # 99 = 0x63 #
CS_SERVICE_NOTIFICATION                              = 0b01100100 # 100 = 0x64 #
DOWNLINK_GENERIC_NAS_TRANSPORT                       = 0b01101000 # 104 = 0x68 #
UPLINK_GENERIC_NAS_TRANSPORT                         = 0b01101001 # 101 = 0x69 #


# Table 9.8.2: Message types for EPS session management
ACTIVATE_DEFAULT_EPS_BEARER_CONTEXT_REQUEST          = 0b11000001 # 193 = 0xc1 #
ACTIVATE_DEFAULT_EPS_BEARER_CONTEXT_ACCEPT           = 0b11000010 # 194 = 0xc2 #
ACTIVATE_DEFAULT_EPS_BEARER_CONTEXT_REJECT           = 0b11000011 # 195 = 0xc3 #
ACTIVATE_DEDICATED_EPS_BEARER_CONTEXT_REQUEST        = 0b11000101 # 197 = 0xc5 #
ACTIVATE_DEDICATED_EPS_BEARER_CONTEXT_ACCEPT         = 0b11000110 # 198 = 0xc6 #
ACTIVATE_DEDICATED_EPS_BEARER_CONTEXT_REJECT         = 0b11000111 # 199 = 0xc7 #
MODIFY_EPS_BEARER_CONTEXT_REQUEST                    = 0b11001001 # 201 = 0xc9 #
MODIFY_EPS_BEARER_CONTEXT_ACCEPT                     = 0b11001010 # 202 = 0xca #
MODIFY_EPS_BEARER_CONTEXT_REJECT                     = 0b11001011 # 203 = 0xcb #
DEACTIVATE_EPS_BEARER_CONTEXT_REQUEST                = 0b11001101 # 205 = 0xcd #
DEACTIVATE_EPS_BEARER_CONTEXT_ACCEPT                 = 0b11001110 # 206 = 0xce #
PDN_CONNECTIVITY_REQUEST                             = 0b11010000 # 208 = 0xd0 #
PDN_CONNECTIVITY_REJECT                              = 0b11010001 # 209 = 0xd1 #
PDN_DISCONNECT_REQUEST                               = 0b11010010 # 210 = 0xd2 #
PDN_DISCONNECT_REJECT                                = 0b11010011 # 211 = 0xd3 #
BEARER_RESOURCE_ALLOCATION_REQUEST                   = 0b11010100 # 212 = 0xd4 #
BEARER_RESOURCE_ALLOCATION_REJECT                    = 0b11010101 # 213 = 0xd5 #
BEARER_RESOURCE_MODIFICATION_REQUEST                 = 0b11010110 # 214 = 0xd6 #
BEARER_RESOURCE_MODIFICATION_REJECT                  = 0b11010111 # 215 = 0xd7 #
ESM_INFORMATION_REQUEST                              = 0b11011001 # 217 = 0xd9 #
ESM_INFORMATION_RESPONSE                             = 0b11011010 # 218 = 0xda #
ESM_STATUS                                           = 0b11101000 # 232 = 0xe8 #

#------------------------------------------------------------------------------
# 9.9 OTHER INFORMATION ELEMENTS
#------------------------------------------------------------------------------

#..............................................................................
#9.9.3 EPS Mobility Management (EMM) information elements
#..............................................................................

#9.9.3.34 UE network capability
UE_NETWORK_CAPABILITY_MINIMUM_LENGTH = 4
UE_NETWORK_CAPABILITY_MAXIMUM_LENGTH = 15


  # EPS encryption algorithms supported (octet 3) #
UE_NETWORK_CAPABILITY_EEA0  = 0b10000000
UE_NETWORK_CAPABILITY_EEA1  = 0b01000000
UE_NETWORK_CAPABILITY_EEA2  = 0b00100000
UE_NETWORK_CAPABILITY_EEA3  = 0b00010000
UE_NETWORK_CAPABILITY_EEA4  = 0b00001000
UE_NETWORK_CAPABILITY_EEA5  = 0b00000100
UE_NETWORK_CAPABILITY_EEA6  = 0b00000010
UE_NETWORK_CAPABILITY_EEA7  = 0b00000001

  # EPS integrity algorithms supported (octet 4) #
UE_NETWORK_CAPABILITY_EIA0  = 0b10000000
UE_NETWORK_CAPABILITY_EIA1  = 0b01000000
UE_NETWORK_CAPABILITY_EIA2  = 0b00100000
UE_NETWORK_CAPABILITY_EIA3  = 0b00010000
UE_NETWORK_CAPABILITY_EIA4  = 0b00001000
UE_NETWORK_CAPABILITY_EIA5  = 0b00000100
UE_NETWORK_CAPABILITY_EIA6  = 0b00000010
UE_NETWORK_CAPABILITY_EIA7  = 0b00000001

  # UMTS encryption algorithms supported (octet 5) #
UE_NETWORK_CAPABILITY_UEA0  = 0b10000000
UE_NETWORK_CAPABILITY_UEA1  = 0b01000000
UE_NETWORK_CAPABILITY_UEA2  = 0b00100000
UE_NETWORK_CAPABILITY_UEA3  = 0b00010000
UE_NETWORK_CAPABILITY_UEA4  = 0b00001000
UE_NETWORK_CAPABILITY_UEA5  = 0b00000100
UE_NETWORK_CAPABILITY_UEA6  = 0b00000010
UE_NETWORK_CAPABILITY_UEA7  = 0b00000001

  # UCS2 support (octet 6, bit 8) #
UE_NETWORK_CAPABILITY_DEFAULT_ALPHABET  = 0
UE_NETWORK_CAPABILITY_UCS2_ALPHABET = 1

  # UMTS integrity algorithms supported (octet 6) #
UE_NETWORK_CAPABILITY_UIA1  = 0b01000000
UE_NETWORK_CAPABILITY_UIA2  = 0b00100000
UE_NETWORK_CAPABILITY_UIA3  = 0b00010000
UE_NETWORK_CAPABILITY_UIA4  = 0b00001000
UE_NETWORK_CAPABILITY_UIA5  = 0b00000100
UE_NETWORK_CAPABILITY_UIA6  = 0b00000010
UE_NETWORK_CAPABILITY_UIA7  = 0b00000001

  # Bits 8 to 6 of octet 7 are spare and shall be coded as zero #

  # eNodeB-based access class control for CSFB capability #
UE_NETWORK_CAPABILITY_CSFB  = 1

  # LTE Positioning Protocol capability #
UE_NETWORK_CAPABILITY_LPP = 1

  # Location services notification mechanisms capability #
UE_NETWORK_CAPABILITY_LCS = 1

  # 1xSRVCC capability #
UE_NETWORK_CAPABILITY_SRVCC = 1

  # NF notification procedure capability #
UE_NETWORK_CAPABILITY_NF  = 1

  #uint8_t spare[0..8]



#9.9.3.36 UE security capability
UE_SECURITY_CAPABILITY_MINIMUM_LENGTH = 4
UE_SECURITY_CAPABILITY_MAXIMUM_LENGTH = 7

  # EPS encryption algorithms supported (octet 3) #
UE_SECURITY_CAPABILITY_EEA0 = 0b10000000
UE_SECURITY_CAPABILITY_EEA1 = 0b01000000
UE_SECURITY_CAPABILITY_EEA2 = 0b00100000
UE_SECURITY_CAPABILITY_EEA3 = 0b00010000
UE_SECURITY_CAPABILITY_EEA4 = 0b00001000
UE_SECURITY_CAPABILITY_EEA5 = 0b00000100
UE_SECURITY_CAPABILITY_EEA6 = 0b00000010
UE_SECURITY_CAPABILITY_EEA7 = 0b00000001
  # EPS integrity algorithms supported (octet 4) #
UE_SECURITY_CAPABILITY_EIA0 = 0b10000000
UE_SECURITY_CAPABILITY_EIA1 = 0b01000000
UE_SECURITY_CAPABILITY_EIA2 = 0b00100000
UE_SECURITY_CAPABILITY_EIA3 = 0b00010000
UE_SECURITY_CAPABILITY_EIA4 = 0b00001000
UE_SECURITY_CAPABILITY_EIA5 = 0b00000100
UE_SECURITY_CAPABILITY_EIA6 = 0b00000010
UE_SECURITY_CAPABILITY_EIA7 = 0b00000001

  # UMTS encryption algorithms supported (octet 5) #
UE_SECURITY_CAPABILITY_UEA0 = 0b10000000
UE_SECURITY_CAPABILITY_UEA1 = 0b01000000
UE_SECURITY_CAPABILITY_UEA2 = 0b00100000
UE_SECURITY_CAPABILITY_UEA3 = 0b00010000
UE_SECURITY_CAPABILITY_UEA4 = 0b00001000
UE_SECURITY_CAPABILITY_UEA5 = 0b00000100
UE_SECURITY_CAPABILITY_UEA6 = 0b00000010
UE_SECURITY_CAPABILITY_UEA7 = 0b00000001

  # UMTS integrity algorithms supported (octet 6) #
UE_SECURITY_CAPABILITY_UIA1 = 0b01000000
UE_SECURITY_CAPABILITY_UIA2 = 0b00100000
UE_SECURITY_CAPABILITY_UIA3 = 0b00010000
UE_SECURITY_CAPABILITY_UIA4 = 0b00001000
UE_SECURITY_CAPABILITY_UIA5 = 0b00000100
UE_SECURITY_CAPABILITY_UIA6 = 0b00000010
UE_SECURITY_CAPABILITY_UIA7 = 0b00000001

  # GPRS encryption algorithms supported (octet 7) #
UE_SECURITY_CAPABILITY_GEA1 = 0b01000000
UE_SECURITY_CAPABILITY_GEA2 = 0b00100000
UE_SECURITY_CAPABILITY_GEA3 = 0b00010000
UE_SECURITY_CAPABILITY_GEA4 = 0b00001000
UE_SECURITY_CAPABILITY_GEA5 = 0b00000100
UE_SECURITY_CAPABILITY_GEA6 = 0b00000010
UE_SECURITY_CAPABILITY_GEA7 = 0b00000001


#------------------------------------------------------------------------------
# 10.2 Timers of EPS mobility management
#------------------------------------------------------------------------------

#..............................................................................
# Table 10.2.1: EPS mobility management timers – UE side
#..............................................................................

T3402_DEFAULT_VALUE          = 720
T3410_DEFAULT_VALUE           = 15
T3411_DEFAULT_VALUE           = 10
T3412_DEFAULT_VALUE         = 3240
T3416_DEFAULT_VALUE           = 30
T3417_DEFAULT_VALUE            = 5
T3417_EXT_DEFAULT_VALUE       = 10
T3420_DEFAULT_VALUE           = 15
T3421_DEFAULT_VALUE           = 15
T3423_DEFAULT_VALUE            = 0   # value provided by network
T3440_DEFAULT_VALUE           = 10
T3442_DEFAULT_VALUE            = 0   # value provided by network

#..............................................................................
# Table 10.2.2: EPS mobility management timers – network side
#..............................................................................
T3413_DEFAULT_VALUE          = 400 # Network dependent    #
T3422_DEFAULT_VALUE            = 6
T3450_DEFAULT_VALUE            = 6
T3460_DEFAULT_VALUE            = 6
T3470_DEFAULT_VALUE            = 6

#------------------------------------------------------------------------------
# 10.3 Timers of EPS session management
#------------------------------------------------------------------------------

#..............................................................................
# Table 10.3.1: EPS session management timers – UE side
#..............................................................................
T3480_DEFAULT_VALUE            = 8
T3481_DEFAULT_VALUE            = 8
T3482_DEFAULT_VALUE            = 8
T3492_DEFAULT_VALUE            = 6

#..............................................................................
# Table 10.3.2: EPS session management timers – network side
#..............................................................................
T3485_DEFAULT_VALUE            = 8
T3486_DEFAULT_VALUE            = 8
T3489_DEFAULT_VALUE            = 4
T3495_DEFAULT_VALUE            = 8


#==============================================================================
# Annex A (informative): Cause values for EPS mobility management
#==============================================================================

#------------------------------------------------------------------------------
# A.1 Causes related to UE identification
#------------------------------------------------------------------------------
EMM_CAUSE_IMSI_UNKNOWN_IN_HSS                    = 2
EMM_CAUSE_ILLEGAL_UE                             = 3
EMM_CAUSE_ILLEGAL_ME                             = 6
EMM_CAUSE_UE_IDENTITY_CANT_BE_DERIVED_BY_NW      = 9
EMM_CAUSE_IMPLICITLY_DETACHED                   = 10

#------------------------------------------------------------------------------
# A.2 Cause related to subscription options
#------------------------------------------------------------------------------
EMM_CAUSE_IMEI_NOT_ACCEPTED                      = 5
EMM_CAUSE_EPS_NOT_ALLOWED                        = 7
EMM_CAUSE_BOTH_NOT_ALLOWED                       = 8
EMM_CAUSE_PLMN_NOT_ALLOWED                      = 11
EMM_CAUSE_TA_NOT_ALLOWED                        = 12
EMM_CAUSE_ROAMING_NOT_ALLOWED                   = 13
EMM_CAUSE_EPS_NOT_ALLOWED_IN_PLMN               = 14
EMM_CAUSE_NO_SUITABLE_CELLS                     = 15
EMM_CAUSE_CSG_NOT_AUTHORIZED                    = 25
EMM_CAUSE_NOT_AUTHORIZED_IN_PLMN                = 35
EMM_CAUSE_NO_EPS_BEARER_CTX_ACTIVE              = 40

#------------------------------------------------------------------------------
# A.3 Causes related to PLMN specific network failures and congestion/authentication failures
#------------------------------------------------------------------------------
EMM_CAUSE_MSC_NOT_REACHABLE                     = 16
EMM_CAUSE_NETWORK_FAILURE                       = 17
EMM_CAUSE_CS_DOMAIN_NOT_AVAILABLE               = 18
EMM_CAUSE_ESM_FAILURE                           = 19
EMM_CAUSE_MAC_FAILURE                           = 20
EMM_CAUSE_SYNCH_FAILURE                         = 21
EMM_CAUSE_CONGESTION                            = 22
EMM_CAUSE_UE_SECURITY_MISMATCH                  = 23
EMM_CAUSE_SECURITY_MODE_REJECTED                = 24
EMM_CAUSE_NON_EPS_AUTH_UNACCEPTABLE             = 26
EMM_CAUSE_CS_SERVICE_NOT_AVAILABLE              = 39

#------------------------------------------------------------------------------
# A.4 Causes related to nature of request
#------------------------------------------------------------------------------
# NOTE: This subclause has no entries in this version of the specification

#------------------------------------------------------------------------------
# A.5 Causes related to invalid messages
#------------------------------------------------------------------------------
EMM_CAUSE_SEMANTICALLY_INCORRECT                = 95
EMM_CAUSE_INVALID_MANDATORY_INFO                = 96
EMM_CAUSE_MESSAGE_TYPE_NOT_IMPLEMENTED          = 97
EMM_CAUSE_MESSAGE_TYPE_NOT_COMPATIBLE           = 98
EMM_CAUSE_IE_NOT_IMPLEMENTED                    = 99
EMM_CAUSE_CONDITIONAL_IE_ERROR                 = 100
EMM_CAUSE_MESSAGE_NOT_COMPATIBLE               = 101
EMM_CAUSE_PROTOCOL_ERROR                       = 111

#==============================================================================
# Annex B (informative): Cause values for EPS session management
#==============================================================================

#------------------------------------------------------------------------------
# B.1 Causes related to nature of request
#------------------------------------------------------------------------------
ESM_CAUSE_OPERATOR_DETERMINED_BARRING               = 8
ESM_CAUSE_INSUFFICIENT_RESOURCES                   = 26
ESM_CAUSE_UNKNOWN_ACCESS_POINT_NAME                = 27
ESM_CAUSE_UNKNOWN_PDN_TYPE                         = 28
ESM_CAUSE_USER_AUTHENTICATION_FAILED               = 29
ESM_CAUSE_REQUEST_REJECTED_BY_GW                   = 30
ESM_CAUSE_REQUEST_REJECTED_UNSPECIFIED             = 31
ESM_CAUSE_SERVICE_OPTION_NOT_SUPPORTED             = 32
ESM_CAUSE_REQUESTED_SERVICE_OPTION_NOT_SUBSCRIBED  = 33
ESM_CAUSE_SERVICE_OPTION_TEMPORARILY_OUT_OF_ORDER  = 34
ESM_CAUSE_PTI_ALREADY_IN_USE                       = 35
ESM_CAUSE_REGULAR_DEACTIVATION                     = 36
ESM_CAUSE_EPS_QOS_NOT_ACCEPTED                     = 37
ESM_CAUSE_NETWORK_FAILURE                          = 38
ESM_CAUSE_REACTIVATION_REQUESTED                   = 39
ESM_CAUSE_SEMANTIC_ERROR_IN_THE_TFT_OPERATION      = 41
ESM_CAUSE_SYNTACTICAL_ERROR_IN_THE_TFT_OPERATION   = 42
ESM_CAUSE_INVALID_EPS_BEARER_IDENTITY              = 43
ESM_CAUSE_SEMANTIC_ERRORS_IN_PACKET_FILTER         = 44
ESM_CAUSE_SYNTACTICAL_ERROR_IN_PACKET_FILTER       = 45
ESM_CAUSE_PTI_MISMATCH                             = 47
ESM_CAUSE_LAST_PDN_DISCONNECTION_NOT_ALLOWED       = 49
ESM_CAUSE_PDN_TYPE_IPV4_ONLY_ALLOWED               = 50
ESM_CAUSE_PDN_TYPE_IPV6_ONLY_ALLOWED               = 51
ESM_CAUSE_SINGLE_ADDRESS_BEARERS_ONLY_ALLOWED      = 52
ESM_CAUSE_ESM_INFORMATION_NOT_RECEIVED             = 53
ESM_CAUSE_PDN_CONNECTION_DOES_NOT_EXIST            = 54
ESM_CAUSE_MULTIPLE_PDN_CONNECTIONS_NOT_ALLOWED     = 55
ESM_CAUSE_COLLISION_WITH_NETWORK_INITIATED_REQUEST = 56
ESM_CAUSE_UNSUPPORTED_QCI_VALUE                    = 59
ESM_CAUSE_BEARER_HANDLING_NOT_SUPPORTED            = 60
ESM_CAUSE_INVALID_PTI_VALUE                        = 81
ESM_CAUSE_APN_RESTRICTION_VALUE_NOT_COMPATIBLE    = 112

#------------------------------------------------------------------------------
# B.2 Protocol errors (e.g., unknown message) class
#------------------------------------------------------------------------------
ESM_CAUSE_SEMANTICALLY_INCORRECT                   = 95
ESM_CAUSE_INVALID_MANDATORY_INFO                   = 96
ESM_CAUSE_MESSAGE_TYPE_NOT_IMPLEMENTED             = 97
ESM_CAUSE_MESSAGE_TYPE_NOT_COMPATIBLE              = 98
ESM_CAUSE_IE_NOT_IMPLEMENTED                       = 99
ESM_CAUSE_CONDITIONAL_IE_ERROR                    = 100
ESM_CAUSE_MESSAGE_NOT_COMPATIBLE                  = 101
ESM_CAUSE_PROTOCOL_ERROR                          = 111




