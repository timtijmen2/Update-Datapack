import os
import os.path
import io
import time

print()
print("It is recommended that you make a backup of your packs before updating")
while True:
    print("Do you wish to continue?")
    a = input("[Y/N] ")

    if a.lower() == "y":
        break
    elif a.lower() == "n":
        exit()



def commandreplaceitem(line):
    startcommand = line.find("replaceitem")
    slots = ['armor.head', 'armor.chest', 'armor.legs', 'armor.feet', 'weapon', 'weapon.mainhand', 'weapon.offhand', 'villager.0', 'villager.1', 'villager.2', 'villager.3', 'villager.4', 'villager.5', 'villager.6', 'villager.7', 'villager.8', 'villager.9', 'villager.10', 'villager.11', 'villager.12', 'villager.13', 'villager.14', 'inventory.0', 'inventory.1', 'inventory.2', 'inventory.3', 'inventory.4', 'inventory.5', 'inventory.6', 'inventory.7', 'inventory.8', 'inventory.9', 'inventory.10', 'inventory.11', 'inventory.12', 'inventory.13', 'inventory.14', 'inventory.15', 'inventory.16', 'inventory.17', 'inventory.18', 'inventory.19', 'inventory.20', 'inventory.21', 'inventory.22', 'inventory.23', 'inventory.24', 'inventory.25', 'inventory.26', 'horse.0', 'horse.1', 'horse.2', 'horse.3', 'horse.4', 'horse.5', 'horse.6', 'horse.7', 'horse.8', 'horse.9', 'horse.10', 'horse.11', 'horse.12', 'horse.13', 'horse.14', 'horse.armor', 'horse.chest', 'horse.saddle', 'enderchest.0', 'enderchest.1', 'enderchest.2', 'enderchest.3', 'enderchest.4', 'enderchest.5', 'enderchest.6', 'enderchest.7', 'enderchest.8', 'enderchest.9', 'enderchest.10', 'enderchest.11', 'enderchest.12', 'enderchest.13', 'enderchest.14', 'enderchest.15', 'enderchest.16', 'enderchest.17', 'enderchest.18', 'enderchest.19', 'enderchest.20', 'enderchest.21', 'enderchest.22', 'enderchest.23', 'enderchest.24', 'enderchest.25', 'enderchest.26', 'container.0', 'container.1', 'container.2', 'container.3', 'container.4', 'container.5', 'container.6', 'container.7', 'container.8', 'container.9', 'container.10', 'container.11', 'container.12', 'container.13', 'container.14', 'container.15', 'container.16', 'container.17', 'container.18', 'container.19', 'container.20', 'container.21', 'container.22', 'container.23', 'container.24', 'container.25', 'container.26', 'container.27', 'container.28', 'container.29', 'container.30', 'container.31', 'container.32', 'container.33', 'container.34', 'container.35', 'container.36', 'container.37', 'container.38', 'container.39', 'container.40', 'container.41', 'container.42', 'container.43', 'container.44', 'container.45', 'container.46', 'container.47', 'container.48', 'container.49', 'container.50', 'container.51', 'container.52', 'container.53']
    
    if not startcommand == -1:
        detect1 = startcommand
        detect2 = line.find(" ", detect1)
        line = line[:detect1] + "item" + line[detect2:]
        for x in slots:
            detect2 = line.find(x, detect1)
            if not detect2 == -1:
                detect1 = line.find(" ", detect2)
                
                command = line[:detect1] + " replace" + line[detect1:]
                return command
    else:
        
        return line


print("\n")
print("Starting Updating...")
time.sleep(5)
updatefilename = "updatefilefunction.txt"
for dirpath, dirnames, filenames in os.walk("."):
    updatefile = open(updatefilename, "w")
    for filename in [f for f in filenames if f.endswith(".mcfunction")]:
        function = os.path.join(dirpath, filename)
        function = function[2:]
        File = open(function, "r")
        updatefile = open(updatefilename, "w")
        
        for line in File:
            readline = line
            if not readline == "":
                newline = commandreplaceitem(readline)
                updatefile.write(newline) 
                
      
        else:            
            updatefile.close()
            File.close()
            updatefile = open(updatefilename, "r")
            File = open(function, "w")
            for line in updatefile:         
                File.write(line)
            else:
                print("Updated: " + File.name)
else:
    updatefile.close()
    os.remove(updatefilename)
    print("\n")
    print("All Functions have been Updated")
    time.sleep(10)

        
