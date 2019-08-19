#!/usr/bin/env python3
#
# A buggy web service in need of a database.

from flask import Flask, request, redirect, url_for, render_template
from flask import Markup

from forumdb import get_data, add_products, add_sales

app = Flask(__name__)


# HTML template data
POST = '''
    <table id="table"> <tr> <td style = "width:100px">%s</td> <td style="width:200px">%s</td> <td>%s</td> </tr> </table>
'''
sales_temp = '''
    <table id="table"> <tr> <td style = "width:100px">%s</td> <td style="width:200px">%s</td> <td>%s</td> </tr> </table>
'''
labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]

@app.route('/products', methods=['GET'])
def products_get():
  query_products = "select id, price, name \
                            from products \
                            order by id"
  product_data = "".join(POST % (id, price, name) for id, price, name in get_data(query_products))
  return render_template("products.html", product_data = product_data)

@app.route('/products', methods=['POST'])
def products_post():
  id = request.form['id']
  price = request.form['price']
  product_name = request.form['product_name']
  add_products(id, price, product_name)
  return redirect(url_for('products_get'))

@app.route("/sales", methods=['GET'])
def sales_get():
  query_sales = "select id, sale_date, count \
                        from sales \
                        order by id"
  sales_data = "".join(sales_temp % (s_id, sale_date, count) for s_id, sale_date, count in get_data(query_sales))
  return render_template("sales.html", sales_data = sales_data)

@app.route('/sales', methods=['POST'])
def sales_post():
  s_id = request.form['s_id']
  sale_date = request.form['sale_date']
  count = request.form['count']
  add_sales(s_id, sale_date, count)
  return redirect(url_for('sales_get'))

@app.route("/chart")
def graph():
  query_graph = "select sum(count * price) as value \
                        from sales, products \
                        where products.id=sales.id \
                        group by extract(month from sales.sale_date) \
                        order by extract(month from sales.sale_date)"
  line_labels=labels
  line_values=[item for item, in get_data(query_graph)]
  return render_template('chart.html', title='Monthly Beer Sales', max=200, labels=line_labels, values=line_values)

@app.route('/')
def main():
	return render_template('index.html')

if __name__ == '__main__':
  app.run()
