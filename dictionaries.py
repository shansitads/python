'''
Dictionary consists of a key (any data type) associated with some data. Each key must be unique.
'''

monthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June"
}
print(monthConversion)
print(monthConversion["Mar"]) # putting an invalid parameter SHOWS ERROR
print(monthConversion.get("Apr"))
print(monthConversion.get("Nov")) # putting an invalid parameter DOES NOT SHOW ERROR, it return none
print(monthConversion.get("Nov", "Not a valid key")) # if first param is invalid, message in second param is printed