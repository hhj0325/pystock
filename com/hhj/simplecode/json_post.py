import requests
from datetime import datetime, timedelta

url = 'http://wj2c.jd.com/jingcheck/notifyCallBack'

body0 = {"sign": "E18529D88249CBE186057E8B67252806", "timestamp": "1535535455879",
         "venderNotifyOrderInfo": {"currentRefundFee": 10, "disCountFee": 32, "erpOrderId": 22, "notifyType": 1,
                                   "operateTime": 1535535454468, "orderFee": 111, "orderId": 1,
                                   "uniqueKey": "fdsafdsafds", "venderOrderId": "1111"}}

body1 = {
    "sign": "73881D93305ED05656F66D0372BD31BF",
    "timestamp": "1535615237507",
    "venderNotifyOrderInfo": {
        "currentRefundFee": None,
        "disCountFee": 32,
        "erpOrderId": 22,
        "notifyType": 1,
        "operateTime": 1535615208573,
        "orderFee": 23,
        "orderId": 1,
        "uniqueKey": None,
        "venderOrderId": "78436212"
    }
}

body2 = {
    "sign": "640583AAF6A88EF582DCFE8BD073413F",
    "timestamp": "1535616157755",
    "venderNotifyOrderInfo": {
        "currentRefundFee": 10,
        "disCountFee": 32,
        "erpOrderId": 22,
        "notifyType": 4,
        "operateTime": 1535616154776,
        "orderFee": 23,
        "orderId": 1,
        "uniqueKey": "56343&33",
        "venderOrderId": "78436212"
    }
}


headers = {'content-type': "application/json"}

# 这里有个细节，如果body需要json形式的话，需要做处理
# 可以是data = json.dumps(body)
# response = requests.post(url, data=json.dumps(body), headers=headers)
# 也可以直接将data字段换成json字段，2.4.3版本之后支持
response = requests.post(url, json=body2, headers=headers)

print(datetime.now())
# 返回信息
print(response.text)

# 返回响应头
print(response.status_code)

dt = datetime(2015, 4, 19, 12, 20)
dt = dt + timedelta(hours=10)
print(dt)
print(dt.timestamp())

