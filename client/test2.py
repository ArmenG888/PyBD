import os


current_dir = os.getcwd()
strr = os.getcwd()
x = -2
for i in os.getcwd():
    if i == "\\":
        x += 1
for i in range(x):
    os.chdir("..")


print(current_dir)

os.chdir(current_dir)
print(os.getcwd())
os.remove("test2.py")