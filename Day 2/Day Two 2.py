# Open dataset file from a txt
DATA = open("Advent-of-Code-2024/Day 2/dataset.txt","r").readlines()

# Format the data from the file and store it in a variable
FORMATTED_DATA = list(map(lambda y: list(map(lambda x: int(x),y)),list(map(lambda x: x.split(), DATA))))

# Check if reports are safe
def IS_SAFE_REPORT(REPORT):
    INCREASING = all(REPORT[i+1] - REPORT[i] >= 1 and REPORT[i+1] - REPORT[i] <= 3 for i in range(len(REPORT)-1))
    DECREASING = all(REPORT[i] - REPORT[i+1] >= 1 and REPORT[i] - REPORT[i+1] <= 3 for i in range(len(REPORT)-1))

    return INCREASING or DECREASING

# Attempts to make reports safe
def CAN_BE_MADE_SAFE(REPORT):
    # Check if the original report is safe
    if IS_SAFE_REPORT(REPORT):
        return True
    
    # Attempts to make each unsafe report safe
    for i in range(len(REPORT)):
        MODIFIED_REPORT = REPORT[:i] + REPORT[i+1:]
        
        if IS_SAFE_REPORT(MODIFIED_REPORT):
            return True
    return False

# Counts number of reports that can also be made safe
def COUNT_SAFE_REPORTS(DATA):
    return sum(1 for REPORT in DATA if CAN_BE_MADE_SAFE(REPORT))

SAFE_REPORTS = COUNT_SAFE_REPORTS(FORMATTED_DATA)
print(SAFE_REPORTS)