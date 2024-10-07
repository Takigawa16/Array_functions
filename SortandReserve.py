mix_list = ['3',"apple",'1',"banana",'2',"cherry"]
choice = input("Would you like to sort or reverse the list ? (Enter 'sort' or 'reverese'):")

if choice == 'sort':
    mix_list.sort()
    print(" Sorted List ", mix_list)
elif choice == 'reverse':
    mix_list.reverse()
    print("The Reversed List ", mix_list)
else:
    print("Invalid Choice Please (Enter 'sor' or 'reverese') ")