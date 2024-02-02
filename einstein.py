# Define a function called C_energy that calculates energy (E) in joules using mass (m) in kilograms
def C_energy(mass_kg):
    # Define the speed of light in meters per second (approximately 300,000,000 m/s)
    speed_of_light = 300000000
    
    # Calculate the energy (E) using the mass-energy equivalence formula (E = m * c^2)
    E_joules = mass_kg * speed_of_light ** 2
    
    # Return the calculated energy in joules
    return E_joules

# Define the main function
def main():
    # Prompt the user to enter a value for mass in kilograms and convert it to an integer
    mass_kg = int(input())
    
    # Call the C_energy function to calculate the energy (E) and store the result in E_joules
    E_joules = C_energy(mass_kg)
    
    # Print the calculated energy in joules
    print(E_joules)

# Call the main function to start the program
main()
