from ctypes import *

class tagbstring(Structure):

	def __str__(self):
		s=[]
		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		return '{%s}'%(','.join([i for i in s]))

	_fields_ = [
				('mlen',c_int),
				('slen',c_int),
				('data',POINTER(c_ubyte)),
				]

bstring = POINTER(tagbstring)

AdditionalUpdateType = c_int

class emm_msg_header_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))

	_fields_ = [
				('protocol_discriminator', c_ubyte, 4),
				('security_header_type', c_ubyte, 4),
				('message_type', c_ubyte),
				]


class esm_msg_header_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))

	_fields_ = [
				('protocol_discriminator', c_ubyte, 4),
				('eps_bearer_identity', c_ubyte, 4),
				('procedure_transaction_identity', c_ubyte),
				('message_type', c_ubyte),
				]


eps_protocol_discriminator_t = c_int


class eci_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))

	_fields_ = [
				('enb_id', c_uint, 20),
				('cell_id', c_uint, 8),
				('empty', c_uint, 4),
				]

class as_stmsi_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))

	_fields_ = [
				('mme_code', c_ubyte),
				('m_tmsi', c_uint),
				]

class plmn_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))

	_fields_ = [
				('mcc_digit2', c_ubyte, 4),
				('mcc_digit1', c_ubyte, 4),
				('mnc_digit3', c_ubyte, 4),
				('mcc_digit3', c_ubyte, 4),
				('mnc_digit2', c_ubyte, 4),
				('mnc_digit1', c_ubyte, 4),
				]

class PLMN_LIST_T(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))

	_fields_ = [
				('n_plmns', c_ubyte),
				('plmn', plmn_t*6),
				]


tac_t = c_ushort
class tai_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))

	_fields_ = [
				('plmn', plmn_t),
				('tac', tac_t),
				]


class ecgi_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))

	_fields_ = [
				('plmn', plmn_t),
				('cell_identity', eci_t),
				]

ksi_t = c_ubyte

tmsi_t = c_uint

mme_gid_t = c_ushort

mme_code_t = c_ubyte

class gummei_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))

	_fields_ = [
				('plmn', plmn_t),
				('mme_gid', mme_gid_t),
				('mme_code', mme_code_t),
				]

class guti_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))

	_fields_ = [
				('gummei', gummei_t),
				('m_tmsi', tmsi_t),
				]
class ms_network_capability_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('gea1',c_ubyte,1),
				('smdc',c_ubyte,1),
				('smgc',c_ubyte,1),
				('ucs2',c_ubyte,1),
				('sssi',c_ubyte,2),
				('solsa',c_ubyte,1),
				('revli',c_ubyte,1),
				('pfc',c_ubyte,1),
				('egea',c_ubyte,6),
				('lcs',c_ubyte,1),
				('ps_ho_utran',c_ubyte,1),
				('ps_ho_eutran',c_ubyte,1),
				('emm_cpc',c_ubyte,1),
				('isr',c_ubyte,1),
				('srvcc',c_ubyte,1),
				('epc_cap',c_ubyte,1),
				('nf_cap',c_ubyte,1),
				('geran_ns',c_ubyte,1),
				]
class pco_protocol_or_container_id_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('id',c_ushort),
				('length',c_ubyte),
				('contents',bstring),
				]
class protocol_configuration_options_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('ext',c_ubyte,1),
				('spare',c_ubyte,4),
				('configuration_protocol',c_ubyte,3),
				('num_protocol_or_container_id',c_ubyte),
				('protocol_or_container_ids[PCO_UNSPEC_MAXIMUM_PROTOCOL_ID_OR_CONTAINER_ID]',pco_protocol_or_container_id_t),
				]
class ue_network_capability_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('eea',c_ubyte),
				('eia',c_ubyte),
				('uea',c_ubyte),
				('ucs2',c_ubyte,1),
				('uia',c_ubyte,7),
				('spare',c_ubyte,3),
				('csfb',c_ubyte,1),
				('lpp',c_ubyte,1),
				('lcs',c_ubyte,1),
				('srvcc',c_ubyte,1),
				('nf',c_ubyte,1),
				('umts_present',c_bool),
				('misc_present',c_bool),
				]
class ue_security_capability_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('eea',c_ubyte),
				('eia',c_ubyte),
				('umts_present',c_bool),
				('gprs_present',c_bool),
				('uea',c_ubyte),
				('uia',c_ubyte,7),
				('gea',c_ubyte,7),
				]
AccessPointName = bstring
AdditionalUpdateResult = c_ubyte
AdditionalUpdateType= c_int
class ApnAggregateMaximumBitRate(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('apnambrfordownlink',c_ubyte),
				('apnambrforuplink',c_ubyte),
				('apnambrfordownlink_extended',c_ubyte),
				('apnambrforuplink_extended',c_ubyte),
				('apnambrfordownlink_extended2',c_ubyte),
				('apnambrforuplink_extended2',c_ubyte),
				('extensions',c_ubyte),
				]
AuthenticationFailureParameter = bstring
AuthenticationParameterAutn = bstring
AuthenticationParameterRand = bstring
AuthenticationResponseParameter = bstring
CipheringKeySequenceNumber = c_ubyte
Cli = bstring
CsfbResponse = c_ubyte
DaylightSavingTime = c_ubyte
class DetachType(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('switchoff',c_ubyte,1),
				('typeofdetach',c_ubyte,3),
				]
class DrxParameter(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('splitpgcyclecode',c_ubyte),
				('cnspecificdrxcyclelengthcoefficientanddrxvaluefors1mode',c_ubyte,4),
				('splitonccch',c_ubyte,1),
				('nondrxtimer',c_ubyte,3),
				]
class EmergencyNumberList(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('lengthofemergency',c_ubyte),
				('emergencyservicecategoryvalue',c_ubyte,5),
				]
EmmCause = c_ubyte
EpsAttachResult = c_ubyte
EpsAttachType = c_ubyte
EpsBearerContextStatus = c_ushort
EpsBearerIdentity = c_ubyte
class GutiEpsMobileIdentity_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('spare',c_ubyte,4),
				('oddeven',c_ubyte,1),
				('typeofidentity',c_ubyte,3),
				('mccdigit2',c_ubyte,4),
				('mccdigit1',c_ubyte,4),
				('mncdigit3',c_ubyte,4),
				('mccdigit3',c_ubyte,4),
				('mncdigit2',c_ubyte,4),
				('mncdigit1',c_ubyte,4),
				('mmegroupid',c_ushort),
				('mmecode',c_ubyte),
				('mtmsi',c_uint),
				]
class ImsiEpsMobileIdentity_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('digit1',c_ubyte,4),
				('oddeven',c_ubyte,1),
				('typeofidentity',c_ubyte,3),
				('digit2',c_ubyte,4),
				('digit3',c_ubyte,4),
				('digit4',c_ubyte,4),
				('digit5',c_ubyte,4),
				('digit6',c_ubyte,4),
				('digit7',c_ubyte,4),
				('digit8',c_ubyte,4),
				('digit9',c_ubyte,4),
				('digit10',c_ubyte,4),
				('digit11',c_ubyte,4),
				('digit12',c_ubyte,4),
				('digit13',c_ubyte,4),
				('digit14',c_ubyte,4),
				('digit15',c_ubyte,4),
				]
ImeiEpsMobileIdentity_t = ImsiEpsMobileIdentity_t
class EpsMobileIdentity(Union):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('imsi',ImsiEpsMobileIdentity_t),
				('guti',GutiEpsMobileIdentity_t),
				('imei',ImeiEpsMobileIdentity_t),
				]
EpsNetworkFeatureSupport = c_ubyte
class EpsQoSBitRates(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('maxBitRateForUL',c_ubyte),
				('maxBitRateForDL',c_ubyte),
				('guarBitRateForUL',c_ubyte),
				('guarBitRateForDL',c_ubyte),
				]
class EpsQualityOfService(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('bitRatesPresent',c_ubyte,1),
				('bitRatesExtPresent',c_ubyte,1),
				('qci',c_ubyte),
				('bitRates',EpsQoSBitRates),
				('bitRatesExt',EpsQoSBitRates),
				]
EpsQualityOfService = c_ubyte
EpsUpdateResult = c_ubyte
class EpsUpdateType(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('activeflag',c_ubyte,1),
				('epsupdatetypevalue',c_ubyte,3),
				]
EsmCause = c_ubyte
EsmInformationTransferFlag = c_ubyte
EsmMessageContainer = bstring
class GprsTimer(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('unit',c_ubyte,3),
				('timervalue',c_ubyte,5),
				]
GutiType = c_ubyte
IdentityType2 = c_ubyte
ImeisvRequest = c_ubyte
class KsiAndSequenceNumber(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('ksi',c_ubyte,3),
				('sequencenumber',c_ubyte,5),
				]
LcsClientIdentity = bstring
LcsIndicator = c_ubyte
LinkedEpsBearerIdentity = c_ubyte
LlcServiceAccessPointIdentifier = c_ubyte
class LocationAreaIdentification(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('mccdigit2',c_ubyte,4),
				('mccdigit1',c_ubyte,4),
				('mncdigit3',c_ubyte,4),
				('mccdigit3',c_ubyte,4),
				('mncdigit2',c_ubyte,4),
				('mncdigit1',c_ubyte,4),
				('lac',c_ushort),
				]
MessageType = c_ubyte
class ImsiMobileIdentity_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('digit1',c_ubyte,4),
				('oddeven',c_ubyte,1),
				('typeofidentity',c_ubyte,3),
				('digit2',c_ubyte,4),
				('digit3',c_ubyte,4),
				('digit4',c_ubyte,4),
				('digit5',c_ubyte,4),
				('digit6',c_ubyte,4),
				('digit7',c_ubyte,4),
				('digit8',c_ubyte,4),
				('digit9',c_ubyte,4),
				('digit10',c_ubyte,4),
				('digit11',c_ubyte,4),
				('digit12',c_ubyte,4),
				('digit13',c_ubyte,4),
				('digit14',c_ubyte,4),
				('digit15',c_ubyte,4),
				]
class ImeiMobileIdentity_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('tac1',c_ubyte,4),
				('oddeven',c_ubyte,1),
				('typeofidentity',c_ubyte,3),
				('tac2',c_ubyte,4),
				('tac3',c_ubyte,4),
				('tac4',c_ubyte,4),
				('tac5',c_ubyte,4),
				('tac6',c_ubyte,4),
				('tac7',c_ubyte,4),
				('tac8',c_ubyte,4),
				('snr1',c_ubyte,4),
				('snr2',c_ubyte,4),
				('snr3',c_ubyte,4),
				('snr4',c_ubyte,4),
				('snr5',c_ubyte,4),
				('snr6',c_ubyte,4),
				('cdsd',c_ubyte,4),
				]
class ImeisvMobileIdentity_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('tac1',c_ubyte,4),
				('oddeven',c_ubyte,1),
				('typeofidentity',c_ubyte,3),
				('tac2',c_ubyte,4),
				('tac3',c_ubyte,4),
				('tac4',c_ubyte,4),
				('tac5',c_ubyte,4),
				('tac6',c_ubyte,4),
				('tac7',c_ubyte,4),
				('tac8',c_ubyte,4),
				('snr1',c_ubyte,4),
				('snr2',c_ubyte,4),
				('snr3',c_ubyte,4),
				('snr4',c_ubyte,4),
				('snr5',c_ubyte,4),
				('snr6',c_ubyte,4),
				('svn1',c_ubyte,4),
				('svn2',c_ubyte,4),
				('last',c_ubyte,4),
				]
class TmgiMobileIdentity_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('spare',c_ubyte,2),
				('mbmssessionidindication',c_ubyte,1),
				('mccmncindication',c_ubyte,1),
				('oddeven',c_ubyte,1),
				('typeofidentity',c_ubyte,3),
				('mbmsserviceid',c_uint),
				('mccdigit2',c_ubyte,4),
				('mccdigit1',c_ubyte,4),
				('mncdigit3',c_ubyte,4),
				('mccdigit3',c_ubyte,4),
				('mncdigit2',c_ubyte,4),
				('mncdigit1',c_ubyte,4),
				('mbmssessionid',c_ubyte),
				]
TmsiMobileIdentity_t = ImsiMobileIdentity_t
NoMobileIdentity_t = ImsiMobileIdentity_t
class MobileIdentity(Union):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('imsi',ImsiMobileIdentity_t),
				('imei',ImeiMobileIdentity_t),
				('imeisv',ImeisvMobileIdentity_t),
				('tmsi',TmsiMobileIdentity_t),
				('tmgi',TmgiMobileIdentity_t),
				('no_id',NoMobileIdentity_t),
				]
class MobileStationClassmark2(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('revisionlevel',c_ubyte,2),
				('esind',c_ubyte,1),
				('a51',c_ubyte,1),
				('rfpowercapability',c_ubyte,3),
				('pscapability',c_ubyte,1),
				('ssscreenindicator',c_ubyte,2),
				('smcapability',c_ubyte,1),
				('vbs',c_ubyte,1),
				('vgcs',c_ubyte,1),
				('fc',c_ubyte,1),
				('cm3',c_ubyte,1),
				('lcsvacap',c_ubyte,1),
				('ucs2',c_ubyte,1),
				('solsa',c_ubyte,1),
				('cmsp',c_ubyte,1),
				('a53',c_ubyte,1),
				('a52',c_ubyte,1),
				]
class MobileStationClassmark3(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('field',c_ubyte),
				]
MsNetworkCapability = ms_network_capability_t
class MsNetworkFeatureSupport(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('spare_bits',c_ubyte,3),
				('extended_periodic_timers',c_ubyte,1),
				]
class NasKeySetIdentifier(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('tsc',c_ubyte,1),
				('naskeysetidentifier',c_ubyte,3),
				]
NasMessageContainer = bstring
RequestType = c_ubyte
class NasSecurityAlgorithms(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('typeofcipheringalgorithm',c_ubyte,3),
				('typeofintegrityalgorithm',c_ubyte,3),
				]
class NetworkName(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('codingscheme',c_ubyte,3),
				('addci',c_ubyte,1),
				('numberofsparebitsinlastoctet',c_ubyte,3),
				('textstring',bstring),
				]
Nonce = c_uint
PTmsiSignature = bstring
PacketFlowIdentifier = c_ubyte
PagingIdentity = c_ubyte
class PdnAddress(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('pdntypevalue',c_ubyte,3),
				('pdnaddressinformation',bstring),
				]
PdnType = c_ubyte
class PlmnList(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('mccdigit2',c_ubyte,4),
				('mccdigit1',c_ubyte,4),
				('mncdigit3',c_ubyte,4),
				('mccdigit3',c_ubyte,4),
				('mncdigit2',c_ubyte,4),
				('mncdigit1',c_ubyte,4),
				]
ProcedureTransactionIdentity = c_ubyte
ProtocolConfigurationOptionsList_ids= c_int
ProtocolConfigurationOptions = protocol_configuration_options_t
ProtocolDiscriminator = c_ubyte
class QualityOfService(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('delayclass',c_ubyte,3),
				('reliabilityclass',c_ubyte,3),
				('peakthroughput',c_ubyte,4),
				('precedenceclass',c_ubyte,3),
				('meanthroughput',c_ubyte,5),
				('trafficclass',c_ubyte,3),
				('deliveryorder',c_ubyte,2),
				('deliveryoferroneoussdu',c_ubyte,3),
				('maximumsdusize',c_ubyte),
				('maximumbitrateuplink',c_ubyte),
				('maximumbitratedownlink',c_ubyte),
				('residualber',c_ubyte,4),
				('sduratioerror',c_ubyte,4),
				('transferdelay',c_ubyte,6),
				('traffichandlingpriority',c_ubyte,2),
				('guaranteedbitrateuplink',c_ubyte),
				('guaranteedbitratedownlink',c_ubyte),
				('signalingindication',c_ubyte,1),
				('sourcestatisticsdescriptor',c_ubyte,4),
				]
RadioPriority = c_ubyte
SecurityHeaderType = c_ubyte
ServiceType = c_ubyte
ShortMac = c_ushort
SsCode = c_ubyte
class SupportedCodecList(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('systemidentification',c_ubyte),
				('lengthofbitmap',c_ubyte),
				('codecbitmap',c_ushort),
				]
TimeZone = c_ubyte
class TimeZoneAndTime(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('year',c_ubyte),
				('month',c_ubyte),
				('day',c_ubyte),
				('hour',c_ubyte),
				('minute',c_ubyte),
				('second',c_ubyte),
				('timezone',c_ubyte),
				]
TmsiStatus = c_ubyte
class TrackingAreaIdentity(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('mccdigit2',c_ubyte,4),
				('mccdigit1',c_ubyte,4),
				('mncdigit3',c_ubyte,4),
				('mccdigit3',c_ubyte,4),
				('mncdigit2',c_ubyte,4),
				('mncdigit1',c_ubyte,4),
				('tac',c_ushort),
				]
class TrackingAreaIdentityList(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('typeoflist',c_ubyte,2),
				('numberofelements',c_ubyte,5),
				('mccdigit2[16]',c_ubyte),
				('mccdigit1[16]',c_ubyte),
				('mncdigit3[16]',c_ubyte),
				('mccdigit3[16]',c_ubyte),
				('mncdigit2[16]',c_ubyte),
				('mncdigit1[16]',c_ubyte),
				('tac[16]',c_ushort),
				]
class TrafficFlowAggregateDescription(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('field',c_ubyte),
				]

class ipv4remoteaddr_one(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))

	_fields_ = [
				('addr', c_ubyte),
				('mask', c_ubyte),
				]
ipv4remoteaddr = ipv4remoteaddr_one*4
class ipv6remoteaddr_one(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))

	_fields_ = [
				('addr', c_ubyte),
				('mask', c_ubyte),
				]
ipv6remoteaddr = ipv6remoteaddr_one*16
class localportrange(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))

	_fields_ = [
				('lowlimit', c_ushort),
				('highlimit', c_ushort),
				]
class remoteportrange(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))

	_fields_ = [
				('lowlimit', c_ushort),
				('highlimit', c_ushort),
				]
class typdeofservice_trafficclass(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))

	_fields_ = [
				('value', c_ubyte),
				('mask', c_ubyte),
				]

class PacketFilter(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))

	_fields_ = [
				('flags', c_ushort),
				('ipv4remoteaddr', ipv4remoteaddr),
				('ipv6remoteaddr', ipv6remoteaddr),
				('protocolidentifier_nextheader', c_ubyte),
				('singlelocalport', c_ushort),
				('localportrange', localportrange),
				('securityparameterindex', c_ushort),
				('typdeofservice_trafficclass', typdeofservice_trafficclass),
				('flowlabel', c_uint),
				]

class flags(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				]
class NoPacketFilter(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				]
DeleteExistingTft = NoPacketFilter
NoTftOperation = NoPacketFilter
class PacketFilterIdentifiers(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('identifier',c_ubyte),
				]
DeletePacketFilter = PacketFilterIdentifiers*16
class PacketFilters(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('identifier',c_ubyte,4),
				('direction',c_ubyte,2),
				('eval_precedence',c_ubyte),
				('packetfilter',PacketFilter),
				]
CreateNewTft = PacketFilters*4
AddPacketFilter = PacketFilters*4
ReplacePacketFilter = PacketFilters*4
class PacketFilterList(Union):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('createtft',CreateNewTft),
				('deletetft',DeleteExistingTft),
				('addpacketfilter',AddPacketFilter),
				('replacepacketfilter',ReplacePacketFilter),
				('deletepacketfilter',DeletePacketFilter),
				('notftoperation',NoTftOperation),
				]
class ParameterList(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				]
class TrafficFlowTemplate(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('tftoperationcode',c_ubyte,3),
				('ebit',c_ubyte,1),
				('numberofpacketfilters',c_ubyte,4),
				('packetfilterlist',PacketFilterList),
				('parameterlist',ParameterList),
				]
class TransactionIdentifier(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('field',c_ubyte),
				]
UeNetworkCapability = ue_network_capability_t
UeRadioCapabilityInformationUpdateNeeded = c_ubyte
UeSecurityCapability = ue_security_capability_t
class VoiceDomainPreferenceAndUeUsageSetting(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('spare',c_ubyte,5),
				('ue_usage_setting',c_ubyte,1),
				('voice_domain_for_eutran',c_ubyte,2),
				]
attach_accept_iei= c_int
class attach_accept_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('securityheadertype',SecurityHeaderType,4),
				('messagetype',MessageType),
				('epsattachresult',EpsAttachResult),
				('t3412value',GprsTimer),
				('tailist',TrackingAreaIdentityList),
				('esmmessagecontainer',EsmMessageContainer),
				('presencemask',c_uint),
				('guti',EpsMobileIdentity),
				('locationareaidentification',LocationAreaIdentification),
				('msidentity',MobileIdentity),
				('emmcause',EmmCause),
				('t3402value',GprsTimer),
				('t3423value',GprsTimer),
				('equivalentplmns',PlmnList),
				('emergencynumberlist',EmergencyNumberList),
				('epsnetworkfeaturesupport',EpsNetworkFeatureSupport),
				('additionalupdateresult',AdditionalUpdateResult),
				]
class attach_complete_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('securityheadertype',SecurityHeaderType,4),
				('messagetype',MessageType),
				('esmmessagecontainer',EsmMessageContainer),
				]
attach_reject_iei= c_int
class attach_reject_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('securityheadertype',SecurityHeaderType,4),
				('messagetype',MessageType),
				('emmcause',EmmCause),
				('presencemask',c_uint),
				('esmmessagecontainer',EsmMessageContainer),
				]
attach_request_iei= c_int
class attach_request_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('securityheadertype',SecurityHeaderType,4),
				('messagetype',MessageType),
				('epsattachtype',EpsAttachType),
				('naskeysetidentifier',NasKeySetIdentifier),
				('oldgutiorimsi',EpsMobileIdentity),
				('uenetworkcapability',UeNetworkCapability),
				('esmmessagecontainer',EsmMessageContainer),
				('presencemask',c_uint),
				('oldptmsisignature',PTmsiSignature),
				('additionalguti',EpsMobileIdentity),
				('lastvisitedregisteredtai',TrackingAreaIdentity),
				('drxparameter',DrxParameter),
				('msnetworkcapability',MsNetworkCapability),
				('oldlocationareaidentification',LocationAreaIdentification),
				('tmsistatus',TmsiStatus),
				('mobilestationclassmark2',MobileStationClassmark2),
				('mobilestationclassmark3',MobileStationClassmark3),
				('supportedcodecs',SupportedCodecList),
				('additionalupdatetype',AdditionalUpdateType),
				('oldgutitype',GutiType),
				('voicedomainpreferenceandueusagesetting',VoiceDomainPreferenceAndUeUsageSetting),
				('msnetworkfeaturesupport',MsNetworkFeatureSupport),
				]
authentication_failure_iei= c_int
class authentication_failure_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('securityheadertype',SecurityHeaderType,4),
				('messagetype',MessageType),
				('emmcause',EmmCause),
				('presencemask',c_uint),
				('authenticationfailureparameter',AuthenticationFailureParameter),
				]
class authentication_reject_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('securityheadertype',SecurityHeaderType,4),
				('messagetype',MessageType),
				]
class authentication_request_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('securityheadertype',SecurityHeaderType,4),
				('messagetype',MessageType),
				('naskeysetidentifierasme',NasKeySetIdentifier),
				('authenticationparameterrand',AuthenticationParameterRand),
				('authenticationparameterautn',AuthenticationParameterAutn),
				]
class authentication_response_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('securityheadertype',SecurityHeaderType,4),
				('messagetype',MessageType),
				('authenticationresponseparameter',AuthenticationResponseParameter),
				]
cs_service_notification_iei= c_int
class cs_service_notification_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('securityheadertype',SecurityHeaderType,4),
				('messagetype',MessageType),
				('pagingidentity',PagingIdentity),
				('presencemask',c_uint),
				('cli',Cli),
				('sscode',SsCode),
				('lcsindicator',LcsIndicator),
				('lcsclientidentity',LcsClientIdentity),
				]
class detach_accept_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('securityheadertype',SecurityHeaderType,4),
				('messagetype',MessageType),
				]
class detach_request_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('securityheadertype',SecurityHeaderType,4),
				('messagetype',MessageType),
				('detachtype',DetachType),
				('naskeysetidentifier',NasKeySetIdentifier),
				('gutiorimsi',EpsMobileIdentity),
				]
class downlink_nas_transport_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('securityheadertype',SecurityHeaderType,4),
				('messagetype',MessageType),
				('nasmessagecontainer',NasMessageContainer),
				]
emm_information_iei= c_int
class emm_information_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('securityheadertype',SecurityHeaderType,4),
				('messagetype',MessageType),
				('presencemask',c_uint),
				('fullnamefornetwork',NetworkName),
				('shortnamefornetwork',NetworkName),
				('localtimezone',TimeZone),
				('universaltimeandlocaltimezone',TimeZoneAndTime),
				('networkdaylightsavingtime',DaylightSavingTime),
				]
class emm_status_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('securityheadertype',SecurityHeaderType,4),
				('messagetype',MessageType),
				('emmcause',EmmCause),
				]
class extended_service_request_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('securityheadertype',SecurityHeaderType,4),
				('messagetype',MessageType),
				('servicetype',ServiceType),
				('naskeysetidentifier',NasKeySetIdentifier),
				('mtmsi',MobileIdentity),
				('presencemask',c_uint),
				('csfbresponse',CsfbResponse),
				]
guti_reallocation_command_iei= c_int
class guti_reallocation_command_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('securityheadertype',SecurityHeaderType,4),
				('messagetype',MessageType),
				('guti',EpsMobileIdentity),
				('presencemask',c_uint),
				('tailist',TrackingAreaIdentityList),
				]
class guti_reallocation_complete_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('securityheadertype',SecurityHeaderType,4),
				('messagetype',MessageType),
				]
class identity_request_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('securityheadertype',SecurityHeaderType,4),
				('messagetype',MessageType),
				('identitytype',IdentityType2),
				]
class identity_response_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('securityheadertype',SecurityHeaderType,4),
				('messagetype',MessageType),
				('mobileidentity',MobileIdentity),
				]
security_mode_command_iei= c_int
class security_mode_command_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('securityheadertype',SecurityHeaderType,4),
				('messagetype',MessageType),
				('selectednassecurityalgorithms',NasSecurityAlgorithms),
				('naskeysetidentifier',NasKeySetIdentifier),
				('replayeduesecuritycapabilities',UeSecurityCapability),
				('presencemask',c_uint),
				('imeisvrequest',ImeisvRequest),
				('replayednonceue',Nonce),
				('noncemme',Nonce),
				]
security_mode_complete_iei= c_int
class security_mode_complete_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('securityheadertype',SecurityHeaderType,4),
				('messagetype',MessageType),
				('presencemask',c_uint),
				('imeisv',MobileIdentity),
				]
class security_mode_reject_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('securityheadertype',SecurityHeaderType,4),
				('messagetype',MessageType),
				('emmcause',EmmCause),
				]
class service_reject_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('securityheadertype',SecurityHeaderType,4),
				('messagetype',MessageType),
				('emmcause',EmmCause),
				('presencemask',c_uint),
				('t3442value',GprsTimer),
				]
class service_request_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('securityheadertype',SecurityHeaderType,4),
				('messagetype',MessageType),
				('ksiandsequencenumber',KsiAndSequenceNumber),
				('messageauthenticationcode',ShortMac),
				]
tracking_area_update_accept_iei= c_int
class tracking_area_update_accept_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('securityheadertype',SecurityHeaderType,4),
				('messagetype',MessageType),
				('epsupdateresult',EpsUpdateResult),
				('presencemask',c_uint),
				('t3412value',GprsTimer),
				('guti',EpsMobileIdentity),
				('tailist',TrackingAreaIdentityList),
				('epsbearercontextstatus',EpsBearerContextStatus),
				('locationareaidentification',LocationAreaIdentification),
				('msidentity',MobileIdentity),
				('emmcause',EmmCause),
				('t3402value',GprsTimer),
				('t3423value',GprsTimer),
				('equivalentplmns',PlmnList),
				('emergencynumberlist',EmergencyNumberList),
				('epsnetworkfeaturesupport',EpsNetworkFeatureSupport),
				('additionalupdateresult',AdditionalUpdateResult),
				]
class tracking_area_update_complete_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('securityheadertype',SecurityHeaderType,4),
				('messagetype',MessageType),
				]
class tracking_area_update_reject_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('securityheadertype',SecurityHeaderType,4),
				('messagetype',MessageType),
				('emmcause',EmmCause),
				]
tracking_area_update_request_iei= c_int
class tracking_area_update_request_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('securityheadertype',SecurityHeaderType,4),
				('messagetype',MessageType),
				('epsupdatetype',EpsUpdateType),
				('naskeysetidentifier',NasKeySetIdentifier),
				('oldguti',EpsMobileIdentity),
				('presencemask',c_uint),
				('noncurrentnativenaskeysetidentifier',NasKeySetIdentifier),
				('gprscipheringkeysequencenumber',CipheringKeySequenceNumber),
				('oldptmsisignature',PTmsiSignature),
				('additionalguti',EpsMobileIdentity),
				('nonceue',Nonce),
				('uenetworkcapability',UeNetworkCapability),
				('lastvisitedregisteredtai',TrackingAreaIdentity),
				('drxparameter',DrxParameter),
				('ueradiocapabilityinformationupdateneeded',UeRadioCapabilityInformationUpdateNeeded),
				('epsbearercontextstatus',EpsBearerContextStatus),
				('msnetworkcapability',MsNetworkCapability),
				('oldlocationareaidentification',LocationAreaIdentification),
				('tmsistatus',TmsiStatus),
				('mobilestationclassmark2',MobileStationClassmark2),
				('mobilestationclassmark3',MobileStationClassmark3),
				('supportedcodecs',SupportedCodecList),
				('additionalupdatetype',AdditionalUpdateType),
				('oldgutitype',GutiType),
				]
class uplink_nas_transport_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('securityheadertype',SecurityHeaderType,4),
				('messagetype',MessageType),
				('nasmessagecontainer',NasMessageContainer),
				]
class EMM_msg(Union):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('header',emm_msg_header_t),
				('attach_request',attach_request_msg),
				('attach_accept',attach_accept_msg),
				('attach_complete',attach_complete_msg),
				('attach_reject',attach_reject_msg),
				('detach_request',detach_request_msg),
				('detach_accept',detach_accept_msg),
				('tracking_area_update_request',tracking_area_update_request_msg),
				('tracking_area_update_accept',tracking_area_update_accept_msg),
				('tracking_area_update_complete',tracking_area_update_complete_msg),
				('tracking_area_update_reject',tracking_area_update_reject_msg),
				('extended_service_request',extended_service_request_msg),
				('service_request',service_request_msg),
				('service_reject',service_reject_msg),
				('guti_reallocation_command',guti_reallocation_command_msg),
				('guti_reallocation_complete',guti_reallocation_complete_msg),
				('authentication_request',authentication_request_msg),
				('authentication_response',authentication_response_msg),
				('authentication_reject',authentication_reject_msg),
				('authentication_failure',authentication_failure_msg),
				('identity_request',identity_request_msg),
				('identity_response',identity_response_msg),
				('security_mode_command',security_mode_command_msg),
				('security_mode_complete',security_mode_complete_msg),
				('security_mode_reject',security_mode_reject_msg),
				('emm_status',emm_status_msg),
				('emm_information',emm_information_msg),
				('downlink_nas_transport',downlink_nas_transport_msg),
				('uplink_nas_transport',uplink_nas_transport_msg),
				('cs_service_notification',cs_service_notification_msg),
				]
class message_type(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocol_discriminator',c_ubyte,4),
				('security_header_type',c_ubyte,4),
				('security_header_type',c_ubyte,4),
				('protocol_discriminator',c_ubyte,4),
				]
activate_dedicated_eps_bearer_context_accept_iei= c_int
class activate_dedicated_eps_bearer_context_accept_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('epsbeareridentity',EpsBearerIdentity,4),
				('proceduretransactionidentity',ProcedureTransactionIdentity),
				('messagetype',MessageType),
				('presencemask',c_uint),
				('protocolconfigurationoptions',ProtocolConfigurationOptions),
				]
activate_dedicated_eps_bearer_context_reject_iei= c_int
class activate_dedicated_eps_bearer_context_reject_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('epsbeareridentity',EpsBearerIdentity,4),
				('proceduretransactionidentity',ProcedureTransactionIdentity),
				('messagetype',MessageType),
				('esmcause',EsmCause),
				('presencemask',c_uint),
				('protocolconfigurationoptions',ProtocolConfigurationOptions),
				]
activate_dedicated_eps_bearer_context_request_iei= c_int
class activate_dedicated_eps_bearer_context_request_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('epsbeareridentity',EpsBearerIdentity,4),
				('proceduretransactionidentity',ProcedureTransactionIdentity),
				('messagetype',MessageType),
				('linkedepsbeareridentity',LinkedEpsBearerIdentity),
				('epsqos',EpsQualityOfService),
				('tft',TrafficFlowTemplate),
				('presencemask',c_uint),
				('transactionidentifier',TransactionIdentifier),
				('negotiatedqos',QualityOfService),
				('negotiatedllcsapi',LlcServiceAccessPointIdentifier),
				('radiopriority',RadioPriority),
				('packetflowidentifier',PacketFlowIdentifier),
				('protocolconfigurationoptions',ProtocolConfigurationOptions),
				]
activate_default_eps_bearer_context_accept_iei= c_int
class activate_default_eps_bearer_context_accept_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('epsbeareridentity',EpsBearerIdentity,4),
				('proceduretransactionidentity',ProcedureTransactionIdentity),
				('messagetype',MessageType),
				('presencemask',c_uint),
				('protocolconfigurationoptions',ProtocolConfigurationOptions),
				]
activate_default_eps_bearer_context_reject_iei= c_int
class activate_default_eps_bearer_context_reject_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('epsbeareridentity',EpsBearerIdentity,4),
				('proceduretransactionidentity',ProcedureTransactionIdentity),
				('messagetype',MessageType),
				('esmcause',EsmCause),
				('presencemask',c_uint),
				('protocolconfigurationoptions',ProtocolConfigurationOptions),
				]
activate_default_eps_bearer_context_request_iei= c_int
class activate_default_eps_bearer_context_request_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('epsbeareridentity',EpsBearerIdentity,4),
				('proceduretransactionidentity',ProcedureTransactionIdentity),
				('messagetype',MessageType),
				('epsqos',EpsQualityOfService),
				('accesspointname',AccessPointName),
				('pdnaddress',PdnAddress),
				('presencemask',c_uint),
				('transactionidentifier',TransactionIdentifier),
				('negotiatedqos',QualityOfService),
				('negotiatedllcsapi',LlcServiceAccessPointIdentifier),
				('radiopriority',RadioPriority),
				('packetflowidentifier',PacketFlowIdentifier),
				('apnambr',ApnAggregateMaximumBitRate),
				('esmcause',EsmCause),
				('protocolconfigurationoptions',ProtocolConfigurationOptions),
				]
bearer_resource_allocation_reject_iei= c_int
class bearer_resource_allocation_reject_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('epsbeareridentity',EpsBearerIdentity,4),
				('proceduretransactionidentity',ProcedureTransactionIdentity),
				('messagetype',MessageType),
				('esmcause',EsmCause),
				('presencemask',c_uint),
				('protocolconfigurationoptions',ProtocolConfigurationOptions),
				]
bearer_resource_allocation_request_iei= c_int
class bearer_resource_allocation_request_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('epsbeareridentity',EpsBearerIdentity,4),
				('proceduretransactionidentity',ProcedureTransactionIdentity),
				('messagetype',MessageType),
				('linkedepsbeareridentity',LinkedEpsBearerIdentity),
				('trafficflowaggregate',TrafficFlowAggregateDescription),
				('requiredtrafficflowqos',EpsQualityOfService),
				('presencemask',c_uint),
				('protocolconfigurationoptions',ProtocolConfigurationOptions),
				]
bearer_resource_modification_reject_iei= c_int
class bearer_resource_modification_reject_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('epsbeareridentity',EpsBearerIdentity,4),
				('proceduretransactionidentity',ProcedureTransactionIdentity),
				('messagetype',MessageType),
				('esmcause',EsmCause),
				('presencemask',c_uint),
				('protocolconfigurationoptions',ProtocolConfigurationOptions),
				]
bearer_resource_modification_request_iei= c_int
class bearer_resource_modification_request_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('epsbeareridentity',EpsBearerIdentity,4),
				('proceduretransactionidentity',ProcedureTransactionIdentity),
				('messagetype',MessageType),
				('epsbeareridentityforpacketfilter',LinkedEpsBearerIdentity),
				('trafficflowaggregate',TrafficFlowAggregateDescription),
				('presencemask',c_uint),
				('requiredtrafficflowqos',EpsQualityOfService),
				('esmcause',EsmCause),
				('protocolconfigurationoptions',ProtocolConfigurationOptions),
				]
deactivate_eps_bearer_context_accept_iei= c_int
class deactivate_eps_bearer_context_accept_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('epsbeareridentity',EpsBearerIdentity,4),
				('proceduretransactionidentity',ProcedureTransactionIdentity),
				('messagetype',MessageType),
				('presencemask',c_uint),
				('protocolconfigurationoptions',ProtocolConfigurationOptions),
				]
deactivate_eps_bearer_context_request_iei= c_int
class deactivate_eps_bearer_context_request_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('epsbeareridentity',EpsBearerIdentity,4),
				('proceduretransactionidentity',ProcedureTransactionIdentity),
				('messagetype',MessageType),
				('esmcause',EsmCause),
				('presencemask',c_uint),
				('protocolconfigurationoptions',ProtocolConfigurationOptions),
				]
class esm_information_request_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('epsbeareridentity',EpsBearerIdentity,4),
				('proceduretransactionidentity',ProcedureTransactionIdentity),
				('messagetype',MessageType),
				]
esm_information_response_iei= c_int
class esm_information_response_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('epsbeareridentity',EpsBearerIdentity,4),
				('proceduretransactionidentity',ProcedureTransactionIdentity),
				('messagetype',MessageType),
				('presencemask',c_uint),
				('accesspointname',AccessPointName),
				('protocolconfigurationoptions',ProtocolConfigurationOptions),
				]
class esm_status_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('epsbeareridentity',EpsBearerIdentity,4),
				('proceduretransactionidentity',ProcedureTransactionIdentity),
				('messagetype',MessageType),
				('esmcause',EsmCause),
				]
modify_eps_bearer_context_accept_iei= c_int
class modify_eps_bearer_context_accept_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('epsbeareridentity',EpsBearerIdentity,4),
				('proceduretransactionidentity',ProcedureTransactionIdentity),
				('messagetype',MessageType),
				('presencemask',c_uint),
				('protocolconfigurationoptions',ProtocolConfigurationOptions),
				]
modify_eps_bearer_context_reject_iei= c_int
class modify_eps_bearer_context_reject_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('epsbeareridentity',EpsBearerIdentity,4),
				('proceduretransactionidentity',ProcedureTransactionIdentity),
				('messagetype',MessageType),
				('esmcause',EsmCause),
				('presencemask',c_uint),
				('protocolconfigurationoptions',ProtocolConfigurationOptions),
				]
modify_eps_bearer_context_request_iei= c_int
class modify_eps_bearer_context_request_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('epsbeareridentity',EpsBearerIdentity,4),
				('proceduretransactionidentity',ProcedureTransactionIdentity),
				('messagetype',MessageType),
				('presencemask',c_uint),
				('newepsqos',EpsQualityOfService),
				('tft',TrafficFlowTemplate),
				('newqos',QualityOfService),
				('negotiatedllcsapi',LlcServiceAccessPointIdentifier),
				('radiopriority',RadioPriority),
				('packetflowidentifier',PacketFlowIdentifier),
				('apnambr',ApnAggregateMaximumBitRate),
				('protocolconfigurationoptions',ProtocolConfigurationOptions),
				]
pdn_connectivity_reject_iei= c_int
class pdn_connectivity_reject_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('epsbeareridentity',EpsBearerIdentity,4),
				('proceduretransactionidentity',ProcedureTransactionIdentity),
				('messagetype',MessageType),
				('esmcause',EsmCause),
				('presencemask',c_uint),
				('protocolconfigurationoptions',ProtocolConfigurationOptions),
				]
pdn_connectivity_request_iei= c_int
class pdn_connectivity_request_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('epsbeareridentity',EpsBearerIdentity,4),
				('proceduretransactionidentity',ProcedureTransactionIdentity),
				('messagetype',MessageType),
				('requesttype',RequestType),
				('pdntype',PdnType),
				('presencemask',c_uint),
				('esminformationtransferflag',EsmInformationTransferFlag),
				('accesspointname',AccessPointName),
				('protocolconfigurationoptions',ProtocolConfigurationOptions),
				]
pdn_disconnect_reject_iei= c_int
class pdn_disconnect_reject_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('epsbeareridentity',EpsBearerIdentity,4),
				('proceduretransactionidentity',ProcedureTransactionIdentity),
				('messagetype',MessageType),
				('esmcause',EsmCause),
				('presencemask',c_uint),
				('protocolconfigurationoptions',ProtocolConfigurationOptions),
				]
pdn_disconnect_request_iei= c_int
class pdn_disconnect_request_msg(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocoldiscriminator',ProtocolDiscriminator,4),
				('epsbeareridentity',EpsBearerIdentity,4),
				('proceduretransactionidentity',ProcedureTransactionIdentity),
				('messagetype',MessageType),
				('linkedepsbeareridentity',LinkedEpsBearerIdentity),
				('presencemask',c_uint),
				('protocolconfigurationoptions',ProtocolConfigurationOptions),
				]
class ESM_msg(Union):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('header',esm_msg_header_t),
				('activate_default_eps_bearer_context_request',activate_default_eps_bearer_context_request_msg),
				('activate_default_eps_bearer_context_accept',activate_default_eps_bearer_context_accept_msg),
				('activate_default_eps_bearer_context_reject',activate_default_eps_bearer_context_reject_msg),
				('activate_dedicated_eps_bearer_context_request',activate_dedicated_eps_bearer_context_request_msg),
				('activate_dedicated_eps_bearer_context_accept',activate_dedicated_eps_bearer_context_accept_msg),
				('activate_dedicated_eps_bearer_context_reject',activate_dedicated_eps_bearer_context_reject_msg),
				('modify_eps_bearer_context_request',modify_eps_bearer_context_request_msg),
				('modify_eps_bearer_context_accept',modify_eps_bearer_context_accept_msg),
				('modify_eps_bearer_context_reject',modify_eps_bearer_context_reject_msg),
				('deactivate_eps_bearer_context_request',deactivate_eps_bearer_context_request_msg),
				('deactivate_eps_bearer_context_accept',deactivate_eps_bearer_context_accept_msg),
				('pdn_connectivity_request',pdn_connectivity_request_msg),
				('pdn_connectivity_reject',pdn_connectivity_reject_msg),
				('pdn_disconnect_request',pdn_disconnect_request_msg),
				('pdn_disconnect_reject',pdn_disconnect_reject_msg),
				('bearer_resource_allocation_request',bearer_resource_allocation_request_msg),
				('bearer_resource_allocation_reject',bearer_resource_allocation_reject_msg),
				('bearer_resource_modification_request',bearer_resource_modification_request_msg),
				('bearer_resource_modification_reject',bearer_resource_modification_reject_msg),
				('esm_information_request',esm_information_request_msg),
				('esm_information_response',esm_information_response_msg),
				('esm_status',esm_status_msg),
				]
class message_type(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocol_discriminator',c_ubyte,4),
				('eps_bearer_identity',c_ubyte,4),
				('eps_bearer_identity',c_ubyte,4),
				('protocol_discriminator',c_ubyte,4),
				('procedure_transaction_identity',c_ubyte),
				]
nas_cause_t= c_int
nas_error_code_t= c_int
core_network_t= c_int
class as_stmsi_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('mme_code',c_ubyte),
				('m_tmsi',c_uint),
				]
as_rab_id_t = c_ubyte
class broadcast_info_ind_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('plmn_ids',PLMN_LIST_T),
				('cell_id',eci_t),
				('tac',c_ushort),
				]
class cell_info_req_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('plmn_id',plmn_t),
				('rat',c_ubyte),
				]
class cell_info_cnf_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('err_code',c_ubyte),
				('cell_id',eci_t),
				('tac',c_ushort),
				('rat',c_ubyte),
				('rsrq',c_ubyte),
				('rsrp',c_ubyte),
				]
class cell_info_ind_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('cell_id',eci_t),
				('tac',c_ushort),
				]
paging_cause_t= c_int
class paging_req_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('s_tmsi',as_stmsi_t),
				('cn_domain',c_ubyte),
				]
class paging_ind_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('cause',paging_cause_t),
				]
as_cause_t= c_int
as_call_type_t= c_int
class nas_establish_req_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('cause',as_cause_t),
				('type',as_call_type_t),
				('s_tmsi',as_stmsi_t),
				('plmn_id',plmn_t),
				('initial_nas_msg',bstring),
				]
class nas_establish_ind_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('ue_id',c_uint),
				('tai',tai_t),
				('cgi',ecgi_t),
				('as_cause',as_cause_t),
				('s_tmsi',as_stmsi_t),
				('initial_nas_msg',bstring),
				]
class nas_establish_rsp_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('ue_id',c_uint),
				('s_tmsi',as_stmsi_t),
				('err_code',nas_error_code_t),
				('nas_msg',bstring),
				('nas_ul_count',c_uint),
				('selected_encryption_algorithm',c_ushort),
				('selected_integrity_algorithm',c_ushort),
				]
class nas_establish_cnf_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('ue_id',c_uint),
				('err_code',nas_error_code_t),
				('nas_msg',bstring),
				('ul_nas_count',c_uint),
				('selected_encryption_algorithm',c_ushort),
				('selected_integrity_algorithm',c_ushort),
				]
release_cause_t= c_int
class nas_release_req_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('ue_id',c_uint),
				('s_tmsi',as_stmsi_t),
				('cause',release_cause_t),
				]
class nas_release_ind_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('cause',release_cause_t),
				]
class ul_info_transfer_req_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('ue_id',c_uint),
				('s_tmsi',as_stmsi_t),
				('nas_msg',bstring),
				]
class ul_info_transfer_cnf_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('ue_id',c_uint),
				('err_code',nas_error_code_t),
				]
class ul_info_transfer_ind_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('ue_id',c_uint),
				('nas_msg',bstring),
				]
class dl_info_transfer_req_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('ue_id',c_uint),
				('s_tmsi',as_stmsi_t),
				('nas_msg',bstring),
				('err_code',nas_error_code_t),
				]
dl_info_transfer_cnf_t = ul_info_transfer_cnf_t
dl_info_transfer_ind_t = ul_info_transfer_ind_t
class as_qos_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				]
class rab_establish_req_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('s_tmsi',as_stmsi_t),
				('rab_id',as_rab_id_t),
				('qos',as_qos_t),
				]
class rab_establish_ind_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('rab_id',as_rab_id_t),
				]
class rab_establish_rsp_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('s_tmsi',as_stmsi_t),
				('rab_id',as_rab_id_t),
				('err_code',nas_error_code_t),
				]
class rab_establish_cnf_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('rab_id',as_rab_id_t),
				('err_code',nas_error_code_t),
				]
class rab_release_req_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('s_tmsi',as_stmsi_t),
				('rab_id',as_rab_id_t),
				]
class rab_release_ind_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('rab_id',as_rab_id_t),
				]
class msg_id(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				]
class nas_message_security_header_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('protocol_discriminator',eps_protocol_discriminator_t,4),
				('security_header_type',c_ubyte,4),
				('security_header_type',c_ubyte,4),
				('protocol_discriminator',c_ubyte,4),
				('message_authentication_code',c_uint),
				('sequence_number',c_ubyte),
				]
class nas_message_plain_t(Union):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('emm',EMM_msg),
				('esm',ESM_msg),
				]
class nas_message_security_protected_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('header',nas_message_security_header_t),
				('plain',nas_message_plain_t),
				]
class nas_message_t(Union):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('header',nas_message_security_header_t),
				('security_protected',nas_message_security_protected_t),
				('plain',nas_message_plain_t),
				]
class nas_message_decode_status_t(Structure):
	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\n\t\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
		# return '\"%s\":{%s}\n\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\"%s\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\"%s\":\"%s\""%(k[0],getattr(self,k[0])))
	
		# return '\"%s\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
	_fields_ = [
				('integrity_protected_message',c_ubyte,1),
				('ciphered_message',c_ubyte,1),
				('mac_matched',c_ubyte,1),
				('security_context_available',c_ubyte,1),
				('emm_cause',c_int),
				]
