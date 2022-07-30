create table contactus
(
    serial_number int auto_increment
        primary key,
    email         text                               null,
    phone_number  varchar(15)                        null,
    frequency     enum ('גבוהה', 'בינונית', 'נמוכה') null,
    text          text                               null
);

INSERT INTO group11.contactus (serial_number, email, phone_number, frequency, text) VALUES (1, 'dana@gmail.com', '523768544', 'גבוהה', 'היי,
שעות הפתיחה של מועדון הגלישה געש השתנו, שימו לב');
INSERT INTO group11.contactus (serial_number, email, phone_number, frequency, text) VALUES (2, 'nurit@gmail.com', '546785543', 'נמוכה', 'לא התחברתי');
INSERT INTO group11.contactus (serial_number, email, phone_number, frequency, text) VALUES (3, 'dani@gmail.com', '543221678', 'נמוכה', 'אהבתי, אתר מהמם');
INSERT INTO group11.contactus (serial_number, email, phone_number, frequency, text) VALUES (5, 'dani@gmail.com', '543221678', 'בינונית', 'שלום,
הייתי שמח שהייתם שמים דגש יותר על שמירה על חופי ישראל באתר, הנושא הינו חשוב מאוד וראוי לכך');
INSERT INTO group11.contactus (serial_number, email, phone_number, frequency, text) VALUES (6, 'dani@gmail.com', '543221678', 'בינונית', 'אשמח שתוסיפו עוד מועדוני גלישה מומלצים באיזור הצפון. 
תודה');
INSERT INTO group11.contactus (serial_number, email, phone_number, frequency, text) VALUES (7, 'ori@gmail.com', '547865121', 'נמוכה', 'זו הפעם הראשונה שאני נכנס לאתר וממש הופתעתי לטובה, אמשיך להתשמש בו!');
INSERT INTO group11.contactus (serial_number, email, phone_number, frequency, text) VALUES (8, 'jonny@gmail.com', '547863342', 'גבוהה', 'כל פעם נהנה להיכנס לאתר מחדש!');
INSERT INTO group11.contactus (serial_number, email, phone_number, frequency, text) VALUES (9, 'weasly@gmail.com', '544612342', 'נמוכה', 'היי,
פתחתי מועדון חדש בהרצליה בשם "surf fun".
אשמח אם תוסיפו אותו לרשימת המועדונים שלכם באתר.');
INSERT INTO group11.contactus (serial_number, email, phone_number, frequency, text) VALUES (10, 'dorin.ghasri@gmail.com', '0524537586', 'בינונית', 'אתר נפלא ומיוחד!!');