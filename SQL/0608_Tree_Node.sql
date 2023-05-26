-- 當沒有 parent id 時就是 Root
-- 當節點是 parent id 的時候，那一定是 inner
-- 節點不是 parent id 的時候才是 leaf

SELECT
    id,
    CASE
        WHEN p_id IS NULL THEN 'Root'
        WHEN p_id IS NOT NULL AND id IN (SELECT DISTINCT p_id FROM Tree) THEN 'Inner'
        ELSE 'Leaf'
    END AS type
FROM Tree
