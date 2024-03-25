# MongoDB Database Manager

## Description:
This project is a Python script that serves as a database manager for MongoDB. It provides functionalities to interact 
with MongoDB collections containing information about students, advisors, and their relationships. The script offers 
basic CRUD operations (Create, Read, Update, Delete) along with specific operations tailored to the aforementioned 
collections.

## Features:

- Add Data: Add data to any specified collection. It checks for duplicate entries before insertion.
- List Data: Retrieve and list all documents from a specified collection.
- Delete Row: Delete a specific document from a collection based on the provided row ID.
- Search: Find and return documents from a collection based on a provided query.
- Update: Update a document in a collection based on a query with new data.
- List Students/Advisors: Retrieve and list all students or advisors stored in their respective collections.
- List Student-Advisor Relations: Retrieve and list all relationships between students and advisors.
- List Advisors with No Students: Retrieve advisors who currently have no associated students.
- Count Most Students Advisor: Identify the advisor with the most associated students.
- List Advisors with Students: Retrieve advisors along with the students associated with each advisor.

## Setup:

1. Ensure you have Python installed on your system.  
Install the required dependencies using pip:
> pip install pymongo

2. Make sure MongoDB server is installed and running on your local machine. Adjust connection settings in the 
script if necessary.


## Usage:

1. Import the DatabaseManager class from the script into your Python project.
2. Initialize an instance of DatabaseManager with the desired MongoDB database name.
3. Utilize the provided methods to interact with the database collections as needed.

you can test the methods by write example code in the main function.
for example:
```python
if __name__ == "__main__":
    db_manager = DatabaseManager("students_advisors")
    db_manager.add_data("students", {"name": "John Doe", "major": "Computer Science", "GPA": 3.5})
    db_manager.add_data("advisors", {"name": "Jane Smith", "department": "Engineering"})
    db_manager.list_data("students")
    db_manager.list_data("advisors")
    db_manager.delete_row("students", {"name": "John Doe"})
    db_manager.search("advisors", {"name": "Jane Smith"})
    db_manager.update("advisors", {"name": "Jane Smith"}, {"department": "Computer Science"})
    db_manager.list_students()
    db_manager.list_advisors()
    db_manager.list_student_advisor_relations()
    db_manager.list_advisors_no_students()
    db_manager.count_most_students_advisor()
    db_manager.list_advisors_students()
```

>>Gvantsa
