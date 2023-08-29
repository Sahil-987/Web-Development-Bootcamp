import os

print("Hello World")
# for i in os.listdir("../../Web-Development-Bootcamp/"):
#     print(i)


print(os.listdir("../main/Web Development Projects/"))
print(os.listdir("../main/Web Development Projects/rough/files-code/"))



print()
print("******** New Approach ********")
print()


# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Set the working directory to the script's directory
os.chdir(script_dir)

print(os.listdir("../files-code/"))
print(os.listdir("../../rough/"))
print(os.listdir("../../../Web Development Projects"))






