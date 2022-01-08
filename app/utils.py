"""Utility file"""


class FormHandler():
    """Utility class to create SQL querys"""
    @staticmethod
    def create_new_case_query(data: dict):
        """set parameters of new case"""
        first_name = FormHandler.quote(str(data.get('first-name')))
        last_name = FormHandler.quote(str(data.get('last-name')))
        birth_date = FormHandler.create_date(str(data.get('birth-date')))
        address = FormHandler.quote(str(data.get('address')))

        test_type = FormHandler.quote('Covid-19')
        test_result = FormHandler.quote(str(data.get('test-result')))
        test_date = FormHandler.create_date(str(data.get('test-date')))
        q_start_date = FormHandler.create_date(
            str(data.get('quarantine-start-date')))if test_result != '\'negativ\'' else 'NULL'
        q_end_date = FormHandler.create_date(
            str(data.get('quarantine-end-date'))) if test_result != '\'negativ\'' else 'NULL'
        q_status = FormHandler.quote(
            'closed') if q_start_date == 'NULL' else FormHandler.quote('open')
        _sql = f"""EXEC terzic_create_case
                @first_name={first_name},
                @last_name={last_name},
                @birth_date={birth_date},
                @address={address},

                @test_type={test_type},
                @test_result={test_result},
                @test_date={test_date},
            
                @q_start_date={q_start_date},
                @q_end_date={q_end_date},
                @q_status={q_status};
                """
        return _sql

    @staticmethod
    def create_date(date: str) -> str:
        """Convert date to right format and surround with quotes"""
        date_tmp = FormHandler.convert_date(date)
        return FormHandler.quote(date_tmp)

    @staticmethod
    def convert_date(date: str) -> str:
        """Convert date in yyyy-mm-dd format to db conform format"""
        return '/'.join([date[0:4], date[5:7], date[8:]])

    @staticmethod
    def quote(statement: str) -> str:
        """surround the input with quotes for sql statement creation"""
        return str('\''+statement+'\'')
