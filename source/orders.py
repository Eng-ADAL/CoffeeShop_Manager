# CoffeeShop - Orders
# Agile - 4

"""
orders.py – Implements the Orders Menu for CoffeeShop Manager CLI.
Handles viewing, creating, updating statuses, and deleting orders,
with CSV persistence and robust input validation.
"""

import products as p
import couriers as c
import utils    as u

def orders_menu(orders_list, products_list,couriers_list):
    new_orders = []
    u.clr_scrn()
    print("")
    while True:
        u.clr_scrn()
        print("""

▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓   ______ _______ _______ _______ _______ _______      _______ _______ _______ ______   ▓▓
▓▓  |      |       |    ___|    ___|    ___|    ___|    |     __|   |   |       |   __ \  ▓▓
▓▓  |   ---|   -   |    ___|    ___|    ___|    ___|    |__     |       |   -   |    __/  ▓▓
▓▓  |______|_______|___|   |___|   |_______|_______|    |_______|___|___|_______|___|     ▓▓
▓▓                                                                                        ▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓                                                                                        ▓▓
▓▓                                                                                        ▓▓
▓▓                                                                                        ▓▓
▓▓                              --- Couriers Menu ---                                     ▓▓
▓▓                                                                                        ▓▓
▓▓                              1 - View Orders                                           ▓▓
▓▓                              2 - Create New Orders                                     ▓▓
▓▓                              3 - Update an Order Status                                ▓▓
▓▓                              4 - Update an Order                                       ▓▓
▓▓                              5 - Delete Order                                          ▓▓
▓▓                                                                                        ▓▓
▓▓                              0 - Return to Main Menu                                   ▓▓
▓▓                                                                                        ▓▓
▓▓                                                                                        ▓▓
▓▓                                                                                        ▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
              """)
        
        choice = input("                                Choose an option: ")

# 0 - Return to Main Menu
        if choice in ['0', 'o', 'q']:
            u.clr_scrn()
            u.rtm()
            print("\n                                🔙 Returning Main Menu 🔙\n")
            u.t_wait(1.5)
            break

# 1 - Print Orders Dictionary
        elif choice == "1":
            u.clr_scrn()

            orders_list[:] = u.load_orders()
            print("\n🧾 Orders List ")
            u.print_orders_list(orders_list) # need to fix ?
            
            input("\n\n\n\n🔙 Press ⏎ Enter ⏎ for return for Orders Menu")
            continue

# 2 - Create New Order 
        elif choice == "2":
            new_orders = []
            while True:
                u.clr_scrn()
                print("\n🆕 Create New Order ☕")
                u.print_products_list(products_list)

                order_items = []
                cancelled = False    # Life saver piece of code v1.1
                
                while True:
                    choice = input("\n➕ Input product numbers to order >\n   (⏎ to finish / 'C' to cancel)  >> ").strip().lower()

                    if choice.lower() in ['c', 'q']:
                        u.clr_scrn()
                        print("\n\n\n❌ Order Cancelled\n\nReturning Orders Menu") 
                        u.t_wait(2)
                        cancelled = True
                        break

                    if choice =='':
                        if not order_items:
                            u.clr_scrn()
                            print("\n\n\n\n⚠️ Need to select at least one product")
                            u.t_wait(2.5)
                            u.clr_scrn()
                            print("📋 Products List:")
                            u.print_products_list(products_list)                            
                            continue
                        break
                    
                    
                    if not choice.isdigit() or int(choice) not in range(1, len(products_list) + 1):
                        u.clr_scrn()
                        print(f"\n\n\n\n\n            '{choice}'\n⚠️ Invalid product number, try again.\n\n\n")
                        u.t_wait(2.5)
                        u.clr_scrn()
                        print("📋 Products List:")
                        u.print_products_list(products_list)
                        
                        print("\n🛒 You have added:")
                        for item in order_items:
                            print(f" - {item['name']:<15} £{item['price']:.2f}")

                        total_price = sum(item['price'] for item in order_items)
                        print("__________________________")
                        print(f"   Total price:    £{total_price:.2f}")
                        continue
                    
                    product = products_list[int(choice) - 1]
                    order_items.append(product)
                    
                    u.clr_scrn()
                    print("📋 Products List:")
                    u.print_products_list(products_list)
                    
                    print("\n🛒 You have added:")
                    for item in order_items:
                        print(f" - {item['name']:<15} £{item['price']:.2f}")

                    total_price = sum(item['price'] for item in order_items)
                    print("__________________________")
                    print(f"   Total price:    £{total_price:.2f}")
                    continue
                        
                if cancelled:   # Life saver piece of code v1.2
                    break

                while True:
                    name = input("👤 Customer Name: ").strip().title()
                    if name:
                        break
                    print("\n⚠️  Name cannot be empty. Please enter your name.")

                while True:
                    address = input("🏡 Address: ").strip().title()
                    if address:
                        break
                    address = input("⚠️  Please mercy for our couriers! How can they find you? \n (For TAKE AWAY Press ⏎) ")
                    
                    if address in [""]:
                        print("\n🚶 TAKE AWAY selected. 🚶‍➡️")
                        address = '[Take Away]'
                    break

                phone = u.valid_uk_phone(orders_list,label=name,check_duplicates = False) 
                if phone is None:
                    break
                # Stretch if phone and name is not same warn phone used by an another customer? Or Authenticator API?

                status = "🧑‍🍳 preparing"

                items = [str(products_list.index(p) + 1) for p in order_items]

                while True:
                    if address == '[Take Away]':
                        courier_name = '[T.A.]'
                        break
                    u.clr_scrn()
                    print("\n🛵💨 Available Couriers:\n")
                    u.print_couriers_list(couriers_list)

                    courier_input = input("\nSelect courier number (or press Enter to for TAKE AWAY): ").strip()

                    u.clr_scrn()

                    if courier_input.lower() in [""]:
                        print("\n🚶 TAKE AWAY selected. 🚶‍➡️")
                        courier_name = '[T.A.]'
                        break

                    if courier_input.isdigit():
                        courier_index = int(courier_input) -1
                        if 0 <= courier_index < len(couriers_list):
                            courier_name = couriers_list[courier_index]['name']
                            print(f"\n✅ Assigned Courier: {courier_name}")
                            break
                        else:
                            u.clr_scrn()
                            print("\n\n\n\n⚠️ Invalid courier number. Try again.")
                            u.t_wait(2.5)
                    else:
                        u.clr_scrn()
                        print("\n\n\n\n⚠️ Please enter a number.")
                        u.t_wait(2.5)

                total_price = sum(item['price'] for item in order_items)

                new_order = {
                    "customer_name": name,
                    "customer_address": address,
                    "customer_phone": phone,
                    "courier": courier_name,
                    "status": status,
                    "items": ",".join(items),
                    "order_date": u.timestamp(),
                    "total_price": round(total_price, 2)
                }

                # add new order

                orders_list.append(new_order)
                u.save_orders(orders_list)
                u.clr_scrn()
                print(f"\n✅ Order for '{name}' has been added!")
                print(f"🕒 Date: {new_order['order_date']}")
                print("\n📦 Items    :")
                print("__________________________\n")
                for item in order_items:
                    print(f" - {item['name']:<15} £{item['price']:.2f}")
                    u.t_wait(0.5)
                
                print("\n__________________________")
                u.t_wait(0.8)
                print(f"Total price:       £{total_price:.2f}")

                again = input("\n➕ Add another order? (Y/N): ").strip().lower()
                if again not in ['y', '']:
                    break

# 3 - Update Existing Order Status
        elif choice == "3":
            u.clr_scrn()
            
            while True:
                u.clr_scrn()

                print("\n🔄 Pick an Order for Delivery Status Update\n\n")
                u.print_orders_list(orders_list)

                selected = input("\nSelect the order number to update status \n(⏎ to return Orders Menu): ").strip()

                if selected in ['', 'q']:
                    u.clr_scrn()
                    print("\n\n\n\n❌ Update cancelled.\n\n\n\n ")
                    u.t_wait(2.5)
                    break

                if not selected.isdigit() or not (1 <= int(selected) <= len(orders_list)):
                    u.clr_scrn()
                    print("\n\n\n\n⚠️ Invalid order number.\n\n\n\n")
                    u.t_wait(2)
                    continue

                u.clr_scrn()
                index = int(selected) - 1
                current_status = orders_list[index]['status']

                while True:
                    u.clr_scrn()
                    print(f"\n\nFor order '{selected}' - {orders_list[index]['customer_name']}'s Current status is: '{current_status}'\n")

                    print("Avaliable Stauses: \n\n")
                    status_options = [ "🧑‍🍳 preparing", "📤 dispached", "🛵 on delivery", "📦✅ delivered", "❌ cancelled"]

                    for i, status in enumerate(status_options, start=1):
                        print(f"{i} - {status}")

                    new_status = input("\n\n🔄 Pick new status ( ⏎ for skip ): ").strip()
                    
                    if new_status.lower() in ['', 'q']:
                        u.clr_scrn()
                        print("\n\n\n\n🔙 Returning Update Menu\n\n\n\n ")
                        u.t_wait(2.5)
                        break

                    if not new_status.isdigit() or not (1 <= int(new_status) <= len(status_options)):
                        u.clr_scrn()
                        print("\n\n\n\n⚠️ Invalid status number.\n\n\n\n")
                        u.t_wait(2.5)
                        continue

                    orders_list[index]['status'] = status_options[int(new_status) -1]

                    u.save_orders(orders_list)
                    u.clr_scrn()
                    print(f"\n\n\n\n🔄  {orders_list[index]['customer_name']}'s order is now: \n\n\n >> '{(orders_list[index]['status'].upper())}' <<")
                    u.t_wait(2.5)
                    input("\n\n\n🔙 Press enter for return menu")
                    break
            
# 4 - Update Existing Order
        elif choice == "4":
            u.clr_scrn()
            print("\n\n\n\n🚧 Under construction 🚧\n\n\n Press  ⏎ Enter ⏎ for return Orders Menu ")
            u.t_wait(1.5)

# 5 - Delete Order
        elif choice == "5":
            u.clr_scrn()
            
            while True:
                u.clr_scrn()
                
                print("\n🗑️ Pick an Order for Delete\n\n")
                u.print_orders_list(orders_list)

                selected = input("\n Select the number of the order to delete \n\n or Press ⏎ Enter ⏎ to skip deletion: ")
                if not selected:
                    u.clr_scrn()
                    print("\n\n\n\n🚫 Deletion cancelled.")
                    u.t_wait(2.5)
                    break

                if not selected.isdigit() or not (1 <= int(selected) <= len(orders_list)):
                    u.clr_scrn()
                    print("\n\n\n\n⚠️ Invalid selection. Please try again.\n\n\n\n")
                    u.t_wait(2)
                    continue

                index = int(selected) -1
                order_to_delete = orders_list[index]

                u.clr_scrn()
                print("\n" + "🗑️  " + " Delete Order Confirmation ".center(50, "─") + " 🗑️\n")
# Make it pretty
                print(f"👤 Customer : {order_to_delete['customer_name']}")
                u.t_wait(0.3)
                print(f"🏠 Address  : {order_to_delete['customer_address']}")
                u.t_wait(0.3)
                print(f"📞 Phone    : {order_to_delete['customer_phone']}")
                u.t_wait(0.3)
                print(f"🛵 Courier  : {order_to_delete['courier']}")
                u.t_wait(0.3)
                print(f"🚚 Status   : {order_to_delete['status']}")
                u.t_wait(0.3)
                print(f"📦 Items    : {order_to_delete['items']}")
                u.t_wait(0.3)
                print(f"🕒 Ordered  : {order_to_delete['order_date']}")
                u.t_wait(0.3)
                print(f"💰 Total    : £{float(order_to_delete['total_price']):.2f}\n")
                u.t_wait(0.3)

                confirm = input("⚠️  Really delete this order? (Y/N): ").strip().lower()

                       

                if confirm in ['y', 'yes', '1']:
                    orders_list.pop(index)
                    print(f"\n✅ {order_to_delete['customer_name']}'s Order deleted successfully.")
                    u.save_orders(orders_list)
                
                else:
                    u.clr_scrn()
                    print("\n\n\n\n🚫 Deletion aborted.\n\n\n\n")
                    u.t_wait(2)
                    break

                u.t_wait(2.5)
                again = input("\n\n🗑️ Delete another order? (Y/N): ").strip().lower()
                if again not in ['y', '']:
                    break

        else:
            u.clr_scrn()
            u.invld()
            
            u.t_wait(3)

    return new_orders
