import csv
import sys
from jinja2 import Template
import matplotlib.pyplot as plt

code1="""
<!DOCTYPE html>
    <html>
    <head>
        <title>Student Data</title>
    </head>
    <body>
        <h1>Student Details</h1>
        <table border="2" id="student-details-table">
            <tr>
                <th>Student ID</th>
                <th>Course ID</th>
                <th>Marks</th>
            </tr>
            {% for row in student_data %}
            <tr>
                {% for column in column_head %}
                <td>{{ row[column] }}</td>
                {% endfor %}
            </tr>
            {% endfor %}
            <tr>
                <td colspan="2" style="text-align:center">Total Marks</td>
                <td>{{ total_marks }}</td>
            </tr>
        </table>
    </body>
    </html> 
"""
code2= """
<!DOCTYPE html>
    <html>
    <head>
        <title>Course Details</title>
    </head>
    <body>
        <h1>Course Details</h1>
        <table border="2" id="course-details-table">
            <tr>
                <th>Average Marks</th>
                <th>Maximum Marks</th>
            </tr>
            <tr>
                <td>{{ average_marks }}</td>
                <td>{{ max_marks }}</td>
            </tr>
        </table>
        <img src="histogram.png" alt="Histogram">
    </body>
    </html>
"""

code3= """
 <!DOCTYPE html>
    <html>
    <head>
        <title>Something Went Wrong</title>
    </head>
    <body>
        <h1>Wrong Inputs</h1>
        <p>Something went wrong</p>
    </body>
    </html>
"""
def error():
    template = Template(code3)
    my_html_document_file = open('output.html', 'w')
    my_html_document_file.write(template.render())
    my_html_document_file.close()

data = []
column_heads = []
# Open the CSV file
with open('data.csv', mode='r') as file:
    table = csv.DictReader(file)
    column_heads = table.fieldnames
    for row in table:
        for column_head in column_heads:
            row[column_head] = int(row[column_head])
        data.append(row)

name=int(sys.argv[2])
flag=False
new_data=[]

# if arg is -s
if(sys.argv[1]=='-s'):
    total=0
    for row in data:
        if row[column_heads[0]] == name:
            total += row[column_heads[2]]
            new_data.append(row)
            flag=True
    if flag==False:
        error()
    else:
        template = Template(code1)
        my_html_document_file = open('output.html', 'w')
        my_html_document_file.write(template.render(student_data=new_data, total_marks=total, column_head=column_heads))
        my_html_document_file.close()

# if arg is -c
elif(sys.argv[1]=='-c'):
    total=0
    n=0
    avg=0.0
    max=0
    for row in data:
        if row[column_heads[1]] == name :
            new_data.append(row[column_heads[2]])
            total += row[column_heads[2]]
            n+=1
            flag=True
            if row[column_heads[2]] >= max:
                max=row[column_heads[2]]
    if flag==True:
        avg=total/n

        # Create histogram
        plt.figure(figsize=(6, 5))
        plt.hist(new_data, bins=10, edgecolor='black')
        # plt.title('Histogram of Student Marks')
        plt.xlabel('Marks')
        plt.ylabel('Frequency')

        # Save the histogram as an image
        image_path = 'histogram.png'
        plt.savefig(image_path)
        plt.close()

        template = Template(code2)
        my_html_document_file = open('output.html', 'w')
        my_html_document_file.write(template.render(average_marks=avg, max_marks=max))
        my_html_document_file.close()

    else:
        error()

# if wrong arg
else:
    error()