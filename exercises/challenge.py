employees = [
    {"name": "Jane", "salary": 90000, "job_title": "developer"},
    {"name": "Bill", "salary": 50000, "job_title": "writer"},
    {"name": "Kathy", "salary": 120000, "job_title": "executive"},
    {"name": "Anna", "salary": 100000, "job_title": "developer"},
    {"name": "Dennis", "salary": 95000, "job_title": "developer"},
    {"name": "Albert", "salary": 70000, "job_title": "marketing specialist"},
]


dev_salaries = {
    employee["salary"] for employee in employees if employee["job_title"] == "developer"
}
print(
    f"The average developer salary of the people in the employees-dict is: {sum(dev_salaries) / len(dev_salaries)}."
)

non_dev_salaries = {
    employee["salary"] for employee in employees if employee["job_title"] != "developer"
}

print(
    f"The average non-developer salary of the people in the employees-dict is: {sum(non_dev_salaries) / len(non_dev_salaries)}."
)
