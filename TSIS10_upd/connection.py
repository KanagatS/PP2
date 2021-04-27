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

print('PostgreSQL database version:')
cur.execute('SELECT version()')

print(cur.fetchone())


# ===============================================
con.commit()
cur.close()
con.close()
