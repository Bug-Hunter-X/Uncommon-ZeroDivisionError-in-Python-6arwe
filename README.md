# Uncommon ZeroDivisionError in Python

This example demonstrates a less common scenario where a `ZeroDivisionError` can still occur in Python even when using conditional statements to prevent division by zero. The error happens because the condition `a == 0` is checked *before* the division operation is performed, not within the context of evaluating `b/a`.  This can be easily overlooked in complex functions.

## Solution
The solution involves rearranging the code to handle the potential `ZeroDivisionError` more robustly.