import numpy as np
import math
import os

#this code count the number of Pion positiv negqtiv the diference per fiile with the associate uncertainty per file and normalised

#define empty list to append the results of the different calculations
averages_positive=[]
averages_negative=[]
nb_events=[]
mean_diff=[]


# Defining the function used for the analysis
# Calculate the average amount of pions per event
def average_nb_pions(a,b):
    if b!=0:
        return a/b
    else:
        return float("inf")
        

# create a loop to prevent the code to crach when the user enter a wrong input file
try:
    
    directory= input("enter your file path")
    
    if directory == "":
        directory = "/../data"
        
            
    # Iterate over each file in the directory
    for filename in os.listdir(directory):
        # Check if the file is a specific type (e.g., .txt)
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            print(f"{filename} is being processed")
            # Open and process the file
            with open(file_path, 'r') as file:
            
            
                #defining the diferent variables 
                total_nb_positive_pions=0
                total_events=0
                total_events_empty=0
                total_nb_negative_pions=0
        
                # create a loop for repeating the process for each line 
                for line in file:
                    
                    
                    # defining each column of the file as different variables  
                    columns = line.split(" ") #the colulums are separated by " "
                    
                    #this is a condition that will only select the line of data that have 4 columns
                    if len(columns) == 4:
                        
                        #Defining each column
                        px = float(columns[0])
                        py = float(columns[1])
                        pz =  float(columns[2])
                        pg = int(columns[3])
                        
                        #I am here focusing on the pions particle. So I add this condition to only count the amount of pions particle. 
                        #this is for positive pions
                        if pg == 211:
                            total_nb_positive_pions += 1
                        
                        #this is for negative pions
                        elif pg == -211:
                            total_nb_negative_pions += 1
                        
                    # if the line doesn't have 4 columns it means it's the line of a new event.
                    #so this count the total amount of event.    
                    # If the line doesn't have 4 columns
                        elif len(columns) == 2 and columns[1] == '0':
                        # This is a special ending line with any number followed by '0', don't count it as a new event
                            total_events_empty += 1
        
                         # Count valid events
                        elif len(columns) == 2:
                            # Assuming valid events have 2 columns
                            total_events += 1
            
                 #this aply the function to calculate the average amount of positive and negative pions per event per file. 
                average_positive_pions= average_nb_pions (total_nb_positive_pions, total_events)
                average_negative_pions= average_nb_pions (total_nb_negative_pions, total_events)
                
                # calculates the mean difference for each file
                meandiff=average_positive_pions-average_negative_pions

                #append the different results to their respective empty list.
                averages_positive.append(average_positive_pions)
                averages_negative.append(average_negative_pions)
                print(f"Total events empty: {total_events_empty}")
                nb_events.append(total_events)
                mean_diff.append(meandiff)
             
    # Convert lists to numpy arrays for calculations
    nb_events = np.array(nb_events)
    averages_positive = np.array(averages_positive)
    averages_negative = np.array(averages_negative)
    mean_diff = np.array(mean_diff)
    print(mean_diff)
    print(nb_events)
    
    if nb_events.size > 0:        
        
        # calculations of the overall averages, their difference and their uncertainties.   
        weighted_average_positive = np.sum(averages_positive * nb_events) / np.sum(nb_events)
        weighted_average_negative = np.sum(averages_negative * nb_events) / np.sum(nb_events)
    
        average_mean_difference= weighted_average_positive - weighted_average_negative
        
        uncertainties_positive = np.std(averages_positive, ddof=1)
        uncertainties_negative = np.std(averages_negative, ddof=1)
        uncertainties_difference=np.std(mean_diff, ddof=1)

        print(f"Average amount of positive pions: {weighted_average_positive}")
        print(f"Average amount of negative pions: {weighted_average_negative}")
        print(f"Average of the difference of the mean of the amount of pions:{average_mean_difference}")
        print(f"Uncertainty (Positive Pions): {uncertainties_positive}")
        print(f"Uncertainty (Negative Pions): {uncertainties_negative}")
        print(f"Uncertainty (Difference of Means): {uncertainties_difference}")
        
    
    else:
        print("there are no events in the file")
    
   


# This is in case the user enter a wrong file path, the code will show an error and ask to correct it 

except FileNotFoundError: #this is specifically if the file is not found 
    print("Error: The file path you entered does not exist. Please check the path and try again.")
except Exception as e: #this for unexpected error 
    print(f"An unexpected error occurred: {e}. Please check your file path and try again.")
 

