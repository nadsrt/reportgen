DROP TABLE IF EXISTS user;

CREATE TABLE user (
  aptdate     TEXT NOT NULL,
  nation      TEXT NOT NULL,
  address     TEXT NOT NULL,
  zipcode     TEXT NOT NULL,
  ziptwodig   TEXT NOT NULL
);

CREATE TABLE sgpost (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ziptwodig  TEXT NOT NULL,
  district   TEXT NOT NULL,
  distno     INTEGER NOT NULL,
  region     TEXT NOT NULL
);
