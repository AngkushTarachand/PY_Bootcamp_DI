
INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Love','Boo','1966-07-05', 2);
INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Grace','Hudgens','2003-01-06', 1);
INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Ludwig','James','10/10/1922', 5),
		('Cameron','Diaz','05/02/1990', 0),
		('Sheen','Shazam','08/10/1970', 2);
		
-- INSERT INTO actors(first_name, last_name, age, number_oscars);
-- VALUES('Marilyn', 'Monrow', '5');
-- 
SELECT * from actors
order by actor_id
-- SELECT * FROM actors LIMIT 4;
-- SELECT * FROM actors ORDER BY last_name DESC LIMIT 4;
-- SELECT * FROM actors WHERE first_name LIKE '%e%';
-- SELECT * FROM actors WHERE number_oscars >= 5;

SELECT
	COUNT (*)
FROM 
	actors;
