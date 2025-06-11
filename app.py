# Student Grade Management System using Python Functions and If-Else

# Global dictionary to store student data
students = {}

def add_student(student_id, name):
    """Add a new student to the system"""
    if student_id in students:
        print(f"Student with ID {student_id} already exists!")
        return False
    else:
        students[student_id] = {
            'name': name,
            'grades': []
        }
        print(f"Student {name} added successfully with ID: {student_id}")
        return True

def add_grade(student_id, subject, grade):
    """Add a grade for a specific student"""
    if student_id not in students:
        print(f"Student with ID {student_id} not found!")
        return False
    else:
        if 0 <= grade <= 100:
            students[student_id]['grades'].append({
                'subject': subject,
                'grade': grade
            })
            print(f"Grade {grade} added for {subject} to student {students[student_id]['name']}")
            return True
        else:
            print("Grade must be between 0 and 100!")
            return False

def calculate_average(student_id):
    """Calculate average grade for a student"""
    if student_id not in students:
        print(f"Student with ID {student_id} not found!")
        return None
    else:
        grades = students[student_id]['grades']
        if len(grades) == 0:
            print(f"No grades found for student {students[student_id]['name']}")
            return None
        else:
            total = sum(grade['grade'] for grade in grades)
            average = total / len(grades)
            return round(average, 2)

def get_letter_grade(average):
    """Convert numerical average to letter grade"""
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def get_grade_status(average):
    """Determine if student is passing or failing"""
    if average >= 60:
        return "Passing"
    else:
        return "Failing"

def display_student_report(student_id):
    """Display detailed report for a specific student"""
    if student_id not in students:
        print(f"Student with ID {student_id} not found!")
        return False
    else:
        student = students[student_id]
        print(f"\n=== STUDENT REPORT ===")
        print(f"Student ID: {student_id}")
        print(f"Name: {student['name']}")
        
        if len(student['grades']) == 0:
            print("No grades recorded yet.")
        else:
            print("\nGrades:")
            for grade_info in student['grades']:
                print(f"  {grade_info['subject']}: {grade_info['grade']}")
            
            average = calculate_average(student_id)
            letter_grade = get_letter_grade(average)
            status = get_grade_status(average)
            
            print(f"\nAverage: {average}")
            print(f"Letter Grade: {letter_grade}")
            print(f"Status: {status}")
        
        print("=" * 25)
        return True

def display_all_students():
    """Display summary of all students"""
    if len(students) == 0:
        print("No students in the system.")
        return False
    else:
        print(f"\n=== ALL STUDENTS SUMMARY ===")
        print(f"{'ID':<5} {'Name':<15} {'Avg':<6} {'Grade':<5} {'Status':<10}")
        print("-" * 45)
        
        for student_id, student_data in students.items():
            name = student_data['name']
            average = calculate_average(student_id)
            
            if average is None:
                avg_str = "N/A"
                letter = "N/A"
                status = "N/A"
            else:
                avg_str = str(average)
                letter = get_letter_grade(average)
                status = get_grade_status(average)
            
            print(f"{student_id:<5} {name:<15} {avg_str:<6} {letter:<5} {status:<10}")
        
        print("=" * 45)
        return True

def find_top_performers():
    """Find students with highest averages"""
    if len(students) == 0:
        print("No students in the system.")
        return []
    
    student_averages = []
    for student_id, student_data in students.items():
        average = calculate_average(student_id)
        if average is not None:
            student_averages.append({
                'id': student_id,
                'name': student_data['name'],
                'average': average
            })
    
    if len(student_averages) == 0:
        print("No students with grades found.")
        return []
    
    # Sort by average in descending order
    student_averages.sort(key=lambda x: x['average'], reverse=True)
    
    print(f"\n=== TOP PERFORMERS ===")
    for i, student in enumerate(student_averages[:5], 1):  # Top 5
        letter_grade = get_letter_grade(student['average'])
        print(f"{i}. {student['name']} (ID: {student['id']}) - {student['average']} ({letter_grade})")
    
    return student_averages

def get_students_by_status(status_filter):
    """Get students based on passing/failing status"""
    if len(students) == 0:
        print("No students in the system.")
        return []
    
    filtered_students = []
    for student_id, student_data in students.items():
        average = calculate_average(student_id)
        if average is not None:
            status = get_grade_status(average)
            if status.lower() == status_filter.lower():
                filtered_students.append({
                    'id': student_id,
                    'name': student_data['name'],
                    'average': average,
                    'status': status
                })
    
    if len(filtered_students) == 0:
        print(f"No {status_filter.lower()} students found.")
    else:
        print(f"\n=== {status_filter.upper()} STUDENTS ===")
        for student in filtered_students:
            letter_grade = get_letter_grade(student['average'])
            print(f"{student['name']} (ID: {student['id']}) - {student['average']} ({letter_grade})")
    
    return filtered_students

def menu():
    """Display main menu and handle user input"""
    while True:
        print(f"\n=== STUDENT GRADE MANAGEMENT SYSTEM ===")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. View Student Report")
        print("4. View All Students")
        print("5. Find Top Performers")
        print("6. View Passing Students")
        print("7. View Failing Students")
        print("8. Exit")
        
        choice = input("\nEnter your choice (1-8): ").strip()
        
        if choice == '1':
            student_id = input("Enter Student ID: ").strip()
            name = input("Enter Student Name: ").strip()
            if student_id and name:
                add_student(student_id, name)
            else:
                print("Please provide both Student ID and Name!")
        
        elif choice == '2':
            student_id = input("Enter Student ID: ").strip()
            subject = input("Enter Subject: ").strip()
            try:
                grade = float(input("Enter Grade (0-100): "))
                if student_id and subject:
                    add_grade(student_id, subject, grade)
                else:
                    print("Please provide Student ID and Subject!")
            except ValueError:
                print("Please enter a valid number for grade!")
        
        elif choice == '3':
            student_id = input("Enter Student ID: ").strip()
            if student_id:
                display_student_report(student_id)
            else:
                print("Please provide Student ID!")
        
        elif choice == '4':
            display_all_students()
        
        elif choice == '5':
            find_top_performers()
        
        elif choice == '6':
            get_students_by_status("Passing")
        
        elif choice == '7':
            get_students_by_status("Failing")
        
        elif choice == '8':
            print("Thank you for using the Student Grade Management System!")
            break
        
        else:
            print("Invalid choice! Please enter a number between 1-8.")

# Demo function to show system functionality
def demo():
    """Demonstrate the system with sample data"""
    print("=== DEMO: Adding Sample Data ===")
    
    # Add sample students
    add_student("001", "Alice Johnson")
    add_student("002", "Bob Smith")
    add_student("003", "Carol Davis")
    
    # Add sample grades
    add_grade("001", "Math", 95)
    add_grade("001", "Science", 88)
    add_grade("001", "English", 92)
    
    add_grade("002", "Math", 78)
    add_grade("002", "Science", 82)
    add_grade("002", "English", 75)
    
    add_grade("003", "Math", 55)
    add_grade("003", "Science", 58)
    
    print("\n=== DEMO: Displaying Reports ===")
    display_all_students()
    find_top_performers()
    get_students_by_status("Passing")
    get_students_by_status("Failing")

# Main execution
if __name__ == "__main__":
    print("Welcome to the Student Grade Management System!")
    choice = input("Would you like to run the demo first? (y/n): ").strip().lower()
    
    if choice == 'y' or choice == 'yes':
        demo()
    
    menu()