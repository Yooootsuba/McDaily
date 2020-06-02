import sys


sys.path.append('.')
sys.path.append('..')


from McDaily.coupon import McDailyCoupon


json = {
    "rc" : 1 ,
    "results" :{
        "coupon" :{
            "coupon_id" : 2147483647 ,
            "object_info" :{
                "content" : "今日已領過，明日驚喜等著你！" ,
                "image" :{
                    "height" : 1920 ,
                    "url" : "https://mcdapp1.azureedge.net/ccrotbJmNrxfvvc7iYXZ.jpg" ,
                    "width" : 1080
                } ,
                 "object_id" : 2147483647 ,
                 "redeem_end_datetime" : "2020/05/27 08:54:08" ,
                 "title" : "今日已領過，明日驚喜等著你！"
            },
            "redeem_datetime":"2020/05/27 08:54:08",
            "status":1,
            "type":"coupon"
        },
        "current_datetime":"2020/05/27 08:54:08 "
    },
    " rm" :"今日已領過，明日驚喜等著你！"
}


coupon = McDailyCoupon(json['results']['coupon'])
