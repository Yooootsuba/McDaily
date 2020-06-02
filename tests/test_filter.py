import sys


sys.path.append('.')
sys.path.append('..')


from McDaily.filter  import McDailyFilter
from McDaily.coupon  import McDailyCoupon
from McDaily.sticker import McDailySticker


json = {
    "rc" : 1 ,
    "results" :{
        "coupons" :[
            {
                "coupon_id" : 1265521127 ,
                "object_info" :{
                    "image" :{
                        "height" : 1920 ,
                        "url" : "https://mcdapp1.azureedge.net/P_G10401.jpg" ,
                        "width" : 1080
                    } ,
                     "object_id" : 352 ,
                     "redeem_end_datetime" : "2020/06/04 23:59:59" ,
                     "title" : "買任一超值全餐送酥嫩鷄翅_ G10401"
                },
                "status":1,
                "type":"coupon"
            },
            {
                "coupon_id" : 1264306815 ,
                "object_info" :{
                    "image" :{
                        "height" : 1920 ,
                        "url" : "https://mcdapp1.azureedge.net/P_G50601.jpg" ,
                        "width" : 1080
                    } ,
                     "object_id" : 398 ,
                     "redeem_end_datetime" : "2020/06/03 23:59:59" ,
                     "title" : "單點薯餅加1元多1份(G50601) "
                },
                "status":1,
                "type":"coupon"
            },
            {
                "coupon_id" : 1261533040 ,
                "object_info" :{
                    "image" :{
                        "height" : 1920 ,
                        "url" : "https://mcdapp1.azureedge.net/P_G20101.png" ,
                        "width" : 1080
                    } ,
                     "object_id" : 358 ,
                     "redeem_end_datetime" : "2020/05/31 23:59:59" ,
                     "title" : "四塊麥克鷄塊單點買一送一_G20101 "
                },
                "redeem_datetime":"2020/05/31 21:28:04",
                "status":2,
                "type":"coupon"
            },
            {
                "coupon_id" : 1260133703 ,
                "object_info" :{
                    "image" :{
                        "height" : 1920 ,
                        "url" : "https://mcdapp1.azureedge.net/P_G11901.jpg" ,
                        "width" : 1080
                    } ,
                     "object_id" : 530 ,
                     "redeem_end_datetime" : "2020/05/29 23:59:59" ,
                     "title" : "買任一超值全餐送蘋果派"
                },
                "status":1,
                "type":"coupon"
            }
        ],
        "current_datetime":"2020/06/02 10:17:43"
    },
    "rm":"成功"
}


filter = McDailyFilter(json)
coupon_list = filter.get_object()
print(coupon_list)


json = {
    "rc" : 1 ,
    "results" :{
        "stickers" :[
            {
                "object_info" :{
                    "expire_datetime" : "2020/06/30 23:59:59" ,
                    "image" :{
                        "height" : 300 ,
                        "url" : "https://mcdapp1.azureedge.net/sticker_01.png" ,
                        "width" : 300
                    } ,
                     "object_id" : 18 ,
                     "title" : "歡樂貼(0)"
                },
                "obtain_datetime":"2020/05/28 00:06:36",
                "status":1,
                "sticker_id":617569212,
                "type":"sticker"
            },
            {
                "object_info" :{
                    "expire_datetime" : "2020/06/30 23:59:59" ,
                    "image" :{
                        "height" : 300 ,
                        "url" : "https://mcdapp1.azureedge.net/sticker_01.png" ,
                        "width" : 300
                    } ,
                     "object_id" : 18 ,
                     "title" : "歡樂貼(0)"
                },
                "obtain_datetime":"2020/05/30 00:40:44",
                "status":1,
                "sticker_id":618115825,
                "type":"sticker"
            },
            {
                "object_info" :{
                    "expire_datetime" : "2020/06/30 23:59:59" ,
                    "image" :{
                        "height" : 300 ,
                        "url" : "https://mcdapp1.azureedge.net/sticker_01.png" ,
                        "width" : 300
                    } ,
                     "object_id" : 18 ,
                     "title" : "歡樂貼(0)"
                },
                "obtain_datetime":"2020/05/31 00:16:40",
                "status":1,
                "sticker_id":618686779,
                "type":"sticker"
            }
        ]
    },
    "rm":"成功"
}


filter = McDailyFilter(json)
sticker_list = filter.get_object()
print(sticker_list)
