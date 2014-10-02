def summera(start, stop):
    summa = 0
    if start < stop:
        while start <= stop:
            summa += start
            start += 1
    else:
        while start >= stop:
            summa += start
            start -= 1
    return summa