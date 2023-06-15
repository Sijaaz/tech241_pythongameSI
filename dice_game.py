import random

user_input = True

while user_input:
    answer = input("Welcome to the dice game! Game rules - This is a two player game. Every player gets three dice rolls. The first one to get to 30 wins.Type 'yes' if you would like to play, and 'no' if you would like to quit: ")
    if answer == "no":
        break
    elif answer == "yes":
        user_name1 = input("What is your name? ")
        print("Hello " + user_name1 + "!")
        input("Press x to roll your dice...")
        user1_number_firstgo = random.randint(1, 6)
        print(user1_number_firstgo)

        print("Now let's play with User Two")
        user_name2 = input("What is your name? ")
        print("Hello " + user_name2 + "!")
        input("Press x to roll your dice...")
        user2_number_firstgo = random.randint(1, 6)
        print(user2_number_firstgo)

        print("Hello " + user_name1 + ", please roll again")
        input("Press x to roll your dice...")
        user1_number_secondgo = random.randint(1, 6)
        print(user1_number_secondgo)
        total_score = user1_number_firstgo + user1_number_secondgo
        print("Your total score so far is " + str(total_score))

        print("Hello " + user_name2 + ", please roll again")
        input("Press x to roll your dice...")
        user2_number_secondgo = random.randint(1, 6)
        print(user2_number_secondgo)
        total_score = user2_number_firstgo + user2_number_secondgo
        print("Your total score so far is " + str(total_score))

        print("Hello " + user_name1 + ", please roll again")
        input("Press x to roll your dice...")
        user1_number_thirdgo = random.randint(1, 6)
        print(user1_number_thirdgo)
        total_score = user1_number_firstgo + user1_number_secondgo + user1_number_thirdgo
        score1 = total_score
        print("Your final score is " + str(total_score))

        print("Hello " + user_name2 + ", please roll again")
        input("Press x to roll your dice...")
        user2_number_thirdgo = random.randint(1, 6)
        print(user2_number_thirdgo)
        total_score = user2_number_firstgo + user2_number_secondgo + user2_number_thirdgo
        print("Your final score is " + str(total_score))
        score2 = total_score

        if score2 > 30:
            print("You win! " + user_name2 + ". You lose! " + user_name1)
        if score2 < 30:
            print("You lose! " + user_name2 + ". You win! " + user_name1)
        if score1 == score2:
            print("It's a tie!:")


# three elif dont
# use lists instead






# if user2_number < user1_number:
#  print("You win!")
# elif user2_number > user1_number:
# print("Opponent wins!")
# else:
# print("It's a tie!")


# if user2_number < user1_number:
        #     print("You win!")
        # elif user2_number > user1_number:
        #     print("Opponent wins!")
        # else:
        #     print("It's a tie!")
























# import random
#
# user_input = True
#
# while user_input:
#     answer = input("Welcome to the dice game! Type 'yes' if you would like to play, and 'no' if you would like to quit: ")
#     if answer == "no":
#         break
#     elif answer == "yes":
#         user_name = input("What is your name? ")
#         print("Hello " + user_name + "!")
#         input("Press x to roll your dice...")
#         user1_number = random.randint(1, 6)
#         print(user1_number)
#
#         print("Now let's play with User Two")
#         user_name2 = input("What is your name? ")
#         print("Hello " + user_name2 + "!")
#         input("Press x to roll your dice...")
#         user2_number = random.randint(1, 6)
#         print(user2_number)
#
#         if user2_number < user1_number:
#             print("You win!")
#         elif user2_number > user1_number:
#             print("Opponent wins!")
#         else:
#             print("It's a tie!")