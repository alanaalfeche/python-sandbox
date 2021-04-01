"""175. Combine Two Tables

Write a SQL query for a report that provides the following information for each person in the Person table,
regardless if there is an address for each of those people: FirstName, LastName, City, State

Table: Person
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+

Table: Address
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+ 
"""
-- We wanted a left join on this query because we want null for person that doesn't have address
SELECT FirstName, LastName, City, State
FROM Person 
LEFT JOIN Address on Person.PersonId = Address.PersonId
