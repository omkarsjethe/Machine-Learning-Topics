import pandas as pd
import random

# Sample data pools
job_titles = ['Data Analyst', 'ML Engineer', 'Data Scientist', 'Business Analyst', 'Software Developer']
companies = ['TCS', 'Infosys', 'Accenture', 'Wipro', 'IBM', 'Capgemini', 'Deloitte', 'ZS Associates', 'EY', 'Cognizant']
locations = ['Mumbai', 'Bangalore', 'Hyderabad', 'Pune', 'Chennai', 'Delhi', 'Kolkata', 'Remote']
salary_ranges = {
    'Data Analyst': (4, 9),
    'ML Engineer': (6, 15),
    'Data Scientist': (6, 18),
    'Business Analyst': (5, 12),
    'Software Developer': (4, 14)
}

# Function to create salary string
def generate_salary(role):
    low, high = salary_ranges[role]
    salary_low = random.randint(low, high - 1)
    salary_high = random.randint(salary_low + 1, high)
    return f"₹{salary_low}L–₹{salary_high}L"

# Generate data
data = []
for _ in range(300):
    title = random.choice(job_titles)
    company = random.choice(companies)
    location = random.choice(locations)
    salary = generate_salary(title)
    experience = f"{random.randint(0, 6)}–{random.randint(1, 10)} yrs"
    
    data.append({
        "Job Title": title,
        "Company": company,
        "Location": location,
        "Salary Estimate": salary,
        "Experience Required": experience
    })

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("fake_glassdoor_jobs.csv", index=False)

df


