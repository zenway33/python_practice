import random

def get_header():
    headers = {'Accept': 'text/html,application/xhtml+xml,applicatiaaon/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'close'}
    headers['User-Agent'] = 'Mozilla/{0}.{1} (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/{2}.0.1271.64 Safari/537.{3}'.format(random.randint(1,9), random.randint(1,9), random.randint(10,30), random.randint(1,20))
    return headers

for i in range(1,100):
        print(i)
        headers = get_header()
        print(headers)
