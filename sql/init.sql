CREATE TABLE courier (
    courier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(36) NOT NULL,
    age INT NOT NULL,
    courier_type VARCHAR(4),
    CHECK (courier_type in('foot', 'car', 'bike')),
    CHECK (16<=age and age<=99)
    );

--CREATE TABLE `order` (
--    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
--    weight FLOAT(4,2) NOT NULL,
--    region INT NOT NULL,
--    time_start TIME(0) NOT NULL,
--    time_finish TIME(0) NOT NULL,
--    CHECK (weight>=0.01 AND weight<=50)
--)