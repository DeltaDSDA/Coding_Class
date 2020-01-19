# Coding_Class

## 1. Python_Codes

### 1.1. BOJ(Baekjoon Online Judge) Problem Solving
We solve 2 problems at BOJ everyday.

<br>

### 1.2. Test codes
There are such test codes for testing python code.

## 2. Projects

### 1.1. Vending_Machine
The first project of us.
In vending_mac directory, there are 2 code files and 1 text file.

> ### 1.1.1. vending.py
> It has class called Vending_Machine and item.

> ### 1.1.2. run.py
> We made main function for vending machine

```
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
```
