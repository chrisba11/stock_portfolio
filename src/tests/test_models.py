class TestCompanyModel():
    """

    """

    def test_create_company(self, company):
        """

        """
        assert company.id > 0

    def test_company_name(self, company):
        """

        """
        assert company.name == 'Fake Company'

    def test_company_symbol(self, comapny):
        """

        """
        assert company.symbol == 'FAKE'
