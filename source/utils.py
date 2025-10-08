# CoffeeShop - Utilis 
# Agile - 4

"""
utils.py – Core utilities for CoffeeShop Manager CLI:
- Screen control (clear, waits, timeouts, timestamps)
- File paths and CSV I/O (load/save)
- Print helpers for formatted lists
- Validation functions (price, UK phone)
"""

import os
import time
import datetime
import threading
import pathlib 
import csv
   

# ─── OS functions ─── #

# Clear Screen
def clr_scrn():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear') # cls for windows 

# ─── Time and  DateTime Functions ─── #

# Time Wait
def t_wait(seconds=1):
    """Pauses execution for a specified number of seconds (default is 1)."""
    time.sleep(seconds)

# Time out
def wot(prompt="Press Enter to continue...", timeout=5): # Wait Or Timeout
    """Waits for user input or timeout (whichever comes first)."""
    input_received = []

    def user_input():
        try:
            input(prompt)
            input_received.append(True)
        except EOFError:
            pass

    thread = threading.Thread(target=user_input) # bug maker
    thread.daemon = True
    thread.start()
    thread.join(timeout)

    if not input_received:
        print(f"\n⏳ Auto continuing after {timeout} seconds...")
        time.sleep(0.5)

# Time stamp

def timestamp():
    """Add date and time stamp in YYYY-MM-DD HH:MM:SS format"""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")



# ─── pathlib core data file paths ─── #

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent   # Goes to base of project cd ../..
DATA_DIR = BASE_DIR /"data"                                 # Goes from base to data directory 

# Menu File Paths
PRODUCTS_FILE = DATA_DIR / "products.csv"
COURIERS_FILE = DATA_DIR / "couriers.csv"
ORDERS_FILE   = DATA_DIR / "orders.csv"

# Menu Fields Names
PRODUCTS_FIELDS = ["name", "price"]
COURIERS_FIELDS = ["name", "phone", "rate"]
ORDERS_FIELDS = ["customer_name", "customer_address", "customer_phone", "courier", "status", "items", "order_date", "total_price"]


# ─── CSV Read/Write and I/O Save/Load Functions ─── #

# Read From csv file function

def read_csv(path: pathlib.Path, fieldsnames: list[str]) -> list[dict]:
    if not path.exists():
        return []
    try:
        with open(path, newline = '', encoding='utf-8') as f:
            return list(csv.DictReader(f, fieldnames = fieldsnames))
    except (OSError, UnicodeDecodeError, csv.Error) as e:
        print(f"Error reading file {path}: {e}")
        return []

# Write as csv function 

def write_csv(path: pathlib.Path, fieldsname: list[str], data: list[dict]) -> None:

    path.parent.mkdir(parents=True, exist_ok=True) #ensure path exist if not create
    
    try:
        with open(path, 'w', newline = '',encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=fieldsname)
                writer.writerows(data)

    except(OSError, UnicodeDecodeError, csv.Error) as e:
        print(f"Failed to write CSV: {e}")



# ─── Loader functions ─── #
def load_products() -> list[dict]:
    rows = read_csv(PRODUCTS_FILE, PRODUCTS_FIELDS)
    for row in rows:
        try: 
            row['price'] = float(row['price'])
        except (ValueError, KeyError):
            row['price'] = 0.00
    return rows

def load_orders() -> list[dict]:
    return read_csv(ORDERS_FILE, ORDERS_FIELDS)

def load_couriers() -> list[dict]:
    return read_csv(COURIERS_FILE, COURIERS_FIELDS)

# ─── saver functions ─── #
def save_products(products: list[dict]) -> None:
    write_csv(PRODUCTS_FILE, PRODUCTS_FIELDS, products)

def save_orders(orders: list[dict]) -> None:
    write_csv(ORDERS_FILE, ORDERS_FIELDS, orders)

def save_couriers(couriers: list[dict]) -> None:
    write_csv(COURIERS_FILE, COURIERS_FIELDS, couriers)



# ─── Print List Functions ─── #

# Print Products
def print_products_list(products: list[dict]) -> None:
    if not products:
        print("\n 📭 No products found!")
        return

    print("\n-------------------------------\n")
    for index, product in enumerate(products, start=1):
        print(f"{index:<3} {product['name']:<15} £{product['price']:>6.2f}")
    print("\n-------------------------------")
    print(f"\n📦 Total products: {len(products)}")


# Print Orders
def print_orders_list(orders: list[dict]) -> None:
    if not orders:
        print("\n 📭 No orders found!")
        return

    print(
        f"{'No.':<4} "
        f"{'Name':<15} "
        f"{'Address':<25} "
        f"{'Phone':<14} "
        f"{'Courier':<12} "
        f"{'Items':<18} "
        f"{'Date':<22} "
        f"{'Total (£)':<12} "
        f"{'Status':<25}"
    )
    print("-" * 147)

    for index, order in enumerate(orders, start=1):
        print(
            f"{index:<4} "
            f"{order['customer_name']:<15} "
            f"{order['customer_address']:<25} "
            f"{order['customer_phone']:<14} "
            f"{order['courier']:<12} "
            f"{order['items']:<18} "
            f"{order['order_date']:<22} "
            f"£{float(order.get('total_price') or 0):<10.2f} "
            f"{order['status']:<25}"
        )

    print(f"\n📦 Total orders: {len(orders)}")

# Print Couriers
def print_couriers_list(couriers: list[dict]) -> None:
    if not couriers:
        print("\n 🚳 No couriers found!")
        return

    print("\n-------------------------------")
    for index, courier in enumerate(couriers, start=1):
        print(f"{index:>3}. {courier['name']:<20} {courier['phone']:<13}")
    print("\n-------------------------------")
    print(f"\n🛵 Total couriers: {len(couriers)}")


# ─── Test Functions ─── #

# is price valid price?
def valid_price(pric_str):
    try:
        price = float(pric_str)
        return price >= 0
    except ValueError:
        return False
    
# ─── Validate Functions ─── #

# Phone validation
def valid_uk_phone(existing_list: list[dict] = None, current_entry: dict = None, label:str ="entry", is_update = False, check_duplicates = True) -> str | None:
    existing_list = existing_list or []
    while True:
#        clr_scrn()

        prompt = (
            f"\n 📞 Enter {label}'s new phone number (press Enter to keep current): "
            if is_update
            else
            f"\n📞 Enter {label}'s phone number (press Enter to cancel): "
        )

        phone = input(prompt).strip()

        if not phone:
            clr_scrn()
            return None
        
        if not phone.isdigit():
            clr_scrn()
            print("\n\n\n\n⚠️ Phone number must be digits. 📞 Try again.")
            t_wait(2.5)
            continue

        if len(phone) != 11:
            clr_scrn()
            print("\n\n\n\n⚠️ Phone number must be 11 digits (UK format). 📞 Try again.")
            t_wait(2.5)
            continue

        if check_duplicates:
            if any(entry['phone'] == phone for entry in existing_list if entry != current_entry):
                clr_scrn()
                print(f"\n\n\n\n⚠️ Phone number: '{phone}' 📞 is already in use!")
                t_wait(2.5)
                continue

        return phone


# Messages

def rtm():
    print("""
       
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓   ______ _______ _______ _______ _______ _______      _______ _______ _______ ______   ▓▓
▓▓  |      |       |    ___|    ___|    ___|    ___|    |     __|   |   |       |   __ \  ▓▓
▓▓  |   ---|   -   |    ___|    ___|    ___|    ___|    |__     |       |   -   |    __/  ▓▓
▓▓  |______|_______|___|   |___|   |_______|_______|    |_______|___|___|_______|___|     ▓▓
▓▓                                                                                        ▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓                 _______ _______ _______ _______ _______ _______ ______                 ▓▓
▓▓     ______     |   |   |   _   |    |  |   _   |     __|    ___|   __ \     ______     ▓▓
▓▓    |______|    |       |       |       |       |    |  |    ___|      <    |______|    ▓▓
▓▓                |__|_|__|___|___|__|____|___|___|_______|_______|___|__|                ▓▓
▓▓                                                                                        ▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓                                                                                        ▓▓
▓▓                                                                                        ▓▓
▓▓    __          ______ _______ _______ _______ ______ _______ _______ _______ _______   ▓▓
▓▓  ,' _|_____   |   __ \    ___|_     _|   |   |   __ \    |  |_     _|    |  |     __|  ▓▓
▓▓ /          |  |      <    ___| |   | |   |   |      <       |_|   |_|       |    |  |  ▓▓
▓▓ \   _______|  |___|__|_______| |___| |_______|___|__|__|____|_______|__|____|_______|  ▓▓
▓▓  `.__|                                                                                 ▓▓
▓▓                                                                                        ▓▓
▓▓                                                                                        ▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 
    """)   


def invld():
    print("""
       
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓   ______ _______ _______ _______ _______ _______      _______ _______ _______ ______   ▓▓
▓▓  |      |       |    ___|    ___|    ___|    ___|    |     __|   |   |       |   __ \  ▓▓
▓▓  |   ---|   -   |    ___|    ___|    ___|    ___|    |__     |       |   -   |    __/  ▓▓
▓▓  |______|_______|___|   |___|   |_______|_______|    |_______|___|___|_______|___|     ▓▓
▓▓                                                                                        ▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓                 _______ _______ _______ _______ _______ _______ ______                 ▓▓
▓▓     ______     |   |   |   _   |    |  |   _   |     __|    ___|   __ \     ______     ▓▓
▓▓    |______|    |       |       |       |       |    |  |    ___|      <    |______|    ▓▓
▓▓                |__|_|__|___|___|__|____|___|___|_______|_______|___|__|                ▓▓
▓▓                                                                                        ▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓                                                                                        ▓▓
▓▓                                                                                        ▓▓
▓▓         __      _______ _______ ___ ___ _______ _____   _______ _____       __         ▓▓
▓▓        |  |    |_     _|    |  |   |   |   _   |     |_|_     _|     \     |  |        ▓▓
▓▓        |__|     _|   |_|       |   |   |       |       |_|   |_|  --  |    |__|        ▓▓
▓▓        |__|    |_______|__|____|\_____/|___|___|_______|_______|_____/     |__|        ▓▓
▓▓                                                                                        ▓▓
▓▓                                                                                        ▓▓
▓▓                                                                                        ▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 
    """) 











"""
Template

▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓   ______ _______ _______ _______ _______ _______      _______ _______ _______ ______   ▓▓
▓▓  |      |       |    ___|    ___|    ___|    ___|    |     __|   |   |       |   __ \  ▓▓
▓▓  |   ---|   -   |    ___|    ___|    ___|    ___|    |__     |       |   -   |    __/  ▓▓
▓▓  |______|_______|___|   |___|   |_______|_______|    |_______|___|___|_______|___|     ▓▓
▓▓                                                                                        ▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓                 _______ _______ _______ _______ _______ _______ ______                 ▓▓
▓▓     ______     |   |   |   _   |    |  |   _   |     __|    ___|   __ \     ______     ▓▓
▓▓    |______|    |       |       |       |       |    |  |    ___|      <    |______|    ▓▓
▓▓                |__|_|__|___|___|__|____|___|___|_______|_______|___|__|                ▓▓
▓▓                                                                                        ▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓                                                                                        ▓▓
▓▓                                                                                        ▓▓
▓▓                                                                                        ▓▓
▓▓                                                                                        ▓▓
▓▓                                                                                        ▓▓
▓▓                                                                                        ▓▓
▓▓                                                                                        ▓▓
▓▓                                                                                        ▓▓
▓▓                                                                                        ▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

"""