def funkcja(tab):
    if len(tab) == 1:
        return 0

    mini = maxi = tab[0]
    i = 0

    if len(tab) % 2 == 1:
        i = 1
    else:
        if tab[1] < mini:
            mini = tab[1]
        if tab[1] > maxi:
            maxi = tab[1]
        i = 2
    
    while i < len(tab):
        if tab[i] < tab[i + 1]:
            if tab[i] < mini:       mini = tab[i]
            if tab[i + 1] > maxi:   maxi = tab[i + 1]
        else:
            if tab[i] > maxi:       maxi = tab[i]
            if tab[i + 1] < mini:   mini = tab[i + 1]
        i += 2
    
    return maxi - mini
    