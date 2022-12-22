import json
import random
import time
import numpy as np


def str_time_prop(start, end, time_format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formatted in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """
    t1 = time.strptime(start, time_format)
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%Y/%m/%d', prop)


data = json.load(open("file_name.json"))
np.random.seed(5)
random.seed(5)
print('\n\n\n\n-- institute')
print("insert into institute values ('IEEE');\ninsert into institute values ('elsevier');\ninsert into institute"
      " values ('acm');\ninsert into institute values ('springer');\ninsert into institute values ('mdpi');\ninsert"
      " into institute values ('oxford');\n")

academy_to_institute = {}
academy_start_date={}
# academy
# insert into academy values ('academy_name', date, 'ins_name')
print('\n\n\n\n-- academy')
ins_namee = ['elsevier', 'springer', 'mdpi', 'oxford']
for i in range(len(data["academy"])):
    date = (random_date("1970/01/19", "2022/01/19", random.random())).replace('/', '-')
    if 'IEEE' in data["academy"][i]:
        printline = 'insert into academy values (\'{academy_name}\', TO_DATE(\'{datee}\', \'yyyy-mm-dd\'), \'{ins_name}\');'.format(
            academy_name=data["academy"][i], datee=date, ins_name='IEEE')
        academy_to_institute[data["academy"][i]] = 'IEEE'
    elif 'ACM' in data["academy"][i]:
        printline = 'insert into academy values (\'{academy_name}\', TO_DATE(\'{datee}\', \'yyyy-mm-dd\'), \'{ins_name}\');'.format(
            academy_name=data["academy"][i], datee=date, ins_name='acm')
        academy_to_institute[data["academy"][i]] = 'acm'
    else:
        ins_namee1 = ins_namee[int(random.random() * 4)]
        printline = 'insert into academy values (\'{academy_name}\', TO_DATE(\'{datee}\', \'yyyy-mm-dd\'), \'{ins_name}\');'.format(
            academy_name=data["academy"][i], datee=date, ins_name=ins_namee1)
        academy_to_institute[data["academy"][i]] = ins_namee1
    academy_start_date[data["academy"][i]]=date.replace('-','/')
    print(printline)

# journal, keyword, citing
print('\n\n\n\n-- journal')
numbers_j = np.random.choice(range(30000, 39999), 193, replace=False)
number_j_list = list(numbers_j)
journal_start_date = {}
journal_institute = {}
for i in range(193):
    journal_id = numbers_j[i]
    views = int(random.random() * 3000)
    title = data["title"][i]
    tmp = random.random()
    if tmp < 0.5:
        open1 = "public"
    else:
        open1 = "subscriber only"
    cite_num = int(random.random() * (views // 50))
    vol_num = int(random.random() * 100)
    academy_name = data["academy"][int(random.random() * len(data["academy"]))]
    journal_institute[str(journal_id)] = academy_to_institute[academy_name]
    date = random_date(academy_start_date[academy_name], "2022/01/19", random.random())
    journal_start_date[str(journal_id)] = date
    date.replace('/', '-')
    str1 = "insert into journal values ({0}, {1}, '{2}', '{3}', TO_DATE('{4}', 'yyyy-mm-dd'), {5}, {6}, '{7}');". \
        format(journal_id, views, title, open1, date, cite_num, vol_num, academy_name)
    print(str1)
    tmp1 = int(random.random() * 5) + 3
    t22 = random.sample(data["keyword"], tmp1)
    for t in t22:
        str2 = "insert into keyword values ({0}, '{1}');".format(journal_id, t)
        print(str2)
    citing_j_n = int(random.random() * 7) + 3
    citing_j = random.sample(number_j_list, citing_j_n)
    for jj in citing_j:
        if jj != journal_id:
            str3 = "insert into citing values ({0}, {1});".format(journal_id, jj)
            print(str3)

# subscriber
print('\n\n\n\n-- subscriber')
subscribe_kind = [["acm", "IEEE"], ["acm", "IEEE", "mdpi"], ["acm", "IEEE", "mdpi", "springer"],
                  ["acm", "IEEE", "springer"], ["acm", "IEEE", "springer", "elsevier"],
                  ["acm", "IEEE", "mdpi", "elsevier"], ["acm", "IEEE", "mdpi", "elsevier", "oxford"],
                  ["acm", "IEEE", "elsevier", "springer", "oxford"], ["acm", "IEEE", "mdpi", "elsevier", "springer"],
                  ["acm", "IEEE", "mdpi", "elsevier", "oxford", "springer"]]
for _ in range(10):
    subscribe_kind.append(["acm", "IEEE", "mdpi", "elsevier", "oxford", "springer"])

numbers = np.random.choice(range(10000, 19999), len(data["name"]) + len(data["subscribed_institution"]), replace=False)
subscribing_since={}
for a in range(len(data["subscribed_institution"])):
    date1 = (random_date("1990/01/19", "2021/05/30", random.random())).replace('/', '-')
    date2 = (random_date("2022/12/01", "2030/12/31", random.random())).replace('/', '-')
    printline = 'insert into subscriber values ({sub_id}, TO_DATE(\'{date1}\', \'yyyy-mm-dd\'), ' \
                'TO_DATE(\'{date2}\',\'yyyy-mm-dd\'), \'{sub_type}\', \'{sub_name}\');' \
        .format(sub_id=numbers[a], date1=date1, date2=date2, sub_type='institution',
                sub_name=data["subscribed_institution"][a])
    subscribing_since[numbers[a]]=date1.replace('-', '/')
    print(printline)

for a in range(len(data["name"])):
    date1 = (random_date("2015/01/19", "2021/08/30", random.random())).replace('/', '-')
    date2 = (random_date("2022/12/01", "2030/12/31", random.random())).replace('/', '-')
    printline = 'insert into subscriber values ({sub_id}, TO_DATE(\'{date1}\', \'yyyy-mm-dd\'), TO_DATE(\'{date2}\', ' \
                '\'yyyy-mm-dd\'), \'{sub_type}\', \'{sub_name}\');' \
        .format(sub_id=numbers[a + len(data["subscribed_institution"])], date1=date1, date2=date2,
                sub_type='individual', sub_name=data["name"][a])
    subscribing_since[numbers[a + len(data["subscribed_institution"])]]=date1.replace('-', '/')
    print(printline)

# manages
print('\n\n\n\n-- manages')
subscribing_inst={}
for i in numbers:
    t1=random.randrange(0,len(subscribe_kind))
    subscribing_inst[str(i)]=[]
    for sub in subscribe_kind[t1]:
        printline = "insert into manages values ('{0}', {1});".format(sub, i)
        print(printline)
        subscribing_inst[str(i)].append(sub)

# rating
# insert into rating values (rating_id, star, TO_DATE('written_date', 'yyyy-mm-dd'), sub_id, j_id)
print('\n\n\n\n-- rating')
cnt=0
# numbers1 = np.random.choice(range(20000, 29999), 400, replace=False)
for i in range(0, 400):
    num1 = random.randrange(1, 6)  # 별 개수
    num2 = random.randrange(0, 193)  # 저널 id
    num3 = random.randrange(0, 200)  # 구독자 id
    date3 = (random_date(max(journal_start_date[str(numbers_j[num2])],subscribing_since[numbers[num3]]), "2022/10/20",
                         random.random())).replace('/', '-')
    if journal_institute[str(numbers_j[num2])] in subscribing_inst[str(numbers[num3])]:
        cnt+=1
        printline = 'insert into rating values ({star}, TO_DATE(\'{date3}\', \'yyyy-mm-dd\'), ' \
                    '{sub_id}, {j_id});' \
            .format(star=num1, date3=date3, sub_id=numbers[num3], j_id=numbers_j[num2])
        print(printline)

# academy worker
# insert into academyworker values (unique_worker_id, 'Fname', 'Lname', 'depart', 'aca_name', salary)
print('\n\n\n\n-- acadmeyworker')
numbers_worker = np.random.choice(range(40000, 49999), 400, replace=False)

for i in range(400):
    aca_num = i % 30
    salary = random.randrange(30, 65) * 1000
    worker = data["worker"][i].split(' ')
    if i>30: tt= int(random.random()*6)
    else: tt=0
    printline = 'insert into academyworker values ({unique_worker_id},\'{fname}\', \'{lname}\', \'{department}\', \'{aca_name}\', {salary});'.format(
        unique_worker_id=numbers_worker[i], fname=worker[0], lname=worker[1],
        department=data["department"][tt], aca_name=data["academy"][aca_num], salary=salary)
    print(printline)

# author, degree
# insert into author values (unique_author_id, 'fname', 'lname', 'judging academy')
print('\n\n\n\n-- author')
numbers_author = np.random.choice(range(50000, 59999), 300, replace=False)
numbers_author_list= list(numbers_author)
for i in range(300):
    author = data["name"][i].split(' ')
    printline = 'insert into author values ({unique_author_id}, \'{fname}\', \'{lname}\');'.format(
        unique_author_id=numbers_author[i], fname=author[0], lname=author[1])
    print(printline)
    degree_n=int(random.random()*100)
    school=data["university"][int(random.random() * len(data["university"]))]
    print("insert into degree values ({0}, 'B.S. {1}');".format(numbers_author[i],school))
    if degree_n<24:
        continue
    if degree_n<55:
        print("insert into degree values ({0}, 'M.S. {1}');".format(numbers_author[i], school))
    else:
        print("insert into degree values ({0}, 'M.S. {1}');".format(numbers_author[i], data["university"][
            int(random.random() * len(data["university"]))]))
    if degree_n%2==0:
        continue
    if degree_n<55:
        print("insert into degree values ({0}, 'Ph.D. {1}');".format(numbers_author[i], school))
    else:
        school = data["university"][int(random.random() * len(data["university"]))]
        print("insert into degree values ({0}, 'Ph.D. {1}');".format(numbers_author[i], school))

# write
# insert into write values (a_id, j_id)
print('\n\n\n\n-- write')
# 각 저널마다 author를 여러명, 하는 걸로 하자
mostlywrite = {}
for i in number_j_list:
    number_write = random.randrange(1, 5)   # 공저자 수
    rand_author = np.random.choice(range(0, 299), number_write, replace=False)
    for j in rand_author:

        if numbers_author[j] not in mostlywrite:
            mostlywrite[numbers_author[j]]=1
        else:
            mostlywrite[numbers_author[j]]+=1
        printline = 'insert into writes values ({a_id}, {j_id});'.format(a_id=numbers_author[j], j_id=i)
        print(printline)

mostlywrite_list=[]
for i in mostlywrite:
    mostlywrite_list.append([mostlywrite[i],i])
mostlywrite_list.sort(reverse=True)


# print(mostl)

# proposal
# insert into proposal values (w_id, a_id, TO_DATE(proposal_date))
print('\n\n\n\n -- proposal')
# 각 직원이 여러명의 author에게 제안하는 것으로 하자
# 가장 많이 쓴 150명의 저자에게 연락
# 한 아카데미당 2-4명 proposal, 0-1명이 accept 안하게
for i in range(len(data['academy'])):
    number_proposal = random.randrange(2, 6)    # 제안 수, per academy(not worker!)
    for j in range(number_proposal):
        number_rand_auth = random.randrange(0, 150)
        pdate = (random_date("2020/01/19", "2022/01/19", random.random())).replace('/', '-')
        accepted = random.random()
        if accepted > 0.3:
            accepted = "YES"
            # print("update author set judging_academy = '{0}' where unique_author_id = {1};".format(data["academy"][i],mostlywrite_list[number_rand_auth][1] ))
        else:
            accepted = "NO"
        printline = 'insert into proposal values ({w_id}, {a_id}, TO_DATE(\'{p_date}\', \'yyyy-mm-dd\'), \'{accepted}\');'\
            .format(w_id = numbers_worker[i], a_id=mostlywrite_list[number_rand_auth][1], p_date=pdate, accepted=accepted)
        print(printline)

# review
# insert into review values (unique_review_id, TO_DATE(review_date), 'review_text Reviews', j_id, a_id);
print('\n\n\n\n -- review')
# review id 60000-70000
# review_date journal date 보다 무조건 더 뒤로 써야함
#journal publication date = journal_start_date
numbers_review = np.random.choice(range(60000, 69999), 60, replace=False)
review_journal_id = numbers_j
random.shuffle(review_journal_id)
random.shuffle(numbers_author_list)
for i in range(60):
    text_num = random.randrange(0, 49)
    jour_id = journal_start_date[str(review_journal_id[i])]
    review_date = random_date(jour_id, "2022/10/19", random.random())
    review_date = review_date.replace('/', '-')
    print('insert into review values ({unique_review_id}, TO_DATE(\'{review_date}\', \'yyyy-mm-dd\'),'
          '\'{review_text}\', {j_id}, {a_id});'.format(unique_review_id=numbers_review[i], review_date=review_date,
                                                        review_text=data['reviews'][text_num],
                                                        j_id=review_journal_id[i],
                                                        a_id=numbers_author_list[i]))
