#coding: utf-8

from flask import Flask, render_template

# app という名前で Flask オブジェクトをインスタンス化
app = Flask(__name__)

# --- View 側の設定 ---

# ルートディレクトリにアクセスした場合の挙動
@app.route('/')

# defいかがアクセス後の操作
def index():
	# DBから以下の変数を読み込んできたと仮定
	title_ = 'ようこそ'
	message_ = 'MTVデザインパターンでWebアプリ作成'

	return render_template('index.html', title=title_, message=message_)

	# # return 'Hello World!'
	# return render_template('index.html')

# エントリーポイント
if __name__ == '__main__':
    app.run()

