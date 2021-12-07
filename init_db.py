import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO cases (insured_name, layer_name, expected_loss, technical_premium) VALUES (?, ?, ?, ?)",
            ('Insured ABC', 'Primary', 100, 120)
            )


connection.commit()
connection.close()