import sys

print("Print file content:")
with open(sys.argv[1], "r") as f:
    for line in f.readlines():
        print(line)


print("\n===================")
print("Open file twice:")
try:
    with open(sys.argv[1], "r") as f:
        with open(sys.argv[1], "r") as f2:
            print("File opened")
except:
    print("Failed to open file second time")
    raise
