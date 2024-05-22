-- task1)
-- İlk olaraq satışı reallaşmış məhsullar üçün bir cədvəl (tabel) 
-- yaradırıq və bu cədvəlimizin sütun olaraq məhsul idsi, sayı və
-- dəyəri (1 dənəsinin)  olacaq. Biz isə hər məhsul 
-- üçün ümumi olan qazancı gətirib sıralamaq lazımdır

-- task2)
-- işçilər adında cədvəlimiz olacaq. Sütun olaraq ad,maaş,
-- departament olacaq. Siz isə departamentinin adı satış olan 
-- və maaşı 600-dən çox olan şəxslərin maaşını azalan sıra ilə 
-- sıralıyın

-- task3)
-- kitablar cədvəlimiz olacaq. Sütunları: adı, janrı, nəşr ili
-- .2015-dən sonra nəşr olunmuş kitbaabları janrına görə artan
-- sıra ilə sıralıyın

-- task4)
-- filmlər adlı cədvəlimiz olacaq. Sütunları : ad, çıxış tarixi,
-- ratinq. Çıxış tarixi 2000-dən kiçik olanları artan sıra və 
-- ratingi 7-dən böyük olanları azalan sıra ilə sıralıyın


-- TASK 1 
DROP TABLE SOLD_ITEMS;

CREATE TABLE SOLD_ITEMS (
    MEHSUL_ID INT PRIMARY KEY,
    MEHSUL_SAY INT,
    MEHSUL_DEYER INT
);

INSERT INTO SOLD_ITEMS (MEHSUL_ID, MEHSUL_SAY, MEHSUL_DEYER)
VALUES (1, 3000, 500),
       (2, 2500, 600),
       (3, 10000, 258),
       (4, 3333, 476);


SELECT MEHSUL_ID,
       SUM(MEHSUL_SAY * MEHSUL_DEYER) AS UMUMI_QAZANC
FROM SOLD_ITEMS
GROUP BY MEHSUL_ID
ORDER BY UMUMI_QAZANC DESC;



-- TASK 2
DROP TABLE ISCILER;
CREATE TABLE ISCILER(
  AD VARCHAR(50),
  MAAS INT,
  SOBE VARCHAR(50)
);

INSERT INTO ISCILER(AD, MAAS, SOBE)
VALUES  ('eli', 500, 'it'),
		('veli', 400, 'satış'),
        ('esmer', 680, 'satış'),
		('nihad', 800, 'it'),
		('fidan', 1100, 'fin'),
		('yusif', 760, 'satış');
        
--SELECT * FROM ISCILER
SELECT MAAS 
FROM ISCILER 
WHERE SOBE = 'satış' AND MAAS > 600 
ORDER BY MAAS DESC;


--TASK 3
DROP TABLE KITABLAR;
CREATE TABLE KITABLAR(
  ADI VARCHAR(50),
  JANRI VARCHAR(50),
  NESR_ILI INT
);

INSERT INTO KITABLAR(ADI, JANRI, NESR_ILI)
VALUES  ('ORIGIN', 'ADVENTURE', 2019),
		('INFERNO', 'ADVENTURE', 2014),
        ('ANIMAL FARM', 'CLASSIC', 2000),
        ('OLIVER', 'NOVEL', 2016),
        ('SAPIENS', 'SCI', 2018);


SELECT JANRI FROM KITABLAR 
WHERE NESR_ILI > 2015
ORDER BY NESR_ILI ASC


--TASK 4
DROP TABLE MOVIES;	
CREATE TABLE MOVIES(
  AD VARCHAR(100),
  CIXIS_TARIX INT,
  RATING INT
);

INSERT INTO MOVIES(AD, CIXIS_TARIX, RATING)
VALUES  ('PANDA', 1980, 5),
		('SPLIT', 2019, 3),
        ('OPPENHEIMER', 2023, 7),
        ('CASABLANCA', 1945, 8),
        ('IRON MAN 4', 2020, 4),
        ('INFITIY WAR', 1999, 2);

SELECT AD
FROM MOVIES
WHERE CIXIS_TARIX < 2000 AND RATING > 7
ORDER BY CIXIS_TARIX ASC, RATING DESC;

