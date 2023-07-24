import pymysql

# Function for connect to the database
def connectDatabase():
    try:
        connection = pymysql.connect(
            host='localhost',
            user= 'root',
            password= '',
            database= 'api'
        )
        if connection.open:
            print('Successful connection to the database')
            return connection
        
    except pymysql.Error as error:
        print('Error connecting to the database', error)
    return None

# Function for close connection to the database
def closeConnection(connection):
    if connection.open:
        connection.close()
        print('Connection to database closed')

