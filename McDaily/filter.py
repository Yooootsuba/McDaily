class Filter:

    def __init__(self, json):
        self.json = json

    def get_objects(self):
        if 'coupon' in self.json:
            for coupon in self.json['results']['coupon']:
                
