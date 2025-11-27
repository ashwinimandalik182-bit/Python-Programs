student={}
while True:
        
    #Display Menu
    print("\nMenu")
    print("A-Add aStudents")
    print("B-Update marks")
    print("C-Search for a stundent")
    print("D-Display all the stundent and marks")
    print("Q-Quite")

    choice=input("Enter your Choice=").upper()

    if choice=='A':
        name=input("Entr name:")
        marks=int(input("Enter marks:"))
        student[name]=marks
        print(f"{name} Added successfully!")

    elif choice=='B':
        name=input("Enter the Student name to Update=")
        
        if name in student:
                marks=int(input("Enter new marks="))
                student[name]=marks
                print(f"{name}'s Marks Added Successfully!")
        else:
            print("Student Not Found!")

    elif choice=='C':
        name=input("Enter name of students to search=")
        if name in student:
            print(f"{name} has {student[name]} marks")
        else:
            print("Student Not Found")
        
    elif choice=='D':
        if student:
            for name,marks in student.items():
                print(f"{name}:{marks}")
        else:
            print("Student in not found in the record")

    elif choice=='Q':
        print("Exist Program....!")
        break
    else:
        print("Invali choice")