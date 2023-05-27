# Write your MySQL query statement below
SELECT s.student_id,
       s.student_name,
       s2.subject_name,
       COUNT(e.subject_name) AS attended_exams
FROM Students AS s
JOIN  Subjects AS s2
LEFT JOIN Examinations AS e
ON s.student_id = e.student_id AND
   e.subject_name = s2.subject_name
GROUP BY 1, 2, 3
ORDER BY 1, 3;
