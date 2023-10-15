# CAN Bus Data Evaluation Tool
The CAN Bus Data Evaluation Tool is a Python script designed to analyze, visualize, and summarize CAN bus data from various car models. This tool enables users to process CSV files, generate line graphs for data visualization, and assess the timing status of specific signals from sensors.

## Table of Contents
Prerequisites
Installation
Usage
Running the Script
Selecting Car Models
Choosing Data Analysis Options
Output
Generated Graphs
CSV Data Files
License
Contributing
Acknowledgments
Prerequisites
Before using the CAN Bus Data Evaluation Tool, ensure you have the following prerequisites installed:

Python 3.x
Pandas
Matplotlib
Joblib

## Installation
Clone or download this repository to your local machine.

Set up a cache directory to store cached data using the cache_loc variable in the script.

Selecting Car Models
The script will prompt you to select a car model:
Enter 1 for the "auto" car model.
Enter 2 for the "auto_pro" car model.
Choosing Data Analysis Options
After selecting a car model, the script will display data analysis options. You can choose an option by entering a corresponding number:

Overview
Overview_Time
Deep_Dive
Deep_Dive_RADAR
Deep_Dive_Front_CAMERA  (Available for "Assist_plus" model)
Continue selecting options until you are done. To exit the program and generate PDF plots, enter "STOP."

## Output
Generated Graphs
The script generates line graphs for the selected data analysis options.
Each graph corresponds to a specific signal or sensor.
CSV Data Files
The tool saves the processed CSV data files in the output directory.
Files are named based on the selected car model and timestamp.
## License
This project is licensed under the MIT License. See the LICENSE file for details.
