# "Database code" for the DB Forum.

import os
import psycopg2


DATABASE_URL = os.environ['DATABASE_URL']

def get_data(query):
  """Return data from the database."""
  db = psycopg2.connect(DATABASE_URL)
  c = db.cursor()
  c.execute(query)
  return c.fetchall()
  db.close()

def add_products(id,price, product_name):
  db = psycopg2.connect(DATABASE_URL)
  c = db.cursor()
  c.execute("insert into products values (%s, %s, %s)", (id, price, product_name))
  db.commit()
  db.close()

def add_sales(s_id, sale_date, count):
  db = psycopg2.connect(DATABASE_URL)
  c = db.cursor()
  c.execute("insert into sales values (%s, %s, %s)", (s_id, sale_date, count))
  db.commit()
  db.close()
