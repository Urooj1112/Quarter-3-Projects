"""
Prompts the user for a weight on Earth
and a planet (in separate inputs). Then 
prints the equivalent weight on that planet.

Note that the user should type in a planet with 
the first letter as uppercase, and you do not need
to handle the case where a user types in something 
other than one of the planets (that is not Earth). 
"""


# Mars Weight

"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""
MARS_MULTIPLE = 0.378

def mars_weight_calculator():
    earth_weight = float(input("Enter a weight on Earth: "))
    mars_weight = earth_weight * MARS_MULTIPLE
    rounded_weight = round(mars_weight,2)
    print(f"The equivalent on Mars: {rounded_weight}")

MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14

def planetary_weight_calculator():
    earth_weight = float(input("Enter a weight on Earth: "))
    planet = input("Enter a planet: ").strip().lower()

    if planet == "mercury":
        gravity_constant = MERCURY_GRAVITY
    elif planet == "venus":
        gravity_constant = VENUS_GRAVITY
    elif planet == "mars":
        gravity_constant = MARS_GRAVITY
    elif planet == "jupiter":
        gravity_constant = JUPITER_GRAVITY
    elif planet == "saturn":
        gravity_constant = SATURN_GRAVITY
    elif planet == "uranus":
        gravity_constant = URANUS_GRAVITY
    elif planet == "neptune":
        gravity_constant = NEPTUNE_GRAVITY

    planetary_weight = gravity_constant * earth_weight
    print(f"The equivalent on Mars: {round(planetary_weight)}")


def main():
    print("Choose an option:")
    print("1. Calculate weight on Mars")
    print("2. Calculate weight on another planet")

    option = input("Choose an option: ")
    if option == "1":
        mars_weight_calculator()
    elif option == "2":
        planetary_weight_calculator()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()