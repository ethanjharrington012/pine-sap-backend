from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DecimalField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
    # email, password, submit_buttom
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email',validators = [DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit_buttom = SubmitField()
    
# class ArtistForm(FlaskForm):
#     your_name = StringField('your name')
#     artist_name = StringForm('artist name')
#     description = StringForm('description')
#     artist_rating = StringField('artist rating')
#     fav_song = StringField('fav song')
