-- 考會不會 JOIN
SELECT
    Person.FirstName,
    Person.LastName,
    Address.City,
    Address.State
FROM Person
LEFT JOIN Address
ON Person.PersonID = Address.PersonId;

-- 這題並不能用 FROM Person p, Address a WHERE p.personId = a.personId
-- 因為這種寫法是 inner join, 結果只會是 Person 和 Address 的交集
-- 要用 left join 才能保留全部的 p.personId
