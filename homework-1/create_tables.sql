-- SQL-команды для создания таблиц
CREATE TABLE employees
(
	first_name text PRIMARY KEY,
	last_name text,
	title text,
	birth_date text,
	notes text
);


CREATE TABLE customers
(
	customer_id text PRIMARY KEY,
	company_name text,
	contact_name text
);

CREATE TABLE orders
(
	order_id text PRIMARY KEY,
	customer_id text,
	employee_id text,
	order_date text,
	ship_city text
);