# Romain Tranchant
# CIS 103 Fundamentals of Programming
# Instructor: MD Ali
# To Do List

# Initialize an empty to-do list
to_do_list = []

def add_task(priority, task):
# Add a task with priority and a completed flag (initially False)
    to_do_list.append((priority, task, False))

def show_task():
# Print header for the task list
    print(f"{'Priority':<10} {'Task':<25} {'Status':<10}")

# Show all tasks, indicating whether they are completed
    for priority, task, completed in sorted(to_do_list):
# Determine the status of the task
        status = "Completed" if completed else "Pending"
# Print the task details
        print(f"{priority:<10} {task:<25} {status:<10}")

def complete_task(task):
    global to_do_list
# Find the task and mark it as completed
    for i in range(len(to_do_list)):
        if to_do_list[i][1] == task and not to_do_list[i][2]:
# Update the task to set completed to True
            to_do_list[i] = (to_do_list[i][0], to_do_list[i][1], True)

# Adding tasks to the list
add_task(1, "Finish lab report")
add_task(4, "Go grocery shopping")
add_task(2, "Call Mom")
add_task(3, "Fix vehicle")
add_task(5, "Cook dinner")

# Show all tasks before completion
print("To-Do List:")
show_task()

# Mark tasks as completed
complete_task("Call Mom")
complete_task("Cook dinner")

# Show all tasks after marking some as completed
print("\nUpdated To-Do List (After completing 'Call Mom' and 'Cook dinner):")
show_task()
