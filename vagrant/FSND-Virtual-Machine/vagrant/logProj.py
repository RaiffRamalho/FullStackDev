import psycopg2
db = psycopg2.connect("dbname=news")

# authors = db.cursor()
# authors.execute("select name, id from authors;")    
# var = authors.fetchall()
# for element in var:
#     print element

# print ("---------------------------")
# articles = db.cursor()
# articles.execute("select author, title from articles;")    
# var2 = articles.fetchall()
# for element in var2:
#     print element

# print ("---------------------------")
# logs = db.cursor()
# logs.execute("select * from log limit 12;")    
# var3 = logs.fetchall()
# for element in var3:
#     print element
# print ("---------------------------")

print ("QUESTION1")
print ("---------------------------")

quest1 = db.cursor()
quest1.execute("select title , count(*) from articles, log where log.path "+
"like '%'||articles.slug group by title order by count desc limit 3;")
var4 = quest1.fetchall()
for element in var4:
    print element

print ("---------------------------")
print ("QUESTION 2")
print ("---------------------------")


quest2 = db.cursor()
quest2.execute("create view articlesPopular as select title , count(*) as mostPop from articles, log where log.path "+
"like '%'||articles.slug group by title order by mostPop desc;")
# quest2.execute("select * from articlesPopular")
# var5 = quest2.fetchall()
# for element in var5:
#     print element
quest2.execute("create view authorPopularNum as select articles.author, sum(mostPop) as totalViews"+
" from articles, articlesPopular where articles.title = articlesPopular.title group by articles.author;")
# quest2.execute("select totalViews from authorPopularNum")
# var5 = quest2.fetchall()
# for element in var5:
#     print element
quest2.execute("select name, totalViews from authors, authorPopularNum "+
"where authors.id = authorPopularNum.author order by totalViews desc;")
var6 = quest2.fetchall()
for element in var6:
    print element

print ("---------------------------")
print ("QUESTION 3")
print ("---------------------------")
logs = db.cursor()
logs.execute("create view errors as select time::date from log where status like 40||'%';")    
logs.execute("create view success as select time::date from log where status like 20||'%';")    
# logs.execute("select time::date from log where status like 40||'%' limit 200;")    
# var7 = logs.fetchall()
logs.execute("create view successCounted as select time::date, count(*) as countin from success group by time;")
# logs.execute("select time from successCounted;")     
# var8 = logs.fetchall()
# for element in var8:
#     print element
# print ("---------------------------")
logs.execute("create view errorsCounted as select time::date, count(*) as countin from errors group by time;")
# logs.execute("select time from errorsCounted;")    
# var9 = logs.fetchall()
# for element in var9:
#     print element
# print ("---------------------------")
logs.execute("select successCounted.time, successCounted.countin, errorsCounted.countin from successCounted, errorsCounted "+
"where successCounted.time = errorsCounted.time;")    
var10 = logs.fetchall()
for element in var10:
    if element[2] > (element[1] * 0.1):
        print element
print ("---------------------------")


db.close()