numbers = 0
column_length = 9
number_length = 5

planets = (
    ('Mercury', 57),
    ('Venus', 108),
    ('Earth', 150),
    ('Mars', 228),
    ('Jupiter', 779),
    ('Saturn', 1430),
    ('Uranus', 2880),
    ('Neptune', 4500)

)

# start of the program
print("============================================================")
print("Planet's Average Distance From Sun")
print("============================================================")

# displays the planets and the distance from each plant to the sun
for planet, distance in planets:
    numbers += 1
    print(f"#{numbers} {planet:<9} ={distance:>6} million miles")

print("============================================================")
print("To calculate the distance between two planets \n")


def main():

    print("Enter two planet numbers or 0 to quit: ")
    print("------------------------------------------------------------")

    while True:
        def get_integer_input(message, min_num=0, max_num=0):

            while True:
                try:
                    user_input = int(input(message))

                    if min == 0 and max == 0:
                        return user_input
                    elif min_num <= user_input <= max_num:
                        return user_input
                    else:
                        print(f"\t Invalid Input: Please enter a number between {min_num} and {max_num}.")
                        continue

                except ValueError:
                    print("\tInvalid Input: Please enter a number.")
                    continue
                break
            break
