DELETE FROM users WHERE id = %(id)s;
DELETE FROM address WHERE user_id = %(id)s;

