SELECT distinct users.id,name,age,others,cast(users.created as char) as created 
FROM users left join address on (user_id=users.id) 
where city = %(city)s;