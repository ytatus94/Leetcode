-- 考會不會 JOIN
SELECT
    Person.FirstName,
    Person.LastName,
    Address.City,
    Address.State
FROM Person
LEFT JOIN Address
ON Person.PersonID = Address.PersonId;
