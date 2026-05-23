CREATE TABLE IF NOT EXISTS users1 (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users1 (name, email) VALUES 
  ('Naman', 'naman@example.com'),
  ('Alice', 'alice@example.com'),
  ('Bob', 'bob1@example.com');

SELECT * FROM users1;

drop table users1;