import random
import database.mysqldb as mydb
import xkcd.comicrequest as cr
import logging
import config as conf


def run():
    """
    2. Insert into MySQL - Please include SQL database schema(s) for any table(s) created in your Github repo
    """
    print("insert to db program started")
    logging.getLogger().setLevel(logging.INFO)
    logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s',
                        level=logging.INFO, filemode='w', filename=conf.config["LOG_FILE_NAME"])

    logging.info("Starting run method..")

    xkcddb = mydb.MySqlDB()
    try:
        xkcddb.connect(host=conf.config["MYSQL_DATABASE_HOST"], database=conf.config["MYSQL_DATABASE"],
                       user=conf.config["MYSQL_DATABASE_USER"])
        logging.info("connection succeeded to database : {}".format(conf.config["MYSQL_DATABASE"]))
    except Exception as e:
        logging.critical(e, exc_info=True)
        exit(2)

    for seq in range(15):
        random_id = random.randint(1, 87)
        logging.info("fetching comic number {} from xkcd.".format(random_id))
        comic_request = cr.ComicRequest()
        my_comic = comic_request.get_comic(random_id)
        try:
            logging.info("save comic no {} to db ".format(str(random_id)))
            xkcddb.save_comic_to_db(my_comic)
        except Exception as e:
            logging.critical(e, exc_info=True)
            xkcddb.close()
            logging.error("Database connection closed , DB Changes will rollback..! existing from code")
            exit(2)

    xkcddb.commit()
    xkcddb.close()
    print("insert to db program end")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()
