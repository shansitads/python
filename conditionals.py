s = input("Do you agree or not? (Y/N): ")

def agreed(s):
    if s == "Y" or s == "y":
        print("Agreed.")
    elif s == "N" or s == "n":
        print("Not agreed.")

    if s in ["Y", "y"]:
        print("Agreed.")

    if s.lower() == "n":
        print("Not agreed.")

agreed(s)

def tallMale():
    is_male = False
    is_tall = True
    if is_male and is_tall:
        print("You are a male and you are tall")
    elif is_male and not is_tall:
        print("You are a male and you are not tall")
    elif not is_male and is_tall:
        print("You are not a male and you are tall")
    else:
        print("You are not a male and you are not tall")

tallMale()

def maxNum(num1, num2, num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num2:
        return num2
    else:
        return num3

print("Largest number is: " + str(maxNum(3,7,2)))