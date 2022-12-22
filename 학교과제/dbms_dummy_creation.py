import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import pyclip as pyperclip
import time
from selenium.webdriver.common.by import By
import json
import random
#
driver = webdriver.Chrome()  # 크롬창 켜기
# cnt = 0
# arr = []
# academy = []
# subscribed_institution = []
# name=[]
# # for j in range(2):
# #     url_sugang = "https://ieeexplore.ieee.org/search/searchresult.jsp?queryText=database&type=alt2&highli" \
# #                  "ght=true&returnFacets=ALL&returnType=SEARCH&matchPubs=true&refinements=Conten" \
# #                  "tType:Journals&pageNumber={0}&rowsPerPage=100".format(j + 1)
# #     driver.get(url_sugang)
# #     time.sleep(8)
# #     for i in range(3, 100):
# #         xpath_title = '/html/body/div[5]/div/div/div/div[3]/div/xpl-root/div/xpl-search-results/main/div[2]' \
# #                       '/div[2]/xpl-results-list/div[{0}]/xpl-results-item/div[1]/div[1]/div[2]/h2/a'.format(i)
# #         tt = driver.find_element(By.XPATH, xpath_title)
# #         arr.append(tt.text)
# #
# # url_academy = 'https://www.scimagojr.com/journalrank.php?area=1700'
# # driver.get(url_academy)
# # time.sleep(4)
# # for i in range(1, 51):
# #     xpath_academy = '/html/body/div[7]/div[7]/table/tbody/tr[{0}]/td[2]'.format(i)
# #     tt2 = driver.find_element(By.XPATH, xpath_academy)
# #     academy.append(tt2.text)
# #
university=[]
url_academy = 'https://www.topuniversities.com/student-info/choosing-university/worlds-top-100-universities'
driver.get(url_academy)
time.sleep(4)
for i in range(3, 100):
    if i==77: continue
    driver.implicitly_wait(5)
    xpath_academy = '/html/body/div[1]/div/div/div[1]/div[2]/main/section/div/div/section/section/div/div/article/' \
                    'div/div[2]/div[2]/div[6]/div/div/table/tbody/tr[{0}]/td[2]/p/a'.format(i)

    tt2 = driver.find_element(By.XPATH, xpath_academy)
    actions = ActionChains(driver)
    actions.move_to_element(tt2).perform()
    print(tt2.text)
    university.append(tt2.text)

# # url_academy = 'https://www.emaxindia.in/no-1-computer-center-name-list/'
# # driver.get(url_academy)
# # time.sleep(4)
# # for i in range(16, 33):
# #     xpath_academy = '/html/body/div[1]/div[2]/div/main/article/div/div/table/tbody/tr[{0}]/td[2]/strong'.format(i)
# #     tt2 = driver.find_element(By.XPATH, xpath_academy)
# #     subscribed_institution.append(tt2.text)
#
# url_academy = 'https://www.name-generator.org.uk/quick/'
# driver.get(url_academy)
# xpath_but='//*[@id="main"]/div/form/input[3]'
# xpath_click='//*[@id="main"]/div/form/input[4]'
#
# for i in range(10):
#     driver.implicitly_wait(25)
#     driver.find_element(By.XPATH, xpath_but).send_keys(0)
#     time.sleep(2)
#     driver.find_element(By.XPATH, xpath_click).click()
#     driver.implicitly_wait(3)
#     for j in range(1,100):
#         xpath_name = '//*[@id="main"]/div/form/div[{0}]'.format(j)
#         name.append(driver.find_element(By.XPATH,xpath_name).text)
#
# print(name)
# department = ["Web Management", "Publisher", "Editorial", "Contract", "Creative", "Marketing", "Human Resource",
#               "Financial", "Planning", "Sales", "Liaison Business", "Protocol", "Company Welfare",
#               "Intellectual Property"]
# reviews = ["one of my hobbies is drawing. and when i'm drawing this works great.",
#            "My neighbor Montserrat has one of these. She works as a circus performer and she says it looks shriveled.",
#            "This journal works really well. It wildly improves my baseball by a lot.",
#            "I tried to scratch it but got cheeseburger all over it.",
#            "This journal works very well. It persistently improves my soccer by a lot.",
#            "heard about this on melodic death metal radio, decided to give it a try.",
#            "heard about this on dance-rock radio, decided to give it a try.",
#            "The box this comes in is 3 meter by 5 foot and weights 11 kilogram.",
#            "It only works when I'm Kuwait.",
#            "talk about hatred!!!",
#            "The box this comes in is 3 meter by 5 foot and weights 11 kilogram.",
#            "My co-worker Cato has one of these. He says it looks sopping.",
#            "It only works when I'm Azerbaijan.",
#            "heard about this on compas radio, decided to give it a try.",
#            "This journal works quite well. It professionally improves my soccer by a lot.",
#            "i use it for 10 weeks when i'm in my sauna.",
#            "heard about this on melodic death metal radio, decided to give it a try.",
#            "heard about this on new jersey hip hop radio, decided to give it a try.",
#            "this journal is honest.",
#            "heard about this on chicha radio, decided to give it a try.",
#            "I saw one of these in Cote d'Ivoire and I bought one.",
#            "heard about this on powerviolence radio, decided to give it a try.",
#            "The box this comes in is 5 kilometer by 6 meter and weights 20 ounce!",
#            "My co-worker Archer has one of these. He says it looks crooked.",
#            "This journal works excessively well. It speedily improves my baseball by a lot.",
#            "this journal is standard.",
#            "heard about this on smooth jazz radio, decided to give it a try.",
#            "My neighbor Montserrat has one of these. She works as a circus performer and she says it looks shriveled.",
#            "My co-worker Aurthur has one of these. He says it looks white.",
#            "The box this comes in is 3 yard by 6 light-year and weights 15 gram!!!",
#            "this journal is amiable.",
#            "I saw one of these in Libya and I bought one.",
#            "works okay.",
#            "heard about this on jump-up radio, decided to give it a try.",
#            "This journal works so well. It imperfectly improves my baseball by a lot.",
#            "My bass loves to play with it.",
#            "heard about this on melodic death metal radio, decided to give it a try.",
#            "It only works when I'm Martinique.",
#            "I saw this on TV and wanted to give it a try.",
#            "I saw one of these in Moldova and I bought one.",
#            "The box this comes in is 3 yard by 6 light-year and weights 15 gram!!!",
#            "The box this comes in is 4 light-year by 5 inch and weights 11 megaton!!",
#            "My demon loves to play with it.",
#            "heard about this on timba radio, decided to give it a try.",
#            "one of my hobbies is toy collecting. and when i'm collecting toys this works great.",
#            "this journal is nifty.",
#            "My baboon loves to play with it.",
#            "this journal is light-hearted.",
#            "My velociraptor loves to play with it.",
#            "It only works when I'm Niger."]
# print(arr)
# print(academy)
# print(subscribed_institution)
# dict1 = {"title": arr, "reviews": reviews, "academy": academy, "name": name, "department": department,
#          "subscribed_institution": subscribed_institution}
# json.dump(dict1, open("file_name.json", 'w'))
data = json.load(open("file_name.json"))
# ttt=['Relational databases', 'Computer science','Database systems','Object oriented databases','Machinery','Prototypes','Mathematics','Education','Deductive databases','Application software','Multidimensional systems','Indexing','Information retrieval','Image databases','Content based retrieval','Lungs','Proteins','Image retrieval','Entropy','Computed tomography','Query processing','Database languages','Relational databases','Data engineering','Artificial intelligence','Computer science','Deductive databases','Indexes','Database systems','Data processing','Biometrics','Hardware','Spatial databases','Internet','Fingerprint recognition','Iris','Biosensors','Sensor phenomena and characterization','Multimodal sensors','Availability']
# for t in ttt:
#     data["keyword"].append(t)
# print(len(data["keyword"]))
# key=set(data["keyword"])
# key=list(key)
# print(key)
# data["keyword"]=key
data["university"]=university
json.dump(data, open("file_name.json", 'w'))


