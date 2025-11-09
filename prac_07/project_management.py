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
