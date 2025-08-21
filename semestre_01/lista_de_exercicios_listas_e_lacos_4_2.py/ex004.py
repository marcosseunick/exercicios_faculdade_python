def printer_error(s):
    valid_chars = set('abcdefghijklm')
    errors = sum(1 for char in s if char not in valid_chars)
    return f"printer_error: {errors}/{len(s)}"

print(printer_error("aaabbbbhaijjjm"))        
print(printer_error("aaaxbbbbyyhwawiwjjjwwm")) 