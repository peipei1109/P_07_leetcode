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
 
--Status <> 'completed' OR NULL 中的 OR NULL 是必须的~~，because any none null value(include false and 0) will be counted
SELECT Request_at AS Day
    , ROUND(COUNT(Status <> 'completed' OR NULL) / COUNT(*), 2) AS `Cancellation Rate`
FROM Trips
JOIN Users
ON Users_Id = Client_Id AND Banned = 'No' AND Request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY Request_at;
 
 
