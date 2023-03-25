import mysql.connector
from mysql.connector import Error

class database:
    connection = None
    messages = []
    results = []
    def __init__(self, host_name, user_name, user_password, db_name):
        try:
            database.connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password,
                database=db_name
            )
            print("Connection to MySQL DB successful")
            database.messages.append("Connection to MySQL DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")
            database.messages.append(f"The error '{e}' occurred")

    def execute(self, query, data):
        cursor = database.connection.cursor(buffered=True)
        try:
            cursor.execute(query, data)
            database.connection.commit()
            print("Executed '" + query + "'")
            database.messages.append("Executed '" + query + "'")

        except Error as e:
            print(f"The error '{e}' occurred")
            database.messages.append(f"The error '{e}' occurred")

        # All done, close the cursor
        cursor.close()

    def queryAll(self, query, data):
        cursor = database.connection.cursor(buffered=True)
        try:
            cursor.execute(query, data)
            result = cursor.fetchall()
            database.connection.commit()

            print("Executed '" + query + "'")
            database.messages.append("Executed '" + query + "'")
            if(result != None):
                #print(result)
                database.results.append(result)
        except Error as e:
            print(f"The error '{e}' occurred")
            database.messages.append(f"The error '{e}' occurred")

        # All done, close the cursor
        cursor.close()

    def clearResult(self):
        database.results.clear()

    def clearMessages(self):
        database.messages.clear()

    def getResults(self):
        return database.results

    def getMessages(self):
        return database.messages

    def close(self):
        database.connection.cursor(buffered=True).close()

