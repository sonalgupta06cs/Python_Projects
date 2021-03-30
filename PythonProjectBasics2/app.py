first = 'Sonal'
last = 'Gupta'
message = first + ' [' + last +'] is a coder'
# Formatted String, define your Formatted Strings, prefix with f'' then use curly braces to dynamically
# insert values into your strings.
msg = f"{first} [{last}] is a coder."
print(msg)


# len(), print() are a general purpose function in python
# Strings Methods upper(), lower(), replace(x,y), find(x), "in" Operator as more user readable
course = 'Learning Python Now'
print(course.upper()) # does not change the original string, rather gives us a new string
print("Length of the string "+str(len(course)))
print("Python" in course)
print(course.find('P')) # 9
print(course.find('p')) # -1
print(course.replace('Now', 'Started'))
print(course.title())

# Math Functions
x = 2.9
print("Rounded to:- ", round(x))
print("Abs to:- ", abs(-2.9)) # always returns the +ve value

