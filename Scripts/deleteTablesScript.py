import mysql.connector

def delete_all_rows():
    # Connect to the database
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            port=3307,
            user="root",
            password="Andreeas18MySQL",
            database="siemensprojectdb"
        )
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return

    # Create a cursor object
    cursor = conn.cursor()

    # Execute the DELETE queries for order_items
    delete_query_1 = "ALTER TABLE order_items DROP FOREIGN KEY order_id"
    delete_query_2 = "DELETE FROM order_items"
    delete_query_3 = "ALTER TABLE order_items ADD CONSTRAINT order_id FOREIGN KEY (order_id) REFERENCES order_status (order_id)"
    cursor.execute(delete_query_1)
    cursor.execute(delete_query_2)
    cursor.execute(delete_query_3)

    # Execute the DELETE queries for order_status
    delete_query_4 = "ALTER TABLE order_status DROP FOREIGN KEY user_id"
    delete_query_5 = "DELETE FROM order_status"
    delete_query_6 = "ALTER TABLE order_status ADD CONSTRAINT user_id FOREIGN KEY (user_id) REFERENCES users (user_id)"
    cursor.execute(delete_query_4)
    cursor.execute(delete_query_5)
    cursor.execute(delete_query_6)

    # Commit the changes and close the connection
    conn.commit()
    cursor.close()
    conn.close()

    # Optional: display a success message
    print("All rows deleted from order_items and order_status tables.")

def main():
    delete_all_rows()

if __name__ == '__main__':
    main()
