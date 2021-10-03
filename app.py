import os
from flask import Flask
# from flask_pymongo import PyMongo # pip install flask_pymongo
import pymysql as db# pip install pymysql
# from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import jsonify
from flask import render_template
from view_form import SongForm, SearchForm
from lib.conf import AWS_db_credential

# credential imported from db_config.cfg
aws_db_conf = AWS_db_credential()
host_name = aws_db_conf.host_name
user_name = aws_db_conf.user_name
password = aws_db_conf.password
port = aws_db_conf.port
db_name = aws_db_conf.db_name


app = Flask(__name__)
# lhc = db.connect(host='127.0.0.1', user='root', password='')

# @app.route('/home')
# def home_page():
#     return render_template('home.html')

@app.route('/home-page')
def home_page():
    return render_template('home2.html', home_active='active')

@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template('market.html', item_name='Phone', items=items)

# @app.route('/test1')
# def index():
#     conn = db.connect(host='127.0.0.1', user='root', password='', port=3306, db='test')
#     cur = conn.cursor()
#     sql = "SELECT `id`, `name` FROM `reply` WHERE 1"
#     cur.execute(sql)
#     u = cur.fetchall()
#     conn.close()
#     return render_template('index.html', u=u)

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
    conn = db.connect(host=host_name, user=user_name, password=password, port=port, db=db_name)
    cur = conn.cursor()
    form = SongForm()
    #  flask_wtf類中提供判斷是否表單提交過來的method，不需要自行利用request.method來做判斷
    if form.validate_on_submit():
        s_name = request.values.get('song_name')
        desc = request.values.get('desc')
        url = request.values.get('url')
        sql = f"""
        INSERT INTO guitar_song(`name`, `desc`, `url`) VALUES ('{s_name}', '{desc}', '{url}')
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


@app.route('/query-song', methods=['GET', 'POST'])
def query_song():
    conn = db.connect(host=host_name, user=user_name, password=password, port=port, db=db_name)
    # conn = db.connect(host='127.0.0.1', user='root', password='', port=3306, db='test')
    cur = conn.cursor()
    form = SearchForm()
    if form.validate_on_submit():
        q_name = request.values.get('query_name')
        sql = f"""
        SELECT `id`, `name`, `desc`, `url` FROM `guitar_song`
        WHERE `name`= '{q_name}'
        """
        print(sql)
        cur.execute(sql)
        res = cur.fetchall() # 返回 tuple
        conn.close()
        if len(res)>0:
            # return f"your query result {res}"
            return render_template('query_result.html', result=res, search_active='active')
        else:
            return render_template('query_failed.html', search_active='active')
    else:
        return render_template('query_song.html', form=form, search_active='active')

@app.route('/css-test')
def css_test():
    return render_template('css_test.html')

@app.route('/accordion')
def test_accordion():
    return render_template('test_accordion.html')


@app.route('/js-test')
def index():
    # js_test.html 會因為點擊觸發 javascript, 進而改變 html
    return render_template('js_test.html')

@app.route('/jquery')
def jquery():
    # js_test.html 會因為點擊觸發 javascript, 進而改變 html
    return render_template('jqry.html')

@app.route('/hover')
def hover():
    return render_template('hover.html')


if __name__ == '__main__':
    app.config['SECRET_KEY']='your key' #這是因為flask_wtf預設需要設置密碼，也是為了避免一開始所說的CSRF攻擊。
    app.run(debug=True)
