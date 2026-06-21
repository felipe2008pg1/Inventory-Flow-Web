import os
from datetime import datetime
import data as da
import time
import json

def save_data():
    try:
        with open(da.FILE, "w", encoding="utf-8") as f:
            json.dump(da.stock, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error saving: {e}")

def load_data():
    if os.path.exists(da.FILE):
        try:
            with open(da.FILE, "r", encoding="utf-8") as f:
                da.stock = json.load(f)
        except Exception as e:
            print(f"Error loading: {e}")

def show_stock():
    if len(da.stock) == 0:
        write_slow("Stock is empty!")
        print('=' * 10)
        input("Press ENTER to go back: ").strip()
    else:
        for i, t in enumerate(da.stock, start=1):
            print(f"{i} - {t['product']:<14} | ${t['price']}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else "clear")

def show_time():
    now = datetime.now()
    br = now.strftime("%d/%m/%Y - %H:%M:%S")
    return br

def add_stock(product, price):
    da.stock.append({'product': product, 'price': price})
    print(f"Product {product} added successfully!")
    save_data()

def remove_from_stock():
    if len(da.stock) == 0:
        write_slow("Stock is empty!")
        print('\n=' * 10)
    else:
        for c, i in enumerate(da.stock, start=1):
            print(f"{c} - {i['product']} | {i['price']}")
        remove = int(input("Enter product index: ")) - 1
        removed = da.stock[remove]['product']
        da.stock.pop(remove)
        write_slow(f"Product {removed} removed successfully.")
        save_data()

def write_menu(text, new_line=True):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(0.05)

    if new_line:
        print()

def write_slow(text):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(0.05)
    print()

def shutdown():
    print("=" * 12)
    write_slow(">> SHUTTING DOWN <<")
    print("=" * 12)

def verify_admin():

    attempts = 0

    while True:
        try:
            admin_name = input("Enter admin user: ").strip().upper()
            admin_password = int(input("").strip())
            found = False

            for p in da.authorized_data:
                if admin_name == p['admin'] and admin_password == p['password']:
                    found = True
                    print('Admin found.')
                    write_slow("LOADING...")
                    time.sleep(1)

            if not found:
                attempts += 1
                print("Admin not found or incorrect data")
                write_slow(f"Attempt {attempts}/3.")
                print("- Restarting.. -")
                time.sleep(0.3)
                clear_screen()

        except ValueError:
            print("Enter numbers when required")
            continue
