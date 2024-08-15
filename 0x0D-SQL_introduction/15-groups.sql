-- score
select score , COUNT(score) AS number 
FROM second_table
group by score;
