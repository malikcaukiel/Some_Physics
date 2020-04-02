### fahrenheit to centigrade ###
"""
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5/9
    return c_temp
print(f_to_c(98.6))
                                                                                                """
####################################################################################################
### centigrade to fahrenheit ###
"""
def c_to_f(c_temp):
    f_temp = 9/5*(c_temp) + 32
    return f_temp
print(c_to_f(37))

### Getting 0 centigrade in fahrenheit, now                                                                                                
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)
                                                                                                """
####################################################################################################

### Global Environment ###
train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

### Calculate force ###
def get_force(mass, acceleration):
    f = mass*acceleration
    return f
#print(get_force(10,10))

train_force = get_force(train_mass, train_acceleration)
print(train_force)
### Printing string and a number together
print("The GE train supplies " + str(train_force) + "Newtons of force.")
########################################
### calculate energy ###
c = 3*10**8
def get_energy(mass = 10):
    f = mass * c
    return f
print(get_energy(20))
# Testing the get_energy function with bomb_mass = 1 defined above
print(get_energy(bomb_mass))

### calculate work ###
def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)        # get_force defined outside function. So can be
    work = force * distance                      # used, but not vice versa.
    return work
#y = get_work(10,10,10)
#print(y)

# Testing with train's variables
#get_work(train_mass, train_acceleration, train_distance)
#print(get_work(train_mass, train_acceleration, train_distance))
train_work = get_work(train_mass, train_acceleration, train_distance)
#print(trian_work)

print("The GE train does " +str(train_work)+ " Joules of work over " +str(train_distance)+ "meters.")

####################################################################################################
