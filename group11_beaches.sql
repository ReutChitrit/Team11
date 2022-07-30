create table beaches
(
    beach_name      varchar(100) not null
        primary key,
    city            varchar(100) null,
    surf_store      bit          null,
    with_life_guard bit          null
);

INSERT INTO group11.beaches (beach_name, city, surf_store, with_life_guard) VALUES ('החוף הנפרד', 'אשקלון', true, true);
INSERT INTO group11.beaches (beach_name, city, surf_store, with_life_guard) VALUES ('החוף השקט', 'חיפה', false, true);
INSERT INTO group11.beaches (beach_name, city, surf_store, with_life_guard) VALUES ('חוף 4X4', 'ראשון-לציון', true, true);
INSERT INTO group11.beaches (beach_name, city, surf_store, with_life_guard) VALUES ('חוף אכדיה דרום', 'הרצליה', true, true);
INSERT INTO group11.beaches (beach_name, city, surf_store, with_life_guard) VALUES ('חוף אכדיה צפון', 'הרצליה', false, true);
INSERT INTO group11.beaches (beach_name, city, surf_store, with_life_guard) VALUES ('חוף ארגמן לגון', 'נתניה', true, false);
INSERT INTO group11.beaches (beach_name, city, surf_store, with_life_guard) VALUES ('חוף בוגרשוב', 'תל-אביב', false, true);
INSERT INTO group11.beaches (beach_name, city, surf_store, with_life_guard) VALUES ('חוף בלו ביי', 'נתניה', true, false);
INSERT INTO group11.beaches (beach_name, city, surf_store, with_life_guard) VALUES ('חוף בר כוכבא', 'אשקלון', true, true);
INSERT INTO group11.beaches (beach_name, city, surf_store, with_life_guard) VALUES ('חוף בת גלים', 'חיפה', true, true);
INSERT INTO group11.beaches (beach_name, city, surf_store, with_life_guard) VALUES ('חוף גורדון', 'תל-אביב', true, true);
INSERT INTO group11.beaches (beach_name, city, surf_store, with_life_guard) VALUES ('חוף דגל כחול', 'אילת', true, true);
INSERT INTO group11.beaches (beach_name, city, surf_store, with_life_guard) VALUES ('חוף דלילה', 'אשקלון', false, true);
INSERT INTO group11.beaches (beach_name, city, surf_store, with_life_guard) VALUES ('חוף הגולשים', 'ראשון-לציון', true, true);
INSERT INTO group11.beaches (beach_name, city, surf_store, with_life_guard) VALUES ('חוף הכרמל-מרידיאן', 'חיפה', false, true);
INSERT INTO group11.beaches (beach_name, city, surf_store, with_life_guard) VALUES ('חוף העונות', 'נתניה', false, true);
INSERT INTO group11.beaches (beach_name, city, surf_store, with_life_guard) VALUES ('חוף הצוק הדרומי', 'תל-אביב', false, true);
INSERT INTO group11.beaches (beach_name, city, surf_store, with_life_guard) VALUES ('חוף הצוק הצפוני', 'תל-אביב', false, true);
INSERT INTO group11.beaches (beach_name, city, surf_store, with_life_guard) VALUES ('חוף הקשתות', 'אשדוד', true, true);
INSERT INTO group11.beaches (beach_name, city, surf_store, with_life_guard) VALUES ('חוף הרצל', 'נתניה', false, true);
INSERT INTO group11.beaches (beach_name, city, surf_store, with_life_guard) VALUES ('חוף השרון', 'הרצליה', true, true);
INSERT INTO group11.beaches (beach_name, city, surf_store, with_life_guard) VALUES ('חוף י"א', 'אשדוד', false, true);
INSERT INTO group11.beaches (beach_name, city, surf_store, with_life_guard) VALUES ('חוף כחול', 'ראשון-לציון', false, true);
INSERT INTO group11.beaches (beach_name, city, surf_store, with_life_guard) VALUES ('חוף סידנא-עלי', 'הרצליה', false, true);
INSERT INTO group11.beaches (beach_name, city, surf_store, with_life_guard) VALUES ('חוף סירונית', 'נתניה', true, true);
INSERT INTO group11.beaches (beach_name, city, surf_store, with_life_guard) VALUES ('חוף פולג', 'נתניה', true, true);
INSERT INTO group11.beaches (beach_name, city, surf_store, with_life_guard) VALUES ('חוף פלמחים', 'ראשון-לציון', false, false);
INSERT INTO group11.beaches (beach_name, city, surf_store, with_life_guard) VALUES ('חוף פרישמן', 'תל-אביב', true, true);
INSERT INTO group11.beaches (beach_name, city, surf_store, with_life_guard) VALUES ('חוף צפוני מערבי', 'אילת', false, true);