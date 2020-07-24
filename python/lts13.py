my_list = [10,20,70]

# Note that for a single value tuple you need to specify the comma to tell Python this is a tuple,
# rather than an operational preference order. Optionally can remove the brackets and have "100,".
# Note that the missing comma seemed to work fine in my Python, but Udemy solution window gave me
# an error:
#   object of type 'int' has no len().
# Google search says "The reason why you are getting this error message is because you are 
# trying to call a method on an int type of a variable.". I am not even calling the length function.
# So very weird. Noting that solution window is only looking for very basic changes, not solutions,
# so not that smart interpreting. Keep solutions simple and specific to only answer the question as
# stated.

my_tuple = (100,)

# Modify set2 so that set1.intersection(set2) returns {5, 77, 9, 12}
set1 = {14, 5, 9, 31, 12, 77, 67, 8}
set2 = {5}
print("Before Intersection: ")
print(f"my_list = {my_list}")
print(f"my_tuple = {my_tuple}")
print(f"set1 = {set1}")
print(f"set2 = {set2}")

# Want to union {5} with {77, 9, 12} so 
set2 = set2.union({77, 9, 12})
print("After Union: ")
print(f"set2 = {set2}")
set3 = set1.intersection(set2)
print("After Intersection: ")
print(f"set3 = {set3}")
