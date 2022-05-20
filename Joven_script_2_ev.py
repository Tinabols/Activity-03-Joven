class Ev_Calc():
    def Ev_Calc_D(Pokemon_Base,Pokemon_IV,Pokemon_EV,Pokemon_Level):
        D = ((2*Pokemon_Base+ Pokemon_IV +(Pokemon_EV/4))*Pokemon_Level/100)
        return D
    def Ev_Calc_EV_Needed(Desired_Increase, Modifier, D, Pokemon_Level):
        EVs_needed = ((((Desired_Increase/Modifier)-(D))*400/Pokemon_Level)/4)*4
        return EVs_needed