#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os
from unicodedata import category
from flask import Flask, flash, redirect, url_for
# from flask_pymongo import PyMongo # pip install flask_pymongo
import pymysql as db # pip install pymysql
# from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import jsonify
from flask import render_template
from flask_login import LoginManager, login_user, logout_user, current_user, login_required, UserMixin
from view_form import SongForm, zh_tw_SongForm, SearchForm, FormRegister
from flask_bcrypt import Bcrypt
# from form import FormRegister
from lib.conf import AWS_db_credential

# credential imported from db_config.cfg
aws_db_conf = AWS_db_credential()
host_name = aws_db_conf.host_name
user_name = aws_db_conf.user_name
password = aws_db_conf.password
port = aws_db_conf.port
db_name = aws_db_conf.db_name
# print(host_name, user_name, password, port, db_name)

app = Flask(__name__)
app.config['SECRET_KEY']='your key' #這是因為flask_wtf預設需要設置密碼，也是為了避免一開始所說的CSRF攻擊。
# lhc = db.connect(host='127.0.0.1', user='root', password='')

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
login_manager.login_message = '請登錄'
login_manager.init_app(app)


class User(UserMixin):
    pass
# users = [
#     {'id':'Tom', 'username': 'Tom', 'password': '111111'},
#     {'id':'Michael', 'username': 'Michael', 'password': '123456'}
# ]

def query_user(user_id):
    with db.connect(host=host_name, user=user_name, password=password, port=port, db=db_name) as conn:
        with conn.cursor() as cur:    
            sql = f"""
            select username, password from user_account where username = '{user_id}'
            """
            cur.execute(sql); res = cur.fetchone()
            print(res)
            if res:
                user = {'id': res[0], 'password': res[1]}
                print(user)
            else:
                user = None
            return user
    # for user in users:
    #     if user_id == user['id']:
            # return user

@login_manager.user_loader
def load_user(user_id):
    if query_user(user_id) is not None:
        curr_user = User()
        curr_user.id = user_id
        return curr_user

@app.route('/index_login')
@login_required
def index_login():
    return 'Logged in as: %s' % current_user.get_id()





@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('home2.html', home_active='active')

@app.route('/login_test')
def login_test():
    return render_template('login_test.html')



@app.route('/')
def index():
    return "SUCCESS! Deploy to K8S!"

@app.route('/home-page')
def home_page():
    return render_template('home2.html', home_active='active')

@app.route('/zh_tw/home-page')
def zh_tw_home_page():
    return render_template('/zh_tw/home2.html', home_active='active')

@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template('market.html', item_name='Phone', items=items)

@app.route('/test2-aws')
def index2():
    conn = db.connect(host=host_name, user=user_name, password=password, port=port, db=db_name)
    cur = conn.cursor()
    sql = "SELECT * FROM `mysql`.`user`"
    cur.execute(sql)
    u = cur.fetchall() # 返回 tuple 
    conn.close()
    return f"hello {u}"

@app.route('/song-share', methods=['GET', 'POST'])
def song_share():
    # conn = db.connect(host=host_name, user=user_name, password=password, port=port, db=db_name)
    # cur = conn.cursor()
    form = SongForm()
    #  flask_wtf類中提供判斷是否表單提交過來的method，不需要自行利用request.method來做判斷
    if form.validate_on_submit():
        s_name = request.values.get('song_name')
        author = request.values.get('author')
        desc = request.values.get('desc')
        url = request.values.get('url')
        with db.connect(host=host_name, user=user_name, password=password, port=port, db=db_name) as conn:
            with conn.cursor() as cur:
                sql = f"""
                INSERT INTO guitar_song(`name`, `author`, `desc`, `url`) VALUES ('{s_name}', '{author}','{desc}', '{url}')
                """
                # print(sql)
                try:
                    cur.execute(sql)
                    conn.commit()
                    return render_template('submit_success.html', s_name=s_name, share_now_active='active')
                except Exception as e:
                    conn.rollback()
                    print(e)
                    return render_template('submit_failed.html', err=e, share_now_active='active')
                # return f'Success Submit {s_name} {desc} {url}'
    #  如果不是提交過來的表單，就是GET，這時候就回傳user.html網頁
    return render_template('guitar_song.html', form=form, share_now_active='active')

@app.route('/zh_tw/song-share', methods=['GET', 'POST'])
def zh_tw_song_share():
    # conn = db.connect(host=host_name, user=user_name, password=password, port=port, db=db_name)
    # cur = conn.cursor()
    form = zh_tw_SongForm()
    #  flask_wtf類中提供判斷是否表單提交過來的method，不需要自行利用request.method來做判斷
    if form.validate_on_submit():
        s_name = request.values.get('song_name')
        author = request.values.get('author')
        desc = request.values.get('desc')
        url = request.values.get('url')
        with db.connect(host=host_name, user=user_name, password=password, port=port, db=db_name) as conn:
            with conn.cursor() as cur:
                sql = f"""
                INSERT INTO guitar_song(`name`, `desc`, `url`) VALUES ('{s_name}', '{desc}', '{url}')
                """
                # print(sql)
                try:
                    cur.execute(sql)
                    conn.commit()
                    return render_template('/zh_tw/submit_success.html', s_name=s_name, share_now_active='active')
                except Exception as e:
                    conn.rollback()
                    print(e)
                    return render_template('/zh_tw/submit_failed.html', err=e, share_now_active='active')
                # return f'Success Submit {s_name} {desc} {url}'
    #  如果不是提交過來的表單，就是GET，這時候就回傳user.html網頁
    return render_template('/zh_tw/guitar_song.html', form=form, share_now_active='active')


@app.route('/query-song', methods=['GET', 'POST'])
def query_song():
    conn = db.connect(host=host_name, user=user_name, password=password, port=port, db=db_name)
    # conn = db.connect(host='127.0.0.1', user='root', password='', port=3306, db='test')
    cur = conn.cursor()
    form = SearchForm()
    if form.validate_on_submit():
        q_name = request.values.get('query_name')
        sql = f"""
        SELECT `id`, `name`, `author`, `desc`, `url` FROM `guitar_song`
        WHERE `name`= '{q_name}'
        """
        print(sql)
        cur.execute(sql)
        res = cur.fetchall() # 返回 tuple
        conn.close()
        if len(res)>0:
            # return f"your query result {res}"
            return render_template('query_result.html', result=res, search_active='active', query_name=q_name)
        else:
            return render_template('query_failed.html', search_active='active', query_name=q_name)
    else:
        return render_template('query_song.html', form=form, search_active='active')

@app.route('/zh_tw/query-song', methods=['GET', 'POST'])
def zh_tw_query_song():
    conn = db.connect(host=host_name, user=user_name, password=password, port=port, db=db_name)
    cur = conn.cursor()
    form = SearchForm()
    if form.validate_on_submit():
        q_name = request.values.get('query_name')
        sql = f"""
        SELECT `id`, `name`, `author`, `desc`, `url` FROM `guitar_song`
        WHERE `name`= '{q_name}'
        """
        print(sql)
        cur.execute(sql)
        res = cur.fetchall() # 返回 tuple
        conn.close()
        if len(res)>0:
            return render_template('/zh_tw/query_result.html', result=res, search_active='active', query_name=q_name)
        else:
            return render_template('/zh_tw/query_failed.html', search_active='active', query_name=q_name)
    else:
        return render_template('/zh_tw/query_song.html', form=form, search_active='active')

@app.route('/css-test')
def css_test():
    return render_template('css_test.html')

@app.route('/accordion')
def test_accordion():
    return render_template('test_accordion.html')

@app.route('/js-test')
def js_index():
    # js_test.html 會因為點擊觸發 javascript, 進而改變 html
    return render_template('js_test.html')

@app.route('/jquery')
def jquery():
    # js_test.html 會因為點擊觸發 javascript, 進而改變 html
    return render_template('jqry.html')

@app.route('/hover')
def hover():
    return render_template('hover.html')

@app.route('/card-accordion')
def card():
    return render_template('card_accordion.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form.get('userid')
        user = query_user(user_id)
        if not user:
            return render_template('login.html', home_active='active', err=True, default_acct=user_id)
            # flash('username does not exist', category='danger')
        else:
            pw_hash = user['password']
            
            if user is not None and Bcrypt().check_password_hash(pw_hash, request.form['password'])==True:

                curr_user = User()
                curr_user.id = user_id

                # 通过Flask-Login的login_user方法登录用户
                login_user(curr_user)

                return render_template('home2.html', home_active='active')
            else:
                return render_template('login.html', home_active='active', err=True, default_acct=user_id)

        # flash('Wrong username or password!')

    # GET 请求
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form =FormRegister()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        username = request.values.get('username')
        email = request.values.get('email')
        pw = request.values.get('password')
        pw_hash = Bcrypt().generate_password_hash(password=pw).decode('utf8')
        with db.connect(host=host_name, user=user_name, password=password, port=port, db=db_name) as conn:
            with conn.cursor() as cur:
                check_sql = f"""
                select * from user_account where username = '{username}'
                """
                cur.execute(check_sql); row = cur.fetchone()
                if row:
                    flash("This account is already registered!!", category='danger')
                else:
                    sql = f"""
                    INSERT INTO user_account(`username`, `email`, `password`) VALUES ('{username}', '{email}', '{pw_hash}')
                    """ 
                    try:
                        cur.execute(sql)
                        conn.commit()
                        return "Success Thank You"
                    except Exception as e:
                        conn.rollback()
                        print(e)
                        return "Opps! something goes wrong"

    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.config['SECRET_KEY']='your key' #這是因為flask_wtf預設需要設置密碼，也是為了避免一開始所說的CSRF攻擊。
    # app.run(debug=True)
    # app.run(host="0.0.0.0", port=8001)
    # 本地測試環境 python3 app.py
    app.run(host="0.0.0.0", port=80, debug=True) # to any port#