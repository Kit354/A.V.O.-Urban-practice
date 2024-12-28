import sqlite3

connection = sqlite3.connect('not_telegram.db')
coursor = connection.cursor()

coursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

for number in range(1, 11):
    coursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                    (f'User{number}', f'example{number}@gmail.com', number * 10, 1000))

for number in range(1, 11, 2):
    coursor.execute('UPDATE Users SET balance = ? WHERE username = ?', (str(500), f'User{number}'))

for number in range(1, 11, 3):
    coursor.execute('DELETE FROM Users WHERE username = ?', (f'User{number}',))


coursor.execute('SELECT * FROM Users WHERE age != ?', (60,))
users = coursor.fetchall()
for user in users:
    print(f'Имя: {user[1]} | Почта: {user[2]}| Возраст: {user[3]}| Баланс: {user[4]}')

coursor.execute('DELETE FROM Users WHERE id = ?', (6,))

coursor.execute('SELECT COUNT(*) FROM Users')
total_users = coursor.fetchone()[0]
print(total_users)

coursor.execute('SELECT SUM(balance) FROM Users')
all_balances = coursor.fetchone()[0]
print(all_balances / total_users)

connection.commit()
connection.close()
