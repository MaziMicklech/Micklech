# file_read_write.py

try:
    # Open input file to read
    with open("Micklech/FILE_HANDLING/input.txt", "r") as infile:
        content = infile.read()

    # Modify content (make it uppercase as an example)
    modified_content = content.upper()

    # Write modified content to a new file
    with open("output.txt", "w") as outfile:
        outfile.write(modified_content)

    print("✅ File has been read, modified, and written to output.txt")

except FileNotFoundError:
    print("❌ input.txt not found. Please make sure the file exists.")
