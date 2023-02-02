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
        
        break
