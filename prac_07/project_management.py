import datetime
from project import Project

DEFAULT_FILE = "projects.txt"
DATE_FORMAT = "%d/%m/%Y"

def parse_date(date_str):
    return datetime.datetime.strptime(date_str, DATE_FORMAT).date()

def row_to_project(row):
    name = row[0]
    start_date = parse_date(row[1])
    priority = int(row[2])
    cost_estimate = float(row[3])
    completion_percentage = int(row[4])
    return Project(name, start_date, priority, cost_estimate, completion_percentage)

def project_to_row(project):
    return [
        project.name,
        project.start_date.strftime(DATE_FORMAT),
        str(project.priority),
        f"{project.cost_estimate:.2f}",
        str(project.completion_percentage)
    ]

def load_projects_from(filename):
    projects = []
    with open(filename, "r") as file:
        next(file)  # skip header
        for line in file:
            row = line.strip().split("\t")
            project = row_to_project(row)
            projects.append(project)
    return projects

def save_projects_to(filename, projects):
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            row = project_to_row(project)
            file.write("\t".join(row) + "\n")

def display_menu():
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")

def display_projects(projects):
    incomplete = [p for p in projects if p.completion_percentage < 100]
    completed = [p for p in projects if p.completion_percentage == 100]
    incomplete.sort(key=lambda p: p.priority)
    completed.sort(key=lambda p: p.priority)
    print("Incomplete projects:")
    for project in incomplete:
        print(f"  {project}")
    print("Completed projects:")
    for project in completed:
        print(f"  {project}")

def filter_projects(projects):
    date_str = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = parse_date(date_str)
    except ValueError:
        print("Invalid date format.")
        return
    filtered = [p for p in projects if p.start_date > filter_date]
    filtered.sort(key=lambda p: p.start_date)
    for project in filtered:
        print(project)

def add_project(projects):
    name = input("Name: ")
    while True:
        start_date_str = input("Start date (dd/mm/yyyy): ")
        try:
            start_date = parse_date(start_date_str)
            break
        except ValueError:
            print("Invalid date format.")
    while True:
        try:
            priority = int(input("Priority: "))
            break
        except ValueError:
            print("Invalid priority.")
    while True:
        try:
            cost_estimate = float(input("Cost estimate: "))
            break
        except ValueError:
            print("Invalid cost.")
    while True:
        try:
            completion_percentage = int(input("Percent complete: "))
            if 0 <= completion_percentage <= 100:
                break
            else:
                print("Completion percentage must be between 0 and 100.")
        except ValueError:
            print("Invalid percentage.")
    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)

def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    try:
        choice = int(input("Project choice: "))
        project = projects[choice]
    except (ValueError, IndexError):
        print("Invalid project choice.")
        return
    print(project)
    # Update completion percentage
    try:
        new_completion = input("New Percentage (leave blank to skip): ")
        if new_completion:
            new_completion = int(new_completion)
            if 0 <= new_completion <= 100:
                project.completion_percentage = new_completion
            else:
                print("Completion percentage must be between 0 and 100.")
    except ValueError:
        print("Invalid percentage.")
    # Update priority
    try:
        new_priority = input("New Priority (leave blank to skip): ")
        if new_priority:
            project.priority = int(new_priority)
    except ValueError:
        print("Invalid priority.")

def main():
    projects = load_projects_from(DEFAULT_FILE)
    print(f"{len(projects)} projects loaded")
    while True:
        display_menu()
        choice = input(">>> ").strip().upper()
        if choice == "L":
            filename = input("Filename: ")
            try:
                projects = load_projects_from(filename)
                print(f"{len(projects)} projects loaded from {filename}")
            except (FileNotFoundError, IndexError):
                print("Could not load file.")
        elif choice == "S":
            filename = input("Filename: ")
            save_projects_to(filename, projects)
            print(f"{len(projects)} projects saved to {filename}")
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        elif choice == "Q":
            save = input(f"Save to {DEFAULT_FILE}? (Y/n): ").strip().lower()
            if save == "" or save == "y":
                save_projects_to(DEFAULT_FILE, projects)
                print(f"{len(projects)} projects saved to {DEFAULT_FILE}")
            print("Thank you for using custom project management software.")
            break
        else:
            print("Invalid menu choice.")

if __name__ == "__main__":
    main()
