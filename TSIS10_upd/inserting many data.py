import psycopg2

con = psycopg2.connect(
    host='localhost',
    database='tsis',
    user='postgres',
    port=6666,
    password=''
)

cur = con.cursor()

# ===============================================

sql = """INSERT INTO student(name) VALUES(%s);"""

cur.executemany(sql, [('is',), ('KBTU',), ('student',)])

con.commit()

# ===============================================

cur.close()
con.close()
