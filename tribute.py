def planet_degree(power):
    levels = {
    90 : "Dangerous",
    80 : "Threat",
    70 : "Potentential Threat",
    60 : "Burgeoning",
    50 : "Unaware",
    }

    for i in levels:
        if power >= i:
            print (levels)
        else:
            print ("Not a Threat")

planet_degree(90)        






