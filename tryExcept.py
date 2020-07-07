'''
Prevent the program from crashing using try/except block.
'''

try:
    value = 10/0
    number = int(input("Enter a value: "))
    print(number)
except ValueError:
    print("Invalid input")
except ZeroDivisionError as error: #error is a variable which stores the error
    print(error)
except:
    # This is like the default case for all unspecified errors.
    print("Unknown error")

'''
The block which corresponds to the first error encountered is the only except block which will run.
'''