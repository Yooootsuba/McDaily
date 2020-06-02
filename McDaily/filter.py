from .coupon  import McDailyCoupon
from .sticker import McDailySticker


class McDailyFilter:

    def __init__(self, json):
        self.json = json

    def get_object(self):
        if   'coupon'  in self.json['results']:
            return self.coupon()
        elif 'coupons' in self.json['results']:
            return self.coupons()
        elif 'sticker' in self.json['results']:
            return self.sticker()
        else:
            return self.stickers()

    def coupon(self):
        return McDailyCoupon(self.json['results']['coupon'])

    def coupons(self):
        coupon_list = []
        for json in self.json['results']['coupons']:
            coupon_list.append(McDailyCoupon(json))
        return coupon_list

    def sticker(self):
        return McDailySticker(self.json['results']['sticker'])

    def stickers(self):
        sticker_list = []
        for json in self.json['results']['stickers']:
            sticker_list.append(McDailySticker(json))
        return sticker_list
