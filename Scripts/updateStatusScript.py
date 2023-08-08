import mysql.connector


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


def update_status():
    
    conn = connect_to_db()
    cursor = conn.cursor()
    
    cursor.execute("SET SQL_SAFE_UPDATES = 0;")
    cursor.execute("UPDATE order_items set item_status = 'PENDING' WHERE item_status = 'DONE';")
    cursor.execute("UPDATE order_items set item_status = 'PENDING' WHERE item_status = 'IN_PREPARATION';")
    cursor.execute("UPDATE order_items set item_status = 'PENDING' WHERE item_status = 'PROCESSING';")
    cursor.execute("UPDATE order_status set status = 'PENDING' WHERE status = 'DONE';")
    cursor.execute("UPDATE order_status set status = 'PENDING' WHERE status = 'IN_PREPARATION';")
    cursor.execute("UPDATE order_status set status = 'PENDING' WHERE status = 'PROCESSING';")
    conn.commit()
    cursor.close()
    conn.close()
    print("Task Succeeded!")


def main():
    update_status()


if __name__ == '__main__':
    main()
