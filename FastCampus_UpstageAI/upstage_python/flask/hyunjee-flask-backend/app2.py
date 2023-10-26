# 서비스를 빨리 구현을 해야하는 상황 -> flask
# AI Engineer -> Developer
from flask import Flask, request, render_template
import sqlite3

# flask 가동
app = Flask(__name__)


# SQlite와 연결
def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


# 데이터베이스 테이블 생성
def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = f"CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT)"
    cursor.execute(sql)
    conn.commit()
    conn.close()


def add_book(title, author):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = f"INSERT INTO books (title, author) VALUES ('{title}','{author}')"
    cursor.execute(sql)  # 실행해
    conn.commit()  # 반영해
    conn.close()


@app.route("/", methods=["GET", "POST"])
def main():
    create_table()

    if request.method == "POST":
        print("유저로부터 POST 요청이 들어왔습니다.")
        title = request.form["title"]
        author = request.form["author"]
        add_book(title, author)

    return render_template("index.html")


if __name__ == "__main__":
    app.run()
