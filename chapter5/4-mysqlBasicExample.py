import pymysql
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', db='mysql')
cur = conn.cursor()
cur.execute("USE wikipedia")
cur.execute("SELECT * FROM links")
print(cur.fetchone())
cur.close()
conn.close()