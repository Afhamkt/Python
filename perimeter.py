while True:
    print("1.Calculate perimeter of circle" )
    print("2.Calculate perimeter of rectangle")
    print("3.Calculate perimeter of square")
    print("4. Exit program")
    choice=int(input("Enter the operation you want to perform"))
    if choice==1:
        radius=int(input("Enter the radius"))
        perimeter=2*3.14*radius
        print(perimeter)
    elif choice==2:
        length=int(input("Enter the length"))
        breadth=int(input("Enter the breadth"))
        perimeter=2*(length+breadth)
        print(perimeter)
    elif choice==3:
        side=int(input("Enter the side"))
        perimeter=4*side
        print(perimeter)
    elif choice==4:
        print("Thanks for using!")
        break


