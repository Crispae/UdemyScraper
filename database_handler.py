import sqlite3

def Create_database():
    conn = sqlite3.connect("udemy.db")
    cur = conn.cursor()

    cur.execute(""" CREATE TABLE udemy_url(date integer,
                                           course_name text,
                                           course_url text)""")

    conn.commit()
    conn.close()

def Insert_ONE(data):
    conn = sqlite3.connect("udemy.db")
    cur  = conn.cursor()

    cur.execute("""INSERT INTO udemy_url VALUES(?,?,?)""",data)
    conn.commit()
    conn.close()

def Check_avail(name):
    conn = sqlite3.connect("udemy.db")
    cur = conn.cursor()

    cur.execute(""" SELECT * FROM udemy_url WHERE course_name = ? """,[name])
    data = cur.fetchall()
    if data:
        return True
    else:
        return False

def query_data():
    data_list = []
    conn = sqlite3.connect("udemy.db")
    cur = conn.cursor()
    cur.execute(""" SELECT * FROM udemy_url """)

    data = cur.fetchall()
    conn.close()
    for dat in data:
        data_list.append(dat)
    return data_list

def query_bydate(today):
    data_list= []
    conn = sqlite3.connect("udemy.db")
    cur = conn.cursor()
    cur.execute(""" SELECT * FROM udemy_url WHERE date = ?""",[today])
    data = cur.fetchall()
    conn.close()
    for dat in data:
        data_list.append(dat)
    return data_list
    


    

