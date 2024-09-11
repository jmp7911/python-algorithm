# Write your MySQL query statement below
select d.name as Department, e.name as Employee, salary as Salary from Employee e join Department d on e.departmentId = d.id
where (e.departmentId, Salary) in (
        SELECT 
            departmentId, 
            MAX(Salary) 
        FROM 
            Employee 
        GROUP BY 
            departmentId
    );