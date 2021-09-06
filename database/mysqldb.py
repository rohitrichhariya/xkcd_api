import mysql.connector

"""
database MySqlDB
"""


class MySqlDB:
    """
    MySqlDB class contain the methods which require to intact with mysql database
    """
    def __init__(self):
        """
        MySqlDB init
        """
        self.cnx = None
        self.cur = None

    def connect(self, host, database, user):
        """
        Method to connect with mysql database
        Parameters
        ----------
        host : str
            mysql database host ip address
        database : str
            mysql database database name
        user : str
            mysql database user name
        """
        self.cnx = mysql.connector.connect(user=user, host=host, database=database)
        self.cur = self.cnx.cursor(buffered=True)

    def save_comic_to_db(self, com):
        """
        Method to save comic details in database comic table
        Parameters
        ----------
        com : xkcd Comic
            object of Comic class
        """
        print("save_comic_to_db start")
        insert_new_comic = """INSERT INTO comic (comic_number, comic_name, comic_alt, comic_link, 
        comic_image_link, comic_image) VALUES (%s, %s, %s, %s, %s, %s)"""
        self.cur.execute(insert_new_comic, (com.num, com.title, com.alt, com.comic_url, com.image_url, com.image))
        print("save_comic_to_db done")
        return 0

    def close(self):
        """  close the mysql connection  """
        if self.cnx.is_connected():
            self.cur.close()
            self.cnx.close()

    def commit(self):
        """commit the mysql database changes """
        self.cnx.commit()




