#!/usr/bin/env python3

import utils.helper
import utils.storage
import utils.steam
import config
import sys
import os
import json
from io import BytesIO

"""
export STORAGE_TYPE="object"
export STORAGE_OBJECT_ENDPOINT="http://localhost:9000"
export STORAGE_OBJECT_BUCKET="steamcmd"
export STORAGE_OBJECT_SECRET_KEY="steamcmd"
export STORAGE_OBJECT_ACCESS_KEY="steamcmd"
export STORAGE_OBJECT_SECURE="False"
"""

apps = utils.storage.list("app/")
