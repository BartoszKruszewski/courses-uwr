DROP TABLE IF EXISTS firstnames
GO

DROP TABLE IF EXISTS lastnames
GO

DROP TABLE IF EXISTS fldata
GO

CREATE TABLE firstnames (
    id INT PRIMARY KEY,
    firstname VARCHAR(255)
);

CREATE TABLE lastnames (
    id INT PRIMARY KEY,
    lastname VARCHAR(255)
);

CREATE TABLE fldata (
    firstname VARCHAR(255),
    lastname VARCHAR(255),
    PRIMARY KEY (firstname, lastname)
);
GO
