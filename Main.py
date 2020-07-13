
import datetime
print("HEALTH MANAGEMENT SYSTEM!!!")
currentdate=datetime.datetime.now()

def userselect():
    print("Whose update you want??")
    admin=int(input("1: Shree 2: Sajana ->"))
    return admin

def clients(clientname):
    if clientname==1:
        print("Select the option")
        choose=int(input("1: Diet 2: Exercise ->"))
        if choose==1:
            with open("Shree_food.txt", "r+") as shreediet:
                print("Recommendation till date:\n", shreediet.read())
                print("Provide your today's suggestion below.")
                suggestion=input("->")
                global currentdate
                shreediet.write(str([str(currentdate.strftime("%A, %B %d, %Y, %H:%M:%S"))])+ ":\t" + suggestion+"\n")
                username = shreediet.name.split("_")
                finalname = username[0]
                print(f"Recommendation has been sent to {finalname} successfully ")

        elif choose==2:
            with open("Shree_exercise.txt", "r+") as shreeexercise:
                print("Recommendation till date:\n", shreeexercise.read())
                print("Provide your today's suggestion below.")
                suggestion=input("->")
                # global currentdate
                shreeexercise.write(str([str(currentdate.strftime("%A, %B %d, %Y, %H:%M:%S"))])+ ":\t" + suggestion+"\n")
                username = shreeexercise.name.split("_")
                finalname = username[0]
                print(f"Recommendation has been sent to {finalname} successfully ")

        else:
            print("Invalid Input. Please select the option carefully.")
            clients(clientname)
    elif clientname ==2:
        print("Select the option")
        choose = int(input("1: Diet 2: Exercise ->"))
        if choose == 1:
            with open("Sajana_food.txt", "r+") as sajanadiet:
                print("Recommendation till date:\n", sajanadiet.read())
                print("Provide your today's suggestion below.")
                suggestion = input("->")
                # global currentdate
                sajanadiet.write(str(currentdate.strftime("%A, %B %d, %Y, %H:%M:%S")) + ":\t" + suggestion + "\n")
                username = sajanadiet.name.split("_")
                finalname = username[0]
                print(f"Recommendation has been sent to {finalname} successfully ")
        elif choose == 2:
            with open("Sajana_exercise.txt", "r+") as sajanaexercise:
                print("Recommendation till date:\n", sajanaexercise.read())
                print("Provide your today's suggestion below.")
                suggestion = input("->")
                # global currentdate
                sajanaexercise.write(str([str(currentdate.strftime("%A, %B %d, %Y, %H:%M:%S"))])+ ":\t" + suggestion+"\n")
                username=sajanaexercise.name.split("_")
                finalname=username[0]
                print(f"Recommendation has been sent to {finalname} successfully ")
        else:
            print("Invalid Input. Please select the option carefully.")
            clients(clientname)
    else:
        print("\nSelect the client name carefully. For now we only have 2 clients")
        userselect()

if __name__=='__main__':
    selectedclient=userselect()
    clients(selectedclient)


