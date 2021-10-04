call get_next_address_id(%(user_id)s,@id); -- a procedure to create a dynamic userID
INSERT INTO address (id,user_id,line1,line2,city,country,zipcode) VALUES (@id,%(user_id)s,%(line1)s,%(line2)s,
%(city)s,%(country)s,%(zipcode)s);