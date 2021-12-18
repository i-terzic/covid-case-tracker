/*
    Drop all tables
*/

DROP TABLE terzic_case;
DROP TABLE terzic_test;
DROP TABLE terzic_person;
/*
    Create necessary tables
*/
CREATE TABLE terzic_person (
    id INT IDENTITY(1,1) PRIMARY KEY,
    first_name CHAR(64),
    last_name CHAR(64),
    birth_date date,
    address CHAR(64)
);

CREATE TABLE terzic_test(
    id INT IDENTITY(1,1) PRIMARY KEY,
    person_id INT FOREIGN KEY REFERENCES terzic_person(id),
    art CHAR(64),
    result CHAR(64),
    datum date
);

CREATE TABLE terzic_case(
    id INT IDENTITY(1,1) PRIMARY KEY,
    person_id INT FOREIGN KEY REFERENCES terzic_person(id),
    test_id INT FOREIGN KEY REFERENCES terzic_test(id),
    start_date date,
    end_date date,
    status char(64)
);

/*
    Create dummy data
*/


INSERT INTO terzic_person(
	first_name,
  	last_name,
  	birth_date,
 	address
) VALUES (
    'Dummy',
    'LastName',
    '01/01/1965',
    'Dummstreet 1'
);


INSERT INTO terzic_test(
    person_id,
    art,
    result,
    datum
) VALUES (
    1,
    'Covid-19',
    'negativ',
    '12/18/2021'
);

INSERT INTO terzic_case( 
    person_id,
    test_id,
    start_date,
    end_date,
    status 
) VALUES(
    1,
    1,
    NULL,
    NULL,
    'closed'
);