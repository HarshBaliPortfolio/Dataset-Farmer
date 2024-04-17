import openpyxl

# Create a new Excel workbook
wb = openpyxl.Workbook()

# Select the active worksheet
ws = wb.active

# Add headers to the worksheet
headers =['First-Name','Last-Name',
        'Date-of-birth','Joining-Date', 
        'Address', 'Position', 'Salary', 
        'Gender', 'NI number', 'Right-to-work' ] 

# Insert columns for headers
for idx, header in enumerate(headers, start=1):
    ws.insert_cols(idx)
    ws.cell(row=1, column=idx, value=header)


# Save the workbook
wb.save('example.xlsx')
