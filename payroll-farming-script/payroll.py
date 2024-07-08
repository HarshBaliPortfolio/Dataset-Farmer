from faker import Faker
from openpyxl import Workbook

# Create a new Excel workbook
wb = Workbook()

# Create an instance of Faker class
fake = Faker()

# Select the active worksheet
ws = wb.active


# Add headers to the worksheet
headers =['First-Name','Last-Name',
        'Date-of-birth','Joining-Date', 
        'Address', 'Department', 'Salary', 
        'Gender', 'NI number', 'Right-to-work' ] 

ws.append(headers)

# Generate fake data and write it onto excel
for _ in range(1000):
    #Every time loop iterates the data is overwritten
    fake_data = [
        fake.first_name(),
        fake.last_name(),
        fake.address(),
        fake.date_of_birth(),
        fake.date_this_decade(),
        # Create departments 
        fake.random_element(elements=('HR', 'Artist', 'Producer', 'Promoter', 'Technician', 'Editor')),
        fake.random_number(digits=5),
        # Create Genders
        fake.random_element(elements=('Male', 'Female')),
        fake.random_number(digits=9),
        fake.boolean()
    ]
    ws.append(fake_data)

# Save the workbook
wb.save('payroll-data.xlsx')
