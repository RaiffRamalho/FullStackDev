#!/usr/bin/env python3

import psycopg2

try:
    db = psycopg2.connect("dbname=news")
except psycopg2.DatabaseError:
    print(psycopg2.DatabaseError)

print("QUESTION 1")
quest1 = db.cursor()
quest1.execute(
    "select title , count(*) from articles, log where log.path =  " +
    "concat('/article/', articles.slug) group by title order by count desc limit 3;"
)
list_one = quest1.fetchall()
for element in list_one:
    print(element[0] + " - " + str(element[1]))

print("---------------------------")

print("QUESTION 2")
quest2 = db.cursor()

quest2.execute(
    "select name, totalViews from authors," +
    "(select articles.author, sum(mostPop) as totalViews from " +
    "articles, (select title , count(*)" +
    " as mostPop from articles, log where log.path " +
    "like '%'||articles.slug group by title order by mostPop desc) as articlesPopular where articles.title = " +
    "articlesPopular.title group by articles.author) as authorPopularNum where authors.id = authorPopularNum.author order by totalViews desc;"
)

list_two = quest2.fetchall()
for element in list_two:
    print(element[0] + " - " + str(element[1]))

print("---------------------------")

print("QUESTION 3")
logs = db.cursor()

logs.execute(
    "select successCounted.time, successCounted.countin," +
    " errorsCounted.countin from (select time::date, count(*)" +
    " as countin from (select time::date from log where status" +
    " like 20||'%') as success group by time) as successCounted, (select time::date, count(*)" +
    " as countin from (select time::date from log where status" +
    " like 40||'%') as errors group by time) as errorsCounted" +
    " where successCounted.time = errorsCounted.time;"
)

list_three = logs.fetchall()
for element in list_three:
    if element[2] > (element[1] * 0.01):
        print(str(element[0]) + " , " + str("%.2f" % (float(element[2])/float(element[1]) * 100))+'% errors')
print("---------------------------")

db.close()
