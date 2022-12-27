SELECT Email
From Person
GROUP BY Email
HAVING COUNT(*) > 1;
