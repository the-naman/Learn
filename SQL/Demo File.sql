CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (name, email) VALUES 
  ('Naman', 'naman@example.com'),
  ('Alice', 'alice@example.com'),
  ('Bob', 'bob@example.com');

SELECT * FROM users;

drop table users;