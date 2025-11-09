import datetime

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
            print(project)

def load_projects_from_file(filename):
    """Load projects from a file and return a list of Project objects."""
    projects = []
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
                    projects.append(project)
                except ValueError as e:
                    print(f"Error parsing line: {line} ({e})")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except IOError as e:
        print(f"Error reading file '{filename}': {e}")
    return projects

def save_projects_to_file(filename, projects):
    """Save a list of Project objects to a file."""
    try:
        with open(filename, 'w') as file:
            file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
            for project in projects:
                line = f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n"
                file.write(line)
    except IOError as e:
        print(f"Error writing to file '{filename}': {e}")

def display_projects(projects):
    """Display projects categorized into incomplete and completed, sorted by priority."""
    if not projects:
        print("No projects to display.")
        return

    incomplete_projects = [p for p in projects if p.completion_percentage < 100]
    completed_projects = [p for p in projects if p.completion_percentage == 100]

    incomplete_projects.sort(key=lambda p: p.priority)
    completed_projects.sort(key=lambda p: p.priority)

    if incomplete_projects:
        print("Incomplete projects:")
        for p in incomplete_projects:
            print(f"{p.name}, Start: {p.start_date.strftime('%d/%m/%Y')}, Priority: {p.priority}, Cost: ${p.cost_estimate:.2f}, Completion: {p.completion_percentage}%")
    else:
        print("No incomplete projects.")

    if completed_projects:
        print("Completed projects:")
        for p in completed_projects:
            print(f"{p.name}, Start: {p.start_date.strftime('%d/%m/%Y')}, Priority: {p.priority}, Cost: ${p.cost_estimate:.2f}, Completion: {p.completion_percentage}%")
    else:
        print("No completed projects.")

if __name__ == "__main__":
    # Assuming Project class and projects list are defined elsewhere
    projects = []
    default_filename = "projects.txt"

    while True:
        print("\nMenu:")
        print("(L)oad projects")
        print("(S)ave projects")
        print("(F)ilter projects by start date")
        print("(D)isplay projects")
        print("(Q)uit")
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
        elif choice == 'Q':
            print("Exiting program.")
            break
        else:
            print("Invalid option, please try again.")
