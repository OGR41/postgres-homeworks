"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
from pprint import pprint

with psycopg2.connect(host='localhost', database='north', user='postgres', password='Xperia99') as conn:

    with conn.cursor() as cur:
        sql = "COPY %s FROM STDIN WITH CSV HEADER DELIMITER AS ','"
        e = open('north_data/employees_data.csv', 'r', encoding='utf8')
        next(e)
        cur.execute("truncate " + 'employees' + ";")
        cur.copy_expert(sql=sql % 'employees', file=e)

        c = open('north_data/customers_data.csv', 'r', encoding='utf8')
        next(c)
        cur.copy_from(c, 'customers', sep=',')

        o = open('north_data/orders_data.csv', 'r', encoding='utf8')
        next(o)
        cur.copy_from(o, 'orders', sep=',')

        conn.commit()

cur.close()
conn.close()

e.close()
c.close()
o.close()
