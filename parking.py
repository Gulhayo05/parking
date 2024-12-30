import os
import random

try:
    n = int(input("Parking dimensions: "))
# except ValueError:
#     print("Given character not integer")
#     exit()
except KeyboardInterrupt:
    print("\n\nCtrl+C was pressed to cancel the next operations. Goodbye!\n\n")
    exit()
except Exception as e:
    print("Unexpected error: " + str(e))
    exit()


parking_zone = [[1 for _ in range(n)] for _ in range(n)]
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

parking_zone[random.randint(0,9)][random.randint(0,9)] = 0
parking_zone[random.randint(0,9)][random.randint(0,9)] = 0
parking_zone[random.randint(0,9)][random.randint(0,9)] = 0
parking_zone[random.randint(0,9)][random.randint(0,9)] = 0
parking_zone[random.randint(0,9)][random.randint(0,9)] = 0
parking_zone[random.randint(0,9)][random.randint(0,9)] = 0
parking_zone[random.randint(0,9)][random.randint(0,9)] = 0


while True:
    clear_console()
    print("Current parking status:\n")
    for i in parking_zone:
        print(*i)
    
    try:
        row = int(input("\nEnter the row: ")) - 1
        col = int(input("Enter the column: ")) - 1
        carname = input("Car: ")
    except KeyboardInterrupt:
        print("\nCtrl+C was pressed to cancel the next operations.Goodbye!")
        break  # Gracefully exit the program if keyboard interrupt occurs
    
    if parking_zone[row][col] == 0:
        parking_zone[row][col] = carname
        print(f"\n{carname} ({row+1}:{col+1}) placed at the destination")
    else:
        print(f"\nThere is a {parking_zone[row][col]} car parked here.")
        print("The following spots are the closest to you:")
        
        empty_spaces = []
        for i in range(n):
            for j in range(n):
                if parking_zone[i][j] == 0:
                    distance = abs(i - row) + abs(j - col)
                    empty_spaces.append((distance, i, j))
        empty_spaces.sort()
        recommended_spaces = empty_spaces[:10]
        
        for distance, i, j in recommended_spaces:
            print(f"({i+1}:{j+1}) - Distance: {distance}")
    
    continue_adding = input("\nDo you want to park another car? (yes/no): ").lower()
    if continue_adding != "yes":
        break

clear_console()
print("The last state:\n")
for i in parking_zone:
    print(*i)