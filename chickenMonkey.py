for i in range(1, 101):
    if ((i%5)==0 and (i%7)==0):
        print(f"ChickenMonkey")
    elif ((i%5)==0):
        print(f"Monkey")
    elif ((i%7)==0):
        print(f"Chicken")
    else:
        print(i)

# Write a program that prints the numbers from 1 to 100. You can use Python's range() to quickly make a list of numbers.

# For multiples of five (5, 10, 15, etc.) print "Chicken" instead of the number
# For the multiples of seven (7, 14, 21, etc.) print "Monkey".
# For numbers which are multiples of both five and seven print "ChickenMonkey".

#example below shown by T.A. Leah:

# def chicken_monkey_run():
#     range_to_100 = range(1, 100)
#     for num in range_to_100:
#         if num % 5 == 0 and num % 7 == 0:
#             print("ChickenMonkey")
#         elif num % 5 == 0:
#             print("Monkey")
#         elif num % 7 == 0:
#             print("Chicken")
#         else:
#             print(num)

# chicken_monkey_run()

#example by Steve Brownlee:

# for i in range(1, 101):
#     output = ""
#     if (i % 5 == 0):
#         output = f'{output}Chicken'
#     if (i % 7 ==0):
#         output = f'{output}Monkey'

#     print(output if output != "" else i)