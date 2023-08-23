Headphone_location = "Drawer"
input("Enter teh location")
Locations=["bed","hall","chair","Drawer","kitchen"]
for i in Locations:
        if i==Headphone_location:
                print("Headphone found in",i)
                break
        else:
                print("Headphone not found in",i)
