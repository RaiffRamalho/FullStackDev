import psycopg2
db = psycopg2.connect("dbname=news")
# authors = db.cursor()
# authors.execute("select * from authors limit 1;")    
# var = authors.fetchall()
# print var

# print ("---------------------------")
# articles = db.cursor()
# articles.execute("select slug from articles;")    
# var2 = articles.fetchall()
# for element in var2:
#     print element[0]

# print ("---------------------------")
# logs = db.cursor()
# logs.execute("select path from log limit 6;")    
# var3 = logs.fetchall()
# for element in var3:
#     print element[0]

# print ("---------------------------")

quest1 = db.cursor()
quest1.execute("select title , count(*) from articles, log where log.path like '%'||articles.slug group by title order by count desc limit 3;")
var4 = quest1.fetchall()
for element in var4:
    print element


db.close()