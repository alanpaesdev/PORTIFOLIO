CREATE TABLE IF NOT EXISTS gps (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    latitude REAL,
    longitude REAL,
    timestamp TEXT
);

CREATE TABLE IF NOT EXISTS diario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    texto TEXT,
    sentimento TEXT,
    timestamp TEXT
);

CREATE TABLE IF NOT EXISTS camera (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    objects TEXT,
    timestamp TEXT
);