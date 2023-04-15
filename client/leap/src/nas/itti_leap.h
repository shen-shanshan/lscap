
// #define FILE_NAS_ITTI_MESSAGING_SEEN
#include <stdint.h>

#include "bstrlib.h"
#include "assertions.h"
#include "log.h"
#include "msc.h"
#include "intertask_interface.h"
#include "3gpp_24.301.h"
#include "esm_proc.h"

int nas_itti_plain_msg(
  const char          *buffer,
  const nas_message_t *msg,
  const size_t         lengthP,
  const bool           is_down_link);
