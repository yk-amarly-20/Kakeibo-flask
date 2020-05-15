from flask import Flask, render_template, redirect, url_for, session, request, flash
from flask_kakeibo import app


@app.route('/login', methods=['GET', 'POST'])
def login():

    # ログイン実装
    # 実はまあまあ時間かかった
    error = None
    if request.method == "POST":
        if request.form['username'] != app.config['USERNAME']:
            flash('ユーザ名が違います')
        elif request.form['password'] != app.config['PASSWORD']:
            flash('パスワードが違います')
        else:
            flash('ログインしました')
            session['logged_in'] = True
            return redirect(url_for('show_entries'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    # ログアウト時はフラッシュメッセージを表示
    flash('ログアウトしました')
    session.pop('logged_in', None)
    return redirect(url_for('show_entries'))
