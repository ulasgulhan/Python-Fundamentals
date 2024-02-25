-- Triggers
-- Bir tablo üzerinde insert, update ve delete işlemlerinden herhangi biri gerçekleştiğinde otomatik olarak devreye girmesini istediğimiz işlemler varsa bunları trigger olarak dizayn ediyoruz. Bu işlemlerde bize yardımcı olacak iki sanal tablo vardır. Bunlar inserted ve deleted tablolarıdır.
-- Bu tablolar trigger'ın üzerinde tanımlı olduğu base tablo ile birebir aynı yapıdadır. Yani girilen bir kaydı INSERTED tablosundan silinen bir kaydı ise DELETED tablosundan elde edebiliriz. Bir kaydı güncellemek istediğimiz zaman INSERTED ve DELETED tablolarından faydalanıyoruz. Yani direkt UPDATED tablomuz yok

-- İki tip trigger vardır
-- DDL(Data Definition Language)
-- DML(Data Manuplation Language): After ve Instead of olmak üzere ikiye ayrılır.

-- After trigger: Yaptığımız işlemden sonra (insert, update, delete) devreye girer
-- Instead of: Tabloda veya view üzerindeki işlemleri gerçekleştirmek için inserted ve deleted tablolarından kayıt atarlar


-- Bir üründen sipariş alındığında stok miktarını düşüren trigger yazalım

CREATE TRIGGER trg_OrderAdded ON [Order Details]
AFTER INSERT
AS
	DECLARE @amount INT, @productId INT;
	SELECT @amount = Quantity, @productId = ProductID FROM inserted
	UPDATE Products
		SET
			UnitsInStock -= @amount
			WHERE ProductID = @productId


-- Aniseed Syrup insert işlemiden önceki stoğu 13
-- OrderID ProductID UnitPrice Quantity
-- 10248   11        14        12
-- 10248   42        9.80      10
-- 10248   72        34.80     5

select * from [Order Details]
select * from Products where ProductID = 11

INSERT INTO [Order Details]
(
	ProductID,
	Quantity,
	OrderID,
	UnitPrice
)
VALUES
(
	3,
	5,
	10248,
	10
)


-- Sipariş silinirse silinen adet kadarını stoğa ekleyen trigger

CREATE TRIGGER trg_OrderDeleted ON [Order Details]
AFTER DELETE
AS
	DECLARE @amount INT, @productId INT;
	SELECT @amount = Quantity, @productId = ProductID FROM deleted
	UPDATE Products
		SET
			UnitsInStock += @amount
			WHERE ProductID = @productId


DELETE FROM [Order Details]
where OrderID = 10248 and ProductID = 3


-- Bir sipariş içerisindeki ürün adedi değiştirildiğinde stok miktarını ona göre güncelleyen trigger

CREATE TRIGGER trg_UpdateOrder ON [Order Details]
AFTER UPDATE
AS
	DECLARE @oldQuantity INT, @newQuantity INT, @productId INT;
	SELECT @oldQuantity = Quantity FROM deleted;
	SELECT @newQuantity = Quantity, @productId = ProductID FROM inserted
	UPDATE Products
	SET UnitsInStock += @oldQuantity - @newQuantity
	WHERE ProductID = @productId


-- 11	Queso Cabrales	5	4	1 kg pkg.	21.00	22	30	30	0

-- OrderID ProductID UnitPrice Quantity
-- 10248   11        14        12

select * from [Order Details] where OrderID = 10248
select * from Products where ProductID = 11

UPDATE [Order Details] SET Quantity = 22 WHERE OrderID = 10248 AND ProductID = 11


-- Instead of trigger
-- Employees tablosunda bir çalışan kaydını sildiğimizi varsayalım. Bu çalışan kaydı diğer tablolarda geçmesi çok olasıdır. Zaten herhangi bir tabloda kayıt silmek çok mantıklı bir hareket değildir. Bunun yerine kayıtları pasife alacağız.

-- Yukarıdaki case göre Employee tablomuzu güncellememiz gerekmektedir. Yani bir yeni sütun ekleyeceğiz.

ALTER TABLE Employees ADD isActive INT;

CREATE TRIGGER trg_DeleteEmployee ON Employees
INSTEAD OF DELETE
AS
	DECLARE @employeeID INT;
	SELECT @employeeID = EmployeeID FROM deleted
	UPDATE Employees
		SET
			isActive = 1
			WHERE EmployeeID = @employeeID

select * from Employees

DELETE FROM Employees
WHERE EmployeeID = 4


-- Shippers tablosuna insert edilirken kargo numarasını 02122235678 şeklinde girdiğimizde onu formatlı olarak 0(212)223-56-78 haline getiren trigger yazınız

select * from Shippers


CREATE TRIGGER trg_InsertShipper ON Shippers
INSTEAD OF INSERT
AS
	DECLARE @companyName NVARCHAR(50), @phone NVARCHAR(50);
	SELECT @companyName = CompanyName, @phone = Phone from inserted
	DECLARE @formatedPhone NVARCHAR(50)
	SET
		@formatedPhone = LEFT(@phone, 1)+'('+SUBSTRING(@phone, 2, 3)+')'+SUBSTRING(@phone, 5, 3)+'-'+SUBSTRING(@phone, 8, 2)+'-'+RIGHT(@phone, 2)
	INSERT INTO Shippers
	(CompanyName, Phone)
	VALUES
	(@companyName, @formatedPhone)


INSERT INTO Shippers VALUES ('ARAS KARGO', '02122235678')