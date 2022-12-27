-- 方法1: 很多 join 所以很慢
# Write your MySQL query statement below
WITH t AS (
    SELECT id,
        month,
        SUM(revenue) AS tot_revenue
    FROM Department
    GROUP BY 1, 2
    ORDER BY 1, 2 
)
SELECT 
    DISTINCT t.id,
    jan.tot_revenue AS "Jan_Revenue",
    feb.tot_revenue AS "Feb_Revenue",
    mar.tot_revenue AS "Mar_Revenue",
    apr.tot_revenue AS "Apr_Revenue",
    may.tot_revenue AS "May_Revenue",
    jun.tot_revenue AS "Jun_Revenue",
    jul.tot_revenue AS "Jul_Revenue",
    aug.tot_revenue AS "Aug_Revenue",
    sep.tot_revenue AS "Sep_Revenue",
    oct.tot_revenue AS "Oct_Revenue",
    nov.tot_revenue AS "Nov_Revenue",
    dece.tot_revenue AS "Dec_Revenue"
FROM t
LEFT JOIN (
    SELECT *
    FROM t
    WHERE month = "Jan"
) AS jan
ON t.id = jan.id
LEFT JOIN (
    SELECT *
    FROM t
    WHERE month = "Feb"
) AS feb
ON t.id = feb.id
LEFT JOIN (
    SELECT *
    FROM t
    WHERE month = "Mar"
) AS mar
ON t.id = mar.id
LEFT JOIN (
    SELECT *
    FROM t
    WHERE month = "Apr"
) AS apr
ON t.id = apr.id
LEFT JOIN (
    SELECT *
    FROM t
    WHERE month = "May"
) AS may
ON t.id = may.id
LEFT JOIN (
    SELECT *
    FROM t
    WHERE month = "Jun"
) AS jun
ON t.id = jun.id
LEFT JOIN (
    SELECT *
    FROM t
    WHERE month = "Jul"
) AS jul
ON t.id = jul.id
LEFT JOIN (
    SELECT *
    FROM t
    WHERE month = "Aug"
) AS aug
ON t.id = aug.id
LEFT JOIN (
    SELECT *
    FROM t
    WHERE month = "Sep"
) AS sep
ON t.id = sep.id
LEFT JOIN (
    SELECT *
    FROM t
    WHERE month = "Oct"
) AS oct
ON t.id = oct.id
LEFT JOIN (
    SELECT *
    FROM t
    WHERE month = "Nov"
) AS nov
ON t.id = nov.id
LEFT JOIN (
    SELECT *
    FROM t
    WHERE month = "Dec"
) AS dece -- 用 dec 會有問題，大概是關鍵字之類的
ON t.id = dece.id

-- 方法2. 用 IF(condition, value_if_true, value_if_false)
SELECT
    id,
    SUM(IF(month = 'Jan', revenue, null)) AS 'Jan_Revenue',
    SUM(IF(month = 'Feb', revenue, null)) AS 'Feb_Revenue',
    SUM(IF(month = 'Mar', revenue, null)) AS 'Mar_Revenue',
    SUM(IF(month = 'Apr', revenue, null)) AS 'Apr_Revenue',
    SUM(IF(month = 'May', revenue, null)) AS 'May_Revenue',
    SUM(IF(month = 'Jun', revenue, null)) AS 'Jun_Revenue',
    SUM(IF(month = 'Jul', revenue, null)) AS 'Jul_Revenue',
    SUM(IF(month = 'Aug', revenue, null)) AS 'Aug_Revenue',
    SUM(IF(month = 'Sep', revenue, null)) AS 'Sep_Revenue',
    SUM(IF(month = 'Oct', revenue, null)) AS 'Oct_Revenue',
    SUM(IF(month = 'Nov', revenue, null)) AS 'Nov_Revenue',
    SUM(IF(month = 'Dec', revenue, null)) AS 'Dec_Revenue'
FROM Department
GROUP BY 1
