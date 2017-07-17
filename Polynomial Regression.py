import numpy as np

x = [-40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90] #list of angles
y = [65.33333333, 99.66666667, 130, 175.3333333, 383.6666667, 446.3333333, 642.6666667, 716.6666667, 717.6666667, 706.3333333, 626, 536.3333333, 365.3333333, 31.66666667] # list of known values

result = np.polyfit(x, y, 2)
eq = np.poly1d(result)

print(eq) #returns the x

l = raw_input("What's the angle: ") #asks for an angle

done = eq(int(l)) # defines the y of the x as a variable

print(done) #returns the y of the x

#My computer's matplotlib wasn't working, but here's the code for it

#x2 = np.arange(-40, 90)
#yfit = np.polyval(result, x2)
#print(yfit)

#plt.plot(x, y, label = "Points")
#plt.plot(x2, yfit, label = "Fit")
#plt.show()
#plt.savefig("example.png")
