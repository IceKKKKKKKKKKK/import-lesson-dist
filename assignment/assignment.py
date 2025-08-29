import subdir1.subdir2.file3


import subdir1.subdir2.file3 as ssf3


from subdir1.subdir2.file3 import divide


from subdir3.new_module import oh_my

# if __name__ == "__main__":
    
#     print("Access via namespace:", assignment.subdir1.subdir2.file3.add(2, 3))
#     print("Access via ssf3 alias:", ssf3.add(10, 5))
#     print("Divide via from-import:", divide(10, 2))
#     print("From new_module:", oh_my)

# create a new subdirectory `assignment.subdir1.subdir2.file3.py` and move this 
# code into it.

#def add(summand1, summand2):
#    return summand1 + summand2

# def divide(dividand1, dividand2):
#    return dividand1 / dividand2

# Do not uncomment the code and leave it in this file.

# In this file, import the code using `import` but do not use `as` or `from` -- 
# we want it to be referenced via the full namespace prefix.


# Now add another `import` statement that imports the same module as `ssf3`
# Importing the same module twice is not something you would do in real life --
# it's just for purposes of this exercise.


# Now use `from` to import `divide` into the global namespace. 
# Do not import `add` into the global namespace.


# Now create a new subdirectory under `assignment` called `subdir3`. Put a file
# called `new_module.py` there. Move the following code into it:

# oh_my = "Oh my!"

# Do not leave it in this file.

# Now import it by name using `from`.
