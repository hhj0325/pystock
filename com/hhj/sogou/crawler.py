"""
爬虫部分
"""
import re

import pandas as pd
import random
import time
import requests
import numpy as np
import bs4 as BeautifulSoup
head = """
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding:gzip, deflate
Accept-Language:zh-CN,zh;q=0.9
Connection:keep-alive
Host:weixin.sogou.com
Referer:'http://weixin.sogou.com/',
Upgrade-Insecure-Requests:1
User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36
"""

# 不包含SNUID值
cookie = "Cookie:ABTEST=0|1543475822|v17; IPLOC=CN4201; SUID=A27BF9DC2613910A000000005BFF926E; SUV=1543475811749084; browerV=2; osV=1; sct=1;"


def get_proxies(i):
    """
    获取代理IP
    """
    df = pd.read_csv('sg_effective_ip.csv', header=None, names=["proxy_type", "proxy_url"])
    proxy_type = ["{}".format(i) for i in np.array(df['proxy_type'])]
    proxy_url = ["{}".format(i) for i in np.array(df['proxy_url'])]
    proxies = {proxy_type[i]: proxy_url[i]}
    return proxies


def get_cookies_snuid():
    """
    获取SNUID值
    """
    time.sleep(float(random.randint(2, 5)))
    url = "http://weixin.sogou.com/weixin?type=2&s_from=input&query=python&ie=utf8&_sug_=n&_sug_type_="
    headers = {"Cookie": "ABTEST=0|1543475822|v17; IPLOC=CN4201; SUID=A27BF9DC2613910A000000005BFF926E; SUV=1543475811749084; browerV=2; osV=1; sct=1"}
    # HEAD请求,请求资源的首部
    response = requests.head(url, headers=headers).headers
    result = re.findall('SNUID=(.*?); expires', response['Set-Cookie'])
    SNUID = result[0]
    return SNUID


def str_to_dict(header):
    """
    构造请求头,可以在不同函数里构造不同的请求头
    """
    header_dict = {}
    print(header)
    print('------')
    header = header.split('\n')
    print(header)
    print('------')

    for h in header:
        h = h.strip()
        if h:
            print(h)
            k, v = h.split(':', 1)
            header_dict[k] = v.strip()
    return header_dict


def get_message():
    """
    获取网页相关信息
    """
    failed_list = []
    for i in range(1, 101):
        print('第' + str(i) + '页')
        print(float(random.randint(15, 20)))
        # 设置延时,这里是度娘查到的,说要设置15s延迟以上,不会被封
        time.sleep(float(random.randint(15, 20)))
        # 每10页换一次SNUID值
        if (i-1) % 10 == 0:
            value = get_cookies_snuid()
            snuid = 'SNUID=' + value + ';'
        # 设置Cookies
        cookies = cookie + snuid
        url = 'http://weixin.sogou.com/weixin?query=python&type=2&page=' + str(i) + '&ie=utf8'
        host = cookies + '\n'
        header = head + host
        headers = str_to_dict(header)
        # 设置代理IP
        proxies = get_proxies(i)
        try:
            response = requests.get(url=url, headers=headers, proxies=proxies)
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            data = soup.find_all('ul', {'class': 'news-list'})
            lis = data[0].find_all('li')
            for j in (range(len(lis))):

                h3 = lis[j].find_all('h3')
                #print(h3[0].get_text().replace('\n', ''))
                title = h3[0].get_text().replace('\n', '').replace(',', '，')

                p = lis[j].find_all('p')
                #print(p[0].get_text())
                article = p[0].get_text().replace(',', '，')

                a = lis[j].find_all('a', {'class': 'account'})
                #print(a[0].get_text())
                name = a[0].get_text()

                span = lis[j].find_all('span', {'class': 's2'})
                cmp = requests.findall("\d{10}", span[0].get_text())
                #print(time.strftime("%Y-%m-%d", time.localtime(int(cmp[0]))) + '\n')
                date = time.strftime("%Y-%m-%d", time.localtime(int(cmp[0])))

                with open('sg_articles.csv', 'a+', encoding='utf-8-sig') as f:
                    f.write(title + ',' + article + ',' + name + ',' + date + '\n')
            print('第' + str(i) + '页成功')
        except Exception as e:
            print('第' + str(i) + '页失败')
            failed_list.append(i)
            continue
    # 获取失败页码
    print(failed_list)


def main():
    get_message()


if __name__ == '__main__':
    main()
