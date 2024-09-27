from flask import Flask, render_template

#웹 서버 역할 Flask APP
app = Flask(__name__)

#라우터 설정
@app.route('/')
def insrx():
    return render_template('index.html')

#Flask App 가동(run)
if __name__=="__main__":
    app.run(debug=True)