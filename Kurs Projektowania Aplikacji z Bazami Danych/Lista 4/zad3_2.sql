INSERT INTO SalesLT.brands(brand_name)
VALUES('Electra');
go

INSERT INTO SalesLT.brands(brand_name)
VALUES('Haro');
go

INSERT INTO SalesLT.brands(brand_name)
VALUES('Trek');
go

INSERT INTO SalesLT.vw_brands(brand_name)
VALUES('Eddy Merckx');
go

SELECT
	brand_name,
	approval_status
FROM
	SalesLT.vw_brands;
go

SELECT 
	*
FROM 
	SalesLT.brand_approvals;
go

