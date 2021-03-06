# Full Stack Nano Degree Final Project Capstone
-----------------------------------------------

## Objective
------------
Building a backend for a Casting Agency, deloying it to Heroku

## App Link Heroku
------------------
https://myappcapstone.herokuapp.com

## Specifications
-----------------
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

Models:
Movies with attributes title and release date
Actors with attributes name, age and gender

Endpoints:
GET /actors and /movies
DELETE /actors/ and /movies/
POST /actors and /movies and
PATCH /actors/ and /movies/

Roles:
Casting Assistant
Can view actors and movies
Casting Director
All permissions a Casting Assistant has and…
Add or delete an actor from the database
Modify actors or movies
Executive Producer
All permissions a Casting Director has and…
Add or delete a movie from the database

Tests:
One test for success behavior of each endpoint
One test for error behavior of each endpoint
At least two tests of RBAC for each role


## File Structure
-----------------
-   .gitignore
-   app.py
-   auth.py
-   config.py
-   manage.py
-   models.py
-   moviedb.psql
-   Procfile
-   README.md
-   requirements.txt
-   setup.sh

    migrations
-   -   alembic.ini
-   -   env.py
-   -   README
-   -   script.py.mako

        versions
-   -   -   3195e62146f5_.py

    Test
-   -  CapstoneMovieLocal.postman_collection.json
-   -  CapstoneMovieLocal.postman_test_run.json
-   -  JWTs.txt
-   -  test_app.py

## Installing Dependencies
--------------------------

### Virtual Enviornment

We recommend working within a virtual environment. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the project directory and running:

```bash
pip install -r requirements.txt
```

### Local Postgres Database
```bash
psql create db movie
```
Load data:
```bash
psql movie < moviedb.psql
```
(alternatively: $ pg_restore -d <yourDBname> movie.psql )

For creating a test database repeat the steps for a database 'movie_test'.

### Setting database path
Set your local database URI in the files 'setup', 'config', 'models' and 'Test/test_app'.
Toggle the line with the URI for the external database. Untoggle the line with the variable 'database_path'.
Put in your URI details for 'database_name', 'user_name', 'user_password' and 'host'.

## Running the server
---------------------

To run the server, execute:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Check browser on given localhost port, page:
{
  "message": "Hello World", 
  "success": true
}

Endpoints require Auth0 identification:
Casting Assistant, Casting Director and Executive Producer.
App, Roles and Users can be set up in Auth0.

### Setup Auth0

1. Create a new Auth0 Account
2. Select a unique tenant domain
3. Create a new, single page web application
4. Create a new API
    - in API Settings:
        - Enable RBAC
        - Enable Add Permissions in the Access Token
5. Create new API permissions:
    - `get:actors`
    - `post:actors`
    - `delete:actors`
    - `patch:actors`
    - `get:movies`
    - `post:movies`
    - `delete:movies`
    - `patch:movies`
6. Create new roles for:
    - Casting Assistant
	Can view actors and movies
    - Casting Director
	All permissions a Casting Assistant has and…
	Add or delete an actor from the database
	Modify actors or movies
    - Executive Producer
	All permissions a Casting Director has and…
	Add or delete a movie from the database
7. Link users, roles and permessions
8. Set your Auth0 details in the 'auth.py' (AUTH0_DOMAIN, API_AUDIENCE)


## Running the tests
--------------------
Copy the file 'Test/test_app.py' into the main folder and run it from there.

Edit the Auth0 JWTs in the file 'setup.sh' (or 'test_app.py' directly).

## 8 Endpoints are defined
--------------------------
1. A list of all actors, paginated with a limit of 10 actors per page

@app.route('/actors', methods=['GET'])
returns: {
            'success': True,
            'actors': paginated_content,
            'total_actors': len(input_list)
        }

2. A list of all movies, paginated with a limit of 10 movies per page

@app.route('/movies', methods=['GET'])
returns: {
            'success': True,
            'movies': paginated_content,
            'total_movies': len(input_list)
        }

3. A post endpoint for adding actors to the database, with attributes 'name', 'age' and 'gender'

@app.route('/actors', methods=['POST'])
returns: {
            'success': True,
            'created': actor.id,
            'name': actor.name
        }

4. A post endpoint for adding movies to the database, with attributes 'title' and 'release_date'

@app.route('/movies', methods=['POST'])
returns: {
            'success': True,
            'created': movie.id,
            'name': movie.name
        }

5. Patch endpoint for patching actors 'name', 'age' or 'gender'

@app.route('/actors/<int:actor_id>', methods=['PATCH'])
returns: {
                'success': True,
                'editied_actor_id': actor.id,
                'actors': paginated_content,
                'total_actors': len(input_list)
            }

6. Patch endpoint for patching movies 'title' or 'release_date'

@app.route('/movies/<int:movie_id>', methods=['PATCH'])
returns: {
                'success': True,
                'edited_movie_id': movie.id,
                'movies': paginated_content,
                'total_movies': len(input_list)
            }

7. Delete endpoint for actors

@app.route('/actors/<int:actor_id>', methods=['DELETE'])
returns: {
                'success': True,
                'deleted_actor_id': actor.id,
                'actors': paginated_content,
                'total_actors': len(input_list)
            }

8. Delete endpoint for movies

@app.route('/movies/<int:movie_id>', methods=['DELETE'])
returns: {
                'success': True,
                'deleted_movie_id': movie.id,
                'movies': paginated_content,
                'total_movies': len(input_list)
            }


## Tests provided in the test_app.py:
- test_get_actors
- test_get_actor_missing_auth
- test_get_movies
- test_get_movie_missing_auth
- test_add_new_actor
- test_add_new_movie
- test_delete_actor
- test_delete_actor_notExistingID
- test_delete_movie
- test_delete_movie_wrong_auth
- test_delete_movie_notExistingID
- test_patch_actor
- test_patch_actor_notExistingID
- test_patch_movie
- test_patch_movie_notExistingID
