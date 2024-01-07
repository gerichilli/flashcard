DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS course;
DROP TABLE IF EXISTS kanji;
DROP TABLE IF EXISTS user_course;
DROP TABLE IF EXISTS course_kanji;
DROP TABLE IF EXISTS user_kanji;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE course (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  level TEXT NOT NULL,
  title TEXT NOT NULL,
  description TEXT NOT NULL
);

CREATE TABLE kanji (
  kanji TEXT PRIMARY KEY,
  jlpt TEXT NOT NULL,
  stroke_count INTEGER NOT NULL,
  on_reading TEXT NOT NULL,
  kun_reading TEXT NOT NULL,
  meanings TEXT NOT NULL
);

CREATE TABLE user_course (
  user_id INTEGER,
  course_id INTEGER,
  percentage FLOAT NOT NULL DEFAULT 0.0,
  PRIMARY KEY (user_id, course_id),
  FOREIGN KEY (user_id) REFERENCES user (id),
  FOREIGN KEY (course_id) REFERENCES course (id)
);

CREATE TABLE course_kanji (
  course_id INTEGER,
  kanji TEXT,
  PRIMARY KEY (course_id, kanji),
  FOREIGN KEY (course_id) REFERENCES course (id),
  FOREIGN KEY (kanji) REFERENCES kanji (kanji)
);

CREATE TABLE user_kanji (
  user_id INTEGER,
  kanji TEXT,
  is_remembered BOOLEAN NOT NULL DEFAULT FALSE,
  PRIMARY KEY (user_id, kanji),
  FOREIGN KEY (user_id) REFERENCES user (id),
  FOREIGN KEY (kanji) REFERENCES kanji (kanji)
);