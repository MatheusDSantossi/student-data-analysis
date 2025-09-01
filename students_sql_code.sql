-- campus	unidade	curso	estado_origem	cidade_origem	quantidade_estudantes

CREATE TABLE students (
	campus VARCHAR(100),
	unidade VARCHAR(100),
	curso VARCHAR(100),
	estado_origem VARCHAR(20),
	cidade_origem VARCHAR(50),
	quantidade_estudantes BIGINT
)

DROP TABLE students

SELECT * FROM students

SET client_encoding TO 'UTF8';
SHOW client_encoding;

ALTER DATABASE testqueries REFRESH COLLATION VERSION

COPY students
FROM 'C:\\Users\\Admin\\Downloads\\alunos-por-cidade-de-origem.csv'
WITH (FORMAT csv, DELIMITER ',', HEADER true, ENCODING 'WIN1252');

SELECT * FROM students
WHERE LENGTH(estado_origem) > 2	
WHERE cidade_origem ILIKE '%uber%'

show port

-- Cleaned table

SELECT * FROM students_cleaned

DROP TABLE students_cleaned
