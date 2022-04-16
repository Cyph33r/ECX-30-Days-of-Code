from re import match


def student_or_prof():
    student = []  # student emails
    profs = []  # professor emails
    invalid = []  # invalid emails
    emails = []  # input, to be populated by the user
    student_pattern = r'^[a-z|A-Z]([a-zA-Z0-9])*@student.college.edu$'  # regex pattern for student email
    prof_pattern = r'^[a-z|A-Z]([a-zA-Z0-9])*@prof.college.edu$'  # regex pattern professor email
    print('Welcome to Student or Prof. I will determine if you are a student or professor.')
    num_email = input('How many email addresses would you be entering: ').strip()
    while not num_email.isnumeric():  # ensure the input is a number
        print('Invalid response. Let\'s try that again.')
        num_email = input('How many email addresses you be entering: ').strip()
    for i in range(1, int(num_email) + 1):
        emails.append(input(f'Enter email {i}: ').strip())  # collect the emails without validating
    for email in emails:
        if match(student_pattern, email):  # check if student email
            student.append(email)
            continue
        if match(prof_pattern, email):
            profs.append(email)  # check of prof email
            continue
        invalid.append(email)  # else email is invalid
    print(
        f'\n{len(profs)} professor(s) found ({profs})\n'
        f'{len(student)} student(s) found ({student})\n'
        f'{len(invalid)} email(s) were invalid ({invalid})')


if __name__ == '__main__':
    student_or_prof()
