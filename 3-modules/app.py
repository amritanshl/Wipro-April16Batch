import hr_utils as hr


salary = hr.calculate_salary(40, 15)
print(f"Calculated Salary: ${salary:.2f}")
experience = 6
eligibility = hr.verify_experience(experience)
print(f"Experience: {experience} years")
print(f"Eligibility: {eligibility}")
print(f"Company Name: {hr.company_name}")