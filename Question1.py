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
    print(doors)
if __name__ == "__main__":
    main()