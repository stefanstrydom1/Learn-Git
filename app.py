from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3
from werkzeug.exceptions import abort
from model import premium_calculation
import pandas as pd

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_case(case_id):
    conn = get_db_connection()
    case = conn.execute('SELECT * FROM cases WHERE case_id = ?',
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

    if request.method == 'POST':
        insured_name = request.form['insured_name']
        inception_date = request.form['inception_date']
        expiry_date = request.form['expiry_date']


        if not insured_name:
            flash('Name is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO cases (insured_name, inception_date, expiry_date) VALUES (?, ?, ?)',
                            (insured_name, inception_date, expiry_date))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/<int:case_id>/edit', methods=('GET', 'POST'))
def edit(case_id):
    case = get_case(case_id)

    if request.method == 'POST':
        insured_name = request.form['insured_name']
        inception_date = request.form['inception_date']
        expiry_date = request.form['expiry_date']


        if not insured_name:
            flash('Name is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE cases SET insured_name = ?, inception_date = ?, expiry_date = ?'
                         ' WHERE case_id = ?',
                         (insured_name, inception_date, expiry_date, case_id))
            conn.commit()
            conn.close()
            return redirect(url_for('case',case_id=case_id))

    return render_template('edit.html', case=case)

@app.route('/<int:case_id>/delete', methods=('POST',))
def delete(case_id):
    case = get_case(case_id)
    conn = get_db_connection()
    conn.execute('DELETE FROM cases WHERE case_id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(case['insured_name']))
    return redirect(url_for('index'))

@app.route('/<int:case_id>/upload_claims', methods=('GET','POST'))
def upload_claims(case_id):
    case = get_case(case_id)
    sqlite_table = "claims"

    if request.method == 'POST':
        file = request.form['upload_claims_file']
        data_table = pd.read_excel(file)
        data_table['case_id'] = case_id
        conn = get_db_connection()
        data_table.to_sql(sqlite_table,conn,if_exists='append',index=False)
        return render_template('data.html', data_table=data_table.to_html())
    return render_template('upload_claims.html', case=case)

@app.route('/data', methods = ('GET','POST'))
def data(data_table):
    manipulated_data = data_table
    return render_template('data.html', data = manipulated_data)




