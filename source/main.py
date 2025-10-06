# CoffeeShop - Main 
# Agile - 4

"""
main.py – Entry point for CoffeeShop Manager CLI.
Loads product, courier, and order data, then presents
the Main Menu until the user decides to exit.
"""

import products as p
import orders   as o
import couriers as c
import utils    as u

# Loading databases
try:
    products_list = u.load_products()
except Exception as e:
    print(f"⚠️ Failed to load products file: {e}")
    products_list = []

try:
    orders_list = u.load_orders()
except Exception as e:
    print(f"⚠️ Failed to load orders file: {e}")
    orders_list = []

try:
    couriers_list = u.load_couriers()
except Exception as e:
    print(f"⚠️ Failed to load couriers file: {e}")
    couriers_list = []

u.clr_scrn()

def main_menu():
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
▓▓                 _______ _______ _______ _______ _______ _______ ______                 ▓▓
▓▓     ______     |   |   |   _   |    |  |   _   |     __|    ___|   __ \     ______     ▓▓
▓▓    |______|    |       |       |       |       |    |  |    ___|      <    |______|    ▓▓
▓▓                |__|_|__|___|___|__|____|___|___|_______|_______|___|__|                ▓▓
▓▓                                                                                        ▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓                                                                                        ▓▓
▓▓                                   === Main Menu ===                                    ▓▓
▓▓                                                                                        ▓▓
▓▓                                   1 - Products Menu                                    ▓▓
▓▓                                   2 - Orders Menu                                      ▓▓
▓▓                                   3 - Couriers Menu                                    ▓▓
▓▓                                                                                        ▓▓
▓▓                                   0 - Exit App                                         ▓▓
▓▓                                                                                        ▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

                """)
          
          choice = input("Choose an option: ")

# 0 - Exit App

          if choice in ['0', 'q']:
               u.clr_scrn()
               are_you = input("\n\n\n            Really! Quit⁉️ \n\n                (Y\\N)\n                  ").lower().strip()
               if are_you == 'y':
                    u.clr_scrn()
                    print('\n\n\n       Exiting App.. 😢 \n\n       See you next time!\n\n')
                    
                    # Before exit make persisten products, orders and couriers data with validation
                    u.save_products(products_list)
                    u.save_orders(orders_list)
                    u.save_couriers(couriers_list)                    
                    exit()
               else:
                    continue
          

# 1 - Products Menu

          elif choice == '1':
               u.clr_scrn()
               p.products_menu(products_list)

# 2 - Orders Menu

          elif choice == '2':
               u.clr_scrn()
               o.orders_menu(orders_list,products_list,couriers_list)


# 3 - Couriers Menu

          elif choice == '3':
               u.clr_scrn()
               c.couriers_menu(couriers_list)

          else:
               u.clr_scrn()
               print("\n\n\n\n           ⚠️  Invalid input.   ⚠️\n\n\n\n")
               u.t_wait(2)
               


# Greeting Screeen 
if __name__ == "__main__":
     try:
          u.clr_scrn()
          print("""
                

                
                Welcome  CoffeeShop Manager!
                
                

                """) 
          u.wot(f"\n                Press Enter to START...\n", 5)    # Auto time out
          main_menu()

# Error handling 
     except KeyboardInterrupt:
          u.clr_scrn()
          print("\n\n\n\n❌ Program interrupted by user 🙄 \n\n        Goodbye! 👋\n\n\n")
          exit()

     try:
          main_menu()
     except Exception as e:
          print(f"\n🚨 Congrats! Unexpected error find!: {e}")
          exit()



#     === Main Menu ===   
#     1 - Products Menu   
#     2 - Orders Menu     
#     3 - Couriers Menu   
#     0 - Exit App        