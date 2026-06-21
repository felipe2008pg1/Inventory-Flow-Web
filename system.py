import time
from backend import datos
from backend import tools as to

to.load_data()
to.clear_screen()

to.write_menu("\n📊 INVENTORY MANAGEMENT 📊 ", skip_line=False)
time.sleep(0.4)
to.write_menu("- By @dlv.gonzalezz")

while True:

    to.clear_screen()

    try:
        print(f"\n🕐 | Date: {to.show_time()}")

        menu = int(input("\n1 - View stock \n2 - Add product \n3 - Remove item \n4 - Exit \n CHOOSE: ").strip())

        if menu == 1:
            to.show_inventory()
            input("\nPress ENTER to go back.")

        elif menu == 2:
            product = input("Product name: ").strip().upper()
            price = float(input("Price: ").strip())
            to.add_inventory(product, price)
            time.sleep(1)

        elif menu == 3:
            to.show_inventory()
            to.remove_from_inventory()
            time.sleep(1)

        elif menu == 4:
            to.shutdown()
            break

        else:
            print("Invalid option! Choose between 1 and 4.")
            time.sleep(2)

    except ValueError:
        print("\n[⚠️] ERROR: Enter only integer numbers for menu options. [⚠️]")
        time.sleep(2)
