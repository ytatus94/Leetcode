-- 要會用函數
-- CONCAT(string1, string2, ...., string_n): 結合字串
-- UPPER(text): 全都變大寫
-- LOWER(text): 全都變小寫
-- LEFT(string, number_of_chars): 從 string 左邊選曲 number_of_chars 個字元
-- SUBSTR(string, start, length) 或是 SUBSTR(string FROM start FOR length): 從 string 選取從 start 開始長度為 length 的子字串
-- SUBSTRING(string, start, length) 和 SUBSTR(string, start, length) 等價

SELECT user_id,
       CONCAT(UPPER(LEFT(name, 1)), LOWER(SUBSTR(name, 2))) AS name
FROM Users
ORDER BY 1

# 方法 2.
# Write your MySQL query statement below
SELECT
    user_id,
    CONCAT(UPPER(LEFT(name, 1)), LOWER(RIGHT(name, LENGTH(name) - 1))) AS name
FROM Users
ORDER BY 1
