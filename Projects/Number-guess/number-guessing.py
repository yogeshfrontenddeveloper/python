import random


chances = 0
user_input = True

while user_input:

    try:
        # getting user input
        user_guess_number = input('enter a number range between 1 to 10 :')

        random_number = random.randint(1, 10)
        chances += 1

        #  to quit the program
        quit_val = 'quit'
        if user_guess_number.lower() == quit_val:
            user_input = False
            print("Okay bye!")

        # changing it into float and int to avoid float number we are rounding up the number
        changed_user_num = int(float(user_guess_number))

        # displaying the output
        # print(changing_num_int)

    # to check the number is negative or not and the no is less than 10
        if changed_user_num > 0 and changed_user_num <= 10:

            # checking the user_guess_number and  random_number is equal or not
            if changed_user_num == random_number:

                print(
                    f' congratulation you have won the no is {changed_user_num} rand no is {random_number}')

                # to check no of steps taken to get the answer
                print(f'Hurray! You got it in {chances} steps!')
                break

            else:
                print(
                    f'you have lost the no is {changed_user_num} rand no is {random_number}')

        else:
            print("don't enter negative value and enter number between 1 to 10")

    except ValueError:
        print("That's not an number!")
