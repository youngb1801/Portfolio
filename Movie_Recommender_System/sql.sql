CREATE TABLE movies (
	movieid int4,
	title varchar(1500),
	genres varchar(1500),
	PRIMARY KEY (movieid)
);

CREATE TABLE links (
	movieid int4,
	imdbid int4,
	tmdbid int4,
	PRIMARY KEY (movieid)
);

CREATE TABLE ratings (
	id serial,
	userid int4,
	movieid int4,
	rating float4,
	timestamp int4,
	PRIMARY KEY (id)
);

CREATE TABLE tags (
	id serial,
	userid int4,
	movieid int4,
	tag varchar(1500),
	timestamp int4,
	PRIMARY KEY (id)
);

COPY movies (
	movieid,
	title,
	genres)
FROM '/Users/bretyoung/Documents/GitHub/DSC_680/Project 1/data/movies.csv'
DELIMITER ','
CSV HEADER;

COPY links (
	movieid,
	imdbid,
	tmdbid)
FROM '/Users/bretyoung/Documents/GitHub/DSC_680/Project 1/data/links.csv'
DELIMITER ','
CSV HEADER;

COPY ratings (
	userid,
	movieid,
	rating,
	timestamp)
FROM '/Users/bretyoung/Documents/GitHub/DSC_680/Project 1/data/ratings.csv'
DELIMITER ','
CSV HEADER;

COPY tags (
	userid,
	movieid,
	tag,
	timestamp)
FROM '/Users/bretyoung/Documents/GitHub/DSC_680/Project 1/data/tags.csv'
DELIMITER ','
CSV HEADER;