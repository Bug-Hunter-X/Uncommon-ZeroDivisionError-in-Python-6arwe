def function_with_uncommon_error(a, b):
    if a == 0:
        return b / a  # ZeroDivisionError
    else:
        return a + b