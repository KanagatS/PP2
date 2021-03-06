import psycopg2
from configparser import ConfigParser


def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()

    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            'Section {0} not found in the {1} file'.format(section, filename))

    return db


def insert_vendor_list(vendor_list):
    """ insert multiple vendors into the vendors table  """

    sql = "INSERT INTO vendors(vendor_name) VALUES(%s)"

    conn = None

    try:
        # read database configuration
        params = config()

        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)

        # create a new cursor
        cur = conn.cursor()

        # execute the INSERT statement
        cur.executemany(sql, vendor_list)

        # commit the changes to the database
        conn.commit()

        # close communication with the database
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()


def insert_vendor(vendor_name):
    """ insert a new vendor into the vendors table """

    sql = """INSERT INTO vendors(vendor_name) 
            VALUES(%s) RETURNING vendor_id;"""

    conn = None
    vendor_id = None

    try:
        # read database configuration
        params = config()

        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)

        # create a new cursor
        cur = conn.cursor()

        # execute the INSERT statement
        cur.execute(sql, (vendor_name,))

        # get the generated id back
        vendor_id = cur.fetchone()[0]

        # commit the changes to the database
        conn.commit()

        # close communication with the database
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

    return vendor_id


if __name__ == '__main__':
    # insert one vendor
    insert_vendor("3M Co.")
    
    # insert multiple vendors
    insert_vendor_list([
        ('AKM Semiconductor Inc.',),
        ('Asahi Glass Co Ltd.',),
        ('Daikin Industries Ltd.',),
        ('Dynacast International Inc.',),
        ('Foster Electric Co. Ltd.',),
        ('Murata Manufacturing Co. Ltd.',)
])
