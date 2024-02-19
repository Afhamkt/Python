cars = []

while True:
    print("\nMenu:")
    print("1. Add Car")
    print("2. Display Cars by Number of Wheels")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter car name: ")
        price = float(input("Enter car price: "))
        wheels = int(input("Enter number of wheels: "))
        car = [name, price, wheels]
        cars.append(car)
        print("Car added successfully!")
    elif choice == '2':
        num_wheels = int(input("Enter the number of wheels to display cars: "))
        print(f"\nCars with {num_wheels} wheels:")
        found = False
        for car in cars:
            if car[2] == num_wheels:
                print(f"Name: {car[0]}, Price: {car[1]}")
                found = True
        if not found:
            print("No cars found with specified number of wheels.")
    elif choice == '3':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")