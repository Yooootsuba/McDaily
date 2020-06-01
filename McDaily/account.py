import hashlib
import requests
from datetime import datetime, timedelta


class McDailyAccount:

    def __init__(self):
        """ User info """
        self.username     = ''                                                     # Username
        self.password     = ''                                                     # Password
        self.access_token = ''                                                     # Token
        self.param_string = ''                                                     # username + password

        """ System info """
        self.str1         = datetime.strftime(datetime.now(), '%Y/%m/%d %H:%M:%S') # Device Time
        self.str2         = '2.2.0'                                                # App Version
        self.str3         = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')      # Call time
        self.model_id     = 'MIX 3'                                                # Model ID
        self.os_version   = '9'                                                    # Android OS Version
        self.platform     = 'Android'                                              # platform
        self.device_uuid  = 'device_uuid'                                          # Device Uuid
        self.order_no     = self.device_uuid + self.str3                           # Order No

    def login(self, username, password):
        self.username     = username
        self.password     = password
        self.param_string = username + password

        """ Mask = md5('Mc' + order_no + platform + os_version + model_id + device_uuid + str1 + str2 + param_string + 'Donalds') """
        data = 'Mc%s%s%s%s%s%s%s%sDonalds' % (
            self.order_no,
            self.platform,
            self.os_version,
            self.model_id,
            self.device_uuid,
            self.str1,
            self.str2,
            self.param_string
        )
        hash = hashlib.md5()
        hash.update(data.encode('utf-8'))

        json = {
            "account"     : self.username,
            "password"    : self.password,
            "OrderNo"     : self.order_no,
            "mask"        : hash.hexdigest(),
            "source_info" : {
                "app_version" : self.str2,
                "device_time" : self.str1,
                "device_uuid" : self.device_uuid,
                "model_id"    : self.model_id,
                "os_version"  : self.os_version,
                "Platform"    : self.platform,
            }
        }

        response = requests.post('https://api.mcddaily.com.tw/login_by_mobile', json = json)
        self.set_token(response.json()['results']['member_info']['access_token'])
        return response

    def set_token(self, access_token):
        self.access_token = access_token
