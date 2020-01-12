import vending

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
    if(bool(input("do you want to end?(True:1 False:0)"))):
        break

vm.save()
