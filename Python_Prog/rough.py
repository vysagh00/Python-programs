# import random
# from random import randint

# def random():
#     l = ["qwert","walj","spoof","gald","dernio","wally","asap","end"]
#     rand = random.randint(0,len(l)-1)
#     return l[rand]

# def change_state(input,insert,current):
#     modified = " "
#     for i in range(len(input)):
#         if current == "_" and input[i] == insert:
#             modified += input[i]
#         else:
#             modified += current[i]
#     return modified

# def input_char(input,current,insert,attempts_rem):
#     if insert in input:
#         current = change_state(input,insert,current)
#     else:
#         attempts_rem -= 1
#         return current,attempts_rem

# def status(current,attempts_rem):
#     print("current ")
#     for i in current:
#         print(i)
#     print("\t attempts_rem ",attempts_rem)


# def result(input, current, attempts_rem):
#     if attempts_rem <= 0:
#         print("sorry you lost! :(  Try again")
#         print("the word was: {}", format(input))
#         return False

#     if input == current:
#         print("congrats!! You won :)")
#         return False
#     return True    

# def game(attempts = 5):
#     input = random()
#     current = ""
#     for i in input:
#         if i == "" or i == "a" or i == "e":
#             current += i
#             continue
#         current += "_"
#     attempts_rem = attempts
#     status(current,attempts_rem)

#     while True:
#         insert = input("Guess: ")
#         print(" ")
#         current,attempts_rem = input_char(input,current,insert,attempts_rem)
#         status(current,attempts_rem)
#         end = result(input, current, attempts_rem)
#         if(end == False):
#             break
                   
                   
# if __name__ == "__main__":
#    game()                   



