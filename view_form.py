#  引入flask_wtf
from flask_wtf import FlaskForm
#  各別引入需求欄位類別
from wtforms import StringField, SubmitField, TextAreaField
# from wtforms.fields.html5 import EmailField
#  引入驗證
from wtforms.validators import DataRequired, Email

#  從繼承FlaskForm開始
class SongForm(FlaskForm):
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
