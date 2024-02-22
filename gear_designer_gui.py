import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
import matplotlib as plt
import math
debug = False
def calculate_solutions():  
    solution_headers = ['Input Module', 'Input Sun Gear Teeth', 'Input Planet Gear Teeth', 'Input Ring Gear Teeth', 'Input Ratio',
                        'Output Module', 'Output Sun Gear Teeth', 'Output Planet Gear Teeth', 'Output Ring Gear Teeth', 'Output Ratio',
                        'Final Ratio'
                        ]
    solutions = pd.DataFrame(columns = solution_headers)
    found_solution = False
    n_solutions = 0

    #Get Values
    min_teeth = float(min_teeth_entry.get())
    n_planet = float(n_planet_entry.get())
    target_size = float(target_size_entry.get())
    min_module = float(min_module_entry.get())
    target_gear_ratio = float(target_gear_ratio_entry.get())
    target_solutions = float(n_solutions_entry.get())   
    max_teeth = float(max_teeth_entry.get())
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
    file_name = file_name_entry.get()
    file_name = f"{file_name}.csv"
    solutions.to_csv(file_name, index = False)


#Create windows
window = tk.Tk()
window.title("Split-Ring Planetary Gearbox Designer")

#Create labels and entry widgets
n_solutions_label = ttk.Label(window, text="# of Solutions:")
n_solutions_label.grid(row=0, column=0, padx=5, pady=5)

n_solutions_entry = ttk.Entry(window)
n_solutions_entry.grid(row=0, column=1, padx=5, pady=5)

target_gear_ratio_label = ttk.Label(window, text="Target Gear Ratio:")
target_gear_ratio_label.grid(row=0, column=2, padx=5, pady=5)

target_gear_ratio_entry = ttk.Entry(window)
target_gear_ratio_entry.grid(row=0, column=3, padx=5, pady=5)

min_module_label = ttk.Label(window, text='Minimum module (mm)')
min_module_label.grid(row=1, column = 0, padx = 5, pady = 5)

min_module_entry = ttk.Entry(window)
min_module_entry.grid(row=1, column = 1, padx = 5, pady = 5)

n_planet_label = ttk.Label(window, text = "# of Planets")
n_planet_label.grid(row = 1, column = 2, padx = 5, pady = 5)

n_planet_entry = ttk.Entry(window)
n_planet_entry.grid(row = 1, column = 3, padx = 5, pady = 5)

max_teeth_label = ttk.Label(window, text="Maximum Gear Teeth")
max_teeth_label.grid(row = 2, column = 0, padx = 5, pady = 5)

max_teeth_entry = ttk.Entry(window)
max_teeth_entry.grid(row=2, column = 1, padx = 5, pady = 5)

min_teeth_label = ttk.Label(window, text = "Minimum Gear Teeth")
min_teeth_label.grid(row = 2, column = 2, padx= 5, pady = 5)

min_teeth_entry = ttk.Entry(window)
min_teeth_entry.grid(row = 2, column = 3, padx = 5, pady= 5)

target_size_label = ttk.Label(window, text = "Target Gear Size")
target_size_label.grid(row=3, column = 0, padx = 5, pady = 5)

target_size_entry = ttk.Entry(window)
target_size_entry.grid(row = 3, column = 1, padx = 5, pady = 5)

file_name_label = ttk.Label(window, text = "File Name")
file_name_label.grid(row = 3, column = 2, padx = 5, pady = 5)

file_name_entry = ttk.Entry(window)
file_name_entry.grid(row = 3, column = 3, padx = 5, pady = 5)


# Create a button to trigger calculations
calculate_button = ttk.Button(window, text="Calculate and Export", command=calculate_solutions)
calculate_button.grid(row=4, column=1, columnspan=2, pady=10)

info_text = ttk.Label(window, text = "Small note: if you make the min/max gear teeth a multiple of the number of planets, it'll find your solutions faster ")
info_text.grid(row = 5, column = 1,padx = 5, pady = 5)
# Run the GUI application
window.mainloop()