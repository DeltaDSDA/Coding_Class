class item(object):
    def __init__(self, name="", num=0, price=0):
        self.name = name
        self.num = num
        self.price = price


class Vending_Machine(object):
    def __init__(self):
        self.menu = []
        self.money = [0,0,0,0,0,0]
        self.admin = "admin"

    def print_whoru(self):
        answer=""
        answer=input("user OR admin")
        if(answer=="user"):
            return True
        else:
            return False

    def print_user(self):
        print(self.menu)
        answer=input("select menu")

    def print_admin(self):
        answer=input("Please enter Administrator Password")
        if(answer==self.admin):
            return True
        else:
            print("Password wrong")
            return False

    def imadmin(self):
        print("What do you want to do")
        print("1.Add Menu")
        print("2.Delete Menu")
        print("3.Add Stock")
        print("4.Put Money")
        print("5.Check Money")
        choose=input()
        if(choose==1):
            self.Add_Menu()
        elif(choose==2):
            self.Del_Menu()
        elif(choose==3):
            self.Add_Stock()
        elif(choose==4):
            self.Put_Money()
        elif(choose==5):
            self.Check_Money()

    def Add_Menu(self):
        self.menu.append(item(input("name"), int(input("num")), int(input("price"))))

    def Del_Menu(self):
        self.menu.pop

    def Add_Stock(self):

    def Put_Money(self):

    def Check_Money(self):




        
    

    
