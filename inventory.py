import sqlite3

# Create or connect to the database
conn = sqlite3.connect('inventory.db')
c = conn.cursor()

# Create table if not exists
c.execute('''
    CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        quantity INTEGER NOT NULL
    )
''')
conn.commit()

def add_item(name, quantity):
    c.execute('INSERT INTO inventory (name, quantity) VALUES (?, ?)', (name, quantity))
    conn.commit()
    print(f"Added {name} with quantity {quantity}.")

def view_items():
    c.execute('SELECT * FROM inventory')
    rows = c.fetchall()
    print("\nInventory:")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Quantity: {row[2]}")

def update_item(item_id, quantity):
    c.execute('UPDATE inventory SET quantity = ? WHERE id = ?', (quantity, item_id))
    conn.commit()
    print(f"Updated item ID {item_id} to quantity {quantity}.")

def delete_item(item_id):
    c.execute('DELETE FROM inventory WHERE id = ?', (item_id,))
    conn.commit()
    print(f"Deleted item ID {item_id}.")

def main():
    while True:
        print("\nChoose an action:")
        print("1. Add Item")
        print("2. View Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")
        choice = input("Enter choice (1-5): ")

        if choice == '1':
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            add_item(name, quantity)
        elif choice == '2':
            view_items()
        elif choice == '3':
            item_id = int(input("Enter item ID to update: "))
            quantity = int(input("Enter new quantity: "))
            update_item(item_id, quantity)
        elif choice == '4':
            item_id = int(input("Enter item ID to delete: "))
            delete_item(item_id)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()

conn.close()
