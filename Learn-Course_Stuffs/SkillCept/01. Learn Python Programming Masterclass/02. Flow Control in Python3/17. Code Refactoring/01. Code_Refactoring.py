# Code Refactoring means : changing the its structure(how it looks) without changing its behaviour(what it works).
# In VS Code use Replace

# old code:-
# ----------------------------------------------------
# splitString = "Welcom\nHow are you?"
# print(splitString)

# tabbedString = "1\t2\t3\t4\t5"
# print(tabbedString)

# anotherString = """
# Welcome \
# to\
#  the\
#  den.
# """
# print(anotherString)
# -----------------------------------------------------


# New Code -----------------------------------------
split_string = "Welcom\nHow are you?"
print(split_string)

tabbed_string = "1\t2\t3\t4\t5"
print(tabbed_string)

another_string = """
Welcome \
to\
 the\
 den.
"""
print(another_string)


