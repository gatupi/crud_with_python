USE Commerce;
GO

DROP TABLE IF EXISTS Customer;
GO

CREATE OR ALTER FUNCTION CalculateAge(@date DATE) RETURNS INT
BEGIN
	DECLARE @today DATE = GETDATE();
	
	IF (@date > @today)
		RETURN NULL;

	DECLARE @yearDiff INT = YEAR(@today) - YEAR(@date);

	IF (@yearDiff > 0) BEGIN
		DECLARE @monthDiff INT = MONTH(@today) - MONTH(@date);
		DECLARE @dayDiff INT = DAY(@today) - DAY(@date);

		RETURN @yearDiff - IIF(@monthDiff < 0 OR (@monthDiff = 0 AND @dayDiff < 0), 1, 0);
	END

	RETURN 0;
END
GO

CREATE TABLE Customer (
	Id INT IDENTITY(1,1) NOT NULL,
	FirstName NVARCHAR(30) NOT NULL,
	MiddleName NVARCHAR(40) NULL,
	LastName NVARCHAR(30) NOT NULL,
	BirthDate DATE NOT NULL,
	Gender CHAR(1) NOT NULL,
	PhoneNumber CHAR(11) NOT NULL,
	Email VARCHAR(60) NOT NULL,
	CONSTRAINT PK_Customer PRIMARY KEY(Id),
	CONSTRAINT CK_Customer_Name CHECK(LEN(FirstName) > 1 AND LEN(LastName) > 1 AND (MiddleName IS NULL OR LEN(MiddleName) > 1)),
	CONSTRAINT CK_Customer_Age CHECK(dbo.CalculateAge(BirthDate) >= 18),
	CONSTRAINT CK_Customer_Gender CHECK(Gender IN ('M', 'F')),
	CONSTRAINT CK_Customer_PhoneNumber CHECK(ISNUMERIC(PhoneNumber) <> 0)
);
GO

CREATE OR ALTER PROCEDURE InsertCustomer(
	@id INT,
	@firstName NVARCHAR(30),
	@middleName NVARCHAR(40),
	@lastName NVARCHAR(30),
	@birthDate DATE,
	@gender CHAR(1),
	@phoneNumber CHAR(11),
	@email VARCHAR(60)) AS
BEGIN
	IF @id IS NOT NULL AND @id > 0 BEGIN
		SET IDENTITY_INSERT Customer ON;
		INSERT INTO Customer (Id, FirstName, MiddleName, LastName, BirthDate, Gender, PhoneNumber, Email)
			VALUES (@id, @firstName, @middleName, @lastName, @birthDate, @gender, @phoneNumber, @email);
		SET IDENTITY_INSERT Customer OFF;
	END
	ELSE BEGIN
		INSERT INTO Customer (FirstName, MiddleName, LastName, BirthDate, Gender, PhoneNumber, Email)
			VALUES (@firstName, @middleName, @lastName, @birthDate, @gender, @phoneNumber, @email);
	END
END
GO

CREATE OR ALTER PROCEDURE UpdateCustomer(
	@customerId INT,
	@firstName NVARCHAR(30),
	@middleName NVARCHAR(40),
	@lastName NVARCHAR(30),
	@birthDate DATE,
	@gender CHAR(1),
	@phoneNumber CHAR(11),
	@email VARCHAR(60)
) AS
BEGIN
	UPDATE Customer SET
		FirstName = @firstName,
		MiddleName = @middleName,
		LastName = @lastName,
		BirthDate = @birthDate,
		Gender = @gender,
		PhoneNumber = @phoneNumber,
		Email = @email
		WHERE Id = @customerId;
END
GO