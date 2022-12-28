-- 考會不會 DISTINCT 和 WHERE 寫的對不對
SELECT DISTINCT viewer_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY 1;
