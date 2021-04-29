# without using with statment
file = open('util/sample_write_file.txt', 'w')
file.write("hello friends!")
file.close()

# without using with statment
file = open('util/sample_write_file.txt', 'w+')
try:
    file.write('using try and catch block')
finally:
    file.close()

# using with statement
with open('util/sample_write_file.txt', 'w') as file:
    file.write('using with statment')
