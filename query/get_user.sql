SELECT id,name,age,others,cast(created as char) as created FROM users where id = %(id)s;