import sqlite3

conn = sqlite3.connect('mydatabase.sqlite3') #conn เปรียบเหมือนบริษัท

c = conn.cursor() #cursor เหมือน ceo ที่ต้องทำงานในบริษัท ให้ c เป็นคนสั่งการ

c.execute("""CREATE TABLE IF NOT EXISTS job (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                fullname TEXT,
                tel TEXT,
                position TEXT)""")


def insert_job(fullname,tel,position):
    with conn:
        command = 'INSERT INTO job VALUES (?,?,?,?)'
        c.execute(command,(None,fullname,tel,position))
    conn.commit()
    print('saved')

insert_job('สมชาย มีเงิน','0812345679','ช่างกล')

def view_job():
    with conn:
        command = 'SELECT * FROM job'
        c.execute(command)
        result = c.fetchall()
    print(result)

# view_job()

def update_job(tel,field,newvalue):
    with conn:
        command = 'UPDATE job SET {} =(?) WHERE tel=(?)'.format(field)
        c.execute(command,(newvalue,tel))
    conn.commit()

update_job('0812345678','position','วิศวกร')
view_job()

def delete_job(tel):
    with conn:
        command = 'DELETE FROM job WHERE tel=(?)'
        c.execute(command,([tel]))
    conn.commit()

# delete_job('0812345671')
# view_job()