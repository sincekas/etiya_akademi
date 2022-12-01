--distinct
select distinct numberofproducts,count(*) from sellers
group by numberofproducts
order by count;

--max
select max(salesprice) as "En Pahalı Ürün" from productprices;
select max(numberofproducts) as "En Fazla Ürün" from sellers;

--min
select min(salesprice) "En Ucuz Ürün" from productprices;
select min(numberofproducts) as "En Az Ürün" from sellers;

--avg
select avg(salesprice) as "Ürünlerin Ortalama Satış Fiyatı" from productprices;
select avg(numberofproducts) as "Ortalama Ürün Sayısı" from sellers;

--sum
select brand_id,sum(stock) from products
group by brand_id
having (brand_id = 2 or brand_id = 5)
order by brand_id;

--count1
select count(*),name from products
group by name
order by count;

--count2
select type,count(*) from categories
group by type;

--count3
select category_id,count(*)from products
group by category_id order by 2 desc;

--count4
select stock,category_id,count(*) from products
group by category_id,stock;

--having1
select stock,count(*) from products
group by stock
having stock> 20;

--having2
select stock,category_id,count(*) from products
where stock > 55
group by category_id,stock
having count(*) >= 1;

--having3
select profitrate,salesprice,count(*) from productprices
group by profitrate,salesprice
having salesprice > 150;