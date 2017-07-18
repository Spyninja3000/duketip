import numpy as np

ones = np.ones((5,4))
print(ones)

print("")

zeros = np.zeros((1,4))
zeros[0][0] = 1
print(zeros)

print("")

print(zeros * ones)

print("")

combined = (zeros * ones)
combined[1][2] = 10
print(combined)

print("")

combined = combined * 2
print(combined)

print("")

print(combined.sum())

print("")

print(combined.max(axis = 1))

print("")

print(combined.mean(axis=0))

#important notes:
#axis=1 is the rows and axis=0 is the columns
#you can do np.anynumber()
#counting starts at zero, always
#(# of rows, # of columns)