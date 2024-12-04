# Open dataset file from a txt
DATA = open("Advent-of-Code-2024/Day 2/dataset.txt","r").readlines()

# Format the data from the file and store it in a variable
FORMATTED_DATA = list(map(lambda y: list(map(lambda x: int(x),y)),list(map(lambda x: x.split(), DATA))))

# Check if reports are safe
def IS_SAFE_REPORT(REPORT):
    INCREASING = all(REPORT[i+1] - REPORT[i] >= 1 and REPORT[i+1] - REPORT[i] <= 3 for i in range(len(REPORT)-1))
    DECREASING = all(REPORT[i] - REPORT[i+1] >= 1 and REPORT[i] - REPORT[i+1] <= 3 for i in range(len(REPORT)-1))
    
    return INCREASING or DECREASING

# Count the number of safe reports
def COUNT_SAFE_REPORTS(DATA):
    return sum(1 for REPORT in DATA if IS_SAFE_REPORT(REPORT))

SAFE_REPORTS = COUNT_SAFE_REPORTS(FORMATTED_DATA)
print(f"Number of safe reports: {SAFE_REPORTS}")