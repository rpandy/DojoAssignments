SELECT * FROM users;

INSERT INTO users (first_name, last_name, created_at, updated_at)
VALUES ('Auburn', 'Pandy', now(), now());

SELECT * FROM friendships;

INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES (4,3,now(),now());

SELECT users.first_name, users.last_name, user2.first_name as 'friends_first_name', user2.last_name as 'friends_last_name'
FROM users
LEFT JOIN friendships 
ON users.id = friendships.user_id
LEFT JOIN users as user2 
ON friendships.friend_id = user2.id
ORDER BY user2.last_name ASC;

