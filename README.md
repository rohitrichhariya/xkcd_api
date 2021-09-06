1 . A Python pakages for the [xkcd webcomic](https://xkcd.com/) API.

usages 
>>>import xkcd.comicrequest as cr

>>>comic_request = cr.ComicRequest()
>>>my_comic = comic_request.get_comic(comic_id)



2 . A Python pakages for to save API response in my sql db.

usages 
>>>import database.mysqldb as mydb

>>>xkcddb = mydb.MySqlDB()
>>>xkcddb.connect(host=conf.config["MYSQL_DATABASE_HOST"], database=conf.config["MYSQL_DATABASE"],
                       user=conf.config["MYSQL_DATABASE_USER"])
>>>xkcddb.save_comic_to_db(my_comic)
>>>xkcddb.commit()
>>>xkcddb.close()


Documentain : pesent in below path

.\documents\index.html

1. GET 15 random comics and following details in using Python.
 python .\tasks\task_get_15_random_comic.py


2.Insert into MySQL - Please include SQL database schema(s) for any table(s) created in your Github repo
 python .\tasks\task_two_save_to_db.py
SQL DDL file store under resource folder


3.Write a script called task_one.py that when called will output something like this to the console. (reference below)
 python .\tasks\task_one.py