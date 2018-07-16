from selenium import webdriver
import time
from PIL import Image

# sku id
skus = [1938010, 1950749, 1938009]

browser_path = "D:\\dong\\driver\\chromedriver.exe"
user_name = "222402ZMD111"
pass_word = "111@aaa"
url_1 = "https://jw.jd.com"
url_2 = "https://jwsl.jd.com/qrcode/qrcode?sku="
img_path = "D:\\image\\"

left = 784 / 2 - 101
top = 668 / 2 - 101
right = 291 + 202
bottom = 233 + 202

browser = webdriver.Chrome(browser_path)
browser.set_window_size(800, 800)
browser.get(url_1)
time.sleep(3)

# 切换为账户登录
browser.find_element_by_class_name("login-tab-r").click()
time.sleep(1)
print("change tab")

browser.find_element_by_id("loginname").send_keys(user_name)
browser.find_element_by_id("nloginpwd").send_keys(pass_word)
# 观察是否需要写验证码
time.sleep(5)
# 提交
browser.find_element_by_id("loginsubmit").click()
print("login")
time.sleep(2)
for sku in skus:
    browser.get(url_2 + str(sku))
    time.sleep(1)
    # 保存浏览器截图
    temp_img_path = img_path + str(sku) + ".png"
    browser.get_screenshot_as_file(temp_img_path)
    time.sleep(2)
    print("download:" + str(sku))
    # 裁剪图片
    im = Image.open(temp_img_path)
    im = im.crop((left, top, right, bottom))
    im.save(temp_img_path)
    print("crop:" + str(sku))

browser.quit()


