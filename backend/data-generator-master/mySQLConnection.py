import pymysql

con= pymysql.connect(user = 'root', passwd='ppp', 
                            host='localhost',
                            database = 'db_grad_cs_1917',
                            charset = 'utf8mb4',
                            cursorclass = pymysql.cursors.DictCursor)

try:

    with con.cursor() as cur:

        cur.execute('SELECT * FROM deal')

        rows = cur.fetchall()

        for row in rows:
            print(row['deal_id'])

        INSERT INTO instruments (name, id) VALUES (?, ?)
        .query/execution(query, output_item['instrument']['name'], ...['id'])

finally:

    con.close()

