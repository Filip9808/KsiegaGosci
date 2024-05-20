import sqlite3


def connect_to_db(db_name):
    """Łączy się z bazą danych SQLite"""
    conn = sqlite3.connect(db_name)
    return conn


def create_table(conn):
    """Tworzy tabelę w bazie danych"""
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS results (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        data TEXT NOT NULL)''')
    conn.commit()


def insert_data(conn, data):
    """Wstawia dane do tabeli"""
    cursor = conn.cursor()
    cursor.execute('INSERT INTO results (data) VALUES (?)', (data,))
    conn.commit()


def fetch_data(conn):
    """Pobiera dane z tabeli"""
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM results')
    rows = cursor.fetchall()
    return rows


def main():
    db_name = 'example.db'
    conn = connect_to_db(db_name)
    create_table(conn)

    # Pobieranie danych od użytkownika
    user_data = input("Podaj dane do zapisania: ")
    insert_data(conn, user_data)

    results = fetch_data(conn)
    for row in results:
        print(row)
    conn.close()


if __name__ == '__main__':
    main()