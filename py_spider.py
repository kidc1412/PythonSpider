import requests

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132'
                      ' Safari/537.36',
        'Host': 'www.66ys.tv',
        'Referer': 'http://www.66ys.tv/',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }

# url = 'http://www.66ys.tv/'
url = 'http://www.66ys.tv/dongzuopian/20180220/36528.html'
response = requests.get(url, headers)
response.encoding = 'gb18030'
if response.status_code == 200:
    with open('D:/66ys.html', 'w', encoding='gb18030') as f:
        f.write(response.text)
        f.close()
        print('done!')