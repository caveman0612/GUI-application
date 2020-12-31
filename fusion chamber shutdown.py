# A laboratory is testing how atoms react in ionic state during nuclear fusion. They introduce different elements with
#     Hydrogen in high temperature and pressurized chamber. Due to unknown reason the chamber lost its power and the
#     elements in it started precipitatingGiven the number of atoms of Carbon [C],Hydrogen[H] and Oxygen[O] in the chamber.
#     Calculate how many molecules of Water [H2O], Carbon Dioxide [CO2] and Methane [CH4] will be produced following the
#     order of reaction affinity below

# 1. Hydrogen reacts with Oxygen   = H2O
# # 2. Carbon   reacts with Oxygen   = CO2
# # 3. Carbon   reacts with Hydrogen = CH4

# Make sure you follow the order of reaction
# output should be H2O,CO2,CH4
def burner(c,h,o):
    water = 0
    co2 = 0
    methane = 0
    carbon = c
    hydrogen = h
    oxygen = o
    while hydrogen >= 2 and oxygen >= 1:
        hydrogen += -2
        oxygen += -1
        water += 1
    while carbon >= 1 and oxygen >= 2:
        oxygen += -2
        carbon += -1
        co2 += 1
    while carbon >= 1 and hydrogen >= 4:
        hydrogen += -4
        carbon += -1
        methane += 1

    return water,co2,methane

    # print(water, co2, methane)

burner(354,1023230,0)
burner(45,11,100)
burner(939,3,694)
