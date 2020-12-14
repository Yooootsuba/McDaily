import hashlib
import requests
from datetime import datetime, timedelta


from .filter import McDailyFilter


class McDailyAccount:

    def __init__(self):
        """ User info """
        self.username     = ''                                                     # Username
        self.password     = ''                                                     # Password
        self.access_token = ''                                                     # Token
        self.param_string = ''                                                     # username + password
        self.card_no      = ''                                                     # Card no

        """ System info """
        self.str1         = datetime.strftime(datetime.now(), '%Y/%m/%d %H:%M:%S') # Device Time
        self.str2         = '2.2.0'                                                # App Version
        self.str3         = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')      # Call time
        self.model_id     = 'Pixel XL'                                             # Model ID
        self.os_version   = '9'                                                    # Android OS Version
        self.platform     = 'Android'                                              # platform
        self.device_uuid  = 'device_uuid'                                          # Device Uuid
        self.order_no     = self.device_uuid + self.str3                           # Order No

        """ Request json data """
        self.json = {
            "access_token" : self.access_token,
            "source_info"  : {
                "app_version" : self.str2,
                "device_time" : self.str1,
                "device_uuid" : self.device_uuid,
                "model_id"    : self.model_id,
                "os_version"  : self.os_version,
                "platform"    : self.platform,
            }
        }

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

        response = requests.post('https://api.mcddaily.com.tw/login_by_mobile', json = json, headers = {'user-agent' : 'okhttp/3.10.0'})
        self.set_token(response.json()['results']['member_info']['access_token'])
        return response

    def set_token(self, access_token):
        self.access_token         = access_token
        self.json['access_token'] = access_token

    def get_card_query(self, card_no):
        self.card_no = card_no

        """ Mask = md5('Mc' + order_no + access_token + card_no + callTime + 'Donalds') """
        data = 'Mc%s%s%s%sDonalds' % (
            self.order_no,
            self.access_token,
            self.card_no,
            self.str3,
        )
        hash = hashlib.md5()
        hash.update(data.encode('utf-8'))

        json = {
            "OrderNo"      : self.order_no,
            "access_token" : self.access_token,
            "callTime"     : self.str3,
            "cardNo"       : self.card_no,
            "mask"         : mask.hexdigest(),
        }

        respones = requests.post('https://api.mcddaily.com.tw/queryBonus', json = json, headers = {'user-agent' : 'okhttp/3.10.0'})
        return respones

    def lottery_get_item(self):
        respones = requests.post('https://api1.mcddailyapp.com/lottery/get_item', json = self.json, headers = {'user-agent' : 'okhttp/3.10.0'})
        return McDailyFilter(respones.json()).get_object()

    def coupon_get_list(self):
        respones = requests.post('https://api1.mcddailyapp.com/coupon/get_list', json = self.json, headers = {'user-agent' : 'okhttp/3.10.0'})
        return McDailyFilter(respones.json()).get_object()

    def sticker_get_list(self):
        respones = requests.post('https://api1.mcddailyapp.com/sticker/get_list', json = self.json, headers = {'user-agent' : 'okhttp/3.10.0'})
        return McDailyFilter(respones.json()).get_object()

    def sticker_redeem(self):
        sticker_list = self.sticker_get_list()
        if len(sticker_list) < 6:
            return 'Just %d stickers' % len(sticker_list)

        sticker_id_list = []
        for i in range(6):
            sticker_id_list.append(sticker_list[i].sticker_id)

        json = self.json
        json['sticker_ids'] = sticker_id_list
        respones = requests.post('https://api1.mcddailyapp.com/sticker/redeem', json = json, headers = {'user-agent' : 'okhttp/3.10.0'})
        return McDailyFilter(respones.json()).get_object()
