#!/usr/bin/env python3

from Main import Moguding
import os
import json
import sys

phone_Key = os.environ['PHONE']
password_Key = os.environ['PASSWORD']
address_Key = os.environ['ADDRESS']

try:
    Md = Moguding(phone_Key, password_Key, address_Key)
    Md.run()
    Md.actions
except KeyError:
    print('Plase check username or password.')

