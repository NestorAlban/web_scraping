import requests
import lxml.html as html
import os
import datetime

HOME_URL = 'https://www.larepublica.co/'

XPATH_LINK_TO_ARTICLE = '//text-fill[not(@class)]/a/@href'
XPATH_LINK_TO_ARTICLE2 = '//h2[@class]/a/@href'
XPATH_TITLE = '//div[@class="col-8 order-2 d-flex flex-column"]/div[@class="mb-auto"]/h2[last()]/span/text()'
XPATH_SUMMARY = '//div[@class="lead"]/p[1]/text()'
XPATH_BODY = '//div[@class="html-content"]/p[not(@class)]/text()'


def parse_notice(link, today):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            notice = response.content.decode('utf-8')
            parsed = html.fromstring(notice)

            try:
                title = parsed.xpath(XPATH_TITLE)[0]
                title = title.strip()
                title = title.replace('\"', '')
                title = title.replace('“', '')
                title = title.replace('?', '')
                title = title.replace('¿', '')
                summary = parsed.xpath(XPATH_SUMMARY)[0]
                body = parsed.xpath(XPATH_BODY)
            except IndexError:
                return
            print(link)
            print(title)
            with open(f'{today}/{title}.txt', 'w', encoding = 'utf-8') as f:
                f.write(title)
                f.write('\n\n')
                f.write(summary)
                f.write('\n\n')
                for p in body:
                    f.write(p)
                    f.write('\n')
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)

def parse_home():
    try:
        response = requests.get(HOME_URL)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            notices_links = parsed.xpath(XPATH_LINK_TO_ARTICLE)
            notices_links2 = parsed.xpath(XPATH_LINK_TO_ARTICLE2)
            print(notices_links)
            today = datetime.date.today().strftime('%d-%m-%Y')
            
            if not os.path.isdir(today):
                os.mkdir(today)
                print("=========nkdir done============")
            for link in notices_links:
                parse_notice(link, today)
                print("=========link done============")
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)


def run():
    parse_home()

if __name__ == '__main__':
    run()
