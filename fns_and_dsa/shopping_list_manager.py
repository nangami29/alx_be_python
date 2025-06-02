def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            add_item=input("Enter the item to add: ")
            shopping_list.append(add_item)
            print(f"{add_item} added to shoppping list.")
            pass
        elif choice == '2':
            # Prompt for and remove an item
            removed_item = input("Enter the item to remove: ")
            if removed_item in shopping_list:
                shopping_list.remove(removed_item)
                print(f"'{removed_item}' removed from shopping list")
            else:
                 print("Item not found in shopping list.")
            pass
        elif choice == '3':
            # Display the shopping list
            print("shopping_list:\n")
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()





            

            
            
            
            
           
            
   