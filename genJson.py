import os
import json


# Directory containing student Python code files
students_code_dir = "StudentsCode"


# Output JSON file
output_file = "students.json"


# List to store student data
students = []


# Loop through files in the directory
for file_name in os.listdir(students_code_dir):
    if file_name.endswith(".py"):  # Only process Python files
        student_code = file_name.replace(".py", "")  # Remove .py extension
        student_name = student_code  # Use the file name without .py as the name (customize as needed)
        student_path = os.path.join(students_code_dir, file_name)  # Relative path to the file
        
        # Add student data to the list
        students.append({
            "name": student_name,
            "codeFile": student_path
        })


# Write data to JSON file
with open(output_file, "w") as json_file:
    json.dump(students, json_file, indent=4)


print(f"Generated {output_file} with {len(students)} entries.")
