from flask import Blueprint, request, jsonify
from pine_sap.helper import token_required
from pine_sap.models import db, artist_schema, artists_schema, Artist

api = Blueprint('api',__name__, url_prefix = '/api')

@api.route('/getdata')
def getdata():
    return {'some':'value'}

@api.route('/artists', methods = ["POST"])
@token_required
def create_artist(our_user):

    your_name = request.json['your_name']
    artist_name = request.json['artist_name']
    description = request.json['description']
    artist_rating = request.json['artist_rating']
    fav_song = request.json['fav_song']
    user_token = our_user.token

    print(f"User Token: {our_user.token}")

    artist = Artist(your_name, artist_name, description, artist_rating, fav_song, user_token=user_token)
    
    db.session.add(artist)
    db.session.commit()

    response = artist_schema.dump(artist)

    return jsonify(response)

# this is going to retreave(READ) all the data

@api.route('/artists', methods = ['GET'])
@token_required
def get_artists(our_user):
    owner = our_user.token
    artists = Artist.query.filter_by(user_token=owner).all()
    response = artists_schema.dump(artists)

    return jsonify(response)

# retreave one artist

@api.route('/artists/<id>', methods=['GET'])
@token_required
def get_artist(our_user, id):
    if id:
        artist = Artist.query.get(id)
        response = artist_schema.dump(artist)
        return jsonify(response)
    else:
        return jsonify({'messagte': 'Valid Id Required'}), 401


@api.route('/artists/<id>', methods=['PUT'])
@token_required
def update_artist(our_user, id):
    artist = Artist.query.get(id)
    artist.your_name = request.json['your_name']
    artist.artist_name = request.json['artist_name']
    artist.description = request.json['description']
    artist.artist_rating = request.json['artist_rating']
    artist.fav_song = request.json['fav_song']
    artist.user_token = our_user.token

    db.session.commit()

    response = artist_schema.dump(artist)

    return jsonify(response)



@api.route('/artists/<id>', methods=['DELETE'])
@token_required
def delete_artists(our_user, id):
    artist = Artist.query.get(id)
    db.session.delete(artist)
    db.session.commit()

    response = artist_schema.dump(artist)
    return jsonify(response)


