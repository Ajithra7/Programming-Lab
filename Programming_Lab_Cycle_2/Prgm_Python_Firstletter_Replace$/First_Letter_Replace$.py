'''Get a string from an input string where all occurrences of first character replaced with ‘$’, except first character.
# [eg: onion -> oni$n]'''

input_string = input("Enter the string ")
print("Input string: "+input_string)
str_replace = input_string[1:].replace(input_string[0].lower(),'$').replace(input_string[0].upper(),'$')
output_string = input_string[0]+str_replace
print("Output string: "+output_string)