CREATE TABLE movies (
    '영화코드' INTEGER PRIMARY KEY,
    '영화이름' TEXT,
    '관람등급' TEXT,
    '감독' TEXT,
    '개봉연도' DATE,
    '누적관객수' INTEGER,
    '상영시간' INTEGER,
    '제작국가' TEXT,
    '장르' TEXT
);
-- import boxoffice csv
.mode csv
.import boxoffice.csv movies

.headers on
.mode column 
-- mode column 으로 다시 변경

SELECT * FROM movies;