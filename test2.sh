#!/bin/bash

# Check if the group number is provided as a command line argument
if [ $# -eq 0 ]; then
  echo "Usage: $0 <group_number>"
  exit 1
fi

group_number=$1

# Create a folder with the group number
folder_name="Temp-Group${group_number}-gtf65dg"
mkdir "$folder_name"

# Unzip the file into the folder
unzip "Group${group_number}.zip" -d "$folder_name"

# Change directory to the folder
cd "$folder_name"

# Define the input string
input_strings=($'8 4\n12 5 8 9 11 13 16 1' $'8 4 4\n12 5 8 9 11 13 16 1')

# Define the expected output strings for each task
expected_outputs=("0 3 7" "0 1 3 7")


# Function to run a task and compare its output
function grade_task {
  task_number=$1
  problem_number=$2

  input_string="${input_strings[$problem_number - 1]}"
  expected_output="${expected_outputs[$problem_number - 1]}"

  # Run the task using 'make runX' and capture the output
  task_output=$(make -s run$task_number <<< "$input_string")

  # Remove trailing newline characters from both outputs
  task_output=$(echo -n "$task_output" | sed -e 's/[[:space:]]*$//')

  # Compare the output with the expected output
  echo "Task $task_number Ouput: $task_output"
  if [ "$task_output" == "$expected_output" ]; then
    echo "Task $task_number Status: Passed"
  else
    echo "Task $task_number: Failed"
  fi
}

# Compile the code using 'make'
make -s

# Loop through each task for problem 1 and grade it
for task_num in 1 2A 2B 3 4; do
  grade_task $task_num 1
done

# Loop through each task for problem 2 and grade it
for task_num in 5 6A 6B 7 8; do
  grade_task $task_num 2
done

# Change back to the original directory
cd ..

# Delete the folder and its contents
rm -rf "$folder_name"