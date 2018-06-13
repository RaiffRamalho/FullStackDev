
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
    "create view articlesPopular as select title , count(*)" +
    " as mostPop from articles, log where log.path " +
    "like '%'||articles.slug group by title order by mostPop desc;"
)
# quest2.execute("select * from articlesPopular")
# var5 = quest2.fetchall()
# for element in var5:
#     print element
quest2.execute(
    "create view authorPopularNum as select articles.author, sum(mostPop)" +
    " as totalViews from articles, articlesPopular where articles.title = " +
    "articlesPopular.title group by articles.author;"
)
# quest2.execute("select totalViews from authorPopularNum")
# var5 = quest2.fetchall()
# for element in var5:
#     print element
quest2.execute(
    "select name, totalViews from authors, authorPopularNum " +
    "where authors.id = authorPopularNum.author order by totalViews desc;"
)
list_two = quest2.fetchall()
for element in list_two:
    print(element[0] + " - " + str(element[1]))

print("---------------------------")
print("QUESTION 3")
logs = db.cursor()
logs.execute(
    "create view errors as select time::date from log where status" +
    " like 40||'%';"
)

logs.execute(
    "create view success as select time::date from log where status" +
    " like 20||'%';"
)

logs.execute(
    "create view successCounted as select time::date, count(*)" +
    " as countin from success group by time;"
)

logs.execute(
    "create view errorsCounted as select time::date, count(*)" +
    " as countin from errors group by time;"
)

logs.execute(
    "select successCounted.time, successCounted.countin, " +
    "errorsCounted.countin from successCounted, errorsCounted " +
    "where successCounted.time = errorsCounted.time;"
)
list_three = logs.fetchall()
for element in list_three:
    if element[2] > (element[1] * 0.01):
        print(str(element[0]) + " , " + str("%.2f" % (float(element[2])/float(element[1]) * 100))+'% errors')
print("---------------------------")

db.close()

# quest2.execute(
#     "select name, totalViews from authors," +
#     "(select articles.author, sum(mostPop) as totalViews from " +
#     "articles, (select title , count(*)" +
#     " as mostPop from articles, log where log.path " +
#     "like '%'||articles.slug group by title order by mostPop desc) as articlesPopular where articles.title = " +
#     "articlesPopular.title group by articles.author) as authorPopularNum where authors.id = authorPopularNum.author order by totalViews desc;"
# )

# var6 = quest2.fetchall()
# for element in var6:
#     print(element[0] + " - " + str(element[1]))

print("---------------------------")
print("QUESTION 3")
print("---------------------------")
logs = db.cursor()
# logs.execute(
#     " select time::date, count(*)" +
#     " as countin from (select time::date from log where status" +
#     " like 40||'%') as errors group by time;"
# )
# logs.execute(
#     " select time::date, count(*)" +
#     " as countin from (select time::date from log where status" +
#     " like 20||'%') as success group by time;"
# )
# logs.execute("select time::date from log where status like" +
# " 40||'%' limit 200;")
# var7 = logs.fetchall()
# logs.execute(
#     "create view successCounted as select time::date, count(*)" +
#     " as countin from success group by time;"
# )
# logs.execute("select time from successCounted;")
# var8 = logs.fetchall()
# for element in var8:
#     print element
# print ("---------------------------")
# logs.execute(
#     "create view errorsCounted as select time::date, count(*)" +
#     " as countin from errors group by time;"
# )
# logs.execute("select time from errorsCounted;")
# var9 = logs.fetchall()
# for element in var9:
#     print element
# print ("---------------------------")
# logs.execute(
#     "select successCounted.time, successCounted.countin, " +
#     "errorsCounted.countin from successCounted, errorsCounted " +
#     "where successCounted.time = errorsCounted.time;"
# )

logs.execute(
    "select successCounted.time, successCounted.countin," +
    " errorsCounted.countin from (select time::date, count(*)" +
    " as countin from (select time::date from log where status" +
    " like 20||'%') as success group by time) as successCounted, (select time::date, count(*)" +
    " as countin from (select time::date from log where status" +
    " like 40||'%') as errors group by time) as errorsCounted" +
    " where successCounted.time = errorsCounted.time;"
)
var10 = logs.fetchall()
for element in var10:
    if element[2] > (element[1] * 0.01):
        print(element)
print("---------------------------")

db.close()
