import csv


CUSTOMERS_PATH = 'north_data/customers_data.csv'
EMPLOYEES_PATH = 'north_data/employees_data.csv'
ORDERS_PATH = 'north_data/orders_data.csv'


class NorthData:
    def __init__(self, customer_id=None, employee_id=None, order_id=None):
        self.customer_id = customer_id
        self.employee_id = employee_id
        self.order_id = order_id


class Customer(NorthData):
    def __init__(self, customer_id, company_name, contact_name):
        super().__init__(customer_id)
        self.company_name = company_name
        self.contact_name = contact_name

    @classmethod
    def instance_from_csv(cls, path):
        customers_list = []
        try:
            with open(path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    customer_id = row['customer_id']
                    company_name = row['company_name']
                    contact_name = row['contact_name']
                    customer = cls(customer_id, company_name, contact_name)
                    customers_list.append(customer)
        except FileNotFoundError:
            raise FileNotFoundError('File not found lol')
        except KeyError:
            raise KeyError('File is damaged')
        return customers_list


class Employee(NorthData):
    def __init__(self, employee_id, first_name, last_name, title, birth_date, notes):
        super().__init__(employee_id)
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.birth_date = birth_date
        self.notes = notes

    @classmethod
    def instance_from_csv(cls, path):
        employees_list = []
        try:
            with open(path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    employee_id = row['employee_id']
                    first_name = row['first_name']
                    last_name = row['last_name']
                    title = row['title']
                    birth_date = row['birth_date']
                    notes = row['notes']
                    employee = cls(employee_id, first_name, last_name, title, birth_date, notes)
                    employees_list.append(employee)
        except FileNotFoundError:
            raise FileNotFoundError('File not found lol')
        return employees_list


class Order(NorthData):
    def __init__(self, order_id, customer_id, employee_id, order_date, ship_city):
        super().__init__(employee_id, order_id, customer_id)
        self.order_date = order_date
        self.ship_city = ship_city

    @classmethod
    def instance_from_csv(cls, path):
        orders_list = []
        try:
            with open(path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    order_id = row['order_id']
                    customer_id = row['customer_id']
                    employee_id = row['employee_id']
                    order_date = row['order_date']
                    ship_city = row['ship_city']
                    order = cls(order_id, customer_id, employee_id, order_date, ship_city)
                    orders_list.append(order)
        except FileNotFoundError:
            raise FileNotFoundError('File not found lol')
        return orders_list


customer = Customer.instance_from_csv(CUSTOMERS_PATH)
employee = Employee.instance_from_csv(EMPLOYEES_PATH)
order = Order.instance_from_csv(ORDERS_PATH)

print(customer[0].company_name)
print(employee[0].title)
print(order[0].order_date)
