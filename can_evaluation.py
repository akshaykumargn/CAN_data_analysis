# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 14:02:01 2023

@author: aksha
"""

import pandas as pd
import matplotlib.pyplot as plt
import random
from fpdf import FPDF
import PyPDF2
from matplotlib.backends.backend_pdf import PdfPages


# Define a function to read the CSV file and return the data as a Pandas DataFrame
def read_csv_file(file_path):
    print('Reading CSV file...')
    # Specify the delimiter, handle missing data, and set data types
    asm_data = pd.read_csv(file_path, sep=",", skip_blank_lines=True, on_bad_lines='skip', low_memory=False)
    return asm_data

# Define the file path to your CSV file
file_path = r'file path'

# Call the function to read the CSV file and cache the data
asm_data = read_csv_file(file_path)
# Define the file path to save the CSV file
output_file_path = r'path to save file'

# Save the DataFrame as a CSV file
asm_data.to_csv(output_file_path, index=False)

# Dropping rows or columns with NA value
asm_data.dropna()

# replacing with previous values
df1 = asm_data.fillna(method='ffill')

# replacing initial NAN with zeros
df2 = df1.fillna(0)

# Iterate over each column in the DataFrame
for column in asm_data.columns:
    # Try to convert the column values to float
    try:
        asm_data[column] = asm_data[column].astype(float)
    except ValueError:
        # Handle any non-convertible values
        pass
        # print(f"Column '{column}' contains non-numeric values.")

print(True)

# List of required column keywords
Overview = ['desired column headings']

Overview_Time = ['desired column headings']

Deep_Dive = ['desired column headings']

Deep_Dive_RADAR= ['desired column headings']

Deep_Dive_Front_CAMERA = ['desired column headings']

#add list of assistance system function signals
auto = [Overview, Overview_Time, Deep_Dive, Deep_Dive_RADAR]

auto_pro =[Overview, Overview_Time, Deep_Dive, Deep_Dive_RADAR,
           Deep_Dive_Front_CAMERA]

options = []  # Declare the options variable outside the loop

car_model = int(input("Select the car model:\n1 - auto\n2 - auto_pro\n"))

while car_model not in [1, 2]:
    print('Wrong input! Please choose between 1 and 2')
    car_model = int(input("Select the car model:\n1 - auto\n2 - auto_pro\n"))

if car_model == 1:
    options = auto
elif car_model == 2:
    options = auto_pro

# accepting user input
while True:
    choice = input("Please choose from one of the options below\n "
                   "1-Overview\n "
                   "2-Overview_Time\n "
                   "3-Deep_Dive\n "
                   "4-Deep_Dive_RADAR\n "
                   "5-Deep_Dive_Front_CAMERA\n "
                   "or Enter 'STOP' to exit the program and print plots in a PDF file\n")
    if choice.lower() == "stop":
        print("Exiting the program...")
        break
    try:
        choice = int(choice)
        while choice < 1 or choice > 9:
            raise ValueError
        print("Valid input:", choice)
        print("Displaying graphs...")
        # Filtering just the column names with required keywords
        column_names = [col for col in df2.columns if any(keyword in col for keyword in options[int(choice) - 1])]

        # Getting the column data of respective filtered column names
        df3 = df2.loc[:, column_names]

        # Creating list of columns names
        columns = list(df3.columns)

        # Create the figure and subplots
        num_rows = len(column_names)

        # generate a list of random colors
        colors = ['#%06x' % random.randint(0, 0xFFFFFF) for i in range(num_rows - 1)]
        # if the colors list is shorter than the number of subplots, extend it with more random colors
        if len(colors) < num_rows:
            colors.extend(['#%06x' % random.randint(0, 0xFFFFFF) for i in range(num_rows - len(colors))])

        fig, axs = plt.subplots(num_rows - 1, 1, figsize=(20, 40), sharex=True)
        for i in range(1, num_rows):
            axs[i - 1].plot(df3[column_names[0]], df3[column_names[i]], linestyle='-', color=colors[i])
            axs[i - 1].set_title(column_names[i], fontsize=5)

            # Add a box between subplots
            # adjust the spacing between subplots
            fig.subplots_adjust(hspace=0.8, top=0.2, bottom=0.05)
            bbox_props = dict(boxstyle="round", fc="white", ec="gray", alpha=1.0)

            # adjust the position of the subplot titles and x-axis labels
            plt.subplots_adjust(top=0.95, bottom=0.08)

            # Add labels and title to the common x-axis
            fig.text(0.5, 0.02, 'Time(s)', ha='center', bbox=bbox_props)
            fig.text(0.01, 0.5, 'Signals', va='center', rotation='vertical', bbox=bbox_props)

    except ValueError:
        # choice = input("Invalid input! Enter a number between 1 and 8 or enter 'Stop':\n")
        print("Invalid input! Enter a number between 1 and 8 or enter 'STOP'.")
        continue
    
    plt.show()


# To print the graph PDFs in separate pages
print('Please wait till the PDFs are generated!')

# To print all the graphs in to a PDF file
# Create a PdfPages object to save plots in a PDF file
pdf_pages = PdfPages("subplots.pdf")

for i, item in enumerate(options):
    # Creating a list of signal headings
    Heading_list = ["Overview", "Overview_Time", "Deep_Dive", "Deep_Dive_RADAR",
               "Deep_Dive_Front_CAMERA"]

    list_name = Heading_list[i]

    # Filtering just the column names with required keywords
    unique_column_list = [col for col in df2.columns if any(keyword in col for keyword in item)]
    num_of_rows = len(unique_column_list)

    # Getting the column data of respective filtered column names
    df4 = df2.loc[:, unique_column_list]

    # Set up the figure and axis objects
    # generate a list of random colors
    colors = ['#%06x' % random.randint(0, 0xFFFFFF) for i in range(num_of_rows - 1)]

    # if the colors list is shorter than the number of subplots, extend it with more random colors
    if len(colors) < num_of_rows:
        colors.extend(['#%06x' % random.randint(0, 0xFFFFFF) for i in range(num_of_rows - len(colors))])

        fig, axs = plt.subplots(num_of_rows - 1, 1, figsize=(20, 40), sharex=True)

        # Create a new page for this plot and add a heading with the list name
        plt.suptitle(list_name, fontsize=30)
        for j in range(1, num_of_rows):
            axs[j - 1].plot(df4[unique_column_list[0]], df4[unique_column_list[j]], linestyle='-', color=colors[j])
            axs[j - 1].set_title(unique_column_list[j], fontsize=12)

        # Add labels and title to the common x-axis
        fig.text(0.5, 0.01, 'Time(s)', ha='center')
        fig.text(0.02, 0.5, 'Signals', va='center', rotation='vertical')

        # fit the plot within the page
        fig.tight_layout(rect=[0, 0.03, 1, 0.95])
        # Save the figure and close the PdfPages object
        pdf_pages.savefig(fig)

# Close the PdfPages object
pdf_pages.close()
print('Check the pdf file in the corresponding folder.\n')

# ASM-Initialisation after engine-start
# Required signal keywords

id_keywords = ['Enter the list of keywords']
engine_start_Signal_kywds = ['Enter the list of keywords']
versions_of_static_events_kywds =['Enter the list of keywords']

if car_model == 1:
    id_keywords = id_keywords[:-4]  # Slice the list to exclude the last two items
    engine_start_Signal_kywds = engine_start_Signal_kywds[:-2]  # Slice the list to exclude the last two items
    versions_of_static_events_kywds = versions_of_static_events_kywds[:-2]


elif car_model == 2:
    pass

column_names_ID = [col for col in asm_data.columns if any(keyword in col for keyword in id_keywords)]

# To get only required columns with data in it
df5 = df2.loc[:, column_names_ID]
desired_col = df5.filter(regex='desired column name')
desired_col_equals_1 = df5[df5[desired_col.columns[0]] == 1]

# To filter next ten seconds after KST hits value '1'
# Extract the starting time value from the first row, first column
start_time = desired_col_equals_1.iloc[0, 0]

# Define the target end time as 10 seconds after the starting time
target_end_time = start_time + 10

# Filter the DataFrame based on the time condition
required_df = desired_col_equals_1[desired_col_equals_1.iloc[:, 0] <= target_end_time]
# Define the file path to save the CSV file
output_file_path = r'output path'

# Save the DataFrame as a CSV file
required_df.to_csv(output_file_path, index=False)

print('CSV file created successfully.')


