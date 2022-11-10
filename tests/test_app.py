import unittest
import os
os.environ['TESTING'] = "true"

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    # home page testing start

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Portfolio</title>" in html
        # testing to check if two people exist
        assert "<h2>Alexis Gray</h2>" in html
        assert "<h2>Paulin Alcoser</h2>" in html
        # testing to see if routes exist
        assert "<a href=\"/home/AlexisGray\">" in html
        assert "<a href=\"/home/PaulinAlcoser\">" in html

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0

        #post
        post = {
            "name": "thisistest!",
            "email": "thisistest@gmail.com",
            "content": "TEST SENT THIS :)"
        }
        response = self.client.post("/api/timeline_post", data=post)
        assert response.status_code == 200
        postJson = response.get_json()
        self.assertEqual(postJson["name"], post["name"])

        #get
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 1

    
    def test_timeline_page(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<h3>Name: thisistest!</h3>"
        assert "<p>Email: thisistest@gmail.com</p>"
        assert "<p>TEST SENT THIS :)</p>"

    def test_malformed_timeline_post(self):
            # POST request missing name
            response = self.client.post(
                "/api/timeline_post", data={"email": "john@example.com", "content": "Hello world, I'm John!"})
            assert response.status_code == 400
            html = response.get_data(as_text=True)
            assert "Invalid name" in html

            # POST request with empty content
            response = self.client.post(
                "/api/timeline_post", data={"name": "John Doe", "email": "john@example.com", "content": ""})
            assert response.status_code == 400
            html = response.get_data(as_text=True)
            assert "Invalid content" in html

            # POST request with malformed email
            response = self.client.post("/api/timeline_post", data={
                                        "name": "John Doe", "email": "not-an-email", "content": "Hello world, I'm John!"})
            assert response.status_code == 400
            html = response.get_data(as_text=True)
            assert "Invalid email" in html
