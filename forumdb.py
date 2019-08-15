# "Database code" for the DB Forum.

import datetime
import os
import psycopg2


DATABASE_URL = os.environ['DATABASE_URL']

def get_posts():
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(DATABASE_URL)
  c = db.cursor()
  c.execute("select name from products order by id desc")
  return c.fetchall()
  db.close()



#def add_post(content):
#  """Add a post to the 'database' with the current timestamp."""
#  db = psycopg2.connect(database=DBNAME)
#  c = db.cursor()
#  c.execute("insert into posts values (%s)", (content,))
#  db.commit()
#  db.close()
