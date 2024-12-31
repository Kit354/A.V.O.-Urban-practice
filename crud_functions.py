import sqlite3

connection = sqlite3.connect('telegram_bot_db.db')
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

    connection.commit()


def get_all_products():
    initiate_db()
    check = cursor.execute('SELECT * FROM Products')

    if check.fetchone() is None:
        for product in range(1, 5):
            cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                           (f'Продукт{product}', f'Описание{product}', f'{product * 100}'))
        connection.commit()
    else:
        cursor.execute('SELECT * FROM Products')
        product = cursor.fetchall()
        return product

    connection.commit()
    connection.close()


if __name__ == '__main__':
    get_all_products()
