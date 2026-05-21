# %d = digit
# %s = string
# %f = float
# %() = parameters
# %x = hexadecimal
# %o = ocatal
# %e = scientific numbers

age = 24
age2 = 6
y = "years"
m = "months"

print("My age is %d years" %age)
print()
print("My age is %d %s %d %s" %(age, y, age2, m))
print()
print("Value of PI is %f" %(22/7))
print()
print("Value of PI is %60.50f" %(22/7))