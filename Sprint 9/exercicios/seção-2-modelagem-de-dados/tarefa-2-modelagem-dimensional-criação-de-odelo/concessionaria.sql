BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "tb_locacao" (
	"idLocacao"	int,
	"idCliente"	int,
	"nomeCliente"	varchar(100),
	"cidadeCliente"	varchar(40),
	"estadoCliente"	varchar(40),
	"paisCliente"	varchar(40),
	"idCarro"	int,
	"kmCarro"	int,
	"classiCarro"	varchar(50),
	"marcaCarro"	varchar(80),
	"modeloCarro"	varchar(80),
	"anoCarro"	int,
	"idcombustivel"	int,
	"tipoCombustivel"	varchar(20),
	"dataLocacao"	datetime,
	"horaLocacao"	time,
	"qtdDiaria"	int,
	"vlrDiaria"	decimal(18, 2),
	"dataEntrega"	date,
	"horaEntrega"	time,
	"idVendedor"	int,
	"nomeVendedor"	varchar(15),
	"sexoVendedor"	smallint,
	"estadoVendedor"	varchar(40),
	PRIMARY KEY("idLocacao")
);
INSERT INTO "tb_locacao" VALUES (1,2,'Cliente dois','São Paulo','São Paulo','Brasil',98,25412,'AKJHKN98JY76539','Fiat','Fiat Uno',2000,1,'Gasolina',20150110,'10:00',2,100,20150112,'10:00',5,'Vendedor cinco',0,'São Paulo');
INSERT INTO "tb_locacao" VALUES (2,2,'Cliente dois','São Paulo','São Paulo','Brasil',98,29450,'AKJHKN98JY76539','Fiat','Fiat Uno',2000,1,'Gasolina',20150210,'12:00',2,100,20150212,'12:00',5,'Vendedor cinco',0,'São Paulo');
INSERT INTO "tb_locacao" VALUES (3,3,'Cliente tres','Rio de Janeiro','Rio de Janeiro','Brasil',99,20000,'IKJHKN98JY76539','Fiat','Fiat Palio',2010,1,'Gasolina',20150213,'12:00',2,150,20150215,'12:00',6,'Vendedora seis',1,'São Paulo');
INSERT INTO "tb_locacao" VALUES (4,4,'Cliente quatro','Rio de Janeiro','Rio de Janeiro','Brasil',99,21000,'IKJHKN98JY76539','Fiat','Fiat Palio',2010,1,'Gasolina',20150215,'13:00',5,150,20150220,'13:00',6,'Vendedora seis',1,'São Paulo');
INSERT INTO "tb_locacao" VALUES (5,4,'Cliente quatro','Rio de Janeiro','Rio de Janeiro','Brasil',99,21700,'IKJHKN98JY76539','Fiat','Fiat Palio',2010,1,'Gasolina',20150302,'14:00',5,150,20150307,'14:00',7,'Vendedora sete',1,'Rio de Janeiro');
INSERT INTO "tb_locacao" VALUES (6,6,'Cliente seis','Belo Horizonte','Minas Gerais','Brasil',3,121700,'DKSHKNS8JS76S39','VW','Fusca 78',1978,1,'Gasolina',20160302,'14:00',10,250,20160312,'14:00',8,'Vendedora oito',1,'Minas Gerais');
INSERT INTO "tb_locacao" VALUES (7,6,'Cliente seis','Belo Horizonte','Minas Gerais','Brasil',3,131800,'DKSHKNS8JS76S39','VW','Fusca 78',1978,1,'Gasolina',20160802,'14:00',10,250,20160812,'14:00',8,'Vendedora oito',1,'Minas Gerais');
INSERT INTO "tb_locacao" VALUES (8,4,'Cliente quatro','Rio de Janeiro','Rio de Janeiro','Brasil',3,151800,'DKSHKNS8JS76S39','VW','Fusca 78',1978,1,'Gasolina',20170102,'18:00',10,250,20170112,'18:00',6,'Vendedora seis',1,'São Paulo');
INSERT INTO "tb_locacao" VALUES (9,4,'Cliente quatro','Rio de Janeiro','Rio de Janeiro','Brasil',3,152800,'DKSHKNS8JS76S39','VW','Fusca 78',1978,1,'Gasolina',20180102,'18:00',10,280,20180112,'18:00',6,'Vendedora seis',1,'São Paulo');
INSERT INTO "tb_locacao" VALUES (10,10,'Cliente dez','Rio Branco','Acre','Brasil',10,211800,'LKIUNS8JS76S39','Fiat','Fiat 147',1996,1,'Gasolina',20180302,'18:00',10,50,20180312,'18:00',16,'Vendedor dezesseis',0,'Amazonas');
INSERT INTO "tb_locacao" VALUES (11,20,'Cliente vinte','Macapá','Amapá','Brasil',7,212800,'SSIUNS8JS76S39','Fiat','Fiat 147',1996,1,'Gasolina',20180401,'11:00',10,50,20180411,'11:00',16,'Vendedor dezesseis',0,'Amazonas');
INSERT INTO "tb_locacao" VALUES (12,20,'Cliente vinte','Macapá','Amapá','Brasil',6,21800,'SKIUNS8JS76S39','Nissan','Versa',2019,1,'Gasolina',20200401,'11:00',10,150,20200411,'11:00',16,'Vendedor dezesseis',0,'Amazonas');
INSERT INTO "tb_locacao" VALUES (13,22,'Cliente vinte e dois','Porto Alegre','Rio Grande do Sul','Brasil',2,10000,'AKIUNS1JS76S39','Nissan','Versa',2019,2,'Etanol',20220501,'8:00',20,150,20220521,'18:00',30,'Vendedor trinta',0,'Rio Grande do Sul');
INSERT INTO "tb_locacao" VALUES (14,22,'Cliente vinte e dois','Porto Alegre','Rio Grande do Sul','Brasil',2,20000,'AKIUNS1JS76S39','Nissan','Versa',2019,2,'Etanol',20220601,'8:00',20,150,20220621,'18:00',30,'Vendedor trinta',0,'Rio Grande do Sul');
INSERT INTO "tb_locacao" VALUES (15,22,'Cliente vinte e dois','Porto Alegre','Rio Grande do Sul','Brasil',2,30000,'AKIUNS1JS76S39','Nissan','Versa',2019,2,'Etanol',20220701,'8:00',20,150,20220721,'18:00',30,'Vendedor trinta',0,'Rio Grande do Sul');
INSERT INTO "tb_locacao" VALUES (16,22,'Cliente vinte e dois','Porto Alegre','Rio Grande do Sul','Brasil',2,40000,'AKIUNS1JS76S39','Nissan','Versa',2019,2,'Etanol',20220801,'8:00',20,150,20220721,'18:00',30,'Vendedor trinta',0,'Rio Grande do Sul');
INSERT INTO "tb_locacao" VALUES (17,23,'Cliente vinte e tres','Eusébio','Ceará','Brasil',4,55000,'LLLUNS1JS76S39','Nissan','Versa',2020,2,'Etanol',20220901,'8:00',20,150,20220921,'18:00',31,'Vendedor trinta e um',0,'Ceará');
INSERT INTO "tb_locacao" VALUES (18,23,'Cliente vinte e tres','Eusébio','Ceará','Brasil',4,56000,'LLLUNS1JS76S39','Nissan','Versa',2020,2,'Etanol',20221001,'8:00',20,150,20221021,'18:00',31,'Vendedor trinta e um',0,'Ceará');
INSERT INTO "tb_locacao" VALUES (19,23,'Cliente vinte e tres','Eusébio','Ceará','Brasil',4,58000,'LLLUNS1JS76S39','Nissan','Versa',2020,2,'Etanol',20221101,'8:00',20,150,20221121,'18:00',31,'Vendedor trinta e um',0,'Ceará');
INSERT INTO "tb_locacao" VALUES (20,5,'Cliente cinco','Manaus','Amazonas','Brasil',1,1800,'AAAKNS8JS76S39','Toyota','Corolla XEI',2023,3,'Flex',20230102,'18:00',10,880,20230112,'18:00',16,'Vendedor dezesseis',0,'Amazonas');
INSERT INTO "tb_locacao" VALUES (21,5,'Cliente cinco','Manaus','Amazonas','Brasil',1,8500,'AAAKNS8JS76S39','Toyota','Corolla XEI',2023,3,'Flex',20230115,'18:00',10,880,20230125,'18:00',16,'Vendedor dezesseis',0,'Amazonas');
INSERT INTO "tb_locacao" VALUES (22,26,'Cliente vinte e seis','Campo Grande','Mato Grosso do Sul','Brasil',5,28000,'MSLUNS1JS76S39','Nissan','Frontier',2022,4,'Diesel',20230125,'8:00',5,600,20230130,'18:00',32,'Vendedora trinta e dois',1,'Mato Grosso do Sul');
INSERT INTO "tb_locacao" VALUES (23,26,'Cliente vinte e seis','Campo Grande','Mato Grosso do Sul','Brasil',5,38000,'MSLUNS1JS76S39','Nissan','Frontier',2022,4,'Diesel',20230131,'8:00',5,600,20230205,'18:00',32,'Vendedora trinta e dois',1,'Mato Grosso do Sul');
INSERT INTO "tb_locacao" VALUES (24,26,'Cliente vinte e seis','Campo Grande','Mato Grosso do Sul','Brasil',5,48000,'MSLUNS1JS76S39','Nissan','Frontier',2022,4,'Diesel',20230206,'8:00',5,600,20230211,'18:00',32,'Vendedora trinta e dois',1,'Mato Grosso do Sul');
INSERT INTO "tb_locacao" VALUES (25,26,'Cliente vinte e seis','Campo Grande','Mato Grosso do Sul','Brasil',5,68000,'MSLUNS1JS76S39','Nissan','Frontier',2022,4,'Diesel',20230212,'8:00',5,600,20230217,'18:00',32,'Vendedora trinta e dois',1,'Mato Grosso do Sul');
INSERT INTO "tb_locacao" VALUES (26,26,'Cliente vinte e seis','Campo Grande','Mato Grosso do Sul','Brasil',5,78000,'MSLUNS1JS76S39','Nissan','Frontier',2022,4,'Diesel',20230218,'8:00',1,600,20230219,'18:00',32,'Vendedora trinta e dois',1,'Mato Grosso do Sul');
CREATE VIEW dimCarro AS
SELECT
	idCarro,
	marcaCarro,
	modeloCarro,
	classiCarro,
	anoCarro
FROM tb_locacao;
CREATE VIEW dimCliente AS
SELECT
	idCliente,
    nomeCliente,
    paisCliente,
    cidadeCliente,
    estadoCliente
FROM tb_locacao;
CREATE VIEW dimCombustivel AS
SELECT
	idcombustivel,
	tipoCombustivel
FROM tb_locacao;
CREATE VIEW dimVendedor AS
SELECT 
	idVendedor,
	nomeVendedor,
	sexoVendedor,
	estadoVendedor
FROM tb_locacao;
CREATE VIEW fatoLocacao AS
SELECT 
	idLocacao,
	idCarro,
	idCliente,
	idVendedor,
	idcombustivel,
	qtdDiaria,
	vlrDiaria,
	kmCarro,
	dataLocacao,
	horaLocacao,
	dataEntrega,
	horaEntrega
FROM tb_locacao;
COMMIT;
