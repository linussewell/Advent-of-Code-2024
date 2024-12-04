import re

def PARSE_DATA(DATA):
    # Regular expressions for different instruction types
    MUL_PATTERN = r'mul\((\d{1,3}),(\d{1,3})\)'
    DO_PATTERN = r'do\(\)'
    DONT_PATTERN = r'don\'t\(\)'

    # Track the current state of mul instructions
    MUL_ENABLED = True

    # Variables to store results
    ORIGNINAL_RESULT = 0
    NEW_RESULT = 0

    # Combine all patterns to process in order
    ALL_PATTERNS = re.findall(f'({MUL_PATTERN}|{DO_PATTERN}|{DONT_PATTERN})', DATA)
    
    # Process instructions in order
    for INTRUCTION in ALL_PATTERNS:
        INTRUCTION = INTRUCTION[0]
        
        # Check for do() and don't() instructions first
        if INTRUCTION == 'do()':
            MUL_ENABLED = True
        elif INTRUCTION == "don't()":
            MUL_ENABLED = False
        
        # Check for mul() instruction
        MUL_MATCH = re.match(MUL_PATTERN, INTRUCTION)
        if MUL_MATCH:
            # Always calculate for original total
            x, y = MUL_MATCH.groups()
            CURRENT_MUL = int(x) * int(y)
            ORIGNINAL_RESULT += CURRENT_MUL
            
            # Only add to new result total if enabled
            if MUL_ENABLED:
                NEW_RESULT += CURRENT_MUL
    
    return ORIGNINAL_RESULT, NEW_RESULT

# Read the entire file content as a single string
def OPEN_DATA(FILE_NAME):
    with open(FILE_NAME, 'r') as file:
        DATA = file.read().strip()
    return DATA

def main():
    DATA = 'Advent-of-Code-2024/Day 3/dataset.txt'
    DATA = OPEN_DATA(DATA)
   
    if DATA:
        # Parse and calculate the sums of multiplications
        ORIGINAL_RESULT, NEW_RESULT = PARSE_DATA(DATA)
        # Print processed data
        print("Original result:", ORIGINAL_RESULT)
        print("New result:", NEW_RESULT)

if __name__ == "__main__":
    main()