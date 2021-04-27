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

sql = """UPDATE student
        SET name = %s
        WHERE id = %s"""

cur.execute(sql, ('SDU', 3))

con.commit()

# ===============================================

cur.close()
con.close()
