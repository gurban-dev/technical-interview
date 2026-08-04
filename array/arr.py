# Arrays allow the storage of data to be referenced
# with a single variable name.

# "passenger" is the variable name in this case.
passenger = ['Alexander', 30, 'business']

print('passenger:', passenger)

print('len(passenger):', len(passenger))

# In certain programming languages like Python,
# arrays have dynamic sizes.
passenger.append(5)

print('len(passenger):', len(passenger))

# In Python, arrays are also mutable.
passenger[0] = 'Thomas'

print('passenger:', passenger)