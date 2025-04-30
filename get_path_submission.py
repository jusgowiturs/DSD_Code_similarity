import os

class GetSubmission:
    @staticmethod
    def get_path_submission(path):
        submissions_by_student = {}  # Dictionary to store submissions grouped by student
        
        # Iterate over the items in the directory path
        for root, dirs, files in os.walk(path):
            if 'submission' in dirs:  # Check if 'submission' folder exists in the directory
                submission_folder = os.path.join(root, 'submission')  # Get full path to the 'submission' folder
                student_name = os.path.basename(root)  # Extract student name from the folder structure
                
                # Initialize the student's submission list if not already in the dictionary
                if student_name not in submissions_by_student:
                    submissions_by_student[student_name] = []
                
                # Append all file paths under the 'submission' folder
                for subfile in os.listdir(submission_folder):
                    subfile_path = os.path.join(submission_folder, subfile)
                    submissions_by_student[student_name].append(subfile_path)
        print(submissions_by_student)
        return submissions_by_student
    
    @staticmethod
    def display_submissions(submissions):
        # Display the results in a structured format
        for student, files in submissions.items():
            print(f"Student: {student}")
            for file in files:
                print(f"  - {file}")



