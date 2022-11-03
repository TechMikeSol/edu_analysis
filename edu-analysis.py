import csv

list_data = []
with open ("states_all.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    for row in reader:
        list_data.append(row)

print("List of dictionaries length is", len(list_data))

state_data = [row for row in list_data if row['STATE'] == 'GEORGIA']
#print(state_data)

AVG_MATH_4_SCORE = [float(row['AVG_MATH_4_SCORE']) for row in state_data if row['AVG_MATH_4_SCORE'] != '']
GA_AVG_MATH_4_SCORE = [AVG_MATH_4_SCORE]

print("GA list length is",len(GA_AVG_MATH_4_SCORE))
print("Our average math scores for Georgia are:",GA_AVG_MATH_4_SCORE)

def filter(state, column):
    for row in list_data:
        state = str,row["STATE"]
    print(state)