import sys


sys.path.append('.')
sys.path.append('..')


from McDaily.sticker import McDailySticker


json = {
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
}


sticker = McDailySticker(json)
