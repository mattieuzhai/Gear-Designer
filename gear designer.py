import numpy as np
import matplotlib as plt
import math
import pandas as pd


#equations
# t_r = t_s + 2*t_p
# (t_r + t_s)/Np = whole number
# input_module = 6.4

solution_headers = ['Input Module', 'Input Sun Gear Teeth', 'Input Planet Gear Teeth', 'Input Ring Gear Teeth', 'Input Ratio',
                    'Output Module', 'Output Sun Gear Teeth', 'Output Planet Gear Teeth', 'Output Ring Gear Teeth', 'Output Ratio',
                    'Final Ratio'
                    ]
solutions = pd.DataFrame(columns = solution_headers)
found_solution = False

#Inputs
target_solutions = 5
n_solutions = 0


target_gear_ratio = 100 #this will be the desired overall gear ratio

min_module = 1 #minimum module of the gears

n_planet = 6 #number of planet gears

max_teeth = 200 #maximum ring gear teeth

min_teeth = 16 #minimum teeth on a gear

target_size = 500 #target size of gear

#Initial Checks
if(max_teeth < min_teeth):
    print("Will never work")
    exit(0)
if(target_size / min_teeth < min_module):
    print("Will never work")
    exit(0)

#Initial Values
input_sun_teeth = min_teeth
input_ring_teeth = min_teeth * (n_planet - 1)
input_planet_teeth = (input_ring_teeth - input_sun_teeth)/2

output_ring_teeth = input_ring_teeth + n_planet
output_planet_teeth = input_planet_teeth
output_sun_teeth = output_ring_teeth -  2 * output_planet_teeth

input_gears = [input_sun_teeth, input_ring_teeth, input_planet_teeth]
output_gears = [output_sun_teeth, output_ring_teeth, output_planet_teeth]

input_ratio = input_ring_teeth/input_sun_teeth + 1
output_ratio = input_ring_teeth/(output_ring_teeth - input_ring_teeth)
final_ratio = input_ratio * output_ratio

input_module = target_size / input_ring_teeth
output_module = input_module * ((input_ring_teeth - input_planet_teeth)/(output_ring_teeth - output_planet_teeth))

#Checks
even_space = (input_ring_teeth + input_sun_teeth)/n_planet
even_space1 = (output_ring_teeth + output_sun_teeth)/n_planet

#Teeth numbers okay?
all_whole_numbers = all(num.is_integer() if isinstance(num, float) else isinstance(num, int) for num in input_gears)
all_whole_numbers1 = all(num.is_integer() if isinstance(num, float) else isinstance(num, int) for num in output_gears)

if(not all_whole_numbers or not all_whole_numbers1): 
    print("Gear teeth are not whole numbers")
elif(input_module < min_module or output_module < min_module): #Gear size okay?
    print("Gear module too small")
elif(even_space % 1 != 0 or even_space1 % 1 != 0): #Evenly spaced?
    print("Gears will not evenly space")
elif(input_planet_teeth + 2 > (input_planet_teeth + input_sun_teeth)*math.sin(math.radians(180/n_planet))): #Will the gear fit?
    print("Inner planet gears do not fit")
elif(output_planet_teeth + 2 > (output_planet_teeth + output_sun_teeth)*math.sin(math.radians(180/n_planet))):
    print("Outer planet gears do not fit")
elif(abs(target_gear_ratio - final_ratio) > 5):
    print("Gear ratio not close enough")
else:
    found_solution = True

if(found_solution):
    print(input_module)
    print(input_ring_teeth)
    print(input_planet_teeth)
    print(input_sun_teeth)

    print(output_module)
    print(output_ring_teeth)
    print(output_planet_teeth)
    print(output_sun_teeth)

    print(final_ratio)
    print("============================")

    new_data = {'Input Module': input_module, 'Input Sun Gear Teeth': input_sun_teeth, 'Input Planet Gear Teeth': input_planet_teeth, 'Input Ring Gear Teeth': input_ring_teeth, 
                'Input Ratio': input_ratio, 'Output Module': output_module, 'Output Sun Gear Teeth': output_sun_teeth, 'Output Planet Gear Teeth': output_planet_teeth, 
                'Output Ring Gear Teeth': output_ring_teeth, 'Output Ratio': output_ratio, 'Final Ratio': final_ratio}
    solutions = pd.concat([solutions, pd.DataFrame(new_data, index = [0])],ignore_index = True)
    found_solution = False
    n_solutions += 1

#Continue
while(n_solutions < target_solutions):
    if(input_ring_teeth - input_sun_teeth < 2 * min_teeth):
        input_ring_teeth += 2
        input_sun_teeth = min_teeth
    if(input_ring_teeth > max_teeth):
        print("No more solutions exist")
        exit(0)
    input_sun_teeth += 1

    input_planet_teeth = (input_ring_teeth - input_sun_teeth)/2

    output_ring_teeth = input_ring_teeth + n_planet
    output_planet_teeth = input_planet_teeth
    output_sun_teeth = output_ring_teeth -  2 * output_planet_teeth

    input_gears = [input_sun_teeth, input_ring_teeth, input_planet_teeth]
    output_gears = [output_sun_teeth, output_ring_teeth, output_planet_teeth]

    input_ratio = input_ring_teeth/input_sun_teeth + 1
    output_ratio = input_ring_teeth/(output_ring_teeth - input_ring_teeth)
    final_ratio = input_ratio * output_ratio

    input_module = target_size / input_ring_teeth
    output_module = input_module * ((input_ring_teeth - input_planet_teeth)/(output_ring_teeth - output_planet_teeth))

    even_space = (input_ring_teeth + input_sun_teeth)/n_planet
    even_space1 = (output_ring_teeth + output_sun_teeth)/n_planet

    #Teeth numbers okay?
    all_whole_numbers = all(num.is_integer() if isinstance(num, float) else isinstance(num, int) for num in input_gears)
    all_whole_numbers1 = all(num.is_integer() if isinstance(num, float) else isinstance(num, int) for num in output_gears)

    if(not all_whole_numbers or not all_whole_numbers1): 
        print("Gear teeth are not whole numbers")
    elif(input_module < min_module or output_module < min_module): #Gear size okay?
        print("Gear module too small")
    elif(even_space % 1 != 0 or even_space1 % 1 != 0): #Evenly spaced?
        print("Gears will not evenly space")
    elif(input_planet_teeth + 2 > (input_planet_teeth + input_sun_teeth)*math.sin(math.radians(180/n_planet))): #Will the gear fit?
        print("Inner planet gears do not fit")
    elif(output_planet_teeth + 2 > (output_planet_teeth + output_sun_teeth)*math.sin(math.radians(180/n_planet))):
        print("Outer planet gears do not fit")
    elif(abs(target_gear_ratio - final_ratio) > 5):
        print("Gear ratio not close enough")
    else:
        found_solution = True

    if(found_solution):
        print(input_module)
        print(input_ring_teeth)
        print(input_planet_teeth)
        print(input_sun_teeth)

        print(output_module)
        print(output_ring_teeth)
        print(output_planet_teeth)
        print(output_sun_teeth)

        print(final_ratio)
        print("============================")

        new_data = {'Input Module': input_module, 'Input Sun Gear Teeth': input_sun_teeth, 'Input Planet Gear Teeth': input_planet_teeth, 'Input Ring Gear Teeth': input_ring_teeth, 
                'Input Ratio': input_ratio, 'Output Module': output_module, 'Output Sun Gear Teeth': output_sun_teeth, 'Output Planet Gear Teeth': output_planet_teeth, 
                'Output Ring Gear Teeth': output_ring_teeth, 'Output Ratio': output_ratio, 'Final Ratio': final_ratio}

        solutions = pd.concat([solutions, pd.DataFrame(new_data, index = [0])],ignore_index = True)
        print(solutions.to_string(index = False))
        found_solution = False
        n_solutions += 1
file_name = 'solutions_1.csv'
solutions.to_csv(file_name, index = False)
