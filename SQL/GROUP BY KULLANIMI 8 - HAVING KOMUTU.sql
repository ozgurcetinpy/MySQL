SELECT CITY, SUM(TOTALPRICE) AS TOTALPRICE
FROM SALES
WHERE SUM(TOTALPRICE) > 40000                 
GROUP BY CITY
ORDER BY SUM(TOTALPRICE) DESC

------- DO�RU KULLANIMI -------

SELECT CITY, SUM(TOTALPRICE) AS TOTALPRICE,
COUNT (DISTINCT CUSTOMERNAME)  AS CUSTOMERCOUNT              -- HER M��TER�Y� B�R KERE SAY
FROM SALES
GROUP BY CITY
HAVING SUM(TOTALPRICE) > 40000
ORDER BY SUM(TOTALPRICE) DESC



SELECT CITY, SUM(TOTALPRICE) AS TOTALPRICE,
COUNT (DISTINCT CUSTOMERNAME)  AS CUSTOMERCOUNT              
FROM SALES
GROUP BY CITY
HAVING COUNT(DISTINCT CUSTOMERNAME ) > 300 AND SUM(TOTALPRICE) > 300000
ORDER BY SUM(TOTALPRICE) DESC




SELECT * FROM SALES WHERE TOTALPRICE > 40000 


-- B�R AGGREGATE FONKS�YON B�R �ART OLARAK KULLANILACAKSA , HAVING KOMUTU �LE B�RL�KTE OLMALI