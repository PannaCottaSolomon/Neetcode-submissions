-- Write your query below

select customer_id from customers 
where revenue > 0
group by customer_id;