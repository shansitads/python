m = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
'''
Unlike Java, Python allows different number of elements in each row i.e. different number of columns. The remaining elements of the last sublist are null.
'''

for row in m:
    for col in row:
        print(col, end=", ")