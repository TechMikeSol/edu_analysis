import csv

list_data = []
with open ("states_all.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    for row in reader:
        list_data.append(row)

print("List of dictionaries length is", len(list_data))

# I select GEORGIA from the rows in the key 'STATE' column

state_data = [row for row in list_data if row['STATE'] == 'GEORGIA']
#print(state_data)

# I'm selecting only the average scores of 
# 4th grade math students in the rows that contain values

AVG_MATH_4_SCORE = [row for row in state_data if row['AVG_MATH_4_SCORE'] != '']
GA_AVG_MATH_4_SCORE = [AVG_MATH_4_SCORE]

# I'm retrieving the length of the value GEORGIA and 
# the average math scores

print("GA list length is",len(GA_AVG_MATH_4_SCORE))
print("Our average math scores for Georgia are:",GA_AVG_MATH_4_SCORE)

# I'm filtering out the strings in the columns

def filter(state, column):
    for row in list_data:
        state = str,row["STATE"]

    print(state)

# Get each year in the dictionary 
# (1st: non-pythonic | 2nd: Pythonic)

years = []
#for row in state_data:
   # all_years = (row["YEAR"])
  #  years.append(all_years)
#print(years)

years = [row["YEAR"] for row in AVG_MATH_4_SCORE]
print(years)

# Percent Change

    
def percent_change(list_data, year1, year2, column):
    """Calculates percent change

    Parameters
    ----------
    list_data : list of dictionaries
        Education data throughout the US
    y1 : str
        Initial year that's being compared
    y2: str
        Secondary year value
    column : str
        Column describing actual year scores

    Returns
    -------
    Float
       returning percent_change.
    """
    old_value = 0
    new_value = 0
    for row in list_data:
        
        # If I'm at year1, assign the value of my column into old_value
        if row["YEAR"] == year1:
            old_value = float(row[column])
        # If I'm at year2, assign the value of my column into new_value
        if row["YEAR"] == year2:
            new_value = float(row[column])
    

    # return (old - new) / old * 100 to calc percent change
    percent_change = (old_value - new_value) / old_value * 100
    return percent_change

print(percent_change(list_data, "2009", "2011", "AVG_MATH_4_SCORE"))

# Applying the percent change 

for i in range(len(years)):
    if i + 1 >= len(years):
        break
    y1 = years[i]
    y2 = years[i + 1]
    
    change = percent_change(AVG_MATH_4_SCORE,y1,y2,"AVG_MATH_4_SCORE")
    # Note: Negatives are increases, Positives are decreases

    print(f"GA Percent change from {y1}-{y2} is {round(change,2)}")

    


