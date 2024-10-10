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
    
    #directory= input("enter your file path")
    
    #if directory == "":
    directory = "data"

            
    # Iterate over each file in the directory
    for filename in os.listdir(directory):
        # Check if the file is a specific type (e.g., .txt)
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            print(f"{filename} is being processed")
            # Open and process the file
            with open(file_path, 'r') as file:
            
            
                #defining the different variables 
                total_nb_positive_pions=0
                total_events=0
                total_events_empty=0
                total_nb_negative_pions=0
        
                # create a loop for repeating the process for each line 
                while True:
                    line = file.readline()
                    if not line: break
                    else : 
                        columns = line.split(" ")
                        if len(columns) == 2 : #ths is a event line
                            if columns[1] == '0': #this is a non event
                                total_events_empty += 1
                            else : #this is a event with potential pions 
                                
                                nb_negative_pions_in_event = 0
                                nb_positive_pions_in_event = 0
                                for i in range(int(columns[1])):
                                    line_record = file.readline()
                                    if not line_record: break
                                    else :  # this is a particle line of  in the event
                                        columns_record = line_record.split(" ")
                                        px = float(columns_record[0])
                                        py = float(columns_record[1])
                                        pz =  float(columns_record[2])
                                        pg = int(columns_record[3])
                                        if pg == 211: #this is for positive pions
                                            nb_positive_pions_in_event += 1
                                            total_nb_positive_pions += 1
                            
                                        elif pg == -211: #this is for negative pions
                                            nb_negative_pions_in_event += 1
                                            total_nb_negative_pions += 1

                                if nb_positive_pions_in_event == 0 and nb_negative_pions_in_event == 0 :
                                    total_events_empty += 1
                                else:
                                    total_events += 1

                 #this apply the function to calculate the average amount of positive and negative pions per event per file. 
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
    
        average_mean_difference = np.sum(mean_diff * nb_events) /np.sum(nb_events)
        
        
        uncertainties_positive = np.std(averages_positive, ddof=1)
        uncertainties_negative = np.std(averages_negative, ddof=1)
        uncertainties_difference=np.std(mean_diff, ddof=1)

        print(f"Average amount of positive pions: {weighted_average_positive}")
        print(f"Average amount of negative pions: {weighted_average_negative}")
        print(f"Average of the difference of the mean of the amount of pions:{average_mean_difference}")
        print(f"Uncertainty (Positive Pions): {uncertainties_positive}")
        print(f"Uncertainty (Negative Pions): {uncertainties_negative}")
        print(f"Uncertainty (Difference of Means): {uncertainties_difference}")

        # Calculate the range of the mean difference
        lower_bound = average_mean_difference - uncertainties_difference
        upper_bound = average_mean_difference + uncertainties_difference

        print(f"Range of the mean difference: ({lower_bound}, {upper_bound})")
        print(mean_diff)
    
    else:
        print("there are no events in the file")
    
   


# This is in case the user enter a wrong file path, the code will show an error and ask to correct it 

except FileNotFoundError: #this is specifically if the file is not found 
    print("Error: The file path you entered does not exist. Please check the path and try again.")
except Exception as e: #this for unexpected error 
    print(f"An unexpected error occurred: {e}. Please check your file path and try again.")
 

print(f"Program finished")