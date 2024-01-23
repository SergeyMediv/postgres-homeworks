"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
from cls import Customer, Employee, Order

CUSTOMERS_PATH = 'north_data/customers_data.csv'
EMPLOYEES_PATH = 'north_data/employees_data.csv'
ORDERS_PATH = 'north_data/orders_data.csv'

conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='gw7MiT43'
)
cur = conn.cursor()

customers_instance = Customer.instance_from_csv(CUSTOMERS_PATH)
employee_instance = Employee.instance_from_csv(EMPLOYEES_PATH)
order_instance = Order.instance_from_csv(ORDERS_PATH)

for customer in customers_instance:
    cur.execute(
        'INSERT INTO customers_data VALUES (%s, %s, %s)',
        (customer.customer_id,
         customer.company_name,
         customer.contact_name)
    )

for employee in employee_instance:
    cur.execute(
        'INSERT INTO employees_data VALUES (%s, %s, %s, %s, %s, %s)',
        (employee.employee_id,
         employee.first_name,
         employee.last_name,
         employee.title,
         employee.birth_date,
         employee.notes)
    )

for order in order_instance:
    cur.execute(
        'INSERT INTO orders_data VALUES (%s, %s, %s, %s, %s)',
        (order.order_id,
         order.customer_id,
         order.employee_id,
         order.order_date,
         order.ship_city)
    )
conn.commit()

# cur.execute('SELECT * FROM orders_data')
# response = cur.fetchall()

# for r in response:
#     print(r)

cur.close()
conn.close()
