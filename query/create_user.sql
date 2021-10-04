CALL get_next_id(@id,'users','created','USR'); -- a procedure to create a dynamic userID
INSERT INTO users (id,name,age,others) VALUES (@id,%(name)s,%(age)s,%(others)s);
-- COMMIT;