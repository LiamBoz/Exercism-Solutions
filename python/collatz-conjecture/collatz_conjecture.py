def steps(number, num_of_steps = 0):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    elif number == 1:
        return num_of_steps
    else:
        return (
            (number%2==0 and steps(number/2, num_of_steps+1)) or
         steps(number*3+1, num_of_steps+1)
        )


    # elif number%2 == 0:
    #     number = number/2
    #     num_of_steps = num_of_steps + 1
    #     return steps(number, num_of_steps+1)
    # elif number%2 != 0:
    #     number = number*3 + 1
    #     num_of_steps = num_of_steps + 1
    #     return steps(number, num_of_steps)

# print(f"collatz of 1 is: {steps(1, 0)}")
# print(f"collatz of 2 is: {steps(2, 0)}")
# print(f"collatz of 3 is: {steps(3, 0)}")
# print(f"collatz of 4 is: {steps(4, 0)}")
print(f"collatz of 534564543 is: {steps(534564543, 0)}")

