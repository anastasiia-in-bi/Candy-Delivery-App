CREATE TABLE courier (
    courier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(36) NOT NULL,
    age INT NOT NULL,
    courier_type VARCHAR(4),
    CHECK (courier_type in('foot', 'car', 'bike')),
    CHECK (16<age and age<99)
    );
