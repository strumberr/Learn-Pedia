import sqlite3
import requests

con = sqlite3.connect('database.db', check_same_thread=False)

cur = con.cursor()

def create_db():
    cur.execute('''CREATE TABLE pagetable
                (title, briefdesc, wholetext, keywords, url, joinedtitle, sliderhard, sliderenjoy, hours, links, authorname, authorcontact, authorcode, admincode, comments, creationdate, edited)''')




def insert_db(title, briefdesc, wholetext, keywords, url, joinedtitle, sliderhard, sliderenjoy, hours, links, authorname, authorcontact, authorcode, admincode, comments, creationdate, edited):
    with con:
        cur = con.cursor()

        cur.execute("INSERT INTO pagetable VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (title, briefdesc, wholetext, keywords, url, joinedtitle, sliderhard, sliderenjoy, hours, links, authorname, authorcontact, authorcode, admincode, comments, creationdate, edited))

        ## call commit on the connection...
        con.commit()



def insert_db_ip(ip):
    with con:
        cur = con.cursor()

        cur.execute("INSERT INTO allowedipaddresses VALUES (?);", (ip, ))

        ## call commit on the connection...
        con.commit()