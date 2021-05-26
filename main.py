from random import randrange
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

#define functions
def find_max(gun_class,category):
    max = 17
    if (category == 1):
        if (gun_class == 1): max = 17      # Number of Available Assault Rifles
        elif (gun_class == 2): max = 10    # Number of Available SMGs
        elif (gun_class == 3): max = 8     # Number of Available Shotguns
        elif (gun_class == 4): max = 9     # Number of Available LMGs
        elif (gun_class == 3): max = 8     # Number of Available Marksman
        elif (gun_class == 3): max = 7     # Number of Available Sniper
        elif (gun_class == 3): max = 1     # Number of Available Melee
    else:
        if (gun_class == 1): max = 17      # Number of Pistols
        elif (gun_class == 2): max = 5     # Number of Launchers
        elif (gun_class == 3): max = 4     # Number of Melees

    return max


# code



perk1 = randrange(1,7)
perk1_list = { 1: "Double Time", 2: "E.O.D", 3: "Scavenger", 
               4: "Cold Blood", 5: "Kill Chain", 6:"Quick Fix" }
perk2 = randrange(1,7)
perk2_list = { 1: "Restock", 2: "Hardliner", 3: "Overkill",
               4: "High Alert", 5: "Ghost", 6: "Pointman" }
perk3 = randrange(1,7)
perk3_list = { 1: "Tune Up", 2: "Amped", 3: "Shrapnel",
               4: "Battle Hardened", 5: "Spotter", 6: "Tracker" }

primary = randrange(1,9)
prime_list = { 1: "Claymore", 2: "Frag", 3: "Molotov", 4: "C4", 5: "Semtex", 
               6: "Throwing Knive", 7: "Proximity Mine", 8: "Thermite"}
secondary = randrange (1,9)
sec_list = { 1: "Flash", 2: "Stun", 3: "Smoke", 4: "Snapshot", 
             5: "Heartbeat", 6: "Gas", 7: "Stim", 8: "Decoy" }

nato = { 1: "alpha", 2: "bravo", 3: "charlie", 4: "delta", 5: "echo", 6: "foxtrott", 7: "golf", 8: "hotel", 9: "india", 10: "juliet", 11: "kilo", 12: "lima", 13: "mike", 14: "November", 15: "oscar" , 16: "papa" }

firstgun_class = randrange(1,8)
class1_list = {1: "Assault", 2: "SMG", 3: "Shotgun", 4: "LMG", 5: "Marksman", 6: "Sniper", 7: "Melee"}

max = find_max(firstgun_class, 1)

firstgun = randrange(1,max+1)

if (perk2 == 3):  
    secondgun_class = randrange(1,7)
    max = find_max(secondgun_class,1)
    secondgun = randrange(1,max+1)
    class2_list = class1_list
else:
    secondgun_class = randrange(1,4)
    max = find_max(secondgun_class,2)
    secondgun = randrange(1,max+1)
    class2_list = {1: "Pistol", 2: "Launcher", 3: "Melee"}

# output

print("Welcome to the Loadout chooser")
print()
print("your perks are:",perk1_list[perk1], ",", perk2_list[perk2],",",perk3_list[perk3])
print("your equipment:",prime_list[primary], sec_list[secondary])
print()
print("your first gun is:", class1_list[firstgun_class], nato[firstgun])
print("your second gun is:", class2_list[secondgun_class], nato[secondgun])
