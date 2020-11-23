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
        self.casting_assistant = os.environ.get('jwt_cast_as')
        self.casting_director = os.environ.get('jwt_cast_dir')
        self.excecutive_producer = os.environ.get('jwt_exec_prod')

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
