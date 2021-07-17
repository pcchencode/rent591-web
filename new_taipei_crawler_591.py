import pandas as pd
import random
import os
from selenium import webdriver  # 從library中引入webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from fake_useragent import UserAgent # !pip install fake-useragent
from selenium.webdriver.chrome.options import Options
import time
import urllib
from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient

options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values':
        {
            'notifications': 2
        }
}
options.add_experimental_option('prefs', prefs)  # 關閉瀏覽器的提示
options.add_argument("disable-infobars")  # 關閉瀏覽器正受到軟體自動測試提示

browser = webdriver.Chrome('./chromedriver', chrome_options=options)
browser.get("https://rent.591.com.tw/?kind=0&region=1") #591不讓你一開始就連進去台北市
browser.find_element_by_id('area-box-close').click()
browser.get("https://rent.591.com.tw/?kind=0&region=3") #直接進去新北市
time.sleep(3)
#獲取總頁數
page_num = int(browser.find_elements_by_xpath('//*[@id="container"]/section[5]/div/div[1]/div[5]/div/a[7]')[0].text)

# 開始爬所有 room_url
room_url_list = []
# page_num = 3 #先試爬3頁就好
for i in range(1, page_num+1):
    #輸入 ESC 關閉google 提示，否則無法點選
    #browser.find_element_by_class_name('pageNext').send_keys(Keys.ESCAPE) #ECS鍵
    next_page_button = browser.find_element_by_xpath('//*[@class="pageNext"]')
    next_page_button = browser.find_element_by_class_name("pageNext")
    print(i)
    next_page_button.click()
    time.sleep(10)
    bs = BeautifulSoup(browser.page_source, 'html.parser')
    titles=bs.findAll('h3') # h3 放置物件的區塊
    for title in titles:
        room_url=title.find('a').get('href') # 每個物件的 url
        room_url = 'https:'+room_url.strip()
        room_url_list.append(room_url)
        #print(room_url)
        #break

# 開爬，並將數據存入 mongoDB
myclient = MongoClient('localhost', 27017) #連入本地端mongoDB
# mongo 是惰性的，沒有插入資料之前不會真的創建 database, collection
db = myclient['rent_591']
col = db['room_object']
for url in room_url_list:
    # 針對 room_url 搜尋物件相關資訊
    region = "新北市"
    print(region)
    print(url)
    browser.get(url)
    # 固話(手機為圖片檔，所以只抓固話)
    phone = browser.find_element_by_xpath('//*[@id="hid_tel"]').get_attribute('value')
    print(phone)
    
    # 出租者
    renter = browser.find_elements_by_xpath('//*[@id="main"]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/i')[0].text
    print(renter)
    # 出租者類型
    renter_info = browser.find_elements_by_xpath('//*[@id="main"]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]')[0].text
    renter_type = renter_info.replace(renter, '')
    # renter_type = renter_type.replace("\n","")
    #renter_type = renter_type[renter_type.find('(')+1:renter_type.find('(')+3]
    renter_type = renter_type[2:4]
    print(renter_type)

    # 其他欄位資訊會變動，必須用 bs
    res=requests.get(url)
    bs=BeautifulSoup(res.text,'html.parser')
    room_attrs = bs.find('ul',{'class':'attr'}).findAll('li')
    for attr in room_attrs:
        if attr.text.split('\xa0:\xa0\xa0')[0]=='型態':
            obj_type=attr.text.split('\xa0:\xa0\xa0')[1]
        elif attr.text.split('\xa0:\xa0\xa0')[0]=='現況':
            status=attr.text.split('\xa0:\xa0\xa0')[1]
    # print(room_attrs)
    print(obj_type)
    print(status)

    r_d_1 = []
    room_desc1 = bs.find('li',{'class':'clearfix'}).findAll('div',{'class':'one'})
    for description in room_desc1:
        r_d_1.append(description.text)
        #print(description.text)

    r_d_2 = []
    room_desc2 = bs.find('li',{'class':'clearfix'}).findAll('div',{'class':'two'})
    for description in room_desc2:
        r_d_2.append(description.text.split('：')[1])
        #print(description.text)

    # 詳細資訊的區塊難抓取，直接抓成dict
    room_desc_dict = dict(zip(r_d_1, r_d_2))
    #print(room_desc_dict)

    # 性別要求
    if '性別要求' in room_desc_dict:
        gender_req = room_desc_dict['性別要求']
    else:
        gender_req = ''
    print(gender_req)
    
    dic = {
        'region':region,
        'room_url':url,
        'phone':phone,
        'renter':renter,
        'renter_type':renter_type,
        'obj_type':obj_type,
        'status':status,
        'gender_req':gender_req
    }
    col.insert_one(dic)
    print("inserted into mongoDB")
    time.sleep(2)

browser.close()
