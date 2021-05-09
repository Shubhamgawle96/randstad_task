from app import app
from main import data_analysis
from flask import send_file
import os

@app.route('/',methods=['GET', 'POST'])
def home():
    return "<h1>Assessment test by Randstad</h1><h3>By- Shubham Gawle</h3> <h4>shubham.gawle.ece14@itbhu.ac.in</h4>"

@app.route('/download/task1', methods=['GET'])
def download_task1():
    try:
        url1 = app.config['WHO_URL']
        url2 = app.config['COVID_URL']
        solution = data_analysis(url1=url1, url2=url2)
        solution()
        parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(parent_dir,'final.csv')
        print("file_path",file_path)
        return send_file(file_path, as_attachment=True,attachment_filename='randstad_task1.csv')
    except Exception as e:
        raise e

@app.route('/download/task2', methods=['GET'])
def download_task2():
    try:
        parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(parent_dir,'solutions')
        print("file_path",file_path)
        return send_file(file_path, as_attachment=True,attachment_filename='randstad_task2')
    except Exception as e:
        raise e

@app.route('/download/problem', methods=['GET'])
def problem():
    try:
        parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(parent_dir,'PythonTask.docx')
        print("file_path",file_path)
        return send_file(file_path, as_attachment=True,attachment_filename='PythonTask.docx')
    except Exception as e:
        raise e