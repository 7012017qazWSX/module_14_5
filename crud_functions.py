import sqlite3


def initiate_db(db_name='products.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL DEFAULT 1000
        )
    ''')

    title = ['product1', 'product2', 'product3', 'product4']
    description = ['описание1', 'описание2', 'описание3', 'описание4']
    price = ['5000', '10000', '15000', '20000']

    for t, d, p in zip(title, description, price):
        cursor.execute('INSERT INTO Products(title, description, price) VALUES (?, ?, ?)', (t, d, p))

    conn.commit()
    conn.close()


def add_user(username, email, age, db_name='products.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO Users(username, email, age, balance) 
        VALUES (?, ?, ?, 1000)
    ''', (username, email, age))

    conn.commit()
    conn.close()


def is_included(username, db_name='products.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('SELECT 1 FROM Users WHERE username = ?', (username,))
    user_exists = cursor.fetchone() is not None

    conn.close()

    return user_exists


def get_all_products(db_name='products.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()

    conn.close()

    return products


if __name__ == '__main__':
    initiate_db()

    add_user('john_doe', 'john@example.com', 30)
    print(is_included('john_doe'))

    products = get_all_products()
    for product in products:
        print(product)