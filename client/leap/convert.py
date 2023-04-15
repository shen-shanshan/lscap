# -*- coding: utf-8 -*-
import os
import re
############################################################################
#  G L O B A L    D E F S
############################################################################
file_write = "variable_def.py"

elements = []

type_converter = {"int8_t":"c_char",
			"int16_t":"c_short",
			"int32_t":"c_int",
			"uint8_t":"c_ubyte",
			"uint16_t":"c_ushort",
			"uint32_t":"c_uint",
			"ebi_t":"c_ubyte",
			"pti_t":"c_ubyte",
			"bool":"c_bool",
			"int":"c_int",
			"tac_t":"c_ushort",
			"AcT_t":"c_ubyte",
			"mme_ue_s1ap_id_t":"c_uint",
			}

content = {}

struct_array_fix = {}

paths = [
		"/home/artifice/leap/src/nas/ies/",
		"/home/artifice/leap/src/nas/emm/msg/",
		"/home/artifice/leap/src/nas/esm/msg/",
		"/home/artifice/leap/src/nas/api/network/",
		]

#test
# paths = []

additional_files = [
					"/home/artifice/leap/src/common/3gpp_24.008.h",
					"/home/artifice/leap/src/nas/3gpp_24.301.h",
					# "/home/artifice/leap/src/nas/emm/sap/emm_asDef.h",
					# "/home/artifice/leap/src/nas/emm/sap/emm_cnDef.h",
					# "/home/artifice/leap/src/nas/emm/sap/emm_esmDef.h",
					# "/home/artifice/leap/src/nas/emm/sap/emm_regDef.h",
					# "/home/artifice/leap/src/nas/emm/sap/emm_sap.h",
					]

file_list = []

print_method = '''	def __str__(self):
		s=[]
		# for k in self._fields_:
		# 	s.append("\\n\\t\\"%s\\":\\"%s\\""%(k[0],getattr(self,k[0])))
		# return '\\"%s\\":{%s}\\n\\t'%(self.__class__.__name__,','.join([i for i in s]))

		for k in self._fields_:
			if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
				s.append("\\"%s\\":%s"%(k[0],getattr(self,k[0])))
			else:
				s.append("\\"%s\\":\\"%s\\""%(k[0],getattr(self,k[0])))
	
		return '{%s}'%(','.join([i for i in s]))

		# for k in self._fields_:
		# 	if type(k[1]) == type(Structure) or type(k[1]) == type(Union):
		# 		s.append("%s"%(getattr(self,k[0])))
		# 	else:
		# 		s.append("\\"%s\\":\\"%s\\""%(k[0],getattr(self,k[0])))
	
		# return '\\"%s\\":{%s}'%(self.__class__.__name__,','.join([i for i in s]))
'''

############################################################################
#  S U P P L E M E N T
############################################################################

TrafficFlowTemplate_supplement = '''
class ipv4remoteaddr_one(Structure):
''' + print_method + '''
	_fields_ = [
				('addr', c_ubyte),
				('mask', c_ubyte),
				]
ipv4remoteaddr = ipv4remoteaddr_one*4
class ipv6remoteaddr_one(Structure):
''' + print_method + '''
	_fields_ = [
				('addr', c_ubyte),
				('mask', c_ubyte),
				]
ipv6remoteaddr = ipv6remoteaddr_one*16
class localportrange(Structure):
''' + print_method + '''
	_fields_ = [
				('lowlimit', c_ushort),
				('highlimit', c_ushort),
				]
class remoteportrange(Structure):
''' + print_method + '''
	_fields_ = [
				('lowlimit', c_ushort),
				('highlimit', c_ushort),
				]
class typdeofservice_trafficclass(Structure):
''' + print_method + '''
	_fields_ = [
				('value', c_ubyte),
				('mask', c_ubyte),
				]

class PacketFilter(Structure):
''' + print_method + '''
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
'''


############################################################################
# P R E  C O M P I L A T I O N
############################################################################

# struct_union_pattern = re.compile(r'typedef[\sa-z_]+{[\n A-Za-z0-9_;*/:#]+}[ A-Za-z0-9_]+;')  #extract struct and union
struct_union_pattern = re.compile(r'typedef[\sA-Za-z0-9_]+\{*[\n \w\'"<>*\(\)/\-,.=\[\];:#]*\}*[ \[\]\w]*;')  #include single def
digit_pattern = re.compile(r'\d+')
name_pattern = re.compile(r'\b[\w]+\b')


############################################################################
# F U N C T I O N S
############################################################################
def not_empty(s):
    return s and s.strip()

def handle_def(blocks, alllines, file):
	# print(blocks)
	with open(file_write,"a") as f_def:
		if "TrafficFlowTemplate.h" in file:
			f_def.write(TrafficFlowTemplate_supplement)
			f_def.write("\n")		

		for block in blocks:
			block = re.sub(r'/\*[^*]*\*+([^/*][^*]*\*+)*/', "", block)
			lines = block.split("\n")
			# print(lines)
			if "enum" in lines[0]:
				f_def.write(name_pattern.findall(lines[-1])[-1] + "= c_int")
				f_def.write("\n")
				continue
			if "struct" in lines[0]:   #process struct
				#write struct header
				# print(lines)
				if "[" in lines[-1]:   #struct array
					# print(lines)
					f_def.write('class ' + name_pattern.findall(lines[-1])[-2] + '(Structure):')
					struct_array_fix[name_pattern.findall(lines[-1])[-2]] = re.search(r"#define " + name_pattern.findall(lines[-1])[-1] + r"\s\w+", alllines).group().split(" ")[-1]
				else:
					f_def.write('class ' + name_pattern.findall(lines[-1])[-1] + '(Structure):')
				f_def.write("\n")

			elif "union" in lines[0]:  #process union
				#write union header
				f_def.write('class ' + name_pattern.findall(lines[-1])[-1] + '(Union):')
				f_def.write("\n")

			elif ";" in lines[0]:
				#write single line definition
				for line in lines:
					if "typedef" not in line:
						continue
					singleline_name = line[:-1].split(" ")[-1]
					# print(line)
					try:
						singleline_type = type_converter[line[:-1].split(" ")[-2]]
					except:
						singleline_type = filter(not_empty, line[:-1].split(" "))[-2]
					if singleline_type in struct_array_fix:
						f_def.write(singleline_name + " = " + singleline_type + "*" + struct_array_fix[singleline_type])
						f_def.write("\n")
					else:
						f_def.write(singleline_name + " = " + singleline_type)
						f_def.write("\n")
				# if singleline_name == "TmsiMobileIdentity_t":   #some bug fixes
				# 	f_def.write("NoMobileIdentity_t = ImsiMobileIdentity_t")
				# 	f_def.write("\n")
					
				# if singleline_name == "DeleteExistingTft":   #some bug fixes
				# 	f_def.write("NoTftOperation = NoPacketFilter")
				# 	f_def.write("\n")
				# if singleline_name == "CreateNewTft":   #some bug fixes
				# 	f_def.write("AddPacketFilter = PacketFilters")
				# 	f_def.write("\n")
				# if singleline_name == "CreateNewTft":   #some bug fixes
				# 	f_def.write("ReplacePacketFilter = PacketFilters")
				# 	f_def.write("\n")

				continue
			#write _fields_ start
			f_def.write(print_method)
			f_def.write("	_fields_ = [")
			f_def.write("\n")
			#write elements
			for element in lines[1:-1]:
				#TODO add #def handle
				# print(element)
				if '/*' in element:
					element = element[:element.index('/*')]
				if "#" in element or "//" in element or '*/' in element:
					continue
				# print(element)
				element = re.split("[ :]", element.strip()[:-1])
				# print(element)
				# print(element)
				element = filter(not_empty, element)
				# print(element)
				if len(element) == 0:
					continue 
				if "const" in element:
					element.remove("const")
				# print(element)
				assert(len(element) == 2 or len(element) == 3)
				element_name = element[1]
				try:
					element_type = type_converter[element[0]]
				except:
					element_type = element[0]
				if element_type == "PLMN_LIST_T(PLMN_LIST_MAX_SIZE)":
					element_type = "PLMN_LIST_T"
				if len(element) == 3:
					element_len = element[2]
					f_def.write("				('" + element_name + "'," + element_type + "," + element_len + "),")
					f_def.write("\n")
				elif len(element) == 2:
					if "*" in element_name:
						f_def.write("				('" + element_name[1:] + "', POINTER(" + element_type + ")),")
						f_def.write("\n")
					else:
						f_def.write("				('" + element_name + "'," + element_type + "),")
						f_def.write("\n")
			#write _fields_ end
			f_def.write("				]")
			f_def.write("\n")
			# print(lines)
			# break
		# f_def.close()
		# print(elements)

def list_files(path, s):
	files =os.listdir(path) 
	files.sort() 
	for file_ in files:     
	#    print(path +file_)
	    if not  os.path.isdir(path +file_):  
	        f_name = str(file_)
	#        print(f_name)
	        s.append(path + f_name)  
 

############################################################################
# M A I N
############################################################################
############################################################################
# F I L E  C L E A R
############################################################################
f_clear = open(file_write,"w")
f_clear.write("from ctypes import *\n")
bstring_str = '''
class tagbstring(Structure):
''' + print_method + '''
	_fields_ = [
				('mlen',c_int),
				('slen',c_int),
				('data',POINTER(c_ubyte)),
				]
bstring = POINTER(tagbstring)
AdditionalUpdateType = c_int
'''
emm_initial = '''
class emm_msg_header_t(Structure):
''' + print_method + '''
	_fields_ = [
				('protocol_discriminator', c_ubyte, 4),
				('security_header_type', c_ubyte, 4),
				('message_type', c_ubyte),
				]

'''

esm_initial = '''
class esm_msg_header_t(Structure):
''' + print_method + '''
	_fields_ = [
				('protocol_discriminator', c_ubyte, 4),
				('eps_bearer_identity', c_ubyte, 4),
				('procedure_transaction_identity', c_ubyte),
				('message_type', c_ubyte),
				]

'''

eps_protocol_discriminator_t_initial = '''
eps_protocol_discriminator_t = c_int

'''

eci_t = '''
class eci_t(Structure):
''' + print_method + '''
	_fields_ = [
				('enb_id', c_uint, 20),
				('cell_id', c_uint, 8),
				('empty', c_uint, 4),
				]
'''
as_stmsi_t = '''
class as_stmsi_t(Structure):
''' + print_method + '''
	_fields_ = [
				('mme_code', c_ubyte),
				('m_tmsi', c_uint),
				]
'''
plmn_t = '''
class plmn_t(Structure):
''' + print_method + '''
	_fields_ = [
				('mcc_digit2', c_ubyte, 4),
				('mcc_digit1', c_ubyte, 4),
				('mnc_digit3', c_ubyte, 4),
				('mcc_digit3', c_ubyte, 4),
				('mnc_digit2', c_ubyte, 4),
				('mnc_digit1', c_ubyte, 4),
				]
'''

PLMN_LIST_T = '''
class PLMN_LIST_T(Structure):
''' + print_method + '''
	_fields_ = [
				('n_plmns', c_ubyte),
				('plmn', plmn_t*6),
				]

'''

tai_t = '''
tac_t = c_ushort
class tai_t(Structure):
''' + print_method + '''
	_fields_ = [
				('plmn', plmn_t),
				('tac', tac_t),
				]

'''
ecgi_t = '''
class ecgi_t(Structure):
''' + print_method + '''
	_fields_ = [
				('plmn', plmn_t),
				('cell_identity', eci_t),
				]
'''
ksi_t = '''
ksi_t = c_ubyte
'''
tmsi_t = '''
tmsi_t = c_uint
'''
mme_gid_t = '''
mme_gid_t = c_ushort
'''
mme_code_t = '''
mme_code_t = c_ubyte
'''
gummei_t = '''
class gummei_t(Structure):
''' + print_method + '''
	_fields_ = [
				('plmn', plmn_t),
				('mme_gid', mme_gid_t),
				('mme_code', mme_code_t),
				]
'''
guti_t = '''
class guti_t(Structure):
''' + print_method + '''
	_fields_ = [
				('gummei', gummei_t),
				('m_tmsi', tmsi_t),
				]
'''
# leap_msg = '''
# class leap_msg(Structure):
# ''' + print_method + '''
# 	_fields_ = [
# 				('tag', c_ubyte),
# 				('length', c_int),
# 				('message', c_int),
# 				]
# '''





f_clear.write(bstring_str)
f_clear.write(emm_initial)
f_clear.write(esm_initial)
f_clear.write(eps_protocol_discriminator_t_initial)
f_clear.write(eci_t)
f_clear.write(as_stmsi_t)
f_clear.write(plmn_t)
f_clear.write(PLMN_LIST_T)
f_clear.write(tai_t)
f_clear.write(ecgi_t)
f_clear.write(ksi_t)
f_clear.write(tmsi_t)
f_clear.write(mme_gid_t)
f_clear.write(mme_code_t)
f_clear.write(gummei_t)
f_clear.write(guti_t)
f_clear.close()


############################################################################
# O P E N  F I L E
############################################################################
# f = open("/home/artifice/leap/src/nas/api/network/nas_message.h","r")
# f = open("/home/artifice/leap/src/nas/esm/msg/esm_msg.h","r")


# alllines = f.read()

# f.close()

# blocks = struct_union_pattern.findall(alllines)

# handle_def(blocks)


for path in paths:
	list_files(path, file_list)

file_list = additional_files + file_list

for file in file_list:
	with open(file,"r") as f:
		alllines = f.read()
	# print(alllines)
	blocks = struct_union_pattern.findall(alllines)
	# print(blocks)
	handle_def(blocks, alllines, file)