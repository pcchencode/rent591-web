from flask import Flask
# from flask_pymongo import PyMongo # pip install flask_pymongo
import pymysql as db# pip install pymysql
# from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import jsonify
from flask import render_template
from view_form import UserForm

app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb://localhost:27017/rent_591"
# app.config['JSON_AS_ASCII'] = False
# app.config['JSONIFY_MIMETYPE'] ="application/json;charset=utf-8" #解決中文亂碼
# mongo = PyMongo(app)


# lhc = db.connect(host='127.0.0.1', user='root', password='')

# @app.route('/home')
# def home_page():
#     return render_template('home.html')

@app.route('/home-page')
def home_page():
    return render_template('home2.html', item_name='Phone_test')

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

# @app.route('/test2')
# def index2():
#     conn = db.connect(host='127.0.0.1', user='root', password='', port=3306, db='test')
#     cur = conn.cursor()
#     sql = "SELECT `id`, `name` FROM `reply` WHERE 1"
#     cur.execute(sql)
#     u = cur.fetchall() # 返回 tuple 
#     conn.close()
#     return f"hello {u}"

@app.route('/submit', methods=['GET', 'POST'])
def submit_page():
    conn = db.connect(host='127.0.0.1', user='root', password='', port=3306, db='test')
    cur = conn.cursor()
    if request.method == 'POST':
        u_name = request.values.get('username')
        sql = f"""
        INSERT INTO reply(name) VALUES ('{u_name}')
        """
        print(sql)
        try:
            cur.execute(sql)
            conn.commit()
            return render_template('submit_success.html', u_name=u_name)
        except Exception as e:
            conn.rollback()
            print(e)
            return render_template('submit_failed.html', err=e)
    return render_template('submit.html')


@app.route('/song-share', methods=['GET', 'POST'])
def song_share():
    conn = db.connect(host='127.0.0.1', user='root', password='', port=3306, db='test')
    cur = conn.cursor()
    form = UserForm()
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
            return render_template('submit_success.html', s_name=s_name)
        except Exception as e:
            conn.rollback()
            print(e)
            return render_template('submit_failed.html', err=e)
        # return f'Success Submit {s_name} {desc} {url}'
    #  如果不是提交過來的表單，就是GET，這時候就回傳user.html網頁
    return render_template('guitar_song.html', form=form)


# @app.route('/all', methods=['GET'])
# def home_page():
#     obj = mongo.db.room_object
#     output = []
#     for s in obj.find():
#         output.append({'地區':s['region'], '物件網址':s['room_url'], '出租者身份':s['renter_type'], '出租者':s['renter'], '聯絡固話':s['phone'], '現況':s['status'], '性別要求':s['gender_req'], '型態':s['obj_type']})
#     return jsonify({'result' : output})

# @app.route('/male-new-taipei', methods=['GET'])
# def get_cond1():
#     obj = mongo.db.room_object
#     output = []
#     for s in obj.find({"region":"新北市", "gender_req":{"$in":["男生","男女生皆可",""]}}):
#         output.append({'地區':s['region'], '物件網址':s['room_url'], '出租者身份':s['renter_type'], '出租者':s['renter'], '聯絡固話':s['phone'], '現況':s['status'], '性別要求':s['gender_req'], '型態':s['obj_type']})
#     return jsonify({'result' : output})

# @app.route('/phone/<phone>', methods=['GET'])
# def get_cond2(phone):
#     obj = mongo.db.room_object
#     output = []
#     s = obj.find({'phone' : phone})
#     if s:
#         for s in obj.find({'phone': phone}):
#             output.append({'地區':s['region'], '物件網址':s['room_url'], '出租者身份':s['renter_type'], '出租者':s['renter'], '聯絡固話':s['phone'], '現況':s['status'], '性別要求':s['gender_req'], '型態':s['obj_type']})
#     else:
#         output = "No such phone"
#     return jsonify({'result' : output})

# @app.route('/non-owner', methods=['GET'])
# def get_cond3():
#     obj = mongo.db.room_object
#     output = []
#     for s in obj.find({"renter_type":{"$ne":"屋主"}}):
#         output.append({'地區':s['region'], '物件網址':s['room_url'], '出租者身份':s['renter_type'], '出租者':s['renter'], '聯絡固話':s['phone'], '現況':s['status'], '性別要求':s['gender_req'], '型態':s['obj_type']})
#     return jsonify({'result' : output})

# @app.route('/taipei-miss-wu', methods=['GET'])
# def get_cond4():
#     obj = mongo.db.room_object
#     output = []
#     for s in obj.find({"region":"台北市", "renter":"吳小姐", "renter_type":"屋主"}):
#         output.append({'地區':s['region'], '物件網址':s['room_url'], '出租者身份':s['renter_type'], '出租者':s['renter'], '聯絡固話':s['phone'], '現況':s['status'], '性別要求':s['gender_req'], '型態':s['obj_type']})
#     return jsonify({'result' : output})

# # 透過網址後面帶參數，進行查詢，EX：
# # http://127.0.0.1:5000/query/?region=台北市
# # http://127.0.0.1:5000/query/?region=台北市&renter=陳先生
# # http://127.0.0.1:5000/query/?region=台北市&renter=陳先生&renter_type=代理
# @app.route('/query/')
# def get_query_result():
#     obj = mongo.db.room_object
#     output = []
#     region = request.args.get('region', type = str)
#     renter = request.args.get('renter', type = str)
#     renter_type = request.args.get('renter_type', type = str)
#     obj_type = request.args.get('obj_type', type = str)
#     phone = request.args.get('phone', type = str)
#     status = request.args.get('status', type = str)
#     gender_req = request.args.get('gender_req', type = str)
#     cond = {}
#     if region:
#         cond["region"] = region
#     if renter:
#         cond["renter"] = renter
#     if renter_type:
#         cond["renter_type"] = renter_type
#     if obj_type:
#         cond["obj_type"] = obj_type
#     if phone:
#         cond["phone"] = phone
#     if status:
#         cond["status"] = status
#     if gender_req:
#         cond["gender_req"] = gender_req

#     for s in obj.find(cond):
#         output.append({'地區':s['region'], '物件網址':s['room_url'], '出租者身份':s['renter_type'], '出租者':s['renter'], '聯絡固話':s['phone'], '現況':s['status'], '性別要求':s['gender_req'], '型態':s['obj_type']})
#     return jsonify({'result' : output})

# # POST:update db
# @app.route('/star', methods=['POST'])
# def add_star():
#   star = mongo.db.stars
#   name = request.json['name']
#   distance = request.json['distance']
#   star_id = star.insert({'name': name, 'distance': distance})
#   new_star = star.find_one({'_id': star_id })
#   output = {'name' : new_star['name'], 'distance' : new_star['distance']}
#   return jsonify({'result' : output})

if __name__ == '__main__':
    app.config['SECRET_KEY']='your key' #這是因為flask_wtf預設需要設置密碼，也是為了避免一開始所說的CSRF攻擊。
    app.run(debug=True)
