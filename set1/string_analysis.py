import string

def char_match(sc):
    english = {
            ' ': {"percent": 0.1918182},
            'e': {"percent": 0.111607, "propotion": 56.88},
            'a': {"percent": 0.084966, "propotion": 43.31},
            'r': {"percent": 0.075809, "propotion": 38.64},
            'i': {"percent": 0.075448, "propotion": 38.45},  
            'o': {"percent": 0.071635, "propotion": 36.51},
            't': {"percent": 0.069509, "propotion": 35.43},
            'n': {"percent": 0.066544, "propotion": 33.92},
            's': {"percent": 0.057351, "propotion": 29.23},
            'l': {"percent": 0.054893, "propotion": 27.98},
            'c': {"percent": 0.045388, "propotion": 23.13},
            'u': {"percent": 0.036308, "propotion": 18.51},
            'd': {"percent": 0.033844, "propotion": 17.25},
            'p': {"percent": 0.031671, "propotion": 16.14},
            'm': {"percent": 0.030129, "propotion": 15.36},
            'h': {"percent": 0.030034, "propotion": 15.31},
            'g': {"percent": 0.024705, "propotion": 12.59},
            'b': {"percent": 0.020720, "propotion": 10.56},
            'f': {"percent": 0.018121, "propotion": 9.24},
            'y': {"percent": 0.017779, "propotion": 9.06},
            'w': {"percent": 0.012899, "propotion": 6.57},
            'k': {"percent": 0.011016, "propotion": 5.61},
            'v': {"percent": 0.010074, "propotion": 5.13},
            'x': {"percent": 0.002902, "propotion": 1.48},
            'z': {"percent": 0.002722, "propotion": 1.39},
            'j': {"percent": 0.001965, "propotion": 1.00},
            'q': {"percent": 0.001962, "propotion": 1}
        }
    error = 0.0
    for char in string.ascii_lowercase + ' ':
        percent = sc["n_char"][char] / sc["n_chars"]
        error += abs(percent - english[char]["percent"])
    return error

def string_characteristics(s):
    n_printable = 0
    n_unprintable = 0
    stat = {}
    for char in string.ascii_lowercase + ' ':
        stat[char] = 0

    for c in s:
        if str(c).isprintable():
            n_printable += 1
        else:
            n_unprintable += 1
        if c.lower() in stat:
            stat[c.lower()] += 1
    
    return {
        "all_printable":  (n_unprintable == 0),
        "n_printable": n_printable,
        "n_unprintable": n_unprintable,
        "n_chars": len(s),
        "n_char": stat
    }
