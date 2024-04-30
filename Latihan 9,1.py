def temukan_tiga_tertinggi(bilangan):
    bilangan_terurut = sorted(bilangan, reverse=True)

    return bilangan_terurut[:3]

bilangan = [5, 2, 9, 1, 7, 6, 3, 8, 4]
print(temukan_tiga_tertinggi(bilangan))