import math
import numpy as np

# Define the function for each calculation:
# Total momentum (p):
def total_momentum(px, py, pz):
    return (px**2 + py**2 + pz**2)**(0.5) 

# Transverse momentum (pt):
def transverse_momentum(px, py):
    return (px**2 + py**2)**(0.5)

# Pseudorapidity (n)
def pseudorapidity(p, pz):
    # Adding a condition to avoid division by 0
    if p == pz:
        return float('inf')  # Changed to float('inf') for consistent handling
    else:
        return (0.5 * math.log((p + pz) / (p - pz)))

# Function to perform bootstrapping
def bootstrap_mean_difference(data1, data2, n_samples=1000):
    means_diff = []
    for _ in range(n_samples):
        sample1 = np.random.choice(data1, size=len(data1), replace=True)
        sample2 = np.random.choice(data2, size=len(data2), replace=True)
        means_diff.append(np.mean(sample1) - np.mean(sample2))
    return np.array(means_diff)

# Initialize lists for storing results
n_positive = []
n_negative = []
p_positive = []
p_negative = []
pt_positive = []
pt_negative = []

# Main code block
try:
    # Prompt for file path
    file_path = input("Enter the path to the file you want to analyze.\nBy default press enter for 'output-Set0.txt' (if it's in the same directory),\nor enter a full path like '/home/user/Desktop/output-Set0.txt'): ")
    
    if file_path == "":
        file_path = "output-Set0.txt"
        
    # Open the file
    with open(file_path, "r") as infile:
        total_nb_positive_pions = 0
        total_nb_negative_pions = 0
        
        for line in infile:
            columns = line.split(" ")
            if len(columns) == 4:
                px = float(columns[0])
                py = float(columns[1])
                pz = float(columns[2])
                pg = int(columns[3])
                
                # Process positive pions
                if pg == 211:
                    total_nb_positive_pions += 1
                    p = total_momentum(px, py, pz)
                    n = pseudorapidity(p, pz)
                    pt = transverse_momentum(px, py)

                    p_positive.append(p)
                    n_positive.append(n)
                    pt_positive.append(pt)
                
                # Process negative pions
                elif pg == -211:
                    total_nb_negative_pions += 1
                    p = total_momentum(px, py, pz)
                    n = pseudorapidity(p, pz)
                    pt = transverse_momentum(px, py)

                    p_negative.append(p)
                    n_negative.append(n)
                    pt_negative.append(pt)
        
        # Calculate averages and uncertainties
        average_n_negative = np.mean(n_negative)
        uncertainty_n_negative = np.std(n_negative)
        
        average_n_positive = np.mean(n_positive)
        uncertainty_n_positive = np.std(n_positive)
        
        average_p_negative = np.mean(p_negative)
        uncertainty_p_negative = np.std(p_negative)
        
        average_p_positive = np.mean(p_positive)
        uncertainty_p_positive = np.std(p_positive)
        
        average_pt_negative = np.mean(pt_negative)
        uncertainty_pt_negative = np.std(pt_negative)
        
        average_pt_positive = np.mean(pt_positive)
        uncertainty_pt_positive = np.std(pt_positive)
        
        # Bootstrapping to find mean differences and their uncertainties
        mean_diffs_n = bootstrap_mean_difference(n_positive, n_negative)
        mean_difference_n = np.mean(mean_diffs_n)
        uncertainty_mean_difference_n = np.std(mean_diffs_n)

        mean_diffs_p = bootstrap_mean_difference(p_positive, p_negative)
        mean_difference_p = np.mean(mean_diffs_p)
        uncertainty_mean_difference_p = np.std(mean_diffs_p)

        mean_diffs_pt = bootstrap_mean_difference(pt_positive, pt_negative)
        mean_difference_pt = np.mean(mean_diffs_pt)
        uncertainty_mean_difference_pt = np.std(mean_diffs_pt)

        # Print results
        print(f"Mean difference in pseudorapidity: {mean_difference_n} uncertainty: {uncertainty_mean_difference_n}")
        print(f"Mean difference in total momentum: {mean_difference_p} uncertainty: {uncertainty_mean_difference_p}")
        print(f"Mean difference in transverse momentum: {mean_difference_pt} uncertainty: {uncertainty_mean_difference_pt}\n")

        print(f"Average pseudorapidity (negative): {average_n_negative:.6f} uncertainty: {uncertainty_n_negative:.6f}")
        print(f"Average pseudorapidity (positive): {average_n_positive:.6f} uncertainty: {uncertainty_n_positive:.6f}")

        print(f"Average total momentum (negative): {average_p_negative:.6f} uncertainty: {uncertainty_p_negative:.6f}")
        print(f"Average total momentum (positive): {average_p_positive:.6f} uncertainty: {uncertainty_p_positive:.6f}")

        print(f"Average transverse momentum (negative): {average_pt_negative:.6f} uncertainty: {uncertainty_pt_negative:.6f}")
        print(f"Average transverse momentum (positive): {average_pt_positive:.6f} uncertainty: {uncertainty_pt_positive:.6f}")

except FileNotFoundError:
    print("Error: The file path you entered does not exist. Please check the path and try again.")
except Exception as e:
    print(f"An unexpected error occurred: {e}. Please check your file path and try again.")
