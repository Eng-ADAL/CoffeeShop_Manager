# CoffeeShop - Products  
# Agile - 4


"""
products.py – Implements the Products Menu for CoffeeShop Manager CLI.
Handles viewing, creating, updating, and deleting products,
with CSV persistence and input validation.
"""

import utils as u

def products_menu(products_list):
    new_products = []
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
▓▓                              --- Products Menu ---                                     ▓▓
▓▓                                                                                        ▓▓
▓▓                                                                                        ▓▓
▓▓                              1 - Print Products List                                   ▓▓
▓▓                              2 - Create New Product                                    ▓▓
▓▓                              3 - Update Existing Product                               ▓▓
▓▓                              4 - Delete Product                                        ▓▓
▓▓                                                                                        ▓▓
▓▓                              0 - Return to Main Menu                                   ▓▓
▓▓                                                                                        ▓▓
▓▓                                                                                        ▓▓
▓▓                                                                                        ▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
              """)
        choice = input("                                Choose an option: ").strip().lower()

# 0 - Return to Main Menu
        if choice in ['0', 'o', 'q']:
            u.clr_scrn()
            u.rtm()
            print("                                   🔙 Returning Main Menu 🔙")
            u.t_wait(1.5)
            break   

# 1 - Print Products List         
        elif choice == "1":
            u.clr_scrn()
            products_list[:] = u.load_products()
            
            print("\n📋 Product List:")
            u.print_products_list(products_list)
            input("\n\n\n🔙 Press ⏎ Enter ⏎ for return for Product Menu\n")
            continue

# 2 - Create New Product
        elif choice == "2":
            new_products = []
            while True:
                u.clr_scrn()
                products_list[:] = u.load_products()
                
                print("\n➕ Add a New Product \n(input 'l' for see product list)")
                name = input("\n\n📋  Enter product name >\n(⏎ Enter ⏎ for return) >> ").strip().title()
             
                cancelled = False

                if name.lower() in ['', 'q']:
                    u.clr_scrn()
                    print("\n\n\n\n         📋 Returning to Products Menu...\n\n\n\n") 
                    u.t_wait(2)
                    break

                if name.lower() == 'l': # It is not '1' or 'one', it is lower 'L'
                    u.print_products_list(products_list)
                    input("\nPress ⏎ to return for add product")
                    continue

                if any(p["name"] == name for p in products_list):
                    u.clr_scrn()
                    print(f"\n\n\n\n⛔ '{name}' is already on the menu! ⛔\n\n\n\n")
                    u.t_wait(2)
                    continue

                while True:
                    u.clr_scrn()
                    price_str = input(f"\n📋 Input '{name}' price >\n   (⏎ Enter ⏎ for return)  >> £").strip()

                    if not price_str:
                        u.clr_scrn()
                        print("\n\n\n\n 🔙 Returning Products Menu \n\n\n") 
                        cancelled = True
                        u.t_wait(2.5)
                        break

                    try:
                        price = float(price_str)
                        if price < 0:
                            raise ValueError
                        break
                    except ValueError:
                        u.clr_scrn()
                        print("\n\n\n\n⚠️ In our world, price must be a positve number.\n\n\n\n")
                        u.t_wait(2)
                        u.clr_scrn()
                
                if cancelled:
                    break

                new_product = {"name": name, "price": price}
                products_list.append(new_product)
                new_products.append(new_product)    # sesion tracking

                u.clr_scrn()
                print(f"\n\n\n\n✅ You added '{new_product['name']}' for £{new_product['price']:.2f} to the menu!\n\n\n\n")
                u.save_products(products_list)
                u.t_wait(2)
                u.clr_scrn()

                print("\n\n\n\n🆕 Products added this session:\n")
                for prod in new_products:
                    print(f" - {prod['name']:<15} £{prod['price']:<4.2f}")
                
                u.t_wait(2)

                again = input("\n\n\n\n➕ Add another product? (Y\\N): ").strip().lower()
                if again != 'y':
                    break

# 3 - Update Existing Product
        elif choice == "3":
            u.clr_scrn()
            
            while True:
                u.clr_scrn()
                products_list[:] = u.load_products()

                print("\n📝 Update a Product\n")
                u.print_products_list(products_list)

                selected_item = input("\n🔁 Please Enter product number to update \n         (or Press ⏎ Enter ⏎ to return) : ").strip()

                if selected_item.lower() in ["", 'q']:
                    u.clr_scrn()
                    print("\n\n\n\n         📋 Returning to Products Menu...\n\n\n\n")
                    u.t_wait(2.5)
                    break

                if not selected_item.isdigit() or not (1 <= int(selected_item) < (len(products_list) + 1)):
                    print("\n⚠️ Whoops! That's not in our list! Try again!\n")
                    u.t_wait(2.5)
                    continue

                product = products_list[(int(selected_item) -1)]
                old_name, old_price = product['name'], product['price']
                
                u.clr_scrn()
                new_name = input(f"\n🆕 Type the new name for             > '{old_name}'\n(or Press ⏎ Enter ⏎ to keep it same) >> ").title().strip()

                if new_name == '':
                    print(f"\nNo changes made, Name still same: {old_name}!")
                    new_name = old_name

                elif any(p["name"] == new_name for p in products_list if p != product):
                    u.clr_scrn()
                    print(f"\n\n\n\n⛔  This product already exists! ⛔\n\n\n\n")
                    u.t_wait(2)
                    continue
                
                else:
                    product["name"] = new_name
                    print(f"\n '{old_name}' updated as '{new_name}' ✅")
                    
                new_price_input = input(f"\n💴 Type the new price for '{new_name}' old price is > £{old_price:.2f}\n               (or Press ⏎ Enter ⏎ to keep it) >> £").strip()


                if new_price_input == "":
                    u.clr_scrn()
                    new_price = old_price
                    print(f"\n\n🔁Product Updated🔁!!!\n")
                    print(f"Old Entry  : {old_name:<15}    ' £{old_price:<4.2f} '")
                    print(f"New Entry  : {new_name:<15}    ' £{float(new_price):<4.2f} ' 💴")

                else:
                    try:
                        new_price = float(new_price_input)
                        if new_price < 0:
                            raise ValueError
                    except ValueError:
                        print("\n⚠️ Invalid. Price should be a non-negative number. Try again.")
                        u.t_wait(2.5)
                        continue

                    else:
                        u.clr_scrn()
                        product['price'] = new_price
                        print(f"\n🔁Product Updated🔁!!!\n")
                        print(f"Old Entry  : {old_name:<15}    ' £{old_price:<4.2f} '")
                        print(f"New Entry  : {new_name:<15}    ' £{float(new_price):<4.2f} ' 💴")
                
                u.save_products(products_list)

                again = input("\n🔁 Update another product? (Y\\N): ").strip().lower()
                if again != 'y':
                    break
            

# 4 - Delete Product
        elif choice == "4":
            u.clr_scrn()
            while True:
                u.clr_scrn()
                products_list[:] = u.load_products()

                print(" 🗑️🧹🧽 Select product to delete: ")
                u.print_products_list(products_list)

                selected_item = input("\n 🗑️  Please Enter product number to delete (or Press ⏎ Enter ⏎ return): ").strip()
                
                if selected_item in ["", "q"]:
                    u.clr_scrn()
                    print("\n\n\n\n         📋 Returning to Products Menu...\n\n\n\n")
                    u.t_wait(2.5)
                    break
                
                if not selected_item.isdigit() or not (1 <= int(selected_item) < (len(products_list) + 1) ):
                    print("\n⚠️ Whoops! That's not in our list! Try again!\n")
                    u.t_wait(2.5)
                    continue

                index = int(selected_item) -1
                product_to_del = products_list[index]
                deleted_product = product_to_del['name']
                
                u.clr_scrn()
                confirm = input(
    f"""
\n\n\n
❓  Are you sure you want to delete this product from the list? ❓

                >>  '{deleted_product.upper()}'  <<

‼️  This action cannot be undone! Think twice! ‼️

                  (Y/N): """
).strip().lower()
                
                if confirm in ['y' , 'yes', 'evet']:
                    products_list.pop(index)
                    u.save_products(products_list)
                    u.clr_scrn()
                    print(f"\n\n\n\n✅ '{deleted_product}' has been deleted. 🗑️")
                    u.t_wait(1.5)

                else:
                    u.clr_scrn()
                    print(f"\n\n\n\n❌ '{deleted_product}' was not deleted.")
                    u.t_wait(2)

                again = input("\n\n🗑️ Delete another product? (Y/N): ").strip().lower()
                if again not in ['y', '']:
                    break
                
        else:
            u.clr_scrn()
            u.invld()
            print("\n                                ⚠️ Invalid input. ⚠️")
            u.t_wait(2)
    
    return new_products
