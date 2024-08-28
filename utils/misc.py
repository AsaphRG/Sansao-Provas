from math import ceil

def round_for_half(value):
    int_value = int(value)
    decimal_part = value - int_value
    
    if decimal_part <= 0.25:
        return int_value
    elif decimal_part <= 0.75:
        return int_value + 0.5
    else:
        return ceil(value)
