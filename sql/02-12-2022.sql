--Hangi ülkeden kaç şehir var
select co.name,count(*) from countries co
inner join cities ci
on co.id = ci.country_id
group by co.name
order by 2 desc
--
select count(*),name from products
group by name
order by count;
--
select p.name,c.name from products p
inner join categories c
on p.category_id = c.id
-- Sepetinde o an en az 2 ürün olan customerları listeleyiniz.
select c.name "Müşteri",basketid "Sepet ID",count(*) "Ürün Sayısı" from products_basket pb
inner join baskets b
on pb.basketid = b.id
inner join customers c
on b.customerid = c.id
group by basketid,c.name
having count(*)>1
--
select stock,category_id,count(*) from products
where stock > 55
group by category_id,stock
having count(*) >= 1;
-- Bugüne kadar verdiği sipariş toplamı 300₺'yi geçen customerları listeleyiniz.
select c.name "Müşteri",po.totalprice "Sipariş Tutarı" from products_orders po
inner join orders o
on po.orderid = o.id
inner join customers c
on o.customerid = c.id
where po.totalprice > 300
--
select brand_id,sum(stock) from products
group by brand_id
having (brand_id = 2 or brand_id = 5)
order by brand_id;
-- Bugüne kadar en az 150₺ satış yapmış satıcıları listeleyiniz.
select s.name,sum(po.totalprice) from products_orders po
full outer join products p
on po.productid = p.id
full outer join products_sellers ps
on p.id = ps.productid
full outer join sellers s
on ps.sellerid = s.id
group by s.name,po.totalprice
having po.totalprice > 150
-- Her kategoride en çok kazandıran ürünü (price * quantity değeri ele alınmalıdır) listeleyiniz.
select * from products_orders po where totalprice = (select max(totalprice) from products_orders)