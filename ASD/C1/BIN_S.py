def funkcja(tab, n):
    s = 0
    e = len(tab) - 1
    m = (s + e) // 2

    while s < e:
        if tab[m] == n:     break
        elif tab[m] < n:    s = m + 1
        elif tab[m] > n:    e = m - 1
        m = (s + e) // 2

    return tab[m] == n