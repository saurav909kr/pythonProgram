import random

l = ["Rock","Paper","scissor"]

while True:
    user_in = int(input('''
      Game start .....
         1.Yes
         2.No | Exit
    '''))
    if user_in == 1:
        print("This tournament will played in 5 round")
        for a in range(1,6):
            comp_count = 0
            user_count = 0
            user_input = int(input('''
             Choice any :------
               1. Rock
               2. Paper
               3. scissor
             '''))
            if user_input == 1:
                user_choice = "Rock"
            elif user_input == 2:
                user_choice = "Paper"
            elif user_input == 3:
                user_choice = "scissor"
            else:
                print("Invalid choice")

            comp_choice = random.choice(l)

            if comp_choice == user_choice:
                print("Computer choice :", comp_choice)
                print("You choice :", user_choice)
                print("No result")
                # comp_count += 1
                # user_count += 1
            elif (user_choice == "Rock" and comp_choice == "scissor") or (user_choice == "Paper" and comp_choice == "Rock") or (user_choice == "scissor" and comp_choice == "Paper"):
                print("Computer choice :", comp_choice)
                print("You choice :", user_choice)
                print("You Win")
                user_count += 1
            else:
                print("Computer choice :", comp_choice)
                print("You choice :", user_choice)
                print("computer Win")
                comp_count += 1

        if user_count > comp_count:
                print()
                print("              you win the tournament")
        elif comp_count > user_count:
                print()
                print("              you loss this tournament")
        else:
                print("This tournament is Drew")

    else:
         break






