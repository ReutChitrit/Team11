create table city_location
(
    latitude  float        null,
    longitude float        null,
    city      varchar(100) not null
        primary key
);

INSERT INTO group11.city_location (latitude, longitude, city) VALUES (29.5579, 34.9519, 'אילת');
INSERT INTO group11.city_location (latitude, longitude, city) VALUES (31.8014, 34.6435, 'אשדוד');
INSERT INTO group11.city_location (latitude, longitude, city) VALUES (31.8014, 34.6435, 'אשקלון');
INSERT INTO group11.city_location (latitude, longitude, city) VALUES (32.28, 34.9999, 'הרצליה');
INSERT INTO group11.city_location (latitude, longitude, city) VALUES (32.1093, 34.8555, 'חיפה');
INSERT INTO group11.city_location (latitude, longitude, city) VALUES (31.973, 34.7925, 'נתניה');
INSERT INTO group11.city_location (latitude, longitude, city) VALUES (32.1663, 34.8433, 'ראשון-לציון');
INSERT INTO group11.city_location (latitude, longitude, city) VALUES (32.794, 34.9896, 'תל-אביב');