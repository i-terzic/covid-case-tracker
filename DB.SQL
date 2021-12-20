-- Drop all tables

DROP TABLE terzic_case;
DROP TABLE terzic_test;
DROP TABLE terzic_person;

-- Create necessary tables

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
    result char(64),
    date date        
);

CREATE TABLE terzic_case(
    id INT IDENTITY(1,1) PRIMARY KEY,
    person_id INT FOREIGN KEY REFERENCES terzic_person(id),
    test_id INT FOREIGN KEY REFERENCES terzic_test(id),
    date date,
    start_date date,
    end_date date,
    status char(64)
);


-- Stored Procedures

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
    DECLARE @today date = CONVERT(date, GETDATE());
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
        
        INSERT INTO terzic_case(person_id, test_id,date, start_date, end_date, status)
        VALUES (@per_id, @test_id, @today, @q_start_date, @q_end_date, @q_status);
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

            INSERT INTO terzic_case(person_id, test_id, date, start_date, end_date, status)
            VALUES (@per_id, @test_id, @today, @q_start_date, @q_end_date, @q_status);
    	END
END;

-- retrieve open/closed cases


-- retrieve open/closed cases
CREATE PROCEDURE terzic_get_cases
    @q_status char(64)
AS
BEGIN
    SELECT  c.id as case_id,
            c.start_date as q_start_date, 
            c.end_date as q_end_date, 
            c.status, 
            c.date as case_date,
            t.type as test_type,
            t.result as test_result,
            t.date as test_date,
            p.last_name,
            p.first_name,
            p.birth_date,
            p.address
    FROM terzic_case c
    INNER JOIN terzic_person p
    ON c.person_id = p.id
    INNER JOIN terzic_test t
    ON c.test_id = t.id
    WHERE status = @q_status;
    RETURN;
END

-- Extend quarantine end date by one week
CREATE PROCEDURE terzic_extend_quarantine
    @case_id int
AS 
BEGIN
	DECLARE @end_date date;
    
    SELECT TOP 1 @end_date = end_date 
    FROM terzic_case
    WHERE id = @case_id
    AND end_date IS NOT NULL;
    
    IF @end_date IS NOT NULL
    BEGIN
      UPDATE terzic_case
      SET end_date = DATEADD(day, 7, @end_date)
      WHERE id = @case_id;
      RETURN;
    END;
END;

CREATE PROCEDURE terzic_extend_quarantine
    @case_id int
AS 
BEGIN
    DECLARE @end_date date;
    SELECT TOP 1 @end_date = end_date 
    FROM terzic_case
    WHERE id = @case_id;
    RETURN;
END

CREATE PROCEDURE terzic_close_case
    @case_id int
AS
BEGIN
    UPDATE terzic_case
    SET q_status = 'closed'
    WHERE id = @case_id;
    RETURN;
END