import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actor, Movie


class MovieTestCase(unittest.TestCase):
    """This class represents the movie test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "movie_test"
        self.database_path = "postgres://{}:{}@{}/{}".format('postgres', 'w1zu', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        self.casting_assistant = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtuaUE2aGR1Z3I1Ulc4bmRoTDhScCJ9.eyJpc3MiOiJodHRwczovL2ZzbmRqdy5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY4OGE0OWRmYjFmNzAwMDc2YWU3ZWMzIiwiYXVkIjoibW92aWUiLCJpYXQiOjE2MDYxMzQ4MjEsImV4cCI6MTYwNjIyMTIyMSwiYXpwIjoiVjFyaVRKWmhsWjRiNFBpQ3FibG5kOFNqTFJEV2lsU3AiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicG9zdDpzZWFyY2hBY3RvcnMiLCJwb3N0OnNlYXJjaE1vdmllcyJdfQ.sJfQ0cPRJtQQrP36fwkafoYpwekjZIEiYiLgT_aGUfWSeAHEB_kEGrZSct42Bimh7Y_nNasmgw0QbB9Ux4p3eOnEgM9bIKfr38yA3IBDvufM0bhVzv_pz6BHy3husfslpZYO_QtyJgGWQtFDpm_65jNzh6dsk7DuJRheeuml5Cj4SMDLB__hpSfof03HlEsgS3VPqXEa8acwSgKsCiCQpTGrrzjjQKoqmR2S8q7V_bvwB8sAyNV3ZMWTnHF7JVgGRt2lHMxmw1x8x4pWYEZ4So99U1OyNIJc1lcfEPfvDIggU0BR8VPXKre_3D5FNc7lDCYLrskXGdAYLiwthVijxw'
        self.casting_director = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtuaUE2aGR1Z3I1Ulc4bmRoTDhScCJ9.eyJpc3MiOiJodHRwczovL2ZzbmRqdy5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZiNTIyODJhYTY3YjIwMDc1OTA5OTc0IiwiYXVkIjoibW92aWUiLCJpYXQiOjE2MDYxMzQ4OTIsImV4cCI6MTYwNjIyMTI5MiwiYXpwIjoiVjFyaVRKWmhsWjRiNFBpQ3FibG5kOFNqTFJEV2lsU3AiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDpzZWFyY2hBY3RvcnMiLCJwb3N0OnNlYXJjaE1vdmllcyJdfQ.zMvXctru3e_FN3L-XyPbzEss_a5faAeu7XwlPuhJJnAtMgEkNN9XoNCrbJa6Jba-2-jTbg4aSMcUhB6vfOLPYp9wnKk2YDFpW-X6AEzN2-RbUfnpIHsjtPjeXeLlDLO17C9yzQgVH9f1nVej9mhgk-jpyytoFvFTdpslm7WBbMXRv2XnVYb4R0tfSzO0xn6fWvyzRYZzAgsmWGnFqTm3UnL3i51K_tIinXC1rsxYSfQ9_o-R-P6gFOgu74iKt8CRlKf5wRA2lhZZx8Xm-_-bRVJU3nJ3Ar8AjAZwYpC2xrLZ91G8t1C0d3DA0kctZvtWvyo6ZAbJESsrC71QJE1FXA'
        self.excecutive_producer = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtuaUE2aGR1Z3I1Ulc4bmRoTDhScCJ9.eyJpc3MiOiJodHRwczovL2ZzbmRqdy5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY4NDNiM2NiZWI2MmIwMDY4ZTI1OGI2IiwiYXVkIjoibW92aWUiLCJpYXQiOjE2MDYxMzQ2OTUsImV4cCI6MTYwNjIyMTA5NSwiYXpwIjoiVjFyaVRKWmhsWjRiNFBpQ3FibG5kOFNqTFJEV2lsU3AiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIiwicG9zdDpzZWFyY2hBY3RvcnMiLCJwb3N0OnNlYXJjaE1vdmllcyJdfQ.LLrh-UGj0DWCJBowOjEfKTcHo1Gx7AEah_XsJUK5Sg6nTHHIYvGJ3YGSt7HQZ5F20AaKMMO66cxwFy-dyZ2OyZ7W7C9cLLcibCVP3OZkZjImzYqlEnyuDZNG_o7xzTHOj7VU8NXaPEy7fF81DzdSdH692znLmgrUIWPdIuBkwuMr3aPhVENMuI0pSWQVI1ivnioey4jTccOGrSQtdkgbDoa6E0TB8HENlPa3HmqLHar04vMfbWLeSN2Qew1-UgkLWIc6J7jRkNo-LUpdcBb7GXhZ3Hn2jZdItYdz9dV3-P0l1zA8PhrQ_PT-D_WsvqxLUb95L1GfaerBQ0JV1gqQyw'

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    
    def test_get_actors(self):
        # Getting response by making the client request
        res = self.client().get('/actors', headers = {'Authorization': 'Bearer ' + self.casting_director})
        data = json.loads(res.data)
        # to check the status code
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
    
    # Test if 401 is sent missing auth
    def test_get_actor_missing_auth(self):
        res = self.client().post('/actors', headers = {})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_get_movies(self):
        # Getting response by making the client request
        res = self.client().get('/movies', headers = {'Authorization': 'Bearer ' + self.casting_assistant})
        data = json.loads(res.data)
        # to check the status code
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
    
    # Test if 401 is sent missing auth
    def test_get_movie_missing_auth(self):
        res = self.client().post('/movies', headers = {})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    # Test if new actor can be added
    def test_add_new_actor(self):
        res = self.client().post('/actors', headers = {'Authorization': 'Bearer ' + self.casting_director}, json = {'name': 'Lucky Luke', 'age': '50', 'gender': 'male'})
        data = json.loads(res.data)
        actor = Actor.query.filter_by(name='Lucky Luke').first()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(actor.format()['age'], 50)

    # Test if new movie can be added
    def test_add_new_movie(self):
        res = self.client().post('/movies', headers = {'Authorization': 'Bearer ' + self.excecutive_producer}, json = {'title': 'Braveheart', 'release_date': '1995'})
        data = json.loads(res.data)
        movie = Movie.query.filter_by(title='Braveheart').first()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(movie.format()['release_date'], '1995')
    
    # Test if new movie can be added by casting assistant (error)
    def test_add_new_movie_wrong_role(self):
        res = self.client().post('/movies', headers = {'Authorization': 'Bearer ' + self.casting_assistant}, json = {'title': 'The Perfect Storm', 'release_date': '2000'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
    
    # Test on successful deletion
    def test_delete_actor(self):
        res = self.client().delete('/actors/1', headers = {'Authorization': 'Bearer ' + self.excecutive_producer})
        data = json.loads(res.data)

        actor = Actor.query.filter(Actor.id == 1).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(actor, None)

    # Test on failing deletion, not existing id
    def test_delete_actor_notExistingID(self):
        res = self.client().delete('/actors/1000', headers = {'Authorization': 'Bearer ' + self.excecutive_producer})
        data = json.loads(res.data)

        actor = Actor.query.filter(Actor.id == 1000).one_or_none()

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(actor, None)
    
    # Test on successful deletion
    def test_delete_movie(self):
        res = self.client().delete('/movies/1', headers = {'Authorization': 'Bearer ' + self.excecutive_producer})
        data = json.loads(res.data)

        movie = Movie.query.filter(Movie.id == 1).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(movie, None)
    
    # Test failing deletion, missing auth
    def test_delete_movie_wrong_auth(self):
        res = self.client().delete('/movies/1', headers = {'Authorization': 'Bearer ' + self.casting_director})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    # Test on failing deletion, not existing id
    def test_delete_movie_notExistingID(self):
        res = self.client().delete('/movies/1000', headers = {'Authorization': 'Bearer ' + self.excecutive_producer})
        data = json.loads(res.data)

        movie = Movie.query.filter(Movie.id == 1000).one_or_none()

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(movie, None)

    # Test on successful patch actor
    def test_patch_actor(self):
        res = self.client().patch('/actors/2', headers = {'Authorization': 'Bearer ' + self.excecutive_producer}, json = {'name': 'Charlize Theron', 'age': '34', 'gender': 'female'})
        data = json.loads(res.data)

        actor = Actor.query.filter(Actor.id == 2).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(actor.age, 34)

    # Test on failing patch actor
    def test_patch_actor_notExistingID(self):
        res = self.client().patch('/actors/2000', headers = {'Authorization': 'Bearer ' + self.excecutive_producer})
        data = json.loads(res.data)

        actor = Actor.query.filter(Actor.id == 2000).one_or_none()

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(actor, None)

    # Test on successful patch movie
    def test_patch_movie(self):
        res = self.client().patch('/movies/2', headers = {'Authorization': 'Bearer ' + self.excecutive_producer}, json = {'title': 'Hancock', 'release_date': '2010'})
        data = json.loads(res.data)

        movie = Movie.query.filter(Movie.id == 2).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(movie.release_date, '2010')

    # Test on failing patch movie
    def test_patch_movie_notExistingID(self):
        res = self.client().patch('/movies/2000', headers = {'Authorization': 'Bearer ' + self.excecutive_producer})
        data = json.loads(res.data)

        movie = Movie.query.filter(Movie.id == 2000).one_or_none()

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(movie, None)

if __name__ == "__main__":
    unittest.main()