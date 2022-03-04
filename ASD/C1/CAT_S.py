def funkcja(tab, x):
    i = 0
    j = 0
    while j < len(tab):
        if      tab[j] - tab[i] == x:   return True
        elif    tab[j] - tab[i] < x:    j += 1
        elif    tab[j] - tab[i] > x:    i += 1
    return False