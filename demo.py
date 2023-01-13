Skip to content
Search or jump to…
Pull requests
Issues
Codespaces
Marketplace
Explore
 
@yangdongfang 
yangdongfang
/
python3_spider
Public
forked from wistbean/learn_python3_spider
Cannot fork because you own this repository and are not a member of any organizations.
Code
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
python3_spider/dangdang_top_500.py /
@wistbean
wistbean fix dangdang_top_500
Latest commit e921852 on Oct 21, 2021
 History
 1 contributor
49 lines (38 sloc)  1.42 KB

import requests
import re
import json


def request_dandan(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException as e:
        print(e)
        return None


def parse_result(html):
    pattern = re.compile(
        '<li.*?list_num.*?(\d+)\.</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span class="price_n">(.*?)</span>.*?</li>', re.S)
    items = re.findall(pattern, html)

    for item in items:
        yield {
            'range': item[0],
            'image': item[1],
            'title': item[2],
            'recommend': item[3],
            'author': item[4],
            'times': item[5],
            'price': item[6]
        }


def write_item_to_file(item):
    print('开始写入数据 ====> ' + str(item))
    with open('book.txt', 'a', encoding='UTF-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')


def main(page):
    url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-' + str(page)
    html = request_dandan(url)
    items = parse_result(html)  # 解析过滤我们想要的信息
    for item in items:
        write_item_to_file(item)


if __name__ == "__main__":
    for i in range(1, 26):
        main(i)
Footer
© 2023 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
python3_spider/dangdang_top_500.py at master · yangdongfang/python3_spider
