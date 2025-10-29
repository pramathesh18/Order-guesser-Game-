import random


def random_num(size):
    arr  = [i for i in range(1,size+1)]
    random.shuffle(arr)

    return arr


def ans_input(size):
    inp_str = input("Enter Order: ")
    inp_arr = inp_str.split()
    inp_arr = [int(item) for item in inp_arr]

    
    if len(inp_arr) != size:
        print(f"Enter exactly {size} numbers.")
        return ans_input(size)
    if len(set(inp_arr)) != size:
        print("Numbers must be unique.")
        return ans_input(size)
    if not all(1 <= n <= size for n in inp_arr):
        print(f"Numbers must be between 1 and {size}.")
        return ans_input(size)



    return inp_arr

def correct_guess(game_arr, guess_arr, size):
    correct = 0
    for i in range(size):
        if(game_arr[i] == guess_arr[i]):
            correct += 1
    return correct

def guess_loop(size):
    game_arr = random_num(size)
    #print(game_arr)
    attempts = 0
    
    while(True):
        guess_arr = ans_input(size)
        attempts += 1
        correct = correct_guess(game_arr, guess_arr, size)
        print(f"Correct positions: {correct}/{size} \n")

        if correct == size:
            print(f"guessed in {attempts} tries!")
            print("<GAME-WON>\n<CONGRATULATIONS>\n\n")
            break


def game_loop():
    while True:
        size = int(input("Enter size (or 0 to quit): "))
        if size == 0:
            print("<GAME-QUITED>")
            break
        guess_loop(size)

    
        


if __name__ == "__main__":

    game_loop()