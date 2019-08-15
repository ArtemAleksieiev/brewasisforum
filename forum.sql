
CREATE TABLE products ( id INTEGER PRIMARY KEY,
                     price NUMERIC(15,6),
                     name TEXT);

CREATE TABLE sales ( id INTEGER REFERENCES products,
                      sale_date DATE NOT NULL DEFAULT CURRENT_DATE,
                      count INTEGER);
