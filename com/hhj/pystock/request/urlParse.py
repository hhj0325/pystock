import urllib.parse
str = "?jsonpCallback=a&positionId=1&rightQueryStr=%7B%22pmInfoId%22%3A%220%22%2C%22productId%22%3A%220%22%2C%22orderCode" \
      "%22%3A%220%22%2C%22merchantId%22%3A%17727%22%2C%22positionId%22%3A%221%22%2C%22mcSiteId%22%3A%223%22%2C%22sellerType" \
      "%22%3A%220%22%7D&merchantId=17727&cid=260035504592f5a55560947c2a041db8cefde9935&sellerType=0"

de = urllib.parse.unquote(str)
print(de)