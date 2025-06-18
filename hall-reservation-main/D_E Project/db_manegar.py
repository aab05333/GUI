import sqlite3
from sqlite3 import Connection
from datetime import datetime

class db_manegar:
    def __init__(self, db_path: str = "database.db"):
        self.db_path = db_path
        self._create_tables()

    def _connect(self) -> Connection:
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON;")
        return conn

    def _create_tables(self):
        conn = self._connect()
        cur = conn.cursor()

        # جدول الحسابات
        cur.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            is_admin BOOLEAN DEFAULT 0
        );
        """)

        # جدول القاعات
        cur.execute("""
        CREATE TABLE IF NOT EXISTS halls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            capacity INTEGER NOT NULL,
            price_per_hour REAL NOT NULL
        );
        """)

        # جدول الحجوزات
        cur.execute("""
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            hall_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            duration INTEGER NOT NULL,
            status TEXT NOT NULL DEFAULT 'Pending',
            FOREIGN KEY(user_id) REFERENCES accounts(id),
            FOREIGN KEY(hall_id) REFERENCES halls(id)
        );
        """)

        # جدول المعاملات المالية
        cur.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            reservation_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            date TEXT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES accounts(id),
            FOREIGN KEY(reservation_id) REFERENCES reservations(id)
        );
        """)

        conn.commit()
        conn.close()


    # === Accounts ===

    def add_account(self, username, password, is_admin=False):
        try:
            conn = self._connect()
            cur = conn.cursor()
            cur.execute("SELECT * FROM accounts WHERE username=?", (username,))
            if cur.fetchone():
                conn.close()
                return False
            cur.execute("INSERT INTO accounts (username, password, is_admin) VALUES (?, ?, ?)",
                        (username, password, is_admin))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error adding account: {e}")
            return False

    def get_account(self, username):
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("SELECT id, username, password, is_admin FROM accounts WHERE username=?", (username,))
        result = cur.fetchone()
        conn.close()
        return result

    # === Halls ===

    def add_hall(self, name: str, capacity: int, price: float):
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO halls (name, capacity, price_per_hour) VALUES (?, ?, ?)",
                    (name, capacity, price))
        conn.commit()
        conn.close()

    def get_halls(self):
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("SELECT id, name, capacity, price_per_hour FROM halls")
        rows = cur.fetchall()
        conn.close()
        return rows

    def update_hall(self, hall_id: int, name: str, capacity: int, price: float):
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("UPDATE halls SET name=?, capacity=?, price_per_hour=? WHERE id=?",
                    (name, capacity, price, hall_id))
        conn.commit()
        conn.close()

    def delete_hall(self, hall_id: int):
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("DELETE FROM halls WHERE id=?", (hall_id,))
        conn.commit()
        conn.close()

    # === Reservations ===

    def add_reservation(self, user_id: int, hall_id: int, date: str, duration: int, status="Confirmed"):
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("""INSERT INTO reservations (user_id, hall_id, date, duration, status)
                       VALUES (?, ?, ?, ?, ?)""",
                    (user_id, hall_id, date, duration, status))
        conn.commit()
        last_id = cur.lastrowid
        conn.close()
        return last_id

    def get_reservations_by_user(self, user_id: int):
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("""SELECT r.id, h.name, r.date, r.duration, r.status
                       FROM reservations r
                       JOIN halls h ON r.hall_id = h.id
                       WHERE r.user_id = ?""", (user_id,))
        rows = cur.fetchall()
        conn.close()
        return rows

    def get_all_reservations(self):
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("""SELECT r.id, a.username, h.id, r.date, r.duration, r.status
                       FROM reservations r
                       JOIN accounts a ON r.user_id = a.id
                       JOIN halls h ON r.hall_id = h.id""")
        rows = cur.fetchall()
        conn.close()
        return rows

    def update_reservation(self, res_id: int, date: str):
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("UPDATE reservations SET date=? WHERE id=?", (date, res_id))
        conn.commit()
        conn.close()

    def delete_reservation(self, res_id: int):
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("DELETE FROM reservations WHERE id=?", (res_id,))
        conn.commit()
        conn.close()

    def cancel_reservation(self, res_id: int):
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("UPDATE reservations SET status='Canceled' WHERE id=?", (res_id,))
        conn.commit()
        conn.close()

    # === Transactions ===

    def add_transaction(self, user_id: int, reservation_id: int, amount: float):
        conn = self._connect()
        cur = conn.cursor()
        date_str = datetime.now().strftime("%Y-%m-%d")
        cur.execute("""INSERT INTO transactions (user_id, reservation_id, amount, date)
                       VALUES (?, ?, ?, ?)""",
                    (user_id, reservation_id, amount, date_str))
        conn.commit()
        conn.close()

    def get_transactions(self):
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("""SELECT t.id, a.username, t.reservation_id, t.amount, t.date
                       FROM transactions t
                       JOIN accounts a ON t.user_id = a.id""")
        rows = cur.fetchall()
        conn.close()
        return rows
