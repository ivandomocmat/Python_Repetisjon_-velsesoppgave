# # GYM WORKOUT PROGRAM



# muscle_groups = ["1.Chest",
#                  "2.Back",
#                  "3.Shoulders",
#                  "4.Arms",
#                  "5.legs",
#                  "6.Abs"]

# chest_list = ["Incline dumbell bench press", 
#                  "Decline dumbell bench press", 
#                  "Incline machine chest press", 
#                  "Standing cable fly",
#                  "Cable iron cross",
#                  "Chest dips"]

# while True:
#     print("MENU")
#     print("1. Muscle Groups")
#     print("2. Add to list")
#     print("3. Remove from list")
#     print("4. End ")

#     choices = input("Choose from (1 - 4): ")
    
    
#     if choices == "1":
#         print("Your excercise:")
#         for i, exercise in enumerate(muscle_groups, 1):
#             print(f"{i}. {exercise}")
#             chest_list.append(exercise)
        

#     elif choices == "2":
#         musclegroup = int(input("Choose a musclegroup from (1 - 6): "))
#         print(f"{i}.{chest_list}")
#         new_exercise = input("Write exercise to add on list:")
#         chest_list.append(new_exercise)
#         print(f"Added to {new_exercise}")

    
    # elif choices == "3":
    #     exercise = int(input("Which exercise you want to remove?")) -1
        
    #     if exercise < len(chest_list) and exercise >= 0:
    #         fjernet = chest_list.pop(exercise)
    #         print(f"Removed {fjernet}")1

    #     else: 
    #         print("Can't find exercise in the list")

    # elif choices == "4":
    #     print("Done")
    #     break 

        
muscle_groups = ["1.Chest",
                 "2.Back",
                 "3.Shoulders",
                 "4.Arms",
                 "5.legs",
                 "6.Abs"]

chest_list = ["Incline Dumbell Bench Press", 
              "Decline Dumbell Bench Press", 
              "Incline Machine Chest Press", 
              "Standing Cable Fly",
              "Cable Iron Cross",
              "Chest Dips"]


back_list =    ["1.Lat Pull Down", 
                "2.Seated Cable Row", 
                "3.Machine Row", 
                "4.Pendlay Row",
                "5.Dumbbell Row"]

shoulder_list = ["1.Dumbbell Shoulder Press", 
                 "2.Incline Machine Shoulder Press", 
                 "3.Machine Lateral Raise", 
                 "4.Sitting Cable Face pull",
                 "5.Dumbbell Lateral Raise"]

                


while True:
    print("MENU")
    print("1. Muscle Groups")
    print("2. Add to list")
    print("3. Remove from list")
    print("4. End ")

    choices = input("Choose from (1 - 4): ")
    
    
    if choices == "1":
        print("Your excercise:")
        for i, exercise in enumerate(muscle_groups, 1):
            print(f"{i}. {exercise}")

    elif choices == "2":
        musclegroup = int(input("Choose a musclegroup from (1 - 6): "))

        #CHEST WORKOUT 
        if musclegroup == 1:
            print("Chest exercises:")
            new_exercise = input("Add exercise to list:")
            chest_list.append(new_exercise)
            print(f"Added to {new_exercise}") 
            
            
            for j, ex in enumerate(chest_list, 1):
                print(f"{j}. {ex}")
                 
            #BACK WORKOUT
        elif musclegroup == 2:
            print("Back exercises:")
            new_exercise = input("Add exercise to back list:")
            if new_exercise:
                back_list.append(new_exercise)
                print(f"Added to {new_exercise}")
                
            for j, ex in enumerate(back_list, 1):
                print(f"{j}. {ex}")


             #SHOULDER WORKOUT
        elif musclegroup == 3:
            print("Shoulder exercises:")
            new_exercise = input("Add exercise to back list:")
            if new_exercise:
                shoulder_list.append(new_exercise)
                print(f"Added to {new_exercise}")
                
            for j, ex in enumerate(shoulder_list, 1):
                print(f"{j}. {ex}")


