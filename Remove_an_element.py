
Names = ['Macky', 'Mark Chrisler', 'Harem', 'Benjie', 'Ramon', 'Andrian Philip']


userdata = input("Do you want to clear by name or index? Type: 'name' or 'index': ")


if userdata == "name":
    remove = input("Enter the name you want to remove: ")
    if remove in Names:
        Names.remove(remove)
      


elif userdata == "index":
        remove = int(input("Enter the index you want to remove: "))
        removed_name = Names.pop(remove)
           

else:
    print("Error: Invalid input. Please type 'Name' or 'Index'.")


print("Updated list of names:", Names)