-- 要知道怎麼用通配符 %
SELECT patient_id,
       patient_name,
       conditions
FROM Patients
WHERE conditions LIKE 'DIAB1%' OR conditions LIKE '% DIAB1%';

# 方法 2.
# Write your MySQL query statement below
SELECT *
FROM Patients
WHERE conditions LIKE 'DIAB1%' OR
      conditions LIKE '% DIAB1%';
