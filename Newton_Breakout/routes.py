from Newton_Breakout import db
from flask import request, jsonify, Blueprint
from Newton_Breakout.models.users import User
from Newton_Breakout.models.score import Score
from Newton_Breakout.models.tour_score import TourScore
from Newton_Breakout.utils import *


game = Blueprint("game", __name__, url_prefix="/game")

#signup route to create a new user
@game.route('/signup', strict_slashes=False, methods=['POST'])
def signup():
    try:
        data = request.get_json()
        email = data.get('email')
        name = data.get('name')
        password = data.get('password')

        if email and name:
            existing_user = User.query.filter_by(email=email).first() or User.query.filter_by(name=name).first()

            if existing_user:
                return jsonify({'success': False, 'message': 'Email or name already exist'}), 400
            user = User(email=email, name=name, password=password)
            user.insert()
            return jsonify({'success': True, 'name': name, 'email': email}), 200
        else:
            return jsonify({'success': False, 'message': 'Invalid email or name'}), 400

    except Exception as e:
        print(f'An error occurred: {e}')
        return({'success': False, 'message': 'An error occurred'}), 404

#user signin route
@game.route('/signin', strict_slashes=False, methods=['POST'])
def signin():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if user.password == password:
                return jsonify({'success': True, 'name': user.name, 'email': user.email}), 200
            else:
                return jsonify({'success': False, 'message': 'Incorrect password'}), 400
        else:
            return jsonify({'success': False, 'message': 'Email does not exist'}), 400
    except Exception as e:
        print(f'An error occurred: {e}')
        return({'success': False, 'message': 'An error occurred'}), 404

#guest login route
@game.route('/guest', strict_slashes=False, methods=['POST'])
def guest():
    try:
        data = request.get_json()
        name = data.get('name')
        if name:
            return jsonify({'success': True, 'name': name}), 200
        else:
            return jsonify({'success': False, 'message': 'Enter a valid name'}), 400
    except Exception as e:
        print(f'An error occurred: {e}')
        return({'success': False, 'message': 'An error occurred'}), 404



#scoreboard route that recieves scores via POST req
@game.route('/scoreboard', strict_slashes=False, methods=['POST'])
def save_score():
    try:
        data = request.get_json()
        name = data.get('name')
        score_value = data.get('score')
        user = User.query.filter_by(name=name).first()
        if user:
            score = Score.query.filter_by(user_id=user.id).first()
            if score and score.score < score_value:
                score.score = score_value
                score.update()
                return jsonify({'success': True, 'name': score.user.name, 'user_id': score.user_id, 'score': score.score, 'score_id': score.id, 'message': 'Score updated successfully'}), 201
            elif score and score.score >= score_value:
                return jsonify({'success': True, 'name': score.user.name, 'user_id': score.user_id, 'previous_score': score.score, 'score_id': score.id, 'message': 'Score not updated previous score is higher or equal'}), 200
            else:
                score = Score(user_id=user.id, score=score_value)
                score.insert()
                return jsonify({'success': True, 'name': score.user.name, 'user_id': score.user_id, 'score': score.score, 'score_id': score.id, 'message': 'Score added successfully'}), 201

        else:
            return jsonify({'success': False, 'message': 'user does not exist'}), 400
    
    except Exception as e:
        print(f'An error occurred: {e}')
        return({'success': False, 'message': 'An error occurred'}), 404


# Get Scoreboard which returns first 20 scores
@game.route('/scoreboard', strict_slashes=False, methods=['GET'])
def get_scoreboard():
    try:
        scores = db.session.query(Score).join(User).order_by(Score.score.desc()).limit(20).all()
        scoreboard = [{'name': score.user.name, 'score': score.score, 'score_id': score.id} for score in scores]
        return jsonify(scoreboard), 200
    
    except Exception as e:
        print(f'An error occurred: {e}')
        return({'success': False, 'message': 'An error occurred'}), 404


# Delete score from scoreboard
@game.route('/scoreboard/<score_id>', strict_slashes=False, methods=['DELETE'])
def delete_score(score_id):
    try:
        score = Score.query.filter_by(id=score_id).first()
        if score:
            score.delete()
            return jsonify({'success': True, 'message': 'score deleted successfully'}), 200
        else:
            return({'success': False, 'message': 'score not found'}), 400
    except Exception as e:
        print(f'An error occurred: {e}')
        return({'success': False, 'message': 'An error occurred'}), 404



#tournament scoreboard route that recieve score via POST req
@game.route('/scoreboard/tournament', strict_slashes=False, methods=['POST'])
def save_tournament_score():
    try:
        data = request.get_json()
        name = data.get('name')
        score_value = data.get('score')
        user = User.query.filter_by(name=name).first()
        if user:
            tour_score = TourScore.query.filter_by(user_id=user.id).first()
            if tour_score and tour_score.score < score_value:
                tour_score.score = score_value
                tour_score.update()
                return jsonify({'success': True, 'name': tour_score.user.name, 'user_id': tour_score.user_id, 'score': tour_score.score, 'score_id': tour_score.id, 'message': 'Score updated successfully'}), 201
            elif tour_score and tour_score.score >= score_value:
                return jsonify({'success': True, 'name': tour_score.user.name, 'user_id': tour_score.user_id, 'previous_score': tour_score.score, 'score_id': tour_score.id, 'message': 'Score not updated previous score is higher or equal'}), 200
            else:
                tour_score = TourScore(user_id=user.id, score=score_value)
                tour_score.insert()
                return jsonify({'success': True, 'name': tour_score.user.name, 'user_id': tour_score.user_id, 'score': tour_score.score, 'score_id': tour_score.id, 'message': 'Score added successfully'}), 201

        else:
            return jsonify({'success': False, 'message': 'user does not exist'}), 400
    
    except Exception as e:
        print(f'An error occurred: {e}')
        return({'success': False, 'message': 'An error occurred'}), 400


#route that returns first 20 score for tournament
@game.route('/scoreboard/tournament', strict_slashes=False, methods=['GET'])
def get_tournament_scoreboard():
    try:
        scores = db.session.query(TourScore).join(User).order_by(TourScore.score.desc()).limit(20).all()
        scoreboard = [{'name': score.user.name, 'score': score.score, 'score_id': score.id} for score in scores]
        return jsonify(scoreboard), 200
    
    except Exception as e:
        print(f'An error occurred: {e}')
        return({'success': False, 'message': 'An error occurred'}), 404


# Delete score from scoreboard
@game.route('/scoreboard/tournament/<score_id>', strict_slashes=False, methods=['DELETE'])
def delete_tournament_score(score_id):
    try:
        score = TourScore.query.filter_by(id=score_id).first()
        if score:
            score.delete()
            return jsonify({'success': True, 'message': 'score deleted successfully'}), 200
        else:
            return({'success': False, 'message': 'score not found'}), 400
    except Exception as e:
        print(f'An error occurred: {e}')
        return({'success': False, 'message': 'An error occurred'}), 404


