import sqlite3
import datetime
con = sqlite3.connect('loginhaslo.db')
cur = con.cursor()
try:
    cur.execute('''CREATE TABLE danelogowania
                (date text, login text, password text, email text)''')
except OperationalError:
    print('chuj CI na kurwe')

login1='z'
password1='z'
email1='z'
cur.execute("INSERT INTO danelogowania VALUES ('24-04-2021','yolo','yoloyolo', 'mo.rda@wp.pl')")

con.commit()
con.close()
