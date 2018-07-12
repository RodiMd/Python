#Kinetic Energy
#KE = 1/2 mv^2
#an object in motion has a kinetic energy
#m-mass(kilograms), v - meters per second
#ask user to enter mass and velocity

mass = 0
velocity = 0

def main():
    mass = input('Enter the mass of the object ')
    mass = float(mass)
    velocity = input('Enter the velocity at which the object is moving ')
    velocity = float(velocity)
    kineticEnergy = kinetic_energy(mass, velocity)
    print('The kinetic energy of the object is %.2f' %kineticEnergy)

def kinetic_energy(m, v):
    KE = 0.5 * m * v**2
    return KE
main()
