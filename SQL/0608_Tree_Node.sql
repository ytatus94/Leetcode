SELECT id, CASE
               WHEN p_id IS NULL THEN 'Root'
               WHEN id IN (SELECT DISTINCT p_id FROM tree) THEN 'Inner'
               ELSE 'Leaf'
           END AS 'Type'
FROM tree

-- 這個比較好，有把 p_id IS NOT NULL 考慮進去
SELECT
    id,
    CASE
        WHEN p_id IS NULL THEN 'Root'
        WHEN p_id IS NOT NULL AND id IN (SELECT DISTINCT p_id FROM Tree) THEN 'Inner'
        ELSE 'Leaf'
    END AS type
FROM Tree
