CREATE TABLE IF NOT EXISTS users11 (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users11 (name, email) VALUES 
  ('Naman', 'naman@example.com'),
  ('Alice', 'alice@example.com'),
  ('Bob', 'bob@example.com');

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
SELECT * FROM users1;

drop table users1;
=======
SELECT * FROM users;

drop table users;
>>>>>>> 5da8053 (Add daily migration workflows)
=======
SELECT * FROM users;

drop table users;
>>>>>>> origin/PROD
=======
SELECT * FROM users11;

Drop table users11;
>>>>>>> origin/PROD
