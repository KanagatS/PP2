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

sql = """DELETE FROM table1 WHERE id = %s"""

cur.execute(sql, (3,))

con.commit()

# ===============================================

cur.close()
con.close()
