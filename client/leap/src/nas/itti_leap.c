
#include <string.h>
#include <ctype.h>

#include "conversions.h"
#include "intertask_interface.h"
#include "msc.h"
#include "mme_app_ue_context.h"
#include "itti_leap.h"
#include "secu_defs.h"


// #define TASK_ORIGIN  TASK_NAS_MME

int
nas_itti_plain_msg (
  const char *buffer,
  const nas_message_t * msg,
  const size_t          length,
  const bool            is_down_link)
{
  return 1;
}