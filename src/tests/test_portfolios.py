class TestPortfolioModel:
    """

    """
    def test_create_portfolio(self, portfolio):
        """

        """
        assert portfolio.id > 0

    def test_portfolio_name(self, portfolio):
        """

        """
        assert portfolio.portfolio_name is not None

    def test_portfolio_user_id(self, portfolio):
        """

        """
        assert portfolio.user_id > 0
