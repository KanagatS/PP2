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

commands = (
    """
        CREATE TABLE table1 (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        )
        """,
    """ CREATE TABLE table2 (
                course SERIAL PRIMARY KEY,
                GPA VARCHAR(255) NOT NULL
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
