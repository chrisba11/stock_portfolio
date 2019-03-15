from ..models import Company


class TestCompanyModel:
    """

    """
    def test_empty(self, db_session):
        """

        """
        companies = Company.query.all()
        assert len(companies) == 0

    def test_create_company(self, company):
        """

        """
        assert company.id > 0

    def test_company_name(self, company):
        """

        """
        assert company.company_name == 'Fake Company'

    def test_company_symbol(self, company):
        """

        """
        assert company.symbol == 'FAKE'

    def test_company_profile_relationship(self, company):
        """

        """
        assert company.portfolio.portfolio_name == 'Potato'

    
