import random

# code = [0, 0, 0, 0]
# correct_digits_and_position = 0
# correct_digits_only = 0
# correct = False


def create_code():
    """Function that creates the 4 digit code, using random digits from 1 to 8"""

    #global code
    code = [0, 0, 0, 0]

    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value

    return code


def show_instructions():
    """Shows instructions to the user"""

    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')


def show_results(correct_digits_and_position,correct_digits_only):
    """Show the results from one turn"""

    print('Number of correct digits in correct place:     ' + str(correct_digits_and_position))
    print('Number of correct digits not in correct place: ' + str(correct_digits_only))


def user_input():
    answer = input("Input 4 digit code: ")
    while len(answer) < 4 or len(answer) > 4:
        print("Please enter exactly 4 digits.")
        answer = input("Input 4 digit code: ")

    return answer



def take_turn(code, answer):
    """Handle the logic of taking a turn, which includes:
       * get answer from user
       * check if answer is valid
       * check correctness of answer
    """

    # global correct_digits_and_position
    # global correct_digits_only

    correct_digits_and_position = 0
    correct_digits_only = 0
    for i in range(len(answer)):
        if code[i] == int(answer[i]):
            correct_digits_and_position += 1
        elif int(answer[i]) in code:
            correct_digits_only += 1

    show_results(correct_digits_and_position,correct_digits_only)

    return correct_digits_and_position


def show_code(code):
    """Show Code that was created to user"""

    print('The code was: '+str(code))


def check_correctness(correct_digits_and_position,turns):
    """Checks correctness of answer and show output to user"""

    # global correct

    if correct_digits_and_position == 4:
        correct = True
        print('Congratulations! You are a codebreaker!')
        return correct
    else:
        correct = False
        print('Turns left: ' + str(12 - turns))

        return correct


def run_game():
    """Main function for running the game"""

    # global correct
    correct = False

    code = create_code()
    show_instructions()

    turns = 0
    while not correct and turns < 12:
        num = user_input()
        answer = take_turn(code,num)
        turns += 1
        correct = check_correctness(answer,turns)

    show_code(code)


if __name__ == "__main__":
    run_game()
