CREATE TABLE M1 (
    K INT PRIMARY KEY,
    V VARCHAR(20)
);

CREATE TABLE S1 (
    K INT PRIMARY KEY,
    MFK INT,
    V VARCHAR(20),
    FOREIGN KEY (MFK) REFERENCES M1(K)
);
