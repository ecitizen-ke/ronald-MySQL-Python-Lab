from flask import current_app
import mysql.connector

class Connection:
    """This class provides connection to our database"""

    def __init__(self):
        self.host = current_app.config["MYSQL_HOST"]
        self.db = current_app.config["MYSQL_DB"]
        self.user = current_app.config["MYSQL_USER"]
        self.password = current_app.config["MYSQL_PASSWORD"]
        

        # Create a db connection
        self.conn = mysql.connector.connect(
            host=self.host, database=self.db, user=self.user, password=self.password
        )

        # Create cursor
        self.cursor = self.conn.cursor()
        

        