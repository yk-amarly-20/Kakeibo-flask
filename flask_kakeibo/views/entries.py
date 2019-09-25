from flask import Flask, render_template, redirect, session, url_for, flash, request
from flask_kakeibo import app, db
from flask_kakeibo.models.entries import Entry


@app.route('/')
def show_entries():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entries = Entry.query.order_by(Entry.id.desc()).all()
    return render_template('entries/index.html', entries=entries)


@app.route('/entries/new', methods=['GET'])
def new_entry():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('entries/new.html')


@app.route('/entries', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        redirect(url_for('login'))
    entry = Entry(
        category=request.form['category'],
        outcome=request.form['outcome'],
        memo=request.form['memo']
    )

    db.session.add(entry)
    db.session.commit()
    flash('項目が追加されました')
    return redirect(url_for('show_entries'))


@app.route('/entries/<int:id>/edit', methods=['GET'])
def edit_entry(id):
    if not session.get('logged_in'):
        redirect(url_for('login'))
    entry = Entry.query.get(id)
    return render_template('entries/edit.html', entry=entry)


@app.route('/entries/<int:id>/update', methods=['POST'])
def update_entry(id):
    if not session.get('logged_in'):
        redirect(url_for('login'))
    entry = Entry.query.get(id)
    entry.category = request.form['category']
    entry.outcome = request.form['outcome']
    entry.memo = request.form['memo']
    db.session.merge(entry)
    db.session.commit()
    flash('更新しました')
    return redirect(url_for('show_entries'))


@app.route('/entries/<int:id>/delete', methods=['POST'])
def delete_entry(id):
    if not session.get('logged_in'):
        redirect(url_for('login'))
    entry = Entry.query.get(id)
    db.session.delete(entry)
    db.session.commit()
    flash('収入を削除しました')
    return redirect(url_for('show_entries'))
