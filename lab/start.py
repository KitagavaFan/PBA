import os
while True:
    print("Enter the number of the desired section.\n" \
    "(1).Build the project\n" \
    "(version) show version")
    inp = input("[LabProject]: ")
    os.system("cls")
    if inp == "1":
        print("building")
    elif inp == "version":
        print("LaboratoryVersion")
    elif inp == "exit":
        break
    