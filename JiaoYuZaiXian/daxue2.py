import spderdaxue as sp
import random
import requests
import json
import xlwt


def code_info():
    name_list = []
    code_list = []

    with open("/Users/apple/Desktop/学院名称.txt") as f1:
        u_name = f1.readlines()
    for name_line in u_name:
        name_line = name_line[0:-1]
        name_list.append(name_line)

    with open("/Users/apple/Desktop/学校代码.txt") as f2:
        u_code = f2.readlines()
    for code_line in u_code:
        code_line = code_line[0:-1]
        code_list.append(code_line)

    d_array = list(zip(name_list, code_list))
    print(d_array[0][0], d_array[0][1])
    print(len(d_array))
    return d_array


def spider_image():
    # "https://static-data.eol.cn/upload/logo/42.jpg"
    head_list = sp.header_list()
    Header = {'User-Agent': random.choice(head_list)}
    two_arr = code_info()

    for arr in two_arr:
        url = "https://static-data.eol.cn/upload/logo/" + arr[1] + ".jpg"
        res = requests.get(url, headers=Header)
        with open('/Users/apple/Desktop/code/unilogo/' + arr[0] + '.png', 'wb') as img:
            img.write(res.content)


def info_json():
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('高校信息', cell_overwrite_ok=True)
    # sheet.write(0, 0, '名称')
    # sheet.write(0, 1, '邮箱')
    # sheet.write(0, 2, '邮编')
    # sheet.write(0, 3, '网站')
    # sheet.write(0, 4, '电话')
    # sheet.write(0, 5, '创建时间')
    # sheet.write(0, 6, '学科')
    row_num = 1
    two_arr = code_info()
    d_list = []
    for arr in two_arr:
        url = "https://static-data.eol.cn/www/2.0/school/" + arr[1] + "/info.json"
        head_list = sp.header_list()
        Header = {'User-Agent': random.choice(head_list)}
        res = requests.get(url, headers=Header)
        text = res.content.decode('utf-8')
        json_res = json.loads(text)
        # print(json_res)
        # name = json_res['data']['name']
        # email = json_res['data']['email']
        # postcode = json_res['data']['postcode']
        # website = json_res['data']['school_site']
        # phone = json_res['data']['phone']
        # c_date = json_res['data']['create_date']

        dual_list = json_res['data']['dualclass']
        for dual in dual_list:
            d_list.append(dual['class'])
            d_list.append(',')
        # sheet.write(row_num, 0, name)
        # sheet.write(row_num, 1, email)
        # sheet.write(row_num, 2, postcode)
        # sheet.write(row_num, 3, website)
        # sheet.write(row_num, 4, phone)
        # sheet.write(row_num, 5, c_date)

        sheet.write(row_num, 6, d_list)
        row_num += 1
        d_list.clear()

    book.save(u'/Users/apple/Desktop/高校信息2.xls')
    # 'email': 'wlxxs@whu.edu.cn'
    # 'postcode': '430072'
    # 'school_site': 'http://www.whu.edu.cn/'
    # 'phone': '027-68754231'
    # 双一流学科：duaclass.get(class)


def no_reapt(ori_list=[]):
    new_list = []
    for n in ori_list:
        if n not in new_list:
            new_list.append(n)
            new_list.append(",")
    return new_list


def xueke():
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('高校信息', cell_overwrite_ok=True)
    sheet.write(0, 0, '名称')
    sheet.write(0, 1, '国家特色专业')
    sheet.write(0, 2, '所有专业')
    two_arr = code_info()
    row_num = 1
    one_list = []
    two_list = []
    for arr in two_arr:
        url = "https://static-data.eol.cn/www/2.0/school/" + arr[1] + "/pc_special.json"
        head_list = sp.header_list()
        HEADERS = {'User-Agent': random.choice(head_list)}
        resp = requests.get(url, headers=HEADERS)
        text = resp.content.decode("utf-8")
        json_res = json.loads(text)
        print(json_res)
        r1_list = json_res['data']['1']
        r2_list = json_res['data']['2']
        r3_list = json_res['data']['special_detail']['1']
        r4_list = json_res['data']['special_detail']['2']
        r5_list = json_res['data']['special']
        r6_list = json_res['data']['nation_feature']
        print(r3_list)
        print(r4_list)
        print(r5_list)
        print(r6_list)

        print("----------------1111---------------------")
        for r1 in r1_list:

            if r1['nation_feature'] == "1":
                one_list.extend((r1['special_name'], ","))
            else:
                two_list.extend((r1['special_name'], ","))

            print(r1['special_name'], r1['nation_feature'], r1['special_id'])
        print("-----------------222--------------------")
        for r2 in r2_list:
            if r2['nation_feature'] == "1":
                one_list.extend((r2['special_name'], ","))
            else:
                two_list.extend((r2['special_name'], ","))
            print(r2['special_name'], r2['nation_feature'], r2['special_id'])
        print("-----------------333--------------------")
        for r3 in r3_list:
            if r3['nation_feature'] == "1":
                one_list.extend((r3['special_name'], ","))
            else:
                two_list.extend((r3['special_name'], ","))
            print(r3['special_name'], r3['nation_feature'], r3['special_id'])
        print("-----------------444--------------------")
        for r4 in r4_list:
            if r4['nation_feature'] == "1":
                one_list.extend((r4['special_name'], ","))
            else:
                two_list.extend((r4['special_name'], ","))
            print(r4['special_name'], r4['nation_feature'], r4['special_id'])
        print("-----------------555--------------------")
        # for r5 in r5_list:
        #     if r5['special']['nation_feature'] == 1:
        #         one_list.append(r5['special_name'])
        #     print(r5['special_name'], r5['nation_feature'],r5['special_id'])
        print("-----------------666--------------------")
        for r6 in r6_list:
            if r6['nation_feature'] == "1":
                one_list.extend((r6['special_name'], ","))
            else:
                two_list.extend((r6['special_name'], ","))
            print(r6['special_name'], r6['nation_feature'], r6['special_id'])
        print("----------------LIST---------------------")
        # print(one_list)
        one_list = no_reapt(one_list)
        two_list = no_reapt(two_list)
        sheet.write(row_num, 0, arr[0])
        sheet.write(row_num, 1, one_list)
        sheet.write(row_num, 2, two_list)
        row_num += 1
        one_list.clear()
        two_list.clear()
    book.save(u'/Users/apple/Desktop/高校信息4.xls')


if __name__ == "__main__":
    # spider_image()
    # info_json()
    xueke()
