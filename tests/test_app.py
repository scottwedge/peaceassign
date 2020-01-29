import json
import unittest
from run import app

class TestMyApp(unittest.TestCase):
    """Tests"""

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.data = {
            "id": 1,
            "first_name": "James",
            "last_name": "Butt",
            "company_name": "Benton, John B Jr",
            "city": "New Orleans",
            "state": "LA",
            "zip": 70116,
            "email": "jbutt@gmail.com",
            "web": "http://www.bentonjohnbjr.com",
            "age": 70
        }
     

    def test_posting_a_user(self):
        resp = self.client.post(path='/api/users', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(resp.status_code, 201)

    def test_getting_all_users(self):
        resp = self.client.get(path='/api/users', content_type='application/json')
        self.assertEqual(resp.status_code, 200)

    def test_getting_a_usere(self):
        post = self.client.post(path='/api/users', data=json.dumps(self.data), content_type='application/json')
        int_id = int(post.json['id'])
        path = '/api/users/{}'.format(int_id)
        response = self.client.get(path, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_deleting_a_blog(self):
        post = self.client.post(path='/blog', data=json.dumps(self.data), content_type='application/json')
        int_id = int(post.json['blog_id'])
        path = '/api/users/{}'.format(int_id)
        response = self.client.delete(path, content_type='application/json')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
