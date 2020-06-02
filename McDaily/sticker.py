from datetime import datetime


class McDailySticker:

    def __init__(self, json):
        self.sticker_id          = json['sticker_id']
        self.redeem_end_datetime = datetime.strptime(json['object_info']['expire_datetime'], '%Y/%m/%d %H:%M:%S')
        self.current_datetime    = datetime.now()

    def __repr__(self):
        return str(self.sticker_id)
