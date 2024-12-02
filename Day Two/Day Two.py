# Open dataset file from a txt
DATA = open("Advent-of-Code-2024/Day Two/dataset.txt","r").readlines()

# Format the data from the file and store it in a variable
FORMATTED_DATA = list(map(lambda y: list(map(lambda x: int(x),y)),list(map(lambda x: x.split(), DATA))))

# Check if reports are safe
def IS_SAFE_REPORT(report):
    INCREASING = all(report[i+1] - report[i] >= 1 and report[i+1] - report[i] <= 3 for i in range(len(report)-1))
    DECREASING = all(report[i] - report[i+1] >= 1 and report[i] - report[i+1] <= 3 for i in range(len(report)-1))
    
    return INCREASING or DECREASING

# Count the number of safe reports
def COUNT_SAFE_REPORTS(data):
    return sum(1 for report in data if IS_SAFE_REPORT(report))

SAFE_REPORTS = COUNT_SAFE_REPORTS(FORMATTED_DATA)
print(f"Number of safe reports: {SAFE_REPORTS}")