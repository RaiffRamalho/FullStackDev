#!/usr/bin/env python3

import psycopg2
try:
    db = psycopg2.connect("dbname=news")
except psycopg2.DatabaseError:
    print(psycopg2.DatabaseError)

print("Create view articlesPopular")
cursor = db.cursor()
cursor.execute(
    "create view articlesPopular as select title , count(*)" +
    " as mostPop from articles, log where log.path " +
    "like '%'||articles.slug group by title order by mostPop desc;"
)
cursor.execute("select * from articlesPopular")
var5 = cursor.fetchall()
for element in var5:
    print (element)
print("----------------------")

print("Create view authorPopularNum")
cursor.execute(
    "create view authorPopularNum as select articles.author, sum(mostPop)" +
    " as totalViews from articles, articlesPopular where articles.title = " +
    "articlesPopular.title group by articles.author;"
)
print("---------------------------")

print("Create view errors")
cursor.execute(
    "create view errors as select time::date from log where status" +
    " like 40||'%';"
)
print("---------------------------")

print("Create view success")
cursor.execute(
    "create view success as select time::date from log where status" +
    " like 20||'%';"
)
print("---------------------------")

print("Create view successCounted")
cursor.execute(
    "create view successCounted as select time::date, count(*)" +
    " as countin from success group by time;"
)
print("---------------------------")

print("Create view errorsCounted")
cursor.execute(
    "create view errorsCounted as select time::date, count(*)" +
    " as countin from errors group by time;"
)
print("---------------------------")
db.close()
