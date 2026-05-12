CREATE DATABASE IF NOT EXISTS ecommerce_etl;

USE ecommerce_etl;

CREATE TABLE IF NOT EXISTS customers(
    customer_id INT PRIMARY KEY,
    email VARCHAR(100),
    name VARCHAR(20),
    city VARCHAR(20),
    phone VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS products(
    product_id INT PRIMARY KEY,
    title VARCHAR(250),
    category VARCHAR(50),
    price FLOAT,
    rating FLOAT,
    rating_count INT
);

CREATE TABLE IF NOT EXISTS carts (
    cart_id INT PRIMARY KEY,
    customer_id INT,
    cart_date DATETIME,
    total_items INT,
    total_quantity INT,
    total_cart_value FLOAT
);

CREATE TABLE IF NOT EXISTS cart_items(
    cart_id INT ,
    product_id INT,
    quantity INT,
    PRIMARY KEY(cart_id, product_id)
)