import vending
import os

vm = vending.Vending_Machine()
vm.load()

while(True):
    if(vm.print_whoru()):
        vm.print_user()
    else:
        if(vm.print_admin()):
            vm.imadmin()
        else:
            continue

    end = input("do you want to end?(True:1 False:0)")
    os.system("clear")
    if end=="1":
        break
    else:
        continue

vm.save()
