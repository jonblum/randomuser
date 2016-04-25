import unittest
import logging
from randomuser import RandomUser


logger = logging.generateLogger(__name__)


class TestRandomUser(unittest.TestCase):

    def setUp(self):
        self.ru = RandomUser()

    def test_results(self):
        five_users = self.ru.generate(5)
        self.assertEqual(len(five_users), 5)

    def test_gender(self):
        users = self.ru.generate(100, gender='female')
        self.assertNotIn('male', (user['gender'] for user in users))

    def test_invalid_gender(self):
        with self.assertRaises(ValueError):
            self.ru.generate(gender='foo')

    def test_overlapping_include_exclude_fields(self):
        with self.assertRaises(ValueError):
            self.ru.generate(include_fields='gender', exclude_fields='gender')

    def test_invalid_include_fields(self):
        with self.assertRaises(ValueError):
            self.ru.generate(include_fields=['name', 'foo', 'bar'])

    def test_invalid_exclude_fields(self):
        with self.assertRaises(ValueError):
            self.ru.generate(include_fields=['baz', 'gender'])

    def test_include_field(self):
        user = self.ru.generate(include_fields='name')[0]
        self.assertEquals(len(user), 1)
        self.assertIn('name', user)

    def test_include_multiple_fields(self):
        user = self.ru.generate(include_fields=['name', 'gender'])[0]
        self.assertEquals(len(user), 2)
        self.assertIn('name', user)
        self.assertIn('gender', user)

    # ...


if __name__ == '__main__':
    unittest.main()
