import json
import requests
import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import Movie, Actor, setup_db, db
from auth import AuthError, requires_auth


def create_app(test_config=None):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('config')
    setup_db(app)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    def paginate(request, input_list, limit_per_page=10):
        page = request.args.get('page', 1, type=int)
        start = (page - 1) * limit_per_page
        end = start + limit_per_page

        listed_content = [i.format() for i in input_list]
        paginated_content = listed_content[start:end]
        return paginated_content

    @app.after_request
    def add_cors_headers(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, PUT, POST, PATCH, DELETE, OPTIONS')
        return response

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(payload):
        input_list = list(Actor.query.order_by(Actor.id).all())
        paginated_content = paginate(request, input_list)

        return jsonify({
            'success': True,
            'actors': paginated_content,
            'total_actors': len(input_list)
        })

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(payload):
        input_list = list(Movie.query.order_by(Movie.id).all())
        paginated_content = paginate(request, input_list)

        return jsonify({
            'success': True,
            'movies': paginated_content,
            'total_movies': len(input_list)
        })

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def add_actor(payload):
        error = False
        body = {}
        try:
            actor = Actor(
                name=request.json.get('name'),
                age=request.json.get('age'),
                gender=request.json.get('gender')
            )
            actor.insert()
            return jsonify({
                'success': True,
                'created': actor.id,
                'name': actor.name
            })
        except():
            db.session.rollback()
            error = True
            print(sys.exc_info())
        finally:
            db.session.close()
        if error:
            abort(500)

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def add_movie(payload):
        error = False
        body = {}
        try:
            movie = Movie(
                title=request.json.get('title'),
                release_date=request.json.get('release_date')
            )
            movie.insert()
            return jsonify({
                'success': True,
                'created': movie.id,
                'title': movie.title
            })
        except():
            db.session.rollback()
            error = True
            print(sys.exc_info())
        finally:
            db.session.close()
        if error:
            abort(500)

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def edit_actor(payload, actor_id):
        try:
            actor = Actor.query.filter(Actor.id ==
                                       actor_id).first_or_404()
            body = request.get_json()

            actor.name = body.get('name', None)
            actor.age = body.get('age', None)
            actor.gender = body.get('gender', None)

            actor.update()

            input_list = list(Actor.query.order_by(Actor.id).all())
            paginated_content = paginate(request, input_list)

            return jsonify({
                'success': True,
                'editied_actor_id': actor.id,
                'actors': paginated_content,
                'total_actors': len(input_list)
            })
        except Exception:
            abort(422)

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def edit_movie(payload, movie_id):
        try:
            movie = Movie.query.filter(Movie.id ==
                                       movie_id).first_or_404()
            body = request.get_json()
            movie.title = body.get('title', None)
            movie.release_date = body.get('release_date', None)

            movie.update()

            input_list = list(Movie.query.order_by(Movie.id).all())
            paginated_content = paginate(request, input_list)

            return jsonify({
                'success': True,
                'edited_movie_id': movie.id,
                'movies': paginated_content,
                'total_movies': len(input_list)
            })
        except Exception:
            abort(422)

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(payload, actor_id):
        try:
            actor = Actor.query.filter(Actor.id ==
                                       actor_id).first_or_404()
            actor.delete()

            input_list = list(Actor.query.order_by(Actor.id).all())
            paginated_content = paginate(request, input_list)

            return jsonify({
                'success': True,
                'deleted_actor_id': actor.id,
                'actors': paginated_content,
                'total_actors': len(input_list)
            })
        except Exception:
            abort(422)

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(payload, movie_id):
        try:

            movie = Movie.query.filter(Movie.id ==
                                       movie_id).first_or_404()
            movie.delete()

            input_list = list(Movie.query.order_by(Movie.id).all())
            paginated_content = paginate(request, input_list)

            return jsonify({
                'success': True,
                'deleted_movie_id': movie.id,
                'movies': paginated_content,
                'total_movies': len(input_list)
            })
        except Exception:
            abort(422)

    @app.route('/')
    def index():
        return jsonify({
            'success': True,
            'message': 'Hello World'
        })

    # ----------------------------------------------
    # Error Handling
    # ----------------------------------------------
    @app.errorhandler(400)
    def bad_request_error(error):
        print('debug')
        print(error)
        return jsonify({
            'success': False,
            'error': 400,
            'message': "Bad Request"
        }), 400

    @app.errorhandler(401)
    def unauthorized_error(error):
        return jsonify({
            'success': False,
            'error': 401,
            'message': "Unauthorized"
        }), 401

    @app.errorhandler(403)
    def forbidden_error(error):
        return jsonify({
            'success': False,
            'error': 403,
            'message': "Forbidden"
        }), 403

    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': "Ressource Not Found"
        }), 404

    @app.errorhandler(405)
    def invalid_method_error(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': "Invalid Method"
        }), 405

    @app.errorhandler(409)
    def duplicate_resource_error(error):
        return jsonify({
            'success': False,
            'error': 409,
            'message': "Duplicate Resource"
        }), 409

    @app.errorhandler(422)
    def not_processable_error(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': "Not Processable"
        }), 422

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': "Server Error"
        }), 500

    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        """
        Unauth error handler to avoid 500 error when authorization missing
        """
        response = jsonify(ex.error)
        response.status_code = ex.status_code
        return response

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
