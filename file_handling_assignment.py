# Task 1: File Creation and Writing
try:
    # Opening the file in write mode
    with open("my_file.txt", "w") as file:
        # Writing three lines of text (mix of strings and numbers)
        file.write("This is the first line.\n")
        file.write("Second line, with number 2.\n")
        file.write("Third line, number 3 follows.\n")
    print("File created and initial content written.")

    # Task 2: Reading and Displaying the File Contents
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("\nFile content after writing:\n", content)

    # Task 3: Appending to the File
    with open("my_file.txt", "a") as file:
        file.write("Appending fourth line.\n")
        file.write("Here is the fifth line, number 5.\n")
        file.write("Finally, the sixth line.\n")
    print("Additional lines appended.")

    # Reading again to display updated file content
    with open("my_file.txt", "r") as file:
        updated_content = file.read()
        print("\nFile content after appending:\n", updated_content)

except FileNotFoundError as fnf_error:
    print(f"Error: {fnf_error}")
except PermissionError as p_error:
    print(f"Error: {p_error}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("File handling tasks completed.")
