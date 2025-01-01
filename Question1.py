

# There are 100 doors in a row, all doors are initially closed. A person walks through all doors multiple times and toggle (if open then close, if close then open) them in the following way: 

# In the first walk, the person toggles every door 

# In the second walk, the person toggles every second door, i.e., 2nd, 4th, 6th, 8th, … 

# In the third walk, the person toggles every third door, i.e. 3rd, 6th, 9th, … 

# Likewise,

# In the 100th walk, the person toggles the 100th door. 


# ========================================================================================================

def main():
    print("Hello, World!")
    
    doors = ["Closed"] * 100
    
    for j in range(0, 100):
        j += 1
        for i in range(j-1, 100):
            if i % j == 0:
                if doors[i] == "Closed":
                    doors[i] = "Open"
                else:doors[i] = "Closed"
            i += j
    
    count = sum(1 for door in doors if door == "Open")
    print(count)
if __name__ == "__main__":
    main()