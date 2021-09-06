from unittest import TestCase
import mysql.connector
from mysql.connector import errorcode
import tasks.config as config
from mock import patch
import tasks.config as c


"""
Moc db classs for database testing
"""


class MockDB(TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass start")
        cnx = mysql.connector.connect(
            host=c.testconfig["MYSQL_DATABASE_HOST"],
            user=c.testconfig["MYSQL_DATABASE_USER"]
        )
        cursor = cnx.cursor(dictionary=True)
        try:
            cursor.execute("DROP DATABASE {}".format(c.testconfig["MYSQL_DATABASE"]))
            cursor.close()
            print("DB dropped")
        except mysql.connector.Error as err:
            print("{}{}".format(c.testconfig["MYSQL_DATABASE"], err))

        cursor = cnx.cursor(dictionary=True)
        # create database
        try:
            cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(c.testconfig["MYSQL_DATABASE"]))
            print("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(c.testconfig["MYSQL_DATABASE"]))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)
        cnx.database = c.testconfig["MYSQL_DATABASE"]

        # create table
        print("CREATE table comic")
        query = """CREATE TABLE `comic` (
            `id` INT NOT NULL AUTO_INCREMENT,
            `comic_number` VARCHAR(500) NOT NULL,
            `comic_name` VARCHAR(500) NOT NULL,
            `comic_alt` TEXT NULL,
            `comic_link` TEXT NULL,
            `comic_image_link` TEXT NULL,
            `comic_image` LONGBLOB NULL,
            PRIMARY KEY (`id`)
        )
        COMMENT='This table will store the details of all comics which are requested using xkcd API';
        """
        try:
            cursor.execute(query)
            cnx.commit()
            print("commit create table")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("test_table already exists.")
            else:
                print(err.msg)
        else:
            print("OK")
        cursor.close()
        cnx.close()

        cls.mock_db_config = patch.dict(c.config, c.testconfig)

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass start")
        cnx = mysql.connector.connect(
            host=c.testconfig["MYSQL_DATABASE_HOST"],
            user=c.testconfig["MYSQL_DATABASE_USER"],
            #password=MYSQL_PASSWORD
        )
        cursor = cnx.cursor(dictionary=True)

        # drop test database
        try:
            cursor.execute("DROP DATABASE {}".format(c.testconfig["MYSQL_DATABASE"]))
            cnx.commit()
            cursor.close()
        except mysql.connector.Error as err:
            print("Database {} does not exists. Dropping db failed".format(c.testconfig["MYSQL_DATABASE"]))
        cnx.close()


