from selenium import webdriver
from selenium.webdriver.common.by import By

# 爬取目录
file = open("/Users/youzhihao/PycharmProjects/liren1/liren1/doc/catalog.txt", "w", encoding="utf-8")
driver = webdriver.Chrome()
driver.get("http://sz.meituan.com/")
driver.get("http://sz.meituan.com/jiankangliren/")
input("等待...")
tag_list = driver.find_elements(By.CSS_SELECTOR, ".tag-empty")
for tag in tag_list:
    tag_url = tag.get_attribute("href")
    if "javascript" not in tag_url:
        file.write(tag_url + "\n")
file.close()
driver.quit()
