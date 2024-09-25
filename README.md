<p align="center">
      <img src="https://i.ibb.co/6gd7Wnj/Log-Aggregation.jpgm" width="726">
</p>


## About

This application is designed for batch processing of user action logs presented in CSV files. It calculates aggregated metrics (CREATE, READ, UPDATE, DELETE) over a specific time window (7 days).

The application combines logs from the previous 7 days and saves the aggregated result as a CSV file, with one row per user and the count of each action type. The result is stored in the output/ directory, with the file name based on the calculation date in the format YYYY-mm-dd.csv.


## Input Data

Each input CSV file contains logs for one day and has three columns: email, action, dt.

 - ***email***: the user's email identifier.
 - ***action***: the action type (CREATE, READ, UPDATE, DELETE).
 - ***dt***: the date and time of the event.


## Use Case


When running the program for the date 2024-09-16, it will process data from 2024-09-09 to 2024-09-15 (inclusive) and create a file in output/2024-09-16.csv.

The final table will include the following columns:

  - ***email***: the user's email address.
    
  - ***create_count***: the number of CREATE operations.
    
  - ***read_count***: the number of READ operations.
    
  - ***update_count***: the number of UPDATE operations.
    
  - ***delete_count***: the number of DELETE operations.
    

## Setup and Configuration

### 1. Clone the repository

   `git clone <repository_URL>` 

### 2. Set up the environment

  `python3 -m venv venv`
  
   `source venv/bin/activate  # For MacOS/Linux`

### 3. Install the dependencies

  `pip install -r requirements.txt`

### 4. Configure environment variables

  Create a `.env` file in the project's root directory and add the following environment variables

### 5. Running the Application

  `python script.py '%Y-%m-%d'`

 The result will be saved as ./OUTPUT_DIR/'%Y-%m-%d'.csv. 
