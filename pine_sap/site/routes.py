from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from pine_sap.forms import ArtistForm
from pine_sap.models import Artist, db

"""
    Note that in the below code,
    some arguments are specified when creating Blueprint objects.
    The first argument, 'site' is the Blueprint's name,
    which flask uses for routing.
    The second argument, __name__,  is the Blueprint's import name, 
    which flask uses to locate the Blueprint's resources
"""

site = Blueprint('site', __name__, template_folder = 'site_templates')

@site.route('/')
def home():
    print("this is inside of site.routes")
    return render_template('index.html')

@site.route('/profile', methods=['GET', 'POST'])
@login_required

def profile():
    my_artist = ArtistForm() # data coming back from the forms

    try:
        print('inside TRY: site/routes')
        if request.method == "POST" and my_artist.validate_on_submit():
            your_name = my_artist.your_name.data
            artist_name = my_artist.artist_name.data
            description = my_artist.description.data
            fav_song = my_artist.fav_song.data
            artist_rating = my_artist.artist_rating.data
            user_token = current_user.token

            artist = Artist(your_name, artist_name, description, artist_rating, fav_song, user_token)

            db.session.add(artist)
            db.session.commit()
            print('Should be in database')
            return redirect(url_for('site.profile'))

    except:
        raise Exception('Artist Not Created: please check form again')
    print('missed exception')
    current_user_token = current_user.token

    artists = Artist.query.filter_by(user_token=current_user_token)
    return render_template('profile.html', form=my_artist, artists= artists)