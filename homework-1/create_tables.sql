CREATE TABLE customers_data
(
	customer_id char(5) PRIMARY KEY,
	company_name varchar(100),
	contact_name varchar(50)
);

CREATE TABLE employees_data
(
	employee_id int PRIMARY KEY,
	first_name varchar(50),
	last_name varchar(50),
	title varchar(50),
	birth_date date,
	notes text
);

CREATE TABLE orders_data
(
	order_id int PRIMARY KEY,
	customer_id char(5) REFERENCES customers_data(customer_id) NOT NULL,
	employee_id int REFERENCES employees_data(employee_id) NOT NULL,
	order_date date,
	ship_city varchar(50)
);