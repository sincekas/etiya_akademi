select * from adresses;
select * from brands
select * from categories;
select * from cities;
select * from customers;
select * from products;
select * from streets;
select * from towns;

-- where
select name from towns where city_id = 2;
select name,unit_price from products where unit_price < 15;
select name,unit_price from products where unit_price between 11 and 18;

-- distinct
select distinct unit_price from products;
select distinct type from categories;
select distinct city_id from towns;

-- like

select * from customers 
where username like '%s%';

select first_name,second_name from customers 
where lower(second_name) like 'a%';

select name from towns 
where lower(name) like '%ya%';

-- order by

select * from streets order by name desc;
select name,unit_price from products order by unit_price desc;
select name from brands order by name;
select name from brands order by name asc;
Select * from products Order By name DESC;

-- And  / Or Filter

select * from products where stock_id = 1 and unit_price > 24;
Select * from products Order By unit_price > 15 and unit_price < 25;

-- In Filter

select * from categories where lower(type) in('ayakkabı');
Select * from Cities Where Name IN('İstanbul','Adana');
select * from towns where name in('Kadıköy');

-- %

Select * from products Where lower(Name) Like '%spor%';
select username,mail from customers where mail like '%etiya.com';
select username,first_name,second_name from customers where username like '_e%'
Select * from products Where lower(Name) Like '%__y%';
