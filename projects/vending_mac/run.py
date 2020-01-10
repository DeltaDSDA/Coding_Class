import vending

vm = vending.Vending_Machine()
while(True):
    if(vm.print_whoru()):
        vm.print_user()
    else:
        if(vm.print_admin()):
            vm.imadmin()
        else:
            continue
