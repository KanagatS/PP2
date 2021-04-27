import psycopg2

con = psycopg2.connect(
    host='localhost',
    database='testing',
    user='postgres',
    port=6666,
    password='***'
)

cur = con.cursor()

# ===============================================

sql = """INSERT INTO table1(name) VALUES(%s);"""

cur.execute(sql, ('Kanagat',))

con.commit()

# ===============================================

cur.close()
con.close()
