# Open dataset file from a txt
DATA = open("Advent-of-Code-2024/Day Two/dataset.txt","r").readlines()

# Format the data from the file and store it in a variable
FORMATTED_DATA = list(map(lambda y: list(map(lambda x: int(x),y)),list(map(lambda x: x.split(), DATA))))

# Check if reports are safe
def IS_SAFE_REPORT(report):
    INCREASING = all(report[i+1] - report[i] >= 1 and report[i+1] - report[i] <= 3 for i in range(len(report)-1))
    DECREASING = all(report[i] - report[i+1] >= 1 and report[i] - report[i+1] <= 3 for i in range(len(report)-1))

    return INCREASING or DECREASING

# Attempts to make reports safe
def CAN_BE_MADE_SAFE(report):
    # Check if the original report is safe
    if IS_SAFE_REPORT(report):
        return True
    
    # Attempts to make each unsafe report safe
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        
        if IS_SAFE_REPORT(modified_report):
            return True
    return False

# Counts number of reports that can also be made safe
def COUNT_SAFE_REPORTS(data):
    return sum(1 for report in data if CAN_BE_MADE_SAFE(report))

SAFE_REPORTS = COUNT_SAFE_REPORTS(FORMATTED_DATA)
print(SAFE_REPORTS)