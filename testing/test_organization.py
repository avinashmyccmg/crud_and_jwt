import unittest
from unittest.mock import Mock
from sqlalchemy.orm import Session
from models.model import Organization
from repository.organization import OrganizationRepository
from schemas import schema


class TestOrganizationRepository(unittest.TestCase):

  def test_get_all(self) -> None:
    mock_db_session = Mock(spec=Session)
    mock_org_1 = Organization(id=1, name="Collance", user_id=1)
    mock_org_2 = Organization(id=2, name="TCS", user_id=2)
    mock_db_session.query.return_value.all.return_value = [mock_org_1, mock_org_2]
    result = OrganizationRepository.get_all(mock_db_session)
    self.assertEqual(len(result), 2)
    self.assertIn(mock_org_1, result)
    self.assertIn(mock_org_2, result)

  def test_create(self) -> None:
    mock_db_session = Mock(spec=Session)
    request = schema.Organization(name="Collance")
    mock_db_session.add = Mock()
    result = OrganizationRepository.create(request, mock_db_session)
    self.assertEqual(result.name, "Collance")
    self.assertEqual(result.user_id, 1)
    mock_db_session.add.assert_called_once_with(result)
    mock_db_session.commit.assert_called_once()


if __name__ == '__main__':
    unittest.main()

