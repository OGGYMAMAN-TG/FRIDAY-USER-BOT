# Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/IRASH1234567 >.
#
# This file is part of < https://github.com/irash1234567/FRIDAY-USER-BOT > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/irash1234567/FRIDAY-USER-BOT/blob/master/LICENSE >
#
# All rights reserved.

import logging

from main_startup import mongo_client
from main_startup.config_var import Config

db_x = mongo_client["Friday"]
