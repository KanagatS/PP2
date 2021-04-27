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

sql = """SELECT id, name FROM student"""

cur.execute(sql)

row = cur.fetchone()

while row is not None:
    print(row)
    row = cur.fetchone()

con.commit()

# ===============================================

cur.close()
con.close()
