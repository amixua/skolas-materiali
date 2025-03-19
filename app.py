from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Flask sẽ trả về file index.html từ thư mục templates

if __name__ == '__main__':
    app.run(debug=True)
