import os
import csv
import requests
from bs4 import BeautifulSoup


# 数据保存为csv文件
def SaveDataToCSV(row, filename='temp', path='Spider_dushi'):
    fpath = os.path.join(path, filename);
    with open(fpath, "a", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(row)
    
# 保存文件
def SaveData(text, filename='temp', path='Spider_dushi'):
    fpath = os.path.join(path, filename)
    with open(fpath, 'a', encoding="utf-8") as  f:
        f.write(text)
        
# 保存到数据库
def SaveDataToMysql(text):
    return;
    
# 从链接中获取所有基本信息
def ParseInfoByHref(href):
    resp = requests.get(href)
    page = resp.content.decode("utf-8")
    page_bs = BeautifulSoup(page, "lxml")
    page_main = page_bs.find("div",class_="main")
    
    # 地址 电话 微信 qq 营业时间 服务项目 人员数量 会员贡献 简介
    spa_name = page_bs.find("h1", class_="shop-name").string
    page_other = page_bs.find("div", class_="other J-other")
    all_span_tag = page_other.find_all("span")
    address = all_span_tag[1].string
    phone   = all_span_tag[3].string
    weixin  = all_span_tag[6].string
    qq      = all_span_tag[8].string
    fuwu    = all_span_tag[12].string
    jianjie = page_other.find("span",id="jjssContent").string
    
    print("名字：{}\n地址：{}\n电话：{}\n微信：{}\nqq：{}\n服务项目：{}\n简介：{}\n".format(
        spa_name,address,phone,weixin,qq,fuwu,jianjie))
        
# 存储抓取到的所有链接
detail_href_dict = {}

#url = "http://www1.dushitiyan.com/replylist.aspx?cityid=7"
# 获取该页面所有相关的链接
def SpiderAllHrefOfPage(url, href_dict):
    resp = requests.get(url)
    page = resp.content.decode("utf-8")
    page_bs = BeautifulSoup(page, "lxml")

    # <div id="newest_c_new">  主要信息都包含在这个标签页中
    newest_tag = page_bs.find("div", id="newest_c_new")
    
    # 每一个单项又放在<li> 标签里面，所以我们只需要查找所有的li标签即可
    # <div class="c1"> 点评用户的链接
    # <div class="c2"> 
    # <div class="c3"> 用户评论
    all_li_tag = newest_tag.find_all("li")
    for each_tag in all_li_tag:
        all_a_tag = each_tag.find_all("a")
        spa_href = all_a_tag[1]["href"]
        spa_name = all_a_tag[1].string

        # 保存链接
        href_dict[spa_name] = spa_href
        

# 下一页
def JumpNextPage():
    return