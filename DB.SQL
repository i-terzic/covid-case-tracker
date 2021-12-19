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
    type CHAR(64),
    result CHAR(64),
    date date
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
    type,
    result,
    date
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
/*
    Stored Procedures
*/
-- Create a new person, test and case entry
CREATE PROCEDURE terzic_create_case
    @first_name char(64),
    @last_name char(64),
    @birth_date date,
    @address char(64),

    @test_type char(64),
    @test_result char(64),
    @test_date date,

    @q_start_date date,
    @q_end_date date,
    @q_status char(64)
AS
BEGIN
    DECLARE @per_id int;
    DECLARE @test_id int;

    SELECT TOP 1 @per_id = id
    FROM terzic_person
    WHERE last_name = @last_name
    AND first_name = @first_name
    AND birth_date = @birth_date;

    IF @per_id IS NULL 
    BEGIN
        INSERT INTO terzic_person(first_name, last_name, birth_date, address)
        VALUES(@first_name, @last_name, @birth_date, @address);

        SELECT TOP 1 @per_id = id
        FROM terzic_person
        WHERE last_name = @last_name
        AND first_name = @first_name
        AND birth_date = @birth_date;

        INSERT INTO terzic_test(person_id, type, result, date)
        VALUES (@per_id, @test_type, @test_result, @test_date);

        SELECT TOP 1 @test_id = id  
        FROM terzic_test
        WHERE person_id = @per_id
        AND type = @test_type
        AND result = @test_result
        AND date = @test_date
        ORDER BY id desc;

        INSERT INTO terzic_case(person_id, test_id, start_date, end_date, status)
        VALUES (@per_id, @test_id, @q_start_date, @q_end_date, @q_status);
    END
    ELSE 
    	BEGIN
    	    INSERT INTO terzic_test(person_id, type, result, date)
            VALUES (@per_id, @test_type, @test_result, @test_date);

	        SELECT TOP 1 @test_id = id  
            FROM terzic_test
            WHERE person_id = @per_id
            AND type = @test_type
            AND result = @test_result
            AND date = @test_date
            ORDER BY id desc;

            INSERT INTO terzic_case(person_id, test_id, start_date, end_date, status)
            VALUES (@per_id, @test_id, @q_start_date, @q_end_date, @q_status);
    	END
END