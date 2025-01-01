import sqlite3

connection = sqlite3.connect('telegram_bot_db_2.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    );
    ''')

    connection.commit()


def add_user(username, email, age):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (f'{username}', f'{email}', f'{age}', 1000))
    connection.commit()
    connection.close()


def is_included(username):
    cursor.execute(f'SELECT id FROM Users WHERE username = ?', (username,))
    user = cursor.fetchone()
    connection.commit()
    if user is not None:
        return True
    else:
        return False


def get_all_products():
    check = cursor.execute('SELECT * FROM Products')

    if check.fetchone() is None:
        for product in range(1, 5):
            cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                           (f'Продукт {product}', f'Описание {product}', f'{product * 100}'))
        connection.commit()
    else:
        cursor.execute('SELECT * FROM Products')
        product = cursor.fetchall()
        return product

    connection.commit()
    connection.close()


if __name__ == '__main__':
    get_all_products()
