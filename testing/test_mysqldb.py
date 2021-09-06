from mock_db import MockDB
import database.mysqldb as mydb
from xkcd.comic import Comic
from testing import jpg_image
from testing import test_comic_record, test_comic_url, test_image
import tasks.config as conf

"""
Tests for database.MySqlDB
"""


class TestMySqlDB(MockDB):

    def test_save_comic_to_db(self):
        print("test started test_save_comic_to_db")
        with self.mock_db_config:
            xkcddb = mydb.MySqlDB()
            xkcddb.connect(host=conf.config["MYSQL_DATABASE_HOST"], database=conf.config["MYSQL_DATABASE"],
                           user=conf.config["MYSQL_DATABASE_USER"])
            c = Comic(test_comic_record, test_comic_url)
            c.set_image(test_image)
            is_saved = xkcddb.save_comic_to_db(c)
            xkcddb.commit()
            xkcddb.close()

            self.assertEqual(is_saved, 0)


