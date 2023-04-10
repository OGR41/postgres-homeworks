-- SQL-команды для создания таблиц
CREATE TABLE employees
(
	first_name name PRIMARY KEY,
	last_name name,
	title name,
	birth_date date,
	notes text
);


CREATE TABLE customers
(
	customer_id varchar(5) PRIMARY KEY,
	company_name name,
	contact_name name
);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id varchar(5),
	employee_id int,
	order_date date,
	ship_city name
);