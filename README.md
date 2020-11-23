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

----migrations
-   -   alembic.ini
-   -   env.py
-   -   README
-   -   script.py.mako
-   -
-   ----versions
-   -   -   3195e62146f5_.py

----Test
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

Edit the Auth0 JWTs in the file 'test_app.py'.

For today following JWTs apply (for given Auth0 configuration already set in the file):
casting_assistant = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtuaUE2aGR1Z3I1Ulc4bmRoTDhScCJ9.eyJpc3MiOiJodHRwczovL2ZzbmRqdy5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY4OGE0OWRmYjFmNzAwMDc2YWU3ZWMzIiwiYXVkIjoibW92aWUiLCJpYXQiOjE2MDYxMzQ4MjEsImV4cCI6MTYwNjIyMTIyMSwiYXpwIjoiVjFyaVRKWmhsWjRiNFBpQ3FibG5kOFNqTFJEV2lsU3AiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicG9zdDpzZWFyY2hBY3RvcnMiLCJwb3N0OnNlYXJjaE1vdmllcyJdfQ.sJfQ0cPRJtQQrP36fwkafoYpwekjZIEiYiLgT_aGUfWSeAHEB_kEGrZSct42Bimh7Y_nNasmgw0QbB9Ux4p3eOnEgM9bIKfr38yA3IBDvufM0bhVzv_pz6BHy3husfslpZYO_QtyJgGWQtFDpm_65jNzh6dsk7DuJRheeuml5Cj4SMDLB__hpSfof03HlEsgS3VPqXEa8acwSgKsCiCQpTGrrzjjQKoqmR2S8q7V_bvwB8sAyNV3ZMWTnHF7JVgGRt2lHMxmw1x8x4pWYEZ4So99U1OyNIJc1lcfEPfvDIggU0BR8VPXKre_3D5FNc7lDCYLrskXGdAYLiwthVijxw'
casting_director = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtuaUE2aGR1Z3I1Ulc4bmRoTDhScCJ9.eyJpc3MiOiJodHRwczovL2ZzbmRqdy5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZiNTIyODJhYTY3YjIwMDc1OTA5OTc0IiwiYXVkIjoibW92aWUiLCJpYXQiOjE2MDYxMzQ4OTIsImV4cCI6MTYwNjIyMTI5MiwiYXpwIjoiVjFyaVRKWmhsWjRiNFBpQ3FibG5kOFNqTFJEV2lsU3AiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDpzZWFyY2hBY3RvcnMiLCJwb3N0OnNlYXJjaE1vdmllcyJdfQ.zMvXctru3e_FN3L-XyPbzEss_a5faAeu7XwlPuhJJnAtMgEkNN9XoNCrbJa6Jba-2-jTbg4aSMcUhB6vfOLPYp9wnKk2YDFpW-X6AEzN2-RbUfnpIHsjtPjeXeLlDLO17C9yzQgVH9f1nVej9mhgk-jpyytoFvFTdpslm7WBbMXRv2XnVYb4R0tfSzO0xn6fWvyzRYZzAgsmWGnFqTm3UnL3i51K_tIinXC1rsxYSfQ9_o-R-P6gFOgu74iKt8CRlKf5wRA2lhZZx8Xm-_-bRVJU3nJ3Ar8AjAZwYpC2xrLZ91G8t1C0d3DA0kctZvtWvyo6ZAbJESsrC71QJE1FXA'
excecutive_producer = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtuaUE2aGR1Z3I1Ulc4bmRoTDhScCJ9.eyJpc3MiOiJodHRwczovL2ZzbmRqdy5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY4NDNiM2NiZWI2MmIwMDY4ZTI1OGI2IiwiYXVkIjoibW92aWUiLCJpYXQiOjE2MDYxMzQ2OTUsImV4cCI6MTYwNjIyMTA5NSwiYXpwIjoiVjFyaVRKWmhsWjRiNFBpQ3FibG5kOFNqTFJEV2lsU3AiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIiwicG9zdDpzZWFyY2hBY3RvcnMiLCJwb3N0OnNlYXJjaE1vdmllcyJdfQ.LLrh-UGj0DWCJBowOjEfKTcHo1Gx7AEah_XsJUK5Sg6nTHHIYvGJ3YGSt7HQZ5F20AaKMMO66cxwFy-dyZ2OyZ7W7C9cLLcibCVP3OZkZjImzYqlEnyuDZNG_o7xzTHOj7VU8NXaPEy7fF81DzdSdH692znLmgrUIWPdIuBkwuMr3aPhVENMuI0pSWQVI1ivnioey4jTccOGrSQtdkgbDoa6E0TB8HENlPa3HmqLHar04vMfbWLeSN2Qew1-UgkLWIc6J7jRkNo-LUpdcBb7GXhZ3Hn2jZdItYdz9dV3-P0l1zA8PhrQ_PT-D_WsvqxLUb95L1GfaerBQ0JV1gqQyw'

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
