import Joven_script_2_ev  as ec
import Joven_script_1_stat as sc

print("1. Stat Calc")
print("2. EV Calc")

Pokemon_Nature_Attack = 1
Pokemon_Nature_Defense = 1
Pokemon_Nature_SPAttack = 1
Pokemon_Nature_SPDefense = 1
Pokemon_Nature_Speed = 1

choice = int(input("Enter: "))


if choice == 1:
    print("Stats")

    Pokemon = str(input("Enter Pokemon: "))

    Pokemon_Level = int(input("Enter Pokemon level: "))

    Pokemon_Nature = str.lower(input("Enter Pokemon's Nature: "))

    Pokemon_Base = int(input("Enter Pokemon's Base: "))

    Pokemon_IV = int(input("Enter Pokemn's IV: "))

    Pokemon_EV = int(input("Enter Pokemon's EV: "))

    #Pokemon Neutral Nature
    if Pokemon_Nature in ['quirky','bashful','serious','docile','hardy']:
        Pokemon_Nature_Attack = 1
        Pokemon_Nature_Defense = 1
        Pokemon_Nature_SPAttack = 1
        Pokemon_Nature_SPDefense = 1
        Pokemon_Nature_Speed = 1
    #Pokemon Attack Nature
    elif Pokemon_Nature in ['lonely','brave','adamant','naughty']:
        Pokemon_Nature_Attack = 1.1
        if Pokemon_Nature in ['lonely']:
            Pokemon_Nature_Defense = 0.9
        elif Pokemon_Nature in ['brave']:
            Pokemon_Nature_Speed = 0.9
        elif Pokemon_Nature in ['adamant']:
            Pokemon_Nature_SPAttack = 0.9
        elif Pokemon_Nature in ['naughty']:
            Pokemon_Nature_SPDefense = 0.9
    #Pokemon Defense Nature
    elif Pokemon_Nature in ['bold','relaxed','impish','lax']:
        Pokemon_Nature_Defense = 1.1
        if Pokemon_Nature in ['bold']:
            Pokemon_Nature_Attack = 0.9
        elif Pokemon_Nature in ['relaxed']:
            Pokemon_Nature_Speed = 0.9
        elif Pokemon_Nature in ['impish']:
            Pokemon_Nature_SPAttack = 0.9
        elif Pokemon_Nature in ['lax']:
            Pokemon_Nature_SPDefense = 0.9
    #Pokemon Speed Nature
    elif Pokemon_Nature in ['timid','hasty','jolly','naive']:
        Pokemon_Nature_Speed = 1.1
        if Pokemon_Nature in ['timid']:
            Pokemon_Nature_Attack = 0.9
        elif Pokemon_Nature in ['hasty']:
            Pokemon_Nature_Defense = 0.9
        elif Pokemon_Nature in ['jolly']:
            Pokemon_Nature_SPAttack = 0.9
        elif Pokemon_Nature in ['naive']:
            Pokemon_Nature_SPDefense = 0.9
    #Pokemon Special Attack Nature
    elif Pokemon_Nature in ['modest','mild','quiet','rash']:
        Pokemon_Nature_SPAttack = 1.1
        if Pokemon_Nature in ['modest']:
            Pokemon_Nature_Attack = 0.9
        elif Pokemon_Nature in ['mild']:
            Pokemon_Nature_Defense = 0.9
        elif Pokemon_Nature in ['quiet']:
            Pokemon_Nature_Speed = 0.9
        elif Pokemon_Nature in ['rash']:
            Pokemon_Nature_SPDefense = 0.9
    #Pokemon Special Defense Nature
    elif Pokemon_Nature in ['calm','gentle','sassy','careful']:
        Pokemon_Nature_SPDefense = 1.1
        if Pokemon_Nature in ['calm']:
            Pokemon_Nature_Attack = 0.9
        elif Pokemon_Nature in ['gentle']:
            Pokemon_Nature_Defense = 0.9
        elif Pokemon_Nature in ['sassy']:
            Pokemon_Nature_Speed = 0.9
        elif Pokemon_Nature in ['careful']:
            Pokemon_Nature_SPAttack = 0.9
    
    print("1. HP")
    print("2. Attack")
    print("3. Defense")
    print("4. Special Attack")
    print("5. Special Defense")
    print("6. Speed")
    
    opt = int(input("Enter: "))

    if opt == 1:
        Pokemon_Base_HP = int(input("Enter Base HP: "))
        Pokemon_Iv = int(input("Enter IV: "))
        Pokemon_Ev = int(input("Enter EV: "))
        print("Total HP: ", sc.Stat_Calc.Stat_Calc_HP(Pokemon_Base_HP,Pokemon_Iv,Pokemon_Ev,Pokemon_Level),"\n")
    if opt == 2:
        Pokemon_Base_Attack = int(input("Enter Base Attack Points: "))
        Pokemon_Iv = int(input("Enter IV: "))
        Pokemon_Ev = int(input("Enter EV: "))
        print("Total Attack Points: ", sc.Stat_Calc.Other_Stat_Attack(Pokemon_Base_Attack,Pokemon_Iv,Pokemon_Ev,Pokemon_Level,Pokemon_Nature_Attack),"\n")
    if opt == 3:
        Pokemon_Base_Defense = int(input("Enter Base Defense Points: "))
        Pokemon_Iv = int(input("Enter IV: "))
        Pokemon_Ev = int(input("Enter EV: "))
        print("Total Defense Points: ", sc.Stat_Calc.Other_Stat_Defense(Pokemon_Base_Defense,Pokemon_Iv,Pokemon_Ev,Pokemon_Level,Pokemon_Nature_Defense),"\n")    
    if opt == 4:
        Pokemon_Base_SPAttack = int(input("Enter Base Special Attack Points: "))
        Pokemon_Iv = int(input("Enter IV: "))
        Pokemon_Ev = int(input("Enter EV: "))
        print("Total Special Attack Points: ", sc.Stat_Calc.Other_Stat_SPAttack(Pokemon_Base_SPAttack,Pokemon_Iv,Pokemon_Ev,Pokemon_Level,Pokemon_Nature_SPAttack),"\n")
    if opt == 5:
        Pokemon_Base_SPDefense = int(input("Enter Base Special Defense Points: "))
        Pokemon_Iv = int(input("Enter IV: "))
        Pokemon_Ev = int(input("Enter EV: "))
        print("Total Special Defenes Points: ", sc.Stat_Calc.Other_Stat_SPDefense(Pokemon_Base_SPDefense,Pokemon_Iv,Pokemon_Ev,Pokemon_Level,Pokemon_Nature_SPDefense),"\n")
    if opt == 6:
        Pokemon_Base_Speed = int(input("Enter Base Speed Points: "))
        Pokemon_Iv = int(input("Enter IV: "))
        Pokemon_Ev = int(input("Enter EV: "))
        print("Total Speed Points: ", sc.Stat_Calc.Other_Stat_Speed(Pokemon_Base_Speed,Pokemon_Iv,Pokemon_Ev,Pokemon_Level,Pokemon_Nature_Speed),"\n")

flag = True
Pokemon_Level =0
Pokemon_Stat = ["HP","Attack","Defense","Special Attack","Special Defenes","Speed"]
Pokemon_Base = [6]
Pokemon_IV = [6]
Pokemon_EV = [6]

if choice == 2:
    print("Evs")

    while flag:
        Pokemon_Level = int(input("Enter Pokemon level: "))
        if Pokemon_Level > 0 and Pokemon_Level < 101:
            flag = False
    
    
    Pokemon_Nature = str.lower(input("Enter Pokemon's Nature: "))

    print("Enter Base Stats")   
    for x in range(1, 6):
        Pokemon_Base.append(int(input("Enter "+ Pokemon_Stat[x] + ": ")))
    
    print("Enter IV on each Stat")    
    i = 1
    while i < 7:
        Pokemon_IV.append(int(input("Enter "+Pokemon_Stat[i]+" IV: ")))
        if (Pokemon_IV[i] < 0 or Pokemon_IV[i] > 31):
            i = i - 1
            print("must be between 0 and 31")
        i = i + 1

            

    print("Enter EV on each Stat")
    j = 1
    while j < 7:
        Pokemon_EV.append(int(input("Enter "+Pokemon_Stat[j]+" EV: ")))
        if (Pokemon_EV[j] < 0 or Pokemon_EV[j] > 255):
            j = j - 1
            print("must be between 0 and 255")
        j = j + 1    

    #Pokemon Neutral Nature
    if Pokemon_Nature in ['quirky','bashful','serious','docile','hardy']:
        Pokemon_Nature_Attack = 1
        Pokemon_Nature_Defense = 1
        Pokemon_Nature_SPAttack = 1
        Pokemon_Nature_SPDefense = 1
        Pokemon_Nature_Speed = 1
    #Pokemon Attack Nature
    elif Pokemon_Nature in ['lonely','brave','adamant','naughty']:
        Pokemon_Nature_Attack = 1.1
        if Pokemon_Nature in ['lonely']:
            Pokemon_Nature_Defense = 0.9
        elif Pokemon_Nature in ['brave']:
            Pokemon_Nature_Speed = 0.9
        elif Pokemon_Nature in ['adamant']:
            Pokemon_Nature_SPAttack = 0.9
        elif Pokemon_Nature in ['naughty']:
            Pokemon_Nature_SPDefense = 0.9
    #Pokemon Defense Nature
    elif Pokemon_Nature in ['bold','relaxed','impish','lax']:
        Pokemon_Nature_Defense = 1.1
        if Pokemon_Nature in ['bold']:
            Pokemon_Nature_Attack = 0.9
        elif Pokemon_Nature in ['relaxed']:
            Pokemon_Nature_Speed = 0.9
        elif Pokemon_Nature in ['impish']:
            Pokemon_Nature_SPAttack = 0.9
        elif Pokemon_Nature in ['lax']:
            Pokemon_Nature_SPDefense = 0.9
    #Pokemon Speed Nature
    elif Pokemon_Nature in ['timid','hasty','jolly','naive']:
        Pokemon_Nature_Speed = 1.1
        if Pokemon_Nature in ['timid']:
            Pokemon_Nature_Attack = 0.9
        elif Pokemon_Nature in ['hasty']:
            Pokemon_Nature_Defense = 0.9
        elif Pokemon_Nature in ['jolly']:
            Pokemon_Nature_SPAttack = 0.9
        elif Pokemon_Nature in ['naive']:
            Pokemon_Nature_SPDefense = 0.9
    #Pokemon Special Attack Nature
    elif Pokemon_Nature in ['modest','mild','quiet','rash']:
        Pokemon_Nature_SPAttack = 1.1
        if Pokemon_Nature in ['modest']:
            Pokemon_Nature_Attack = 0.9
        elif Pokemon_Nature in ['mild']:
            Pokemon_Nature_Defense = 0.9
        elif Pokemon_Nature in ['quiet']:
            Pokemon_Nature_Speed = 0.9
        elif Pokemon_Nature in ['rash']:
            Pokemon_Nature_SPDefense = 0.9
    #Pokemon Special Defense Nature
    elif Pokemon_Nature in ['calm','gentle','sassy','careful']:
        Pokemon_Nature_SPDefense = 1.1
        if Pokemon_Nature in ['calm']:
            Pokemon_Nature_Attack = 0.9
        elif Pokemon_Nature in ['gentle']:
            Pokemon_Nature_Defense = 0.9
        elif Pokemon_Nature in ['sassy']:
            Pokemon_Nature_Speed = 0.9
        elif Pokemon_Nature in ['careful']:
            Pokemon_Nature_SPAttack = 0.9

    
    print("1. Attack")
    print("2. Defense")
    print("3. Special Attack")
    print("4. Special Defense")
    print("5. Speed")
    
    opt = int(input("Enter: "))

    if opt == 1:
        Modifier = Pokemon_Nature_Attack
    if opt == 2:
        Modifier = Pokemon_Nature_Defense
    if opt == 3:
        Modifier = Pokemon_Nature_SPAttack
    if opt == 4:
        Modifier = Pokemon_Nature_SPDefense
    if opt == 5:
        Modifier = Pokemon_Nature_Speed

    Desired_Increase = int(input("Enter Desired Increase: "))

    D = ec.Ev_Calc.Ev_Calc_D( Pokemon_Base[opt+1],Pokemon_IV[opt+1],Pokemon_EV[opt+1],Pokemon_Level)

    EVs_needed = ec.Ev_Calc.Ev_Calc_EV_Needed( Desired_Increase,Modifier,D,Pokemon_Level)

    print("The total amount of Evs needed for your pokemon ", EVs_needed)
