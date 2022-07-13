#  引入flask_wtf
from flask_wtf import FlaskForm
#  各別引入需求欄位類別
from wtforms import StringField, SubmitField, TextAreaField, validators, PasswordField
# from wtforms.fields.html5 import EmailField
#  引入驗證
from wtforms.validators import DataRequired, Email, Length
from wtforms.fields.html5 import EmailField

#  從繼承FlaskForm開始
class SongForm(FlaskForm):
    # username = StringField('UserName', validators=[DataRequired(message='Not Null')])
    # email = EmailField('Email', validators=[DataRequired(message='Not Null')])
    song_name = StringField('Song Name*', validators=[DataRequired(message='Not Null')])
    author = TextAreaField('Author*', validators=[DataRequired(message='Not Null')])
    desc = TextAreaField('Description*', validators=[DataRequired(message='Not Null')])
    url = TextAreaField('Ref Link*', validators=[DataRequired(message='Not Null')])
    submit = SubmitField('Submit')

class zh_tw_SongForm(FlaskForm):
    # username = StringField('UserName', validators=[DataRequired(message='Not Null')])
    # email = EmailField('Email', validators=[DataRequired(message='Not Null')])
    song_name = StringField('歌曲名稱*', validators=[DataRequired(message='Not Null')])
    author = TextAreaField('作者*', validators=[DataRequired(message='Not Null')])
    desc = TextAreaField('詳細描述*', validators=[DataRequired(message='Not Null')])
    url = TextAreaField('參考連結*', validators=[DataRequired(message='Not Null')])
    submit = SubmitField('Submit')

class SearchForm(FlaskForm):
    # username = StringField('UserName', validators=[DataRequired(message='Not Null')])
    # email = EmailField('Email', validators=[DataRequired(message='Not Null')])
    query_name = StringField('SongName', validators=[DataRequired(message='Not Null')])
    search = SubmitField('Search')

class FormRegister(FlaskForm):
    """依照Model來建置相對應的Form
    
    password2: 用來確認兩次的密碼輸入相同
    """
    username = StringField('UserName', validators=[
        validators.DataRequired(),
        validators.Length(min=5, max=30, message='UserName should be between 5 and 30 charc')
    ])
    email = EmailField('Email', validators=[
        validators.DataRequired(),
        validators.Length(1, 50),
        validators.Email()
    ])
    password = PasswordField('PassWord', validators=[
        validators.DataRequired(),
        validators.Length(min=5, message='Password should be at least 5 charc'),
        validators.EqualTo('password2', message='Confirm password NOT matched')
    ])
    password2 = PasswordField('Confirm PassWord', validators=[
        validators.DataRequired()
    ])
    submit = SubmitField('Register New Account')