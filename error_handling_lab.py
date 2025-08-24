# error_handling_lab.py

filename = input("Micklech/FILE_HANDLING/input.txt ")

try:
    with open(filename, "r") as file:
        print("\n📂 File content:\n")
        print(file.read())
except FileNotFoundError:
    print(f"❌ Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"⚠️ Error: You don't have permission to read '{filename}'.")
except Exception as e:
    print(f"⚠️ An unexpected error occurred: {e}")
