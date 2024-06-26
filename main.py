# app.py
from flask import Flask, request,jsonify
from apiServer.user_api import user_blueprint
from apiServer.message_api import message_blueprint
from apiServer.session_api import session_blueprint
from apiServer.role_api import role_blueprint
from apiServer.information_api import information_blueprint
from apiServer.chat_emloyee_api import chat_blueprint
from apiServer.data_score_api import data_score_blueprint
from apiServer.faculty_api import faculty_blueprint
from apiServer.admission_subject_api import admission_subject_blueprint
from apiServer.data_score_vs_subject_combination_api import data_score_vs_subject_combination_blueprint
from apiServer.subject_combination_api import subject_combination_blueprint
from apiServer.subject_combination_vs_admission_subject_api import subject_combination_vs_admission_subject_blueprint
from apiServer.new_page_api import new_page_blueprint
from apiServer.bug_question_api import bug_question_blueprint
from apiServer.bug_comment_api import bug_comment_blueprint

import datetime
import hashlib
from flask_cors import CORS
# from apiServer.gpt_api import callGpt
import os
#Tạo token 
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

from datetime import timedelta


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Welcome to backend botchat2024 Lê Văn Chiến!'

# @app.route('/gpt', methods=['POST'])
# def callgpt():
#     data = request.json
#     gpt = callGpt(data)
#     if gpt:
       
#         return jsonify(gpt), 200
#     else:
#         return jsonify({"error": "Failed to Gpt"}), 500
# Tính toán giá trị cho JWT_SECRET_KEY
def generate_secret_key():
    # Tạo một chuỗi ngẫu nhiên với độ dài 64 ký tự
    random_bytes = os.urandom(32)
    secret_key = hashlib.sha256(random_bytes).hexdigest()
    return secret_key
# Khai báo key bí mật cho việc tạo token
app.config['JWT_SECRET_KEY'] = generate_secret_key()
# Cấu hình thời gian sống của token
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)  # Token truy cập hết hạn sau 30 ngày
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=1) # Token làm mới hết hạn sau 60 ngày

# Khởi tạo JWTManager với ứng dụng Flask của bạn
jwt = JWTManager(app)

# Đăng ký các blueprint
app.register_blueprint(user_blueprint)
app.register_blueprint(message_blueprint)
app.register_blueprint(session_blueprint)
app.register_blueprint(role_blueprint)
app.register_blueprint(information_blueprint)
app.register_blueprint(chat_blueprint)
app.register_blueprint(data_score_blueprint)
app.register_blueprint(faculty_blueprint)
app.register_blueprint(admission_subject_blueprint)
app.register_blueprint(data_score_vs_subject_combination_blueprint)
app.register_blueprint(subject_combination_blueprint)
app.register_blueprint(subject_combination_vs_admission_subject_blueprint)
app.register_blueprint(new_page_blueprint)
app.register_blueprint(bug_question_blueprint)
app.register_blueprint(bug_comment_blueprint)


if __name__ == '__main__':
    app.run(debug=True)
    
