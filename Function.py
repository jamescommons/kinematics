# Class for a standard polynomial (maybe do trig stuff later)
import math


# Where a is an array of values for a and n is an array of values for n in at^n
# Type is a string (x, v, a, j) determining the type of function
# Func is an instance variable used to define the function in a String
class Function:
    def __init__(self, a, n, t):
        self.aValues = a
        self.nValues = n
        self.type = t
        self.func = ""
        self.aDeriv = []
        self.nDeriv = []
        self.aInteg = []
        self.nInteg = []
        self.derivative()
        self.integral()

    def to_string(self):
        if self.type == "x":
            self.func = "x(t) = "
        elif self.type == "v":
            self.func = "v(t) = "
        elif self.type == "a":
            self.func = "a(t) = "
        elif self.type == "j":
            self.func = "j(t) = "

        for i in range(len(self.aValues)):
            if i > 0:
                self.func += "+ (" + str(self.aValues[i]) + "t^" + str(self.nValues[i]) + ") "
            else:
                self.func += "(" + str(self.aValues[i]) + "t^" + str(self.nValues[i]) + ") "

        return self.func

    def derivative(self):
        for i in range(len(self.aValues)):
            self.aDeriv.append(self.aValues[i] * self.nValues[i])
            self.nDeriv.append(self.nValues[i] - 1)

    def integral(self):
        self.aInteg.clear()
        self.nInteg.clear()

        for i in range(len(self.aValues)):
            try:
                self.aInteg.append(self.aValues[i] / (self.nValues[i] + 1))
            except ZeroDivisionError:
                self.aInteg.append(None)
            self.nInteg.append(self.nValues[i] + 1)

    def get_value_at_t(self, time):
        value = 0.0
        for i in range(len(self.aValues)):
            value = value + (self.aValues[i] * math.pow(time, self.nValues[i]))

        return value
