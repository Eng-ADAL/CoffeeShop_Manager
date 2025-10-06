# CoffeeShop - Couriers
# Agile - 4

"""
couriers.py - Implements the Couriers Menu for CoffeeShop Manager CLI.
Handles viewing, adding, updating, and deleting couriers
with CSV persistence and UK‑phone validation.
"""

import utils as u

def couriers_menu(couriers_list: list[str]):
    new_couriers = []
    u.clr_scrn()

    while True:
        u.clr_scrn()
        print("""
--- Couriers Menu ---

1 - View couriers
2 - Add a courier
3 - Update a courier
4 - Delete a courier

0 - Return to Main Menu
              """)

        choice = input("\n\nChoose an option: ").strip()

# 0 - Return to Main Menu
        if choice in ['0', 'o', 'q']:
            u.clr_scrn()
            print("\n\n\n\n🔙 Returning Main Menu\n")
            u.t_wait(1.5)
            break

# 1 - View couriers
        elif choice == "1":
            u.clr_scrn()
            print("\n📋 Courier List:\n")
            u.print_couriers_list(couriers_list)

            input("\n\n\n🔙 Press ⏎ Enter ⏎ for return for Couriers Menu")
            continue

# 2 - Add a courier
        elif choice == "2":
            
            while True:
                u.clr_scrn()
                print("\n🆕➕🛵 Add New Courier \n(input 'l' for see couriers list)")

                name = input("\n\nPlease input new courier Name (Enter for skip): ").strip().title()

                if name.lower() == 'l': # It is not '1' or 'one', it is lower 'L'
                    u.print_couriers_list(couriers_list)
                    input("\nPress ⏎ to return for Add New Courier")
                    continue

                if not name:
                    u.clr_scrn()
                    print("\n\n\n\n Wait... While returning Couriers Menu 🛵💨")
                    u.t_wait(2.5)
                    break
                    
                u.clr_scrn()

                phone = u.valid_uk_phone(couriers_list, label=name)
                if phone is None:
                    break

                #Passed all checks for phone and name!
                new_courier = {"name": name, "phone": phone}
                couriers_list.append(new_courier)
                u.save_couriers(couriers_list)
                print(f"\n\n\n✅ 'New courier added: {new_courier['name']}'\n📞 phone number: {new_courier['phone']}\n")

                again = input("\n➕ Add another? (Y\\N): ").strip().lower()
                if again not in ['y', '']:
                    return


# 3 - Update a courier
        elif choice == "3":
            while True:
                u.clr_scrn()

                print("\n📝 Update a courier 🛵\n")

                u.print_couriers_list(couriers_list)

                selected = input("\n  Select the courier from the list to update \n\n  or Press ⏎ Enter ⏎ to Return Couriers Menu: ")

                if selected.strip().lower() in ['', 'q']:
                    u.clr_scrn()
                    print("\n\n\n\n             Wait... \n\nWhile returning Couriers Menu \n\n             🛵💨\n\n")
                    u.t_wait(2)
                    break
                
                if selected.isdigit():
                    index = int(selected) -1
                    
                    if 0 <= index <= (len(couriers_list) -1):
                        
                        courier = couriers_list[index]

                        while True:
                            u.clr_scrn()
                            print(f"\nUpdating courier: {courier['name']} - {courier['phone']}")

                            old_name = courier['name']
                            old_phone = courier['phone']
                            
                            new_courier = old_name
                            new_phone = old_phone

                            new_name = input("\n✏️ New name (or press ⏎ Enter ⏎ to keep current): ").strip().title()


                            # Name validation 
                            if new_name and new_name.isdigit():
                                print("\nThats looks like a 📞 phone number. This is a name field")
                                confirm = input("\nAre you sure you want to still use it? \n               (Y\\N): ").strip().lower()
                                                    
                                if confirm not in ['y', 'yes', '']:
                                    continue
                                
                            while True:
                                u.clr_scrn()
                                print(f"\nUpdating courier: {courier['name']} - {courier['phone']}")

                                if new_name == '':
                                    print(f"\nName still same: {courier['name']}") 
                                else:
                                    print(f"\nNew name: {new_name}") 

                                new_phone = u.valid_uk_phone(couriers_list, current_entry=courier, label=new_name or courier['name'], is_update = True)

                                changes_made = False

                                if new_name:
                                    courier['name'] = new_name
                                    changes_made = True

                                if new_phone is not None:
                                    courier['phone'] = new_phone
                                    changes_made = True

                                if changes_made:
                                    u.clr_scrn()
                                    print("\n🔄 Update details!\n\n")
                                    print(f"Old Entry  : {old_name:<15}    ' {old_phone:<11} '")
                                    print(f"New Entry  : {new_name or '':<15}    ' {new_phone or '':<11} '")

                                    u.save_couriers(couriers_list)
                                    print(f"\n\n💾 Changes saved to: \n     {u.COURIERS_FILE}")
                                    print("\n✅ Courier updated successfully.")
                                    u.t_wait(2.5)
                                
                                else:
                                    print("\n\n\n\n⚠️ No changes made. ⚠️\n\n\n\n")
                                    u.t_wait(2)
                                    break
                                    
                                again = input("\n\n🆕 Update another courier? \n           🔄 (Y\\N): ").strip().lower()
                                if again not in ['y', 'yes', '']: 
                                    return
                                
                                break # exit number update
                            
                            break # exit name update 

                    else:
                        u.clr_scrn()
                        print("\n\n\n\n⚠️ Selection isn't in list ⚠️\n\n")
                        u.t_wait(2)
                else:
                    u.clr_scrn()
                    print("\n\n\n\n⚠️ Invalid selection ⚠️\n\n")
                    u.t_wait(2)

        
        
# 4 - Delete a courier
        elif choice == "4":
            while True:
                u.clr_scrn()
                print("\n🗑️ Pick a courier from the list to delete\n\n")
                u.print_couriers_list(couriers_list)
                        
                selected = input("\n  Select the courier from the list to delete \n\n or Press ⏎ Enter ⏎ to skip deletion: ").strip()

                if selected.lower() in ["", "q"]:
                    u.clr_scrn()
                    print("\n\n\n       🚫 Deletion cancelled.\n\nWait... Returning Couriers Menu 🛵💨")
                    u.t_wait(2.5)
                    break

                if not selected.isdigit() or not (1 <= int(selected) <= len(couriers_list)):
                    u.clr_scrn()
                    print("\n\n\n\n   ⚠️ Invalid selection ⚠️")
                    u.t_wait(2.5)
                    continue

                u.clr_scrn()
                index = int(selected) -1
                courier_to_delete = couriers_list[index]

                confirm = input(f"""
⚠️ Are you sure you want to delete from list? ⚠️ 
        
        🛵 '{courier_to_delete['name']}' 🛵  
        
            (Y\\N): """).strip().lower()
                
                if confirm in ['y', 'yes', '1']:
                    u.clr_scrn()
                    couriers_list.pop(index)
                    u.save_couriers(couriers_list)
                    print(f"\n\n\n✅ {courier_to_delete['name']} is deleted from courier list 🗑️\n\n Wait... While returning...")
                    u.t_wait(2.5)
                    continue

                else:
                    u.clr_scrn()
                    print("\n\n\n\n               🚫 Deletion aborted.\n\n\n🔙 Wait while returning Couriers Menu... 🛵💨")
                    u.t_wait(2.5)
                continue

        else:
            print("\n⚠️  Invalid input. Please enter 0–4.")
            u.t_wait(2.5)
    return new_couriers

