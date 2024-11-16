
habits = ["Wake Early", "Eat breakfast", "Go for university","Eat lunch","study for 3 hours","Exercise for 20 minutes","Sleep for 8 hours"]
completed_habits = {}

for habit in habits:
    response = input(f"Did you complete this habit today: '{habit}'? (yes/no): ").strip().lower()  
    if response == "yes":
        completed_habits[habit] = "Completed"       
    else:
        completed_habits[habit] = "Not completed"
print(f"\nToday's Habit Summary:")
for habit, status in completed_habits.items():
    print("{habit}: {status}")