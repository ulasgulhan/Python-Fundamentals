-- Stored Procedures
-- SP'ler server tarafında tutulan, bir kez derlendikten yani bir kez çalıştırıldıktan sonra derlenmeyen sorgulardır. Bu da bize hız sağlar
-- Client'lar SP'leri çalıştırırken kendi bilgisayarlarında değil server tarafomdam yapılacak işlemlerin sonucunu beklerler
-- Fonksyionlar gibi parametre alabilirler
-- Takvime bağlayarak belirli gün ve saatlerde çalışabilirler. Job olarak da çalıştırabiliriz.
-- Network trafiğini yormazlar. SQL saldırılarından Injection atağına karşı parametreli olarak yazılırlar, böylece güvenlik sağlanmaya çalışılınır. View gibi SP'leri kullanabiliriz. Ancak View'lar parametre almazken SP'ler alabilirler. Böylelikle dinamik View'lar oluşturabiliriz.
-- Uygulumalar arasında ortak çalışabilirler. Yani app hangi dille yazılırsa yazılsın ortak SP kullanılabilinir.
-- App tarafındaki business logic'lerimizi SQL tarafında SP'ler ile yapabiliriz. Örneğin bir insert işlemi gerçekleştiğinde bu işlem ile birlikte olması gereken tüm işleri SP içerisinde kurgulayabiliriz. Hatta işlem sonucunda TSQL ile select yapıp sonucu dönebiliriz.


CREATE PROCEDURE sp_ListEmployee
AS
	BEGIN
		SELECT FirstName, LastName, Title FROM Employees
	END;

execute sp_ListEmployee
drop procedure sp_ListEmployee

select * from Categories
select * from [Order Details]


CREATE PROCEDURE sp_CategorySales
AS
	BEGIN
		SELECT c.CategoryName, sum(od.Quantity) as Quantity, ROUND(SUM((1-od.Discount) * od.Quantity * od.UnitPrice), 2) as Income FROM Categories as c
		join Products as p on c.CategoryID = p.ProductID
		join [Order Details] as od on p.ProductID = od.ProductID
		group by c.CategoryName
		order by Income DESC
	END;

execute sp_CategorySales


-- ID sine göre çalışan getirelim

CREATE PROCEDURE sp_EmployeeById @employeeId INT
AS
	BEGIN
		SELECT (TitleOfCourtesy+SPACE(1)+FirstName+SPACE(1)+LastName) as [Full Name], dbo.calculateage(BirthDate) as [Age] FROM Employees where EmployeeID = @employeeId
	END;


exec sp_EmployeeById 9


ALTER PROCEDURE sp_EmployeeById @firstName NVARCHAR(50), @lastName NVARCHAR(50)
AS
	BEGIN
		SELECT (TitleOfCourtesy+SPACE(1)+FirstName+SPACE(1)+LastName) as [Full Name], dbo.calculateage(BirthDate) as [Age] FROM Employees where FirstName = @firstName and LastName = @lastName
	END;


exec sp_EmployeeById @firstName = 'Robert', @lastName = 'King'


CREATE PROCEDURE sp_InsertOrderDetail
	@productId int,
	@quantity int,
	@orderId int,
	@unitPrice int
AS
	BEGiN
		INSERT INTO [Order Details]
		(
			ProductID, Quantity, OrderID, UnitPrice
		)
		VALUES
		(
			@productId, @quantity, @orderId, @unitPrice
		)
		select * from [Order Details] where OrderID = @orderId
	END


exec sp_InsertOrderDetail
	@productId = 10,
	@quantity = 1,
	@orderId = 10248,
	@unitPrice = 31

select * from Products where ProductID = 10
select * from [Order Details]