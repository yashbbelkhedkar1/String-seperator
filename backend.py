import sqlite3

def connect():
    conn=sqlite3.connect("candidate_database.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS candidate (name TEXT, address TEXT )")
    conn.commit()
    conn.close()

def view() :
    conn=sqlite3.connect("candidate_database.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM candidate")
    rows=cur.fetchall()
    conn.close()
    
    if rows == [] :
        print("The database is empty\n")
    else :
        print("-"*50)
        for i in rows :
            print(i)
        print("-"*50)

def insert(name,address) :
    conn=sqlite3.connect("candidate_database.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO candidate VALUES(?,?)",(name,address))
    conn.commit()
    conn.close()

def drop():
    conn=sqlite3.connect("candidate_database.db")
    cur=conn.cursor()
    cur.execute("DROP TABLE IF EXISTS candidate")
    conn.commit()
    conn.close()

