import os
import csv
import requests
from bs4 import BeautifulSoup


# ���ݱ���Ϊcsv�ļ�
def SaveDataToCSV(row, filename='temp', path='Spider_dushi'):
    fpath = os.path.join(path, filename);
    with open(fpath, "a", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(row)
    
# �����ļ�
def SaveData(text, filename='temp', path='Spider_dushi'):
    fpath = os.path.join(path, filename)
    with open(fpath, 'a', encoding="utf-8") as  f:
        f.write(text)
        
# ���浽���ݿ�
def SaveDataToMysql(text):
    return;
    
# �������л�ȡ���л�����Ϣ
def ParseInfoByHref(href):
    resp = requests.get(href)
    page = resp.content.decode("utf-8")
    page_bs = BeautifulSoup(page, "lxml")
    page_main = page_bs.find("div",class_="main")
    
    # ��ַ �绰 ΢�� qq Ӫҵʱ�� ������Ŀ ��Ա���� ��Ա���� ���
    spa_name = page_bs.find("h1", class_="shop-name").string
    page_other = page_bs.find("div", class_="other J-other")
    all_span_tag = page_other.find_all("span")
    address = all_span_tag[1].string
    phone   = all_span_tag[3].string
    weixin  = all_span_tag[6].string
    qq      = all_span_tag[8].string
    fuwu    = all_span_tag[12].string
    jianjie = page_other.find("span",id="jjssContent").string
    
    print("���֣�{}\n��ַ��{}\n�绰��{}\n΢�ţ�{}\nqq��{}\n������Ŀ��{}\n��飺{}\n".format(
        spa_name,address,phone,weixin,qq,fuwu,jianjie))
        
# �洢ץȡ������������
detail_href_dict = {}

#url = "http://www1.dushitiyan.com/replylist.aspx?cityid=7"
# ��ȡ��ҳ��������ص�����
def SpiderAllHrefOfPage(url, href_dict):
    resp = requests.get(url)
    page = resp.content.decode("utf-8")
    page_bs = BeautifulSoup(page, "lxml")

    # <div id="newest_c_new">  ��Ҫ��Ϣ�������������ǩҳ��
    newest_tag = page_bs.find("div", id="newest_c_new")
    
    # ÿһ�������ַ���<li> ��ǩ���棬��������ֻ��Ҫ�������е�li��ǩ����
    # <div class="c1"> �����û�������
    # <div class="c2"> 
    # <div class="c3"> �û�����
    all_li_tag = newest_tag.find_all("li")
    for each_tag in all_li_tag:
        all_a_tag = each_tag.find_all("a")
        spa_href = all_a_tag[1]["href"]
        spa_name = all_a_tag[1].string

        # ��������
        href_dict[spa_name] = spa_href
        

# ��һҳ
def JumpNextPage():
    return