import os

from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import logging
logging.basicConfig(level=logging.DEBUG)

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
  
    @app.route('/')
    def index():
        return render_template('index.html', title="Welcome")

    # INSERT DATA INTO TABLE
    @app.route('/insert', methods=['POST'])
    def insert():
        kanji_list = request.json.get('kanji_list')

        conn = sqlite3.connect(app.config['DATABASE'])
        c = conn.cursor()

        try:
            for kanji in kanji_list:
                c.execute("INSERT INTO user_kanji (user_id, kanji, is_remembered) VALUES (?, ?, ?)", (2, kanji, 1))
                conn.commit()
        except sqlite3.IntegrityError:
            return jsonify({"status": "failed", "message": "Can not insert data"}), 400

        conn.close()
        return jsonify({"status": "success", "data": "Success"}), 201
    
    # LOGIN
    @app.route('/login', methods=['POST'])
    def login():
        username = request.json.get('username')
        password = request.json.get('password')

        conn = sqlite3.connect(app.config['DATABASE'])
        c = conn.cursor()

        c.execute("SELECT * FROM user WHERE username = ?", (username,))
        user = c.fetchone()

        if user is None or not check_password_hash(user[2], password):
            return jsonify({"error": "Incorrect username or password"}), 401

        conn.close()
        return jsonify({
            "status": "success",
            "data": { 'id': user[0], 'username': user[1]}
        }), 201
    
    # REGISTER
    @app.route('/register', methods=['POST'])
    def register():
        username = request.json.get('username')
        password = request.json.get('password')

        if not username or not password:
            return jsonify({"status": "failed", "message": "Username and password required"}), 400

        hashed_password = generate_password_hash(password)

        conn = sqlite3.connect(app.config['DATABASE'])
        c = conn.cursor()
        
        try:
            c.execute("INSERT INTO user (username, password) VALUES (?, ?)", (username, hashed_password))
            conn.commit()
        except sqlite3.IntegrityError:
            return jsonify({"status": "failed", "message": "Username already taken"}), 400
        
        # Get the userdata from database
        c.execute("SELECT * FROM user WHERE username = ?", (username,))
        user = c.fetchone()

        conn.close()
        return jsonify({"status": "success", "data": {'id': user[0], 'username': user[1]}}), 201
    
    # ALL COURSES
    @app.route('/courses', methods=['GET'])
    def get_courses():
        conn = sqlite3.connect(app.config['DATABASE'])
        c = conn.cursor()

        c.execute("""
            SELECT course.id, course.level, course.title, course.description,
                GROUP_CONCAT(kanji.kanji) as kanjis
            FROM course
            LEFT JOIN course_kanji ON course.id = course_kanji.course_id
            LEFT JOIN kanji ON course_kanji.kanji = kanji.kanji
            GROUP BY course.id
        """)

        courses = c.fetchall()
        conn.close()
        
        return jsonify({
            'status': "success", 
            'data': [{'id': course[0], 'level': course[1], 'title': course[2], 'description': course[3], 'kanjis': course[4]} for course in courses]
            })
    
    # USER COURSES
    @app.route('/user_courses/<int:user_id>', methods=['GET'])
    def get_user_courses(user_id):
        conn = sqlite3.connect(app.config['DATABASE'])
        c = conn.cursor()

        c.execute("""
            SELECT course.id, course.level, course.title, course.description, user_course.percentage,
                GROUP_CONCAT(kanji.kanji || ':' || IFNULL(user_kanji.is_remembered, 0)) as kanjis
            FROM course
            JOIN user_course ON course.id = user_course.course_id
            LEFT JOIN course_kanji ON course.id = course_kanji.course_id
            LEFT JOIN kanji ON course_kanji.kanji = kanji.kanji
            LEFT JOIN user_kanji ON kanji.kanji = user_kanji.kanji AND user_kanji.user_id = user_course.user_id
            WHERE user_course.user_id = ?
            GROUP BY course.id
        """, (user_id,))

        courses = c.fetchall()
        conn.close()
        
        return jsonify({
            'status': "success",
            'data': [{'id': course[0], 'level': course[1], 'title': course[2], 'description': course[3], 'percentage': course[4], 'kanjis': {kanji.split(':')[0]: bool(int(kanji.split(':')[1])) for kanji in course[5].split(',')} if course[5] else {}} for course in courses]
            })
    
    # COURSE KANJI
    @app.route('/course_kanji/<int:course_id>', methods=['GET'])
    def get_course_kanji(course_id):        
        conn = sqlite3.connect(app.config['DATABASE'])
        c = conn.cursor()

        c.execute("""
            SELECT kanji.kanji, kanji.stroke_count, kanji.meanings, kanji.on_reading, kanji.kun_reading, IFNULL(user_kanji.is_remembered, 0) as is_remembered
            FROM kanji
            JOIN course_kanji ON kanji.kanji = course_kanji.kanji
            LEFT JOIN user_kanji ON kanji.kanji = user_kanji.kanji
            WHERE course_kanji.course_id = ?
        """, (course_id,))

        kanjis = c.fetchall()
        
        c.execute("""
            SELECT course.id, course.level, course.title, course.description
            FROM course 
            WHERE course.id = ?
        """, (course_id,))
        
        course = c.fetchone()
        conn.close()
        
        return jsonify({
                'status': "success",
                'data': {'kanjis': [{'kanji': kanji[0], 'stroke_count': kanji[1], 'meanings': kanji[2], 'on_reading': kanji[3], 'kun_reading': kanji[4], 'is_remembered': bool(int(kanji[5])) if kanji[5] else False} for kanji in kanjis],
                'id': course[0], 'level': course[1], 'title': course[2], 'description': course[3], 'percentage': 0
                }
            })
 
    # KANJI
    @app.route('/kanji/<string:kanji>', methods=['GET'])
    def get_kanji(kanji): 
        conn = sqlite3.connect(app.config['DATABASE'])
        c = conn.cursor()
        
        c.execute("""
            SELECT kanji.kanji, kanji.stroke_count, kanji.meanings, kanji.on_reading, kanji.kun_reading, kanji.jlpt
            FROM kanji
            WHERE kanji.kanji = ?
        """, (kanji))
        
        kanji = c.fetchone()
        conn.close()
        
        return jsonify({
            'status': "success",
            'data': {'kanji': kanji[0], 'stroke_count': kanji[1], 'meanings': kanji[2], 'on_reading': kanji[3], 'kun_reading': kanji[4], 'jlpt': kanji[5]}
        })
        
    # LEARN KANJI
    @app.route('/learning', methods=['POST'])
    def get_learning_kanji():
        course_id = request.json.get('course_id')
        user_id = request.json.get('user_id')
        
        conn = sqlite3.connect(app.config['DATABASE'])
        c = conn.cursor()

        c.execute("""
            SELECT kanji.kanji, kanji.stroke_count, kanji.meanings, kanji.on_reading, kanji.kun_reading, IFNULL(user_kanji.is_remembered, 0) as is_remembered
            FROM kanji
            JOIN course_kanji ON kanji.kanji = course_kanji.kanji
            LEFT JOIN user_kanji ON kanji.kanji = user_kanji.kanji AND user_kanji.user_id = ?
            WHERE course_kanji.course_id = ? AND (user_kanji.is_remembered = 0 OR user_kanji.is_remembered IS NULL)
            LIMIT 5
        """, (user_id, course_id))

        kanjis = c.fetchall()
        conn.close()

        return jsonify({
            'status': 'success',
            'data': [
                {'kanji': kanji[0], 'stroke_count': kanji[1], 'meanings': kanji[2], 'on_reading': kanji[3], 'kun_reading': kanji[4], 'is_remembered': bool(int(kanji[5])) if kanji[5] else False} for kanji in kanjis
            ]
        })

    # UPDATE KANJI
    @app.route('/update_learning', methods=['POST'])
    def update_kanji():
        data = request.get_json()
        user_id = data['user_id']
        kanji_list = data['kanji_list']

        conn = sqlite3.connect(app.config['DATABASE'])
        c = conn.cursor()

        for kanji in kanji_list:
            c.execute("""
                INSERT INTO user_kanji (user_id, kanji, is_remembered)
                VALUES (?, ?, 1)
                ON CONFLICT (user_id, kanji)
                DO UPDATE SET is_remembered = 1;
            """, (user_id, kanji))

        conn.commit()
        conn.close()

        return jsonify({'status': 'success', 'message': 'Kanji updated successfully'})
    
    @app.route('/update_course', methods=['POST'])
    def update_course():
        course_id = request.json.get('course_id')
        user_id = request.json.get('user_id')
        conn = sqlite3.connect(app.config['DATABASE'])
        c = conn.cursor()

        c.execute("""
                INSERT INTO user_course
                VALUES (?, ?, ?)
            """, (user_id, course_id, 0))

        conn.commit()
        conn.close()

        return jsonify({'status': 'success', 'message': 'Course updated successfully'})

    from . import db
    db.init_app(app)

    return app

