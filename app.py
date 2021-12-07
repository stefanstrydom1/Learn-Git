from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3
from werkzeug.exceptions import abort
from model import premium_calculation

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_case(case_id):
    conn = get_db_connection()
    case = conn.execute('SELECT * FROM cases WHERE id = ?',
                        (case_id,)).fetchone()
    conn.close()
    if case is None:
        abort(404)
    return case

def calculate_premium(frequency, severity, target_loss_ratio):
    expected_loss, technical_premium = premium_calculation(frequency, severity, target_loss_ratio)
    return expected_loss, technical_premium

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

@app.route('/')
def index():
    conn = get_db_connection()
    cases = conn.execute('SELECT * FROM cases').fetchall()
    conn.close()
    return render_template('index.html', cases=cases)

@app.route('/<int:case_id>')
def case(case_id):
    case = get_case(case_id)
    return render_template('case.html', case=case)

@app.route('/create', methods=('GET', 'POST'))
def create():
    frequency = 0.0
    severity = 0.0
    expected_loss = 0.0
    technical_premium = 0.0

    if request.method == 'POST':
        insured_name = request.form['insured_name']
        layer_name = request.form['layer_name']
        frequency = float(request.form['frequency'])
        severity = float(request.form['severity'])
        target_loss_ratio = float(request.form['target_loss_ratio'])
        expected_loss, technical_premium = calculate_premium(frequency, severity, target_loss_ratio)

        if not insured_name:
            flash('Name is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO cases (insured_name, layer_name, frequency, severity, target_loss_ratio, expected_loss, technical_premium) VALUES (?, ?, ?, ?, ?, ?, ?)',
                            (insured_name, layer_name, frequency, severity, target_loss_ratio, expected_loss, technical_premium))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    case = get_case(id)

    if request.method == 'POST':
        insured_name = request.form['insured_name']
        layer_name = request.form['layer_name']
        frequency = float(request.form['frequency'])
        severity = float(request.form['severity'])
        target_loss_ratio = float(request.form['target_loss_ratio'])
        expected_loss, technical_premium = calculate_premium(frequency, severity, target_loss_ratio)


        if not insured_name:
            flash('Name is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE cases SET insured_name = ?, layer_name = ?, frequency = ?, severity = ?, target_loss_ratio = ?, expected_loss = ?,  technical_premium = ?'
                         ' WHERE id = ?',
                         (insured_name, layer_name, frequency, severity, target_loss_ratio, expected_loss, technical_premium, id))
            conn.commit()
            conn.close()
            return redirect(url_for('case',case_id=id))

    return render_template('edit.html', case=case)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    case = get_case(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM cases WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(case['insured_name']))
    return redirect(url_for('index'))