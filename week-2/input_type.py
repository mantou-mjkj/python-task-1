

def is_int(number):
    try:
        isint=int(number)
    except ValueError as e:
        return 0
    return 1

def is_float(number):
    try:
        isint=float(number)
    except ValueError as e:
        return 0
    return 1