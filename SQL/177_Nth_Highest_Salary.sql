-- 第一高的 salary 不用 offset (offset 0)
-- 第二高的 salary 要 offset 1
-- 第 n 高的 salary 要 offset n-1

-- 方法 1.
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE M INT;
  SET M=N-1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT salary
      FROM Employee
      ORDER BY salary DESC
      LIMIT 1
      OFFSET M
  );
END

-- 方法 2.
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE M INT;
  SET M=N-1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT IFNULL(
          (SELECT DISTINCT salary FROM Employee ORDER BY salary DESC LIMIT M, 1),
          NULL
      )
  );
END
