--

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
       SELECT e1.Salary
      FROM (SELECT DISTINCT Salary FROM Employee) e1
      WHERE (SELECT COUNT(*) FROM (SELECT DISTINCT Salary FROM Employee) e2 WHERE e2.Salary > e1.Salary) = N - 1      
      
      LIMIT 1
      
  );
END


CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
 BEGIN
 set N=N-1;
 RETURN (
 # Write your MySQL query statement below.
 select( select distinct Salary from Employee order by Salary Desc limit 1 offset N )as nthHightestSalary

);
 END
 
 CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
 BEGIN
 set N=N-1;
 RETURN (
 # Write your MySQL query statement below.
 select( select distinct Salary from Employee order by Salary Desc limit N, 1 )as nthHightestSalary

);
 END
 
 
 
