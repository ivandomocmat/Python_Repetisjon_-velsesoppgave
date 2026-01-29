# Chest Workouts to do list

exercise_list = ["Incline dumbell bench press", 
                 "Decline dumbell bench press", 
                 "Incline machine chest press", 
                 "Standing cable fly",
                 "Cable iron cross",
                 "Chest dips"]

while True:
    print("CHEST DAY EXCERCISES")
    print("1. Show list")
    print("2. Add to list")
    print("3. Remove from list")
    print("4. End ")

    choices = input("Choose from (1 - 4): ")

    if choices == "1":
        print("Your excercise:")
        for i, exercise in enumerate(exercise_list, 1):
            print(f"{i}. {exercise}")

    elif choices == "2":
        new_exercise = input("Add exercise to list:")
        exercise_list.append(new_exercise)
        print(f"Added to {new_exercise}")

    elif choices == "3":
        exercise = int(input("Which exercise you want to remove?")) -1
        
        if exercise < len(exercise_list) and exercise >= 0:
            fjernet = exercise_list.pop(exercise)
            print(f"Removed {fjernet}")

        else: 
            print("Can't find exercise in the list")

    elif choices == "4":
        print("Done")
        break 





