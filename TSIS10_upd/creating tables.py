import psycopg2

con = psycopg2.connect(
    host='localhost',
    database='testing',
    user='postgres',
    port=6666,
    password=''
)

cur = con.cursor()

# ===============================================

commands = (
    """ CREATE TABLE test(
                id serial primary key,
                name varchar(200) not null
                )
        """,
)

# creating tables one by one
for i in commands:
    cur.execute(i)

con.commit()

# ===============================================

cur.close()
con.close()
