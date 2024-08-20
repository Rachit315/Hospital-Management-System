# Hospital Management System in Python

Welcome to the **Hospital Management System** project. This is a simple Python program designed to help manage basic hospital operations such as admitting patients, scheduling appointments, and viewing patient information.


## Prerequisites

To run this project, you'll need to have Python installed on your computer. You can download it from [here](https://www.python.org/downloads/).

## How to Run the Project

1. **Clone the Repository:** 
   ```bash
   git clone https://github.com/yourusername/hospital-management-system.git
   ```
2. **Navigate to the Project Directory:** 
   ```bash
   cd hospital-management-system
   ```
3. **Run the Python Script:**
   ```bash
   python hospital_management_system.py
   ```

## Code Structure

The code is organized into functions to keep it simple and readable. Here are the main components used:

- **Functions:**
  - `register_patient()`: Adds a new patient to the system.
  - `schedule_appointment()`: Schedules appointments for patients.
  - `assign_doctor()`: Assigns a doctor to a patient.
  - `view_patients()`: Displays the list of registered patients.

- **Data Handling:**
  - Patient information is stored in a list for easy access and modification.

- **User Input:**
  - The system uses simple input prompts to get data from the user, like patient details and appointment schedules.

## Example Code Snippet

```python
def register_patient():
    name = input("Enter patient's name: ")
    age = input("Enter patient's age: ")
    gender = input("Enter patient's gender: ")
    contact = input("Enter contact number: ")

    patient = {
        'name': name,
        'age': age,
        'gender': gender,
        'contact': contact
    }
    patients.append(patient)
    print(f"Patient {name} registered successfully!\n")
```

## Technologies Used

- **Python**: The entire system is built using Python.
- **Basic Data Structures**: Lists and dictionaries are used to manage patient data and appointments.

## Future Enhancements

Some possible improvements for this project include:
- Storing patient information in a file or a database.
- Adding login functionality for doctors and hospital staff.
- Implementing search functionality for patient records.
  
