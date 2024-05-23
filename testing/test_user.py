import unittest
from unittest.mock import Mock
from sqlalchemy.orm import Session
from models.model import User
from repository.user import UserRepository
from schemas import schema


class TestUserRepository(unittest.TestCase):

  def test_create(self) -> None:

    mock_db_session = Mock(spec=Session)

    request = schema.User(name="Avinash", email="akraushan@gmail.com", password="password")
    mock_db_session.add = Mock()
    result = UserRepository.create(request, mock_db_session)

    self.assertEqual(result.name, "Avinash")
    self.assertEqual(result.email, "akraushan@gmail.com")
    mock_db_session.add.assert_called_once()

  def test_get_all(self) -> None:

    mock_db_session = Mock(spec=Session)

    mock_user = User(id=1, name="Avinash", email="akraushan@gmail.com", password="password")
    mock_db_session.query.return_value.all.return_value = [mock_user]
    result = UserRepository.get_all(mock_db_session)

    self.assertEqual(len(result), 1)
    self.assertIn(mock_user, result)


if __name__ == '__main__':
    unittest.main()

