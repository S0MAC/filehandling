def read_and_modify_file():
    """Reads a file, modifies its content, and writes to a new file with error handling."""
    filename = input("Enter the filename to read: ")

    try:
        # Open the file for reading
        with open(filename, "r") as file:
            content = file.readlines()  # Read all lines into a list

        # Modify content (e.g., add line numbers)
        modified_content = [f"{i + 1}: {line}" for i, line in enumerate(content)]

        # Create a new filename
        new_filename = f"modified_{filename}"

        # Write modified content to a new file
        with open(new_filename, "w") as new_file:
            new_file.writelines(modified_content)

        print(f"Modified file saved as: {new_filename}")

    except FileNotFoundError:
        print("❌ Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("❌ Error: Permission denied. You don’t have access to this file.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

# Run the function
read_and_modify_file()
