"""
Practical 7 Project Management
Estimated time taken to complete: 1 hour
Actual time taken to complete: 1h 15 mins
"""

import datetime
from project import Project

def parse_date(date_str):
    """Convert a string in dd/mm/yyyy format to a date object."""
    return datetime.datetime.strptime(date_str, "%d/%m/%Y").date()

def filter_projects(projects):
    """Filter and display projects that start after a given date."""
    date_str = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = parse_date(date_str)
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")
        return

    filtered_projects = [p for p in projects if p.start_date > filter_date]
    filtered_projects.sort(key=lambda p: p.start_date)

    if not filtered_projects:
        print("No projects found starting after that date.")
    else:
        for project in filtered_projects:
            print(f"{project.name}, start: {project.start_date.strftime('%d/%m/%Y')}, priority {project.priority}, estimate: ${project.cost_estimate:.2f}, completion: {project.completion_percentage}%")

def load_projects_from_file(filename):
    """Load projects from a file and return a list of Project objects."""
    loaded_projects = []
    try:
        with open(filename, 'r') as file:
            next(file)  # skip header line
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split('\t')
                if len(parts) != 5:
                    print(f"Skipping malformed line: {line}")
                    continue
                name, start_date_str, priority_str, cost_estimate_str, completion_percentage_str = parts
                try:
                    start_date = parse_date(start_date_str)
                    priority = int(priority_str)
                    cost_estimate = float(cost_estimate_str)
                    completion_percentage = int(completion_percentage_str)
                    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
                    loaded_projects.append(project)
                except ValueError as e:
                    print(f"Error parsing line: {line} ({e})")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except IOError as e:
        print(f"Error reading file '{filename}': {e}")
    return loaded_projects

def save_projects_to_file(filename, project_list):
    """Save a list of Project objects to a file."""
    try:
        with open(filename, 'w') as file:
            file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
            for project in project_list:
                line = f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n"
                file.write(line)
    except IOError as e:
        print(f"Error writing to file '{filename}': {e}")

def display_projects(project_list):
    """Display projects categorized into incomplete and completed, sorted by priority."""
    if not project_list:
        print("No projects to display.")
        return

    incomplete_projects = [p for p in project_list if p.completion_percentage < 100]
    completed_projects = [p for p in project_list if p.completion_percentage == 100]

    incomplete_projects.sort(key=lambda p: p.priority)
    completed_projects.sort(key=lambda p: p.priority)

    if incomplete_projects:
        print("Incomplete projects:")
        for p in incomplete_projects:
            print(f"  {p.name}, start: {p.start_date.strftime('%d/%m/%Y')}, priority {p.priority}, estimate: ${p.cost_estimate:.2f}, completion: {p.completion_percentage}%")
    else:
        print("No incomplete projects.")

    if completed_projects:
        print("Completed projects:")
        for p in completed_projects:
            print(f"  {p.name}, start: {p.start_date.strftime('%d/%m/%Y')}, priority {p.priority}, estimate: ${p.cost_estimate:.2f}, completion: {p.completion_percentage}%")
    else:
        print("No completed projects.")

def add_new_project(project_list):
    """Prompt user for project details and add a new Project to the list."""
    print("Let's add a new project")
    name = input("Name: ").strip()
    start_date_str = input("Start date (dd/mm/yyyy): ").strip()
    try:
        start_date = parse_date(start_date_str)
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")
        return
    try:
        priority = int(input("Priority: ").strip())
    except ValueError:
        print("Invalid priority. Must be an integer.")
        return
    try:
        cost_estimate = float(input("Cost estimate: ").strip())
    except ValueError:
        print("Invalid cost estimate. Must be a number.")
        return
    try:
        completion_percentage = int(input("Percent complete: ").strip())
        if not (0 <= completion_percentage <= 100):
            print("Completion percentage must be between 0 and 100.")
            return
    except ValueError:
        print("Invalid completion percentage. Must be an integer between 0 and 100.")
        return

    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    project_list.append(project)
    print(f"Project '{name}' added.")

def update_project(project_list):
    """Allow user to update the completion percentage and/or priority of a selected project."""
    if not project_list:
        print("No projects to update.")
        return
    print("Projects:")
    for i, project in enumerate(project_list):
        print(f"{i} {project}")
    try:
        index_str = input("Project choice: ").strip()
        index = int(index_str)
        if not (0 <= index < len(project_list)):
            print("Invalid project number.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid project number.")
        return

    project = project_list[index]
    completion_str = input(f"New completion percentage (current: {project.completion_percentage}%): ").strip()
    if completion_str:
        try:
            completion = int(completion_str)
            if 0 <= completion <= 100:
                project.completion_percentage = completion
            else:
                print("Completion percentage must be between 0 and 100. Keeping previous value.")
        except ValueError:
            print("Invalid completion percentage. Keeping previous value.")

    priority_str = input(f"New priority (current: {project.priority}): ").strip()
    if priority_str:
        try:
            priority = int(priority_str)
            project.priority = priority
        except ValueError:
            print("Invalid priority. Keeping previous value.")

if __name__ == "__main__":
    # Assuming Project class and projects list are defined elsewhere
    print("Welcome to Pythonic Project Management")
    projects = load_projects_from_file("projects.txt")
    print(f"Loaded {len(projects)} projects from projects.txt")
    default_filename = "projects.txt"

    while True:
        print("\nMenu:")
        print("- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")
        choice = input("Choose an option: ").strip().upper()

        if choice == 'L':
            filename = input(f"Enter filename to load from (default: {default_filename}): ").strip()
            if not filename:
                filename = default_filename
            loaded_projects = load_projects_from_file(filename)
            if loaded_projects:
                projects = loaded_projects
                print(f"Loaded {len(projects)} projects from {filename}.")
            else:
                print("No projects loaded.")
        elif choice == 'S':
            filename = input(f"Enter filename to save to (default: {default_filename}): ").strip()
            if not filename:
                filename = default_filename
            save_projects_to_file(filename, projects)
            print(f"Projects saved to {filename}.")
        elif choice == 'F':
            if projects:
                filter_projects(projects)
            else:
                print("No projects to filter.")
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'A':
            add_new_project(projects)
        elif choice == 'U':
            update_project(projects)
        elif choice == 'Q':
            save_choice = input("Would you like to save to projects.txt? ").strip()
            if save_choice and save_choice[0].upper() == 'Y':
                save_projects_to_file(default_filename, projects)
                print(f"Projects saved to {default_filename}.")
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid option, please try again.")
