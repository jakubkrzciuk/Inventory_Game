import sys
import csv
from collections import Counter

def drago():
    print('\n''\n' "YOU KILL A DRAGON !!")
    print("""                                                         _____------------___
                                                    ._--':::::'-------____
                .___------__       /-.._.    _---_ '|:::::::::::::::::::::---
           ._--'.---::::::/ `      \ .-. '-'' *__*|/:::::::::::::::::::::::::
      .__-'  _-'::::::::/ ._------_| '_'  __--' _'/::::::::::::::::::::::::::
  _--'    _-'::::::::::|.'  ._----_\    -'  ._-':::::::::::::::::::::::::::::
       _-':::::::::::::\  .'       /  .__--' -':::::::::_--_:::::::::::.-----
   _-'::::::::::::::::::-_|       /    /   /::::::::::/      \:::::::/
  '::::::::::::::::::::::::----__-   .   .  |.--_:::/          \:::/
 .----_::::::::::::::::::::/                \  \\ \/             \/
| ._.-_'-_:::.----.:::.:. . .    .         . |  \\
 -_. -.\  \ .-.----..-----. .----. .---. .-.----:|\\
  | | | |  | | .-. ||._-  || .-. || .-. | | .-. |\|
 .| |/__/  / | |  - .'.-. || '_' || | | | | | | |
|       ._- .| |.   | '-' |'___. || '_' |.| |.| |.
 -------    '---'    '----:--._| | '---' '---'---'
                          '______'.----_
                                  | ._.-_'-_
                                   -_. -.\  \ .-----. ----..---------.-.----.
                                    | | | |  ||._-  |  \  \\'/ \\'\  /  | .-. |
                                   .| |/__/  /.'.-. |   \  ' . '' /   | | | |
                                  |       ._- | '-' |    \  / \  /   .| |.| |.
                                   -------     '----'     ''   ''    '---'---'
                                   """)
def print_table(inventory, order):   #   Print inventory.
    n = max(len(key) for key in inventory)
    m = max(len(str(value)) for value in inventory.values())
    if m < 7:
        m = 7
    print ("count".rjust(m),"item name".rjust(n+3))
    print ("-"*(n+m+4))
    if order == ("count,desc"):
        for key, value in sorted(inventory.items(), key = lambda i: i[1], reverse = True):
            print (str(inventory[key]).rjust(m), key.rjust(n+3))
    elif order == ("count,asc"):
        for key, value in sorted(inventory.items(), key = lambda i: i[1]):
            print (str(inventory[key]).rjust(m), key.rjust(n+3))
    else:
        for key, value in inventory.items():
            print (str(inventory[key]).rjust(m), key.rjust(n+3))
    print ("-"*(n+m+4))

def loot(items):   #   Loot from dragon.
    print("loot = ",items)

def import_inventory(inventory, filename):   #   Import inventory from file.
    with open(filename , "r") as invent:
        next(invent)
        import_loot = dict(filter(None, csv.reader(invent)))
        import_loot2 = dict((k,int(v)) for k,v in import_loot.items())
    return Counter(inventory) + Counter (import_loot2)


def add_to_inventory(inventory, items): #   Add to Inventory.
    for i in items:
        inventory[i]=inventory.get(i,0)+1
    display_inventory(inventory)

def display_inventory(inventory): #  Display inventory.
    lista=inventory.values()
    itm=inventory.keys()
    print("inventory : ")
    for itm,lista in inventory.items():
        print(lista , itm)
    print("Total number of items:",sum(inventory.values()))

def export_inventory(inventory, filename):  #   Export inventory to file .
    with open(filename, "w") as csv_file:
        writer = csv.writer(csv_file)
        for key, value in inventory.items():
            writer.writerow([key, value])

def main():  #MY main-general function.
    dict={}
    inventory={"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}
    items=["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
    display_inventory(inventory)
    input("\n""Press any Key : ")
    drago()
    loot(items)
    input("\n""\n""Press any key to add loot to your inventory"'\n')
    add_to_inventory(inventory,items)
    import_inventory(inventory,"inventory.csv")
    order=sys.argv
    input("\n""Press any Key : ")
    print_table(inventory, order)
    export_inventory(inventory,"inventory.csv")
main()
