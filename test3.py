
from bs4 import BeautifulSoup
import requests
import urllib.request
import wget
import os
import json



# 建立一个目录:
path = os.getcwd()
path = os.path.join(path,'baozou2016')
if not os.path.exists(path):
  os.mkdir(path)


'''
# 调试打印单页的相关图片;

#urls = 'http://baozoumanhua.com/catalogs/gif?page=1'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text, 'html.parser')

titles = soup.select('div.article-content > h4 > a[target="_blank"]')
imgs = soup.select('div.article-content > video')


# 打印标题及图表相关的信息,并构造成字典
for title,img in zip(titles,imgs):
    data = {
        'title' :title.get_text(),
        'img_url' :img.get('data-original-image-url')
    }

    print(data)
    #title = print(data['title'])
    #url = print(data['img_url'])

'''

def download(img_url):
    r = requests.get(img_url, stream = True)
    if r.status_code != 200:
        return

    with open(img_name, "wb") as fs:
        fs.write(r.content)

    print("%s => %s" % (img_url, path))

#构建函数获取页面相关的图片.
def get_page_within(pages):
    for page_num in  range(1,pages+1):
        wb_data = requests.get('http://baozoumanhua.com/catalogs/gif?page={}'.format(page_num))
        soup = BeautifulSoup(wb_data.text, 'html.parser')
        titles = soup.select('div.article-content > h4 > a[target="_blank"]')
        imgs = soup.select('div.article-content > video')

        for title,img in zip(titles,imgs):
            data = {
                'title' :title.get_text(),
                'img_url' :img.get('data-original-image-url')
            }
            print(data)
            img_url = data['img_url']
            img_name = data['title'] + '.gif'
            download(img_url)

    #print('woo ... %d pages done' % pages)


get_page_within(1)






'''
for img_url in img_urls:
    img = requests.get(img_url,stream = True)
    print(img)
'''


'''
def dl_image(url):
    urllib.request.urlretrieve(url)
    print('Done')


for img_url in get_page_within(10):
    #print(data['img_url'])
    #dl_image(url)

'''


'''
/usr/local/bin/python3 /Users/netseek/github/python_practice/test1.py
{'title': '这体重，一会怎么救上来', 'img': 'http://wanzao2.b0.upaiyun.com/system/pictures/36074785/original/1464255479_240x131.gif'}
{'title': '放上点特效就是不一样的画风了', 'img': 'http://wanzao2.b0.upaiyun.com/system/pictures/36072280/original/1464243973_400x283.gif'}
{'title': '睡一觉起来感觉好饿。随便吃点吧！', 'img': 'http://wanzao2.b0.upaiyun.com/system/pictures/36073551/original/1464250611_440x303.gif'}
{'title': '宝宝好困。宝宝要睡觉！', 'img': 'http://wanzao2.b0.upaiyun.com/system/pictures/36073503/original/1464250382_350x229.gif'}
{'title': '你这是侮辱佛门 还是侮辱自己 替表演者感到羞愧！', 'img': 'http://wanzao2.b0.upaiyun.com/system/pictures/36073802/original/1464251597_320x240.gif'}
{'title': '有谁试过', 'img': 'http://wanzao2.b0.upaiyun.com/system/pictures/36071341/original/1464239840_233x413.gif'}
{'title': '机智。', 'img': 'http://wanzao2.b0.upaiyun.com/system/pictures/36071680/original/1464241151_400x207.gif'}
{'title': '叫你买个好的女朋友。', 'img': 'http://wanzao2.b0.upaiyun.com/system/pictures/36071797/original/1464241611_300x299.gif'}

Process finished with exit code 0

'''