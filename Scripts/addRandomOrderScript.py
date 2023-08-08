import mysql.connector
import random

import mysql.connector
import random


def connect_to_db():
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            port=3307,
            user="root",
            password="Andreeas18MySQL",
            database="siemensprojectdb"
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None


def get_random_order():
    con = connect_to_db()
    cursor = con.cursor()

    cursor.execute("SELECT user_id FROM users ORDER BY RAND() LIMIT 1")
    user_id = cursor.fetchone()[0]

    cursor.execute("SELECT item_id FROM menu_items ORDER BY RAND() LIMIT 1")
    item_id = cursor.fetchone()[0]

    quantity = random.randint(1, 10)

    cursor.close()
    con.close()

    return user_id, item_id, quantity


def add_order():
    user_id, item_id, quantity = get_random_order()

    if not all([user_id, item_id, quantity]):
        print("Error: please fill in all fields.")
        return

    con = connect_to_db()
    cursor = con.cursor()

    cursor.execute("START TRANSACTION")
    cursor.execute(
        "INSERT INTO order_status (user_id) VALUES (%s)", (user_id,))
    cursor.execute("SELECT LAST_INSERT_ID()")
    order_id = cursor.fetchone()[0]
    cursor.execute("INSERT INTO order_items (order_id, item_id, quantity) VALUES (%s, %s, %s)",
                   (order_id, item_id, quantity))
    cursor.execute("COMMIT")

    cursor.close()
    con.close()

    print("Order added successfully.")

def main():
    add_order()

if __name__ == '__main__':
    main()
