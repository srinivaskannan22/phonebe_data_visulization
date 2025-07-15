'''
connect with database
'''
from contextlib import ContextDecorator
import psycopg2
import os 
from dotenv import load_dotenv
load_dotenv()

'''
context manager for database
'''

class databaseconnection(ContextDecorator):

    def __init__(self):
        self.db_name=os.getenv('db_databasename')
        self.db_user=os.getenv('db_user')
        self.host=os.getenv('db_host')
        self.port=os.getenv('db_port')
        self.password=os.getenv('db_password')

    def __enter__(self):
        self.conn = psycopg2.connect(
            dbname='phonebe',
            user='postgres',
            port=5432,
            host='localhost',
            password='Seenu2218'
        )
        return self.conn
    
    def __exit__(self, exc_type, exc_value, traceback):
        return self.conn.close()



'''
data base injection using the query 
'''
def data_injection(query):
    with databaseconnection() as database:
        with database.cursor() as cursor:
            cursor=database.cursor()
            cursor.execute('select * from '+query)
            data=cursor.fetchall()
            cursor.execute(f"""
            SELECT column_name
            FROM information_schema.columns
            WHERE table_name = '{query}'
            ORDER BY ordinal_position;
        """)
        columns = [row[0] for row in cursor.fetchall()]      
        return data,columns
        
        
