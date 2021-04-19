# Kinematics program
# Type a function in the form (x, v, a, j)(t) = (at^n) + ...

from Function import *

# Prompts user to input an equation
print()
print("Enter an equation of the form (x, v, a, j)(t) = (at^n) + ...   Example: x(t) = (3t^45) + "
      "(-3t^2)")
print("If \"None\" appears in your equation, it means that a natural logarithm was present "
      "in one of the integrations.")
print("If that is the case, you should not use what ever the system outputs.")
print()
eq = input("Equation: ")
print()
a = []
n = []

# Determines what the type of equation is
if eq[0] == "x":
    t = "x"
elif eq[0] == "v":
    t = "v"
elif eq[0] == "a":
    t = "a"
elif eq[0] == "j":
    t = "j"
else:
    print("Equation requires x, v, a, j to be the first character.")
    t = None
    exit()

# Finds a values and stores them into the "a" array
index = 0
for i in eq:
    if i == "(" and index > 1:
        a_from_string = float(eq[index + 1:eq.index("t", index)])
        a.append(a_from_string)
    index += 1

# Finds n values and stores them into the "n" array
index = 0
for i in eq:
    if i == "^":
        n_from_string = float(eq[index + 1:eq.index(")", index)])
        n.append(n_from_string)
    index += 1

# Returns remaining kinematic equations and initial equation
if t == "x":
    position = Function(a, n, t)
    velocity = Function(position.aDeriv, position.nDeriv, "v")
    acceleration = Function(velocity.aDeriv, velocity.nDeriv, "a")
    jerk = Function(acceleration.aDeriv, acceleration.nDeriv, "j")

    print(position.to_string())
    print(velocity.to_string())
    print(acceleration.to_string())
    print(jerk.to_string())
elif t == "v":
    velocity = Function(a, n, t)

    position = Function(velocity.aInteg, velocity.nInteg, "x")
    position.aValues.append(float(input("What is the initial position? ")))
    position.nValues.append(1.0)

    acceleration = Function(velocity.aDeriv, velocity.nDeriv, "a")
    jerk = Function(acceleration.aDeriv, acceleration.nDeriv, "j")

    print()
    print(position.to_string())
    print(velocity.to_string())
    print(acceleration.to_string())
    print(jerk.to_string())
elif t == "a":
    acceleration = Function(a, n, t)

    velocity = Function(acceleration.aInteg, acceleration.nInteg, "v")
    velocity.aValues.append(float(input("What is the initial velocity? ")))
    velocity.nValues.append(1.0)

    velocity.integral()
    position = Function(velocity.aInteg, velocity.nInteg, "x")
    position.aValues.append(float(input("What is the initial position? ")))
    position.nValues.append(1.0)

    jerk = Function(acceleration.aDeriv, acceleration.nDeriv, "j")

    print()
    print(position.to_string())
    print(velocity.to_string())
    print(acceleration.to_string())
    print(jerk.to_string())
elif t == "j":
    jerk = Function(a, n, t)

    acceleration = Function(jerk.aInteg, jerk.nInteg, "a")
    acceleration.aValues.append(float(input("What is the initial acceleration? ")))
    acceleration.nValues.append(1.0)

    acceleration.integral()
    velocity = Function(acceleration.aInteg, acceleration.nInteg, "v")
    velocity.aValues.append(float(input("What is the initial velocity? ")))
    velocity.nValues.append(1.0)

    velocity.integral()
    position = Function(velocity.aInteg, velocity.nInteg, "x")
    position.aValues.append(float(input("What is the initial position? ")))
    position.nValues.append(1.0)

    print()
    print(position.to_string())
    print(velocity.to_string())
    print(acceleration.to_string())
    print(jerk.to_string())
else:
    position = None
    velocity = None
    acceleration = None
    jerk = None

# Allows user to input a value for time and get the respective values back
print()
running = True
while running:
    time = float(input("Enter a value for time: "))

    print()
    print("Position @t=" + str(time) + " is " + str(position.get_value_at_t(time)))
    print("Velocity @t=" + str(time) + " is " + str(velocity.get_value_at_t(time)))
    print("Acceleration @t=" + str(time) + " is " + str(acceleration.get_value_at_t(time)))
    print("Jerk @t=" + str(time) + " is " + str(jerk.get_value_at_t(time)))
    print()

    if input("Would you like to input another value for time? (y/n): ") == "y":
        running = True
    else:
        running = False
