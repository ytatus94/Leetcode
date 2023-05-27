# 方法 1.
# Write your MySQL query statement below
SELECT
    ROUND(AVG(d.order_date = d.customer_pref_delivery_date) * 100., 2) AS immediate_percentage
FROM Delivery AS d
JOIN (
    SELECT
        customer_id,
        MIN(order_date) AS min_order_date
    FROM Delivery
    GROUP BY 1
) AS d2
ON d.customer_id = d2.customer_id AND
   d.order_date = d2.min_order_date;
   
# 方法 2.
# Write your MySQL query statement below
SELECT
    ROUND(AVG(order_date = customer_pref_delivery_date) * 100., 2) AS immediate_percentage
FROM Delivery
WHERE (customer_id, order_date) IN (
    SELECT
        customer_id,
        MIN(order_date)
    FROM Delivery
    GROUP BY 1
);
