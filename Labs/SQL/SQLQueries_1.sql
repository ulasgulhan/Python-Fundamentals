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
