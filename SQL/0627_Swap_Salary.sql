-- 需要用 if condition 來交換 f 和 m
-- 有兩種 if conditions:
-- IF(condition, value_if_true, value_if_false)
-- CASE WHEN condition1 THEN result1 ... WHEN conditionN THEN resultN ELSE result END;

-- 方法1.
UPDATE salary
SET sex = 
  CASE
    WHEN sex = 'm' THEN 'f'
    ELSE 'm'
  END;

-- 方法2.
UPDATE Salary
SET sex = IF(sex = 'm', 'f', 'm');
