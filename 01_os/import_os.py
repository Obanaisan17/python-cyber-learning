import os

f = "os_test.py"

# result = os.path.isfile(f)
result = os.path.isfile("/home/theo/Documents/os_test.py")
print(result)

if os.path.isfile(f):
    print(f, "existe")
else:
    print(f, "existe pas")

print("\n")
print(os.getcwd())
print(os.listdir("/home/theo"))

print("\nCMD")

# os.system("mkdir test")

for actual, dirs, files in os.walk("/home/theo"):
    print(actual)
    print(dirs)
    print(files)
    print("\n")
