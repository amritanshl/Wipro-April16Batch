def calculate_package(base_salary, bonus=0, tax_rate=0.2):
    gross_salary = base_salary + bonus
    tax_amount = gross_salary * tax_rate
    net_salary = gross_salary - tax_amount
    return net_salary

def verify_experience(years_of_experience):
    if years_of_experience >= 5:
        return "Eligible for senior position"
    else:
        return "Not eligible for senior position"

company_name = "Tech Solutions Inc."