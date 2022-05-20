class Stat_Calc():
    def Stat_Calc_HP(Pokemon_Base_HP, Pokemon_IV, Pokemon_EV, Pokemon_Level):
        Hp = (((2 * Pokemon_Base_HP + Pokemon_IV + (Pokemon_EV/4)) * Pokemon_Level)/100) + Pokemon_Level + 10
        return Hp

    def Other_Stat_Attack(Pokemon_Base_Attack, Pokemon_IV, Pokemon_EV, Pokemon_Level,Pokemon_Nature):
        Stat_Attack = ((((2 * Pokemon_Base_Attack + Pokemon_IV + (Pokemon_EV/4)) * Pokemon_Level)/100) + 5) * (((2 * Pokemon_Base_Attack + Pokemon_IV + (Pokemon_EV/4)) * Pokemon_Level)/100) + Pokemon_Nature
        return Stat_Attack

    def Other_Stat_Defense(Pokemon_Base_Defense, Pokemon_IV, Pokemon_EV, Pokemon_Level,Pokemon_Nature):
        Stat_Defense = ((((2 * Pokemon_Base_Defense + Pokemon_IV + (Pokemon_EV/4)) * Pokemon_Level)/100) + 5) * (((2 * Pokemon_Base_Defense + Pokemon_IV + (Pokemon_EV/4)) * Pokemon_Level)/100) + Pokemon_Nature
        return Stat_Defense

    def Other_Stat_SPAttack(Pokemon_Base_SPAttack, Pokemon_IV, Pokemon_EV, Pokemon_Level,Pokemon_Nature):
        Stat_SPAttack = ((((2 * Pokemon_Base_SPAttack + Pokemon_IV + (Pokemon_EV/4)) * Pokemon_Level)/100) + 5) * (((2 * Pokemon_Base_SPAttack + Pokemon_IV + (Pokemon_EV/4)) * Pokemon_Level)/100) + Pokemon_Nature
        return Stat_SPAttack

    def Other_Stat_SPDefense(Pokemon_Base_SPDefense, Pokemon_IV, Pokemon_EV, Pokemon_Level,Pokemon_Nature):
        Stat_SPDefense = ((((2 * Pokemon_Base_SPDefense + Pokemon_IV + (Pokemon_EV/4)) * Pokemon_Level)/100) + 5) * (((2 * Pokemon_Base_SPDefense + Pokemon_IV + (Pokemon_EV/4)) * Pokemon_Level)/100) + Pokemon_Nature
        return Stat_SPDefense

    def Other_Stat_Speed(Pokemon_Base_Speed, Pokemon_IV, Pokemon_EV, Pokemon_Level,Pokemon_Nature):
        Stat_Speed = ((((2 * Pokemon_Base_Speed + Pokemon_IV + (Pokemon_EV/4)) * Pokemon_Level)/100) + 5) * (((2 * Pokemon_Base_Speed + Pokemon_IV + (Pokemon_EV/4)) * Pokemon_Level)/100) + Pokemon_Nature
        return Stat_Speed