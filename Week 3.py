print ("Welcome to the FiberPro calculator!")

company_name = input("Please enter your company name: ")

feet_of_cable = input("Please enter the number of feet of fiber optic cable to be installed: ")

feet_of_cable = float(feet_of_cable)

cost_of_cable = feet_of_cable * .87

str(cost_of_cable)

print ("Your company name: ",company_name)

print ("Your total cost of cable: $",round(cost_of_cable,2))