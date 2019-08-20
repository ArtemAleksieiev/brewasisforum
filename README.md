# brewasisforum
Python Postgresql database

This project uses Postgres database and allow users add items in two tables: products and sales. 
Then the result graphically shows the change in sales by month. Database contain two tables:
* Products

    Include these columns:
     - id(primary key)
     - price
     - name
* Sales 

    Include these columns:
     - id
     - date
     - count
     
     

  ## Steps you need to run these code
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
See deployment for notes on how to deploy the project on a live system.
  
  Install the required software:
- a.Vagrant: https://www.vagrantup.com/downloads.html
- b. Virtual Machine: https://www.virtualbox.org/wiki/Downloads
- c. Download a virtual machine: https://github.com/udacity/fullstack-nanodegree-vm

Once installed, download this project as zip file, then extract the files into the vagrant folder "/vagrant" using your prefered command line , input the following commands:
```
cd vagrant
vagrant up 
vagrant ssh
cd /vagrant
```

This means that vagrant is ready, now you have to input the following commands:

Once you're ready, input these command:
```
python app.py
```
The project should be excuted and now you can browse the main page by going to your prefered internet browser and enter the url: http://localhost:8000/
To view and update the products table you can use the following url: http://localhost:8000/products
To view and update the sales table you can use the following url: http://localhost:8000/sales
To view the chart you can use the following url: http://localhost:8000/chart
