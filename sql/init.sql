CREATE TABLE courier (
    courier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(36) NOT NULL,
    age INT NOT NULL,
    courier_type VARCHAR(4),
    CONSTRAINT courier_type CHECK (courier_type in('foot', 'car', 'bike')),
    CONSTRAINT courier_age CHECK (16<=age and age<=99)
    );

--CREATE TABLE courier_working_hours (
--    courier_id INTEGER NOT NULL,
--    working_hours_start TIME(0) NOT NULL,
--    working_hours_finish TIME(0) NOT NULL,
--    CONSTRAINT courier_working_hours_pk PRIMARY KEY (courier_id),
--    CONSTRAINT courier_working_hours_fk FOREIGN KEY (courier_id) REFERENCES courier(courier_id),
--    CONSTRAINT courier_working_hours_unique UNIQUE (courier_id, working_hours_start, working_hours_finish)
--    );

--CREATE TABLE courier_regions (
--    courier_id INTEGER NOT NULL,
--    region_id INTEGER NOT NULL,
--    CONSTRAINT courier_regions_pk PRIMARY KEY (courier_id, region_id),
--    CONSTRAINT courier_regions_fk FOREIGN KEY (courier_id) REFERENCES courier(courier_id)
--    );

--CREATE TABLE `order` (
--    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
--    weight FLOAT(4,2) NOT NULL,
--    region INT NOT NULL,
--    time_start TIME(0) NOT NULL,
--    time_finish TIME(0) NOT NULL,
--    CONSTRAINT order_weight CHECK (weight >=0.01 AND weight<=50)
--);

--CREATE TABLE order_delivery_hours (
--    order_id INTEGER NOT NULL,
--    delivery_hours_start TIME(0) NOT NULL,
--    delivery_hours_finish TIME(0) NOT NULL,
--    CONSTRAINT order_delivery_hours_pk PRIMARY KEY (order_id),
--    CONSTRAINT order_delivery_hours_fk FOREIGN KEY (order_id) REFERENCES `order`(order_id),
--    CONSTRAINT order_delivery_hours_unique UNIQUE (order_id, delivery_hours_start, delivery_hours_finish)
--    );

--CREATE TABLE order_assign (
--    courier_id INTEGER NOT NULL,
--    order_id INTEGER NOT NULL,
--    assign_time TIME(0) NOT NULL,
--    complete_time TIME(0),
--    CONSTRAINT order_assign_pk PRIMARY KEY (courier_id, order_id),
--    CONSTRAINT order_assign_unique_order UNIQUE (order_id)
--    );