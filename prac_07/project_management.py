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

def main():
    projects = load_projects_from(DEFAULT_FILE)
    print(f"{len(projects)} projects loaded")
    # exit for now, menu to be added later

if __name__ == "__main__":
    main()
