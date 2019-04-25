-- SQL Homework

-- Use 'sakila' database
USE sakila;

-- Use either of these commands to see how table is structured
-- SHOW FIELDS FROM film;
-- DESCRIBE film;

-- 1a. Display the first and last names of all actors from the table 'actor'
SELECT first_name 'First Name', last_name 'Last Name'
FROM actor;
-- SELECT COUNT(*)
-- FROM actor;

-- 1b. Display the first and last name of each actor in a single column in upper case letters. 
-- Name the column `Actor Name`
SELECT UPPER(CONCAT(first_name, ' ', last_name)) 'Actor Name'
FROM actor;

-- 2a. You need to find the ID number, first name, and last name of an actor, 
-- of whom you know only the first name, "Joe." 
-- What is one query would you use to obtain this information?
SELECT actor_id 'Actor ID', first_name 'First Name', last_name 'Last Name'
FROM actor
WHERE first_name = "Joe";

-- 2b. Find all actors whose last name contain the letters `GEN`
-- Use WildCard
SELECT actor_id 'Actor ID', first_name 'First Name', last_name 'Last Name'
FROM actor
WHERE last_name LIKE '%GEN%';

-- 2c. Find all actors whose last names contain the letters `LI`. 
-- This time, order the rows by last name and first name, in that order
SELECT actor_id 'Actor ID', first_name 'First Name', last_name 'Last Name'
FROM actor
WHERE last_name LIKE '%LI%'
ORDER BY last_name, first_name;

-- 2d. Using `IN`, display the `country_id` and `country` columns of the
-- following countries: Afghanistan, Bangladesh, and China
SELECT country_id 'Country ID', country 'Country'
FROM country
WHERE country IN ('Afghanistan', 'Bangladesh', 'China');

-- 3a. You want to keep a description of each actor. 
-- You don't think you will be performing queries on a description, 
-- so create a column in the table `actor` named `description` 
-- and use the data type `BLOB` (Make sure to research the type `BLOB`, 
-- as the difference between it and `VARCHAR` are significant)
ALTER TABLE actor
ADD COLUMN description BLOB AFTER last_name;

-- 3b. Very quickly you realize that entering descriptions for each actor is too much effort. 
-- Delete the `description` column
ALTER TABLE actor
DROP COLUMN description;

-- 4a. List the last names of actors, as well as how many actors have that last name.
