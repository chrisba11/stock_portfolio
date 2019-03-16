from ..models import User


class TestUserModel:
    """

    """
    def test_user_create(self, user):
        """

        """
        assert user.id > 0

    def test_user_email(self, user):
        """

        """
        assert user.email == 'test@testing.com'

    def test_user_password(self, user):
        """

        """
        assert User.check_password_hash(user, 'secret')
