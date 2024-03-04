select * from Products

select ProductID, ProductName from Products

select ProductID, ProductName, UnitPrice from Products where UnitPrice > 100


-- Unit in Stock değeri 100 den büyük olan ürünlerin id, name, price, stock bilgilerini listeleyiniz

select ProductID, ProductName, UnitPrice, UnitsInStock from Products where UnitsInStock >= 100

-- Category id si 8 olan category getirin

select CategoryID, CategoryName as [Category Name] from Categories where CategoryID = 8


-- Employeeid'si 1 ile 5 arasında olan çalışanların Id, TiteOfCourtesy, FirstName, LastName

select EmployeeID, (TitleOfCourtesy + SPACE(1) + FirstName + SPACE(1) + LastName) as [Full Name] 
from Employees
where EmployeeID <= 5 and EmployeeID >= 1

-- unit price 20 ile 100 arasındaki ürünleri listeleyin (between kullanın)

select ProductID, ProductName, UnitPrice from Products where UnitPrice BETWEEN 20 and 100

-- unit in stock 10 ya da 20 ya da 30 olan ürünleri listeleyiniz

select ProductID, ProductName, UnitPrice, UnitsInStock from Products where UnitsInStock in(10, 20, 30)

-- price 20 ile 100 arasında olan ve unit in stock 10 ya da 20 ya da 30 olan ürünleri listeleyiniz

select ProductID, ProductName, UnitPrice, UnitsInStock 
from Products 
where (UnitPrice BETWEEN 20 and 100) and (UnitsInStock in(10, 20, 30))

-- Orders, ShipCountry bilgisi USA olan ve Freight 100 ile 200 arasında olan siparişleri listeleyiniz

select * from Orders where (ShipCountry = 'USA') and (Freight between 100 and 200)

-- ProductName A-K aralığında olan ve stok miktarı 5 ile 50 arasında olan birim fiyatı 20 ile 100 arasında olan ürünleri çoktan aza sıralayarak listeleyin

select ProductID, ProductName, UnitsInStock, UnitPrice from Products 
where (ProductName like '[A-K]%') and (UnitsInStock between 5 and 50) and (UnitPrice between 20 and 100) 
order by UnitPrice DESC

-- UnitPrice 35 ten küçük olan ürünleri kategorilerine göre gruplayalım

select CategoryID, COUNT(ProductID) as [Product Count] 
from Products 
where UnitPrice < 35 
group by CategoryID 
order by [Product Count] desc

-- her siparişi tutarına göre çoktan aza sıralayalım
-- (1 - Discount) * Quantity * Unitprice

select OrderID, ROUND(SUM((1-Discount) * Quantity * UnitPrice), 2) as [Total] 
from [Order Details] 
group by OrderID order by Total desc

-- ProductName A-K aralığında olan ve stok miktarı 5 ile 50 arasında olan birim fiyatı 20 ile 100 arasında olan ürünleri çoktan aza sıralayarak kategori bilgisine göre listeleyin

select CategoryID, Count(*) as [Product Count] from Products 
where (ProductName like '[A-K]%') and (UnitsInStock between 5 and 50) and (UnitPrice between 20 and 100)
group by CategoryID
order by [Product Count] DESC

-- Her siparişteki ürün sayısını bulalım çoktan aza sıralayalım

select OrderID, SUM(Quantity) as Amount from [Order Details] group by OrderID order by Amount desc

-- Having: Aggregate function çalışması sonucunda dönen sonuç kümesi üzerinde filtre yapmaya yarar
-- Toplam tutarı 2500 ile 3500 arasında olan siparişleri sıralayınız

select OrderID as [Sipariş Kodu], ROUND(SUM((1-Discount) * Quantity * UnitPrice), 2) as [Toplam Tutar]
from [Order Details]
where OrderID = 10359
group by OrderID
having ROUND(SUM((1-Discount) * Quantity * UnitPrice), 2) between 2500 and 3500
order by [Toplam Tutar] desc

-- Her bir siparişteki toplam ürün sayısı 200 den fazla olan siparişleri sıralayınız

select OrderID, SUM(Quantity) as [Amount]
from [Order Details]
group by OrderID
having SUM(Quantity) > 200
order by Amount desc


-- JOIN İşlemleri

-- Product tablosundan ProductId, ProductName, CategoryId
-- Categories tablosundan da CategoryName ve Description
-- Alanlarını getirelim

select p.ProductID, p.ProductName, p.CategoryID, c.CategoryName, c.Description from Products as p
join Categories as c on p.CategoryID = c.CategoryID

-- Supplier tablosundan CompanyName, ContactName
-- Product tablosundan ProductName, UnitPrice
-- Category tablosundan CategoryName
-- CompanyName göre artan sırada ekrana getirilsin

select p.ProductName, p.UnitPrice, c.CategoryName, s.CompanyName, s.ContactName from Products as p
join Categories as c on p.CategoryID = c.CategoryID
join Suppliers as s on p.SupplierID = s.SupplierID
order by s.CompanyName ASC

-- Ürünlere göre satışlarım nasıl?

select Top 5 
p.ProductName, sum(o.Quantity) as Quantity, ROUND(SUM((1-o.Discount) * o.Quantity * o.UnitPrice), 2) as Income from Products as p
join [Order Details] as o on p.ProductID = o.ProductID
group by p.ProductName
order by Income DESC

-- Kategorilerime göre satışlarım nasıl?

select c.CategoryName, sum(od.Quantity) as Quantity, ROUND(SUM((1-od.Discount) * od.Quantity * od.UnitPrice), 2) as Income
from Categories as c
join Products as p on c.CategoryID = p.ProductID
join [Order Details] as od on p.ProductID = od.ProductID
group by c.CategoryName
order by Income DESC

-- Hangi kargo firmasına toplamda ne kadar para vermişiz

select s.CompanyName, ROUND(SUM(o.Freight), 2) as Total from Orders as o
join Suppliers as s on o.ShipVia = s.SupplierID
group by s.CompanyName
order by Total DESC

-- En değerli müşterim kim

select Top 1
c.CompanyName, sum(od.Quantity) as Quantity, ROUND(SUM((1-od.Discount) * od.Quantity * od.UnitPrice), 2) as Income 
from Customers as c
join Orders as o on c.CustomerID = o.CustomerID
join [Order Details] as od on od.OrderID = o.OrderID
group by c.CompanyName
order by Income DESC

-- Hangi tedarikçiden aldığım üründen ne kadar satmışım

select s.CompanyName, p.ProductName, sum(od.Quantity) as Quantity, ROUND(SUM((1-od.Discount) * od.Quantity * od.UnitPrice), 2) as Income 
from Suppliers as s
join Products as p on s.SupplierID = p.ProductID
join [Order Details] as od on od.ProductID = p.ProductID
group by s.CompanyName, p.ProductName
order by Income DESC

-- Hangi siparişi hangi çalışan tarafından hangi müşteriye yapılmış

select o.OrderID, o.OrderDate, c.CompanyName, (e.FirstName + ' ' + e.LastName) as [Full Name], e.Title from Employees as e
join Orders as o on e.EmployeeID = o.EmployeeID
join Customers as c on c.CustomerID = o.CustomerID

-- Hangi sipariş
-- Hangi müşteri vermiş
-- Hangi çalışan onaylamış
-- Hangi tarihte
-- Hangi kargo ile taşınmış
-- Hangi fiyattan alınmış
-- Hangi kategoridenmiş
-- Bu ürün hangi tedarikçiden sağşanmış

select 
o.OrderID, o.OrderDate, cus.CompanyName, c.CategoryID, (e.FirstName + ' ' + e.LastName) as [Full Name], 
sh.CompanyName, sum(od.Quantity) as Quantity, ROUND(SUM((1-od.Discount) * od.Quantity * od.UnitPrice), 2) as Income
from Orders as o
join [Order Details] as od on o.OrderID = od.OrderID
join Products as p on od.ProductID = p.ProductID
join Categories as c on c.CategoryID = p.ProductID
join Suppliers as s on s.SupplierID = p.SupplierID
join Shippers as sh on o.ShipVia = sh.ShipperID
join Customers as cus on o.CustomerID = cus.CustomerID
join Employees as e on e.EmployeeID = o.EmployeeID
group by o.OrderID, o.OrderDate, cus.CompanyName, c.CategoryID, e.FirstName, e.LastName, sh.CompanyName

-- User Defined Function

Create Function KDVHesapla(@fiyat money)
returns money
	begin
		return @fiyat * 1.08
	end;

select p.ProductName, c.CategoryName, p.UnitPrice, dbo.KDVHesapla(UnitPrice) as [KDV Included] from Products as p
join Categories as c on p.CategoryID = c.CategoryID

Alter Function dbo.KDVHesapla(@fiyat money)
returns money
	begin
		return @fiyat * 2.08
	end;


-- Kişilerin yaşlarını hesaplayan UDF yazın

Create Function calculateage(@born datetime)
returns int
	begin
		declare @age int;
		set @age=DATEDIFF(YY, @born, getdate())
		return @age
	end;

-- Fosilleşmiş çalışanı bulalım
select Top 1 FirstName + ' ' + LastName as [Full Name], dbo.calculateage(BirthDate) as [Age] from Employees
order by dbo.calculateage(BirthDate) desc

select * from Employees

-- Tablo döndüren UDF

create function getemployeebyid(@pk int)
returns table
		return select (TitleOfCourtesy + ' ' + FirstName + ' ' + LastName) as [Full Name], 
		dbo.calculateage(BirthDate) as [Age],
		City, 
		HomePhone 
		from Employees 
		where EmployeeID = @pk

select * from getemployeebyid(5)
