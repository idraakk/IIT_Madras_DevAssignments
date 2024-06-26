# IIT Madras - Modern Application Development Assignments

Welcome to my repository for the Modern Application Development course at IIT Madras. This README provides a week-by-week overview of the problems tackled, along with the topics and techniques covered.

## Table of Contents

1. [Week 2: HTML Lab Assignment](#week-2-html-lab-assignment)
   - [Overview](#overview)
   - [Pages and Requirements](#pages-and-requirements)
   - [Techniques and Learnings](#techniques-and-learnings)
   - [Included Files](#included-files)

2. [Week 3: Python Scripting, HTML Generation, and Data Visualization](#week-3-python-scripting-html-generation-and-data-visualization)
   - [Problem Statement](#problem-statement)
   - [Assignment Details](#assignment-details)
   - [Techniques and Topics Covered](#techniques-and-topics-covered)
   - [Frameworks and Libraries Used](#frameworks-and-libraries-used)
   - [Instructions to Run the Script](#instructions-to-run-the-script)
   - [Example Usage](#example-usage)
   - [Output](#output)
   - [Files in This Directory](#files-in-this-directory)


# Week 2: HTML Lab Assignment

### Overview

This week's task was to create a basic website with five HTML pages, focusing on fundamental HTML skills without using CSS.

### Pages and Requirements

1. **Home Page (`index.html`)**
   - **Header:** Links to Academics, Personal, Contact, Resume.
   - **Main Section:** Student data including name, roll number, and a brief introduction.
   - **Footer:** Student's name, batch, copyright, and year.

2. **Academics Page (`academics.html`)**
   - **Main Section:** Marks displayed in a table.
   - **Header & Footer:** Same as Home page.

3. **Personal Page (`personal.html`)**
   - **Main Section:** Two images and a link to the IITM Online Degree webpage.
   - **Header & Footer:** Same as Home page.

4. **Contact Page (`contact.html`)**
   - **Main Section:** Address and email ID using the `address` tag.
   - **Header % Footer:** Same as Home page.

5. **Resume Page (`resume.html`)**
   - **Main Section:** Link to download the resume.
   - **Header & Footer:** Same as Home page.

### Techniques and Learnings

- **HTML5 Compliance**
- **Structured Layouts with `div` Tags**
- **Navigation with Anchor (`a`) Tags**
- **Data Display with Tables**
- **Embedding Images and Links**
- **Using Semantic Tags like `address`**

### Included Files

- `index.html`
- `academics.html`
- `personal.html`
- `contact.html`
- `resume.html`
- Images for the personal page


# Week 3: Python Scripting, HTML Generation, and Data Visualization

### Problem Statement
In Week 3, we focused on using Python to process data from a CSV file and generate HTML output. The assignment involved creating a Python script (`app.py`) that reads student marks from a CSV file and produces an HTML page based on user input.

### Assignment Details
The tasks for this week required us to:

1. **Read and Process CSV Data**: The CSV file (`data.csv`) contains student IDs, course IDs, and marks.
2. **Command Line Arguments**: The script takes two command line arguments:
    - A flag (`-s` for student ID or `-c` for course ID).
    - The actual student ID or course ID.
3. **Generate HTML Output**:
    - For a student ID, display the student's marks in a tabular format.
    - For a course ID, display the highest and average marks for the course, along with a histogram.
4. **Error Handling**: Ensure proper error messages for invalid inputs.

### Techniques and Topics Covered
- **Python File Handling**: Reading data from CSV files using Python's `csv` module. I converted the csv table into python dictionary
- **Command Line Interfaces**: Using `sys.argv` to handle command line arguments
- **Data Processing**: Calculating total marks, average marks, and finding the maximum mark.
- **HTML Generation**: Creating HTML pages dynamically with Python.
- **Data Visualization**: Plotting histograms using `matplotlib`.
- **Error Handling**: Implementing robust error handling to manage incorrect inputs gracefully.

### Frameworks and Libraries Used
- **Python**: The main programming language used for scripting and data processing.
- **csv**: Standard library for reading and writing CSV files.
- **matplotlib**: A powerful library for creating static, animated, and interactive visualizations in Python.
- **sys**: Standard library for accessing command line arguments.
- **pyhtml**: A lightweight library for generating HTML.
- **jinja2**: A modern and designer-friendly templating engine for Python.

### Instructions to Run the Script
1. **Ensure Required Packages are Installed**:
   ```bash
   pip install matplotlib pyhtml jinja2
   ```
2. **Command to Run the Script**:
   ```bash
   python app.py -s <student_id>
   python app.py -c <course_id>
   ```
   - Replace `<student_id>` with the actual student ID.
   - Replace `<course_id>` with the actual course ID.

### Example Usage
- To get details for a student with ID `101`:
  ```bash
  python app.py -s 1001
- To get details for a course with ID `201`:
  ```bash
  python app.py -c 2001
### Output
- **Student Details Page**:
  Displays the student ID, course IDs, and marks in a table, along with the total marks.

- **Course Details Page**:
  Shows the average and maximum marks for the course, along with a histogram of marks distribution.

### Files in This Directory
- `app.py`: The main Python script for this assignment.
- `data.csv`: The CSV file containing student marks (provided by IIT Madras).
- `output.html`: The generated HTML output file.

  
