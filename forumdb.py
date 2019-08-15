# "Database code" for the DB Forum.

import datetime
import psycopg2

DBNAME = "brewasis"

def get_posts():
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(database=DBNAME)
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
