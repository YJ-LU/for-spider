import time
import requests
import json
import random
import xlwt


def header_list():
    # 设置请求头
    user_agent = [
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
        "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
        "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
        "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
        "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
        "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
        "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
        "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
        "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
        "UCWEB7.0.2.37/28/999",
        "NOKIA5700/ UCWEB7.0.2.37/28/999",
        "Openwave/ UCWEB7.0.2.37/28/999",
        "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
        "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",

    ]
    return user_agent


if __name__ == '__main__':

    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('高校信息', cell_overwrite_ok=True)

    font = xlwt.Font()  # Create Font
    font.bold = True  # Set font to Bold
    font.name = u'宋体 (正文)'
    font.height = 20 * 11
    style = xlwt.XFStyle()  # Create Style
    style.font = font  # Add Bold Font to Style

    sheet.write(0, 0, '学校名称', style)
    sheet.write(0, 1, '学校类别', style)  # 普通本科 level_name
    sheet.write(0, 2, '学校类型', style)  # 综合类/理工类 type_name
    sheet.write(0, 3, '办理类型', style)  # 公办/名办 nature_name
    sheet.write(0, 4, '211工程', style)  # f211 1
    sheet.write(0, 5, '985工程', style)  # f985 1
    sheet.write(0, 6, '双一流大学', style)  # dual class 双一流
    sheet.write(0, 7, '强基计划', style)
    sheet.write(0, 8, '一流大学建设高校A类', style)
    sheet.write(0, 9, '归属', style)  # belong
    sheet.write(0, 10, '省份', style)  # province_name
    sheet.write(0, 11, '城市', style)  # city_name
    sheet.write(0, 12, '区', style)  # country_name
    sheet.write(0, 13, '地址', style)  # address
    sheet.write(0, 14, '官方网址', style)  # address
    sheet.write(0, 15, '官方电话', style)  # address
    sheet.write(0, 16, '电子邮箱', style)  # school_id
    sheet.write(0, 17, '国家特色专业', style)  # school_id
    sheet.write(0, 18, '创办时间', style)  # school_id
    sheet.write(0, 19, '学校代码', style)  # school_id

    T = True
    i = 1
    while T:
        url = f"""https://api.eol.cn/gkcx/api/?access_token=&admissions=&central=&department=&dual_class=&is_doublehigh=&is_dual_class=&keyword=&nature=&page={i}&province_id=42&ranktype=&request_type=1&school_type=&signsafe=&size=20&sort=view_total&top_school_id=[2858]&type=&uri=apidata/api/gk/school/lists"""

        head_list = header_list()
        HEADERS = {'User-Agent': random.choice(head_list)}
        # request = Request(url, headers=HEADERS)
        resp = requests.get(url, headers=HEADERS)
        html = resp.content.decode('utf-8')

        bbb = json.loads(html)
        print(bbb['message'])
        list = bbb['data']['item']
        if len(list) > 0:
            print(len(list), list)
            count = 0
            for item in list:
                value = ((
                    item['name'],
                    item['level_name'],
                    item['type_name'],
                    item['nature_name'],
                    item['f211'],
                    item['f985'],
                    item['dual_class_name'],
                    item['belong'],
                    item['province_name'],
                    item['city_name'],
                    item['county_name'],
                    item['address'],
                    item['school_id']
                ))
                k = 20 * (i-1) + 1
                sheet.write(count + k, 0, value[0])
                sheet.write(count + k, 1, value[1])
                sheet.write(count + k, 2, value[2])
                sheet.write(count + k, 3, value[3])

                if value[4] == 1:
                    sheet.write(count + k, 4, "是")
                else:
                    sheet.write(count + k, 4, "否")

                if value[5] == 1:
                    sheet.write(count + k, 5, "是")
                else:
                    sheet.write(count + k, 5, "否")

                if value[6] == '双一流':
                    sheet.write(count + k, 6, "双一流大学")
                else:
                    sheet.write(count + k, 6, value[6])

                sheet.write(count + k, 9, value[7])
                sheet.write(count + k, 10, value[8])
                sheet.write(count + k, 11, value[9])
                sheet.write(count + k, 12, value[10])
                sheet.write(count + k, 13, value[11])
                sheet.write(count + k, 19, value[12])
                count += 1
                print(value)

        print('当前完成爬取页面数：', i)
        T = True
        # T = False
        time.sleep(5)
        i += 1
        if i > 7:
            T = False
            print('结束爬取，结束页面数：', i)
        book.save(u'/Users/apple/Desktop/高校信息.xls')
