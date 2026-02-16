# ====================================================================================================================
# #PLASMA TEMPERATURE CLASSIFIER
# ===================================================================================================================

#defining function(which will characterise the body)
def classify_plasma_temp(temp):
    if temp < 10**4:
        return "Cold plasma"
    elif 10**4 <= temp <= 10**6:
        return "Warm plasma"
    else:
        return "Hot plasma"
    
#---------------------------------------------------------------------------------------------------------
#Creating empty list
results = []

#storing input and its category by using loop and def func.
count = 0
while count < 5:
    try:
        input_tem= float(input(f"Enter temperature {count+1} in Kelvin: "))
        category = classify_plasma_temp(input_tem)
        results.append((input_tem, category))
        count += 1
    except ValueError:
        print("Invalid input! Please enter in numbers.")
print(results)
#---------------------------------------------------------------------------------------------------------
# creating a structure of table
print("\nPlasma Classification Table")
print("-" * 40)
print(f"{'Temperature (K)':<20}{'Category'}")  #prints temp. and eleminate space making 20 total character
print("-" * 40)

#printing the result as temp. and its category by using for loop
for input_tem, category in results:
    print(f"{input_tem:<20.2f}{category}")

print("-" * 40)
print("\nWhy Temperature Classification Matters ")
print("Plasma behaviour strongly depends on temperature because ionization level, particle collisions, and energy transport change with temperature. In plasma physics experiments (fusion, space plasma, laboratory plasma), knowing whether plasma is cold, warm, or hot helps determine confinement methods, diagnostics, and energy control strategies.")