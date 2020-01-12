class item(object):
    def __init__(self, name="", num=0, price=0):
        self.name = name
        self.num = num
        self.price = price


class Vending_Machine(object):
    def __init__(self):
        self.menu = []
        self.money = [0,0,0,0,0]
        self.admin = "admin"
    
    def save(self):
        f = open("data.txt", 'w')
        f.write(str(len(self.menu))+"\n")
        for i in range(len(self.menu)):
            f.write(self.menu[i].name+"\n")
            f.write(str(self.menu[i].num)+"\n")
            f.write(str(self.menu[i].price)+"\n")
        for i in range(len(self.money)):
            f.write(str(self.money[i])+"\n")
        f.close()

    def load(self):
        f = open("data.txt", 'r')
        num = int(f.readline())
        for i in range(num):
            self.menu.append(item(f.readline()[:-1],int(f.readline()),int(f.readline())))
        for i in range(5):
            self.money[i] = int(f.readline())
        f.close()

    def print_whoru(self):
        answer=""
        answer=input("user OR admin? ")
        if(answer=="user"):
            return True
        else:
            return False

    def print_user(self): 
        for i in range(len(self.menu)):
            print(i+1,". ", self.menu[i].name," ", self.menu[i].price)
        answer=int(input("select menu : "))
        print("Price: ", self.menu[answer-1].price," Put money")
        
        money=[10000, 5000, 1000, 500, 100]
        
        tot=0
        for i in range(len(money)):
            print(money[i])
            don=int(input())
            tot=tot+money[i]*don
            self.money[i]=self.money[i]+don

        re = tot

        if (tot >= self.menu[answer-1].price):
            tot = tot - self.menu[answer-1].price
            print("Charge : ")
            for i in range(len(money)):
                if tot>=money[i]:
                    num=min(tot//money[i],self.money[i])
                    tot=tot-num*money[i]
                    self.money[i]=self.money[i]-num
                    print(money[i], " : ", num)
                    
        elif (tot<self.menu[answer-1].price):
            print(self.menu[answer-1].price-tot, " need. Put more money")
            ltot = tot
            for i in range(len(money)):
                print(money[i])
                don=int(input())
                ltot=ltot+money[i]*don
                self.money[i]=self.money[i]+don
            re = ltot

            if ltot>=self.menu[answer-1].price:
                ltot = ltot - self.menu[answer-1].price
                print("Charge : ")
                for i in range(len(money)):
                    if ltot>=money[i]:
                        num=min(ltot//money[i],self.money[i])
                        ltot=ltot-num*money[i]
                        self.money[i]=self.money[i]-num
                        print(money[i], " : ", num)

            elif ltot<self.menu[answer-1].price:
                print("Bye")
                print("Charge: ")
                for i in range(len(money)):
                    if re>=money[i]:
                        num=min(re//money[i], self.money[i])
                        re=re-num*money[i]
                        self.money[i]=self.money[i]-num
                        print(money[i], " : ", num)
                print("All returned")


    def print_admin(self):
        answer=input("Please enter Administrator Password : ")
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
        choose=int(input())
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
        print("What menu do you want to add?")
        self.menu.append(item(input("name"), int(input("num")), int(input("price"))))

    def Del_Menu(self):
        print("What menu do you want to delete?")
        for i in range(len(self.menu)):
            print(i+1,". ", self.menu[i].name)
        choose=int(input())
        self.menu.pop(choose-1)

    def Add_Stock(self):
        print("What menu stock do you want to add?")
        for i in range(len(self.menu)):
            print(i+1,". ", self.menu[i].name," ", self.menu[i].num)
        choose=int(input())
        stock=int(input())
        self.menu[choose-1].num=self.menu[choose-1].num+stock


    def Put_Money(self):
        money=["10000", "5000", "1000", "500", "100"]
        for i in range(len(money)):
            print(money[i]," ",self.money[i])
        for i in range(len(money)):
            print(money[i])
            don=int(input())
            self.money[i]=self.money[i]+don

    def Check_Money(self):
        money=["10000","5000","1000","500","100"]
        don=0
        for i in range(len(money)):
            print(money[i], self.money[i])
            don=don+int(money[i])*self.money[i]
        print(don)
