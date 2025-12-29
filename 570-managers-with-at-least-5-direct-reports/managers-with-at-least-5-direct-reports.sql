# Write your MySQL query statement below
SELECT
e.name
FROM 
Employee e
JOIN 
Employee ee ON e.id = ee.managerId
Group By 
e.id, e.name
Having 
Count(*) >= 5;