import unittest

import unh698


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.app = unh698.app.test_client()

    def tearDown(self):
        pass

    def test_home_page(self):
        # Render the / path of the website
        rv = self.app.get('/')
        # Chech that the page contians the desired phrase
        assert b'UNH698 Website' in rv.data

    def test_first_page(self):
        # Render the / path of the website
        rv = self.app.get('/firstPage')
        # Chech that the page contians the desired phrase
        assert b'This is my first page' in rv.data

    def test_cool_page(self):
        # Render the / path of the website
        rv = self.app.get('/myCoolTopic')
        # Chech that the page contians the desired phrase
        assert b'site Build' in rv.data


if __name__ == '__main__':
    unittest.main()
