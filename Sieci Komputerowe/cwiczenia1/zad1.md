**Adresy sieci** są pierwsze w danej sieci.
**Adresy rozgłoszeniowe** są ostatnie w danej sieci.
**Adresy komputerów** są pomiędzy.

| Adres CIDR          | Adres sieci     | Adres sieci      | Adres rozgłoszeniowy | Przykładowy adres komputera |
|---------------------|-----------------|------------------|----------------------|-----------------------------|
| 10.1.2.3/8          | 10.0.0.0        | Adres komputera  | 10.255.255.255       | 10.0.0.1                    |
| 156.17.0.0/16       | 156.17.0.0      | Adres sieci      | 156.17.255.255       | 156.17.0.1                  |
| 99.99.99.99/27      | 99.99.99.96     | Adres komputera  | 99.99.99.127         | 99.99.99.97                 |
| 156.17.64.4/30      | 156.17.64.4     | Adres sieci      | 156.17.64.7          | 156.17.64.5                 |
| 123.123.123.123/32  | 123.123.123.123 | Oba na raz       | 123.123.123.123      | Brak dostępnych hostów      |
