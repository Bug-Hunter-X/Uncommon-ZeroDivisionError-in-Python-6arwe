def function_with_uncommon_error_solution(a, b):
    try:
        result = b / a
    except ZeroDivisionError:
        result = float('inf')  # Or another appropriate handling
    else:
        result = a + b
    return result