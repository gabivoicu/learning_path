import csv, sys


MAX_UNITS_PER_STUDENT = 5
OUTPUT_FILE = 'student_learning_paths.csv'


def read_domains_ordered_by_grade_from_file(domain_order_file):
    """Reads ordered domains from a given file and stores them in a tuple of tuples.
    Each tuple represents a grade level with its available domains in order, represented so:
    (('1', ('RF', 'RL', 'RI')),)
    'K' is replaced with '0' to make it easier to do comparisons.
    """
    domains_ordered_by_grade = ()
    with open(domain_order_file, 'r') as data_file:
        for row in data_file:
            row = row.strip()
            row = row.replace('K', '0')
            row_elements = row.split(',')
            grade_level = row_elements.pop(0)
            row_units = ((grade_level, tuple(row_elements)), )
            domains_ordered_by_grade = domains_ordered_by_grade + row_units
    return domains_ordered_by_grade


def read_student_test_scores_from_file(student_test_scores_file):
    """Reads student test score data from a given file and stores them in a list of dictionaries.
    Each student score is stored in a dictionary:
    {'RL': '3', 'Student Name': 'Albin Stanton', 'RF': '2', 'L': '3', 'RI': 'K'}
    """
    student_test_scores = []
    with open(student_test_scores_file, 'r') as data_file:
        file_reader = csv.DictReader(data_file)
        for row in file_reader:
            student_test_scores.append(row)
    return student_test_scores


def create_individual_learning_path(domains_ordered_by_grade, student_test_score):
    """Creates a learning path for a single student from the domains passed.
    Starts at the beginning of the available grades and units, and checks each one against the
    student's score for that particular unit. If the student has scored below or at that grade level,
    then that particular unit is added to their learning path. For ease of making comparisons, replaces
    'K' with '0'. Once 5 units have been added to a student's path, the path is returned. If 5 units have
    not been added and all available grade units options have been exhausted, the path is returned.
    Returns a learning path as a string containing the student's name followed by the units
    generated for that student.
    """
    units_per_student = 0
    path = student_test_score['Student Name']
    for grade_with_units in domains_ordered_by_grade:
        grade = grade_with_units[0]
        units_for_grade = grade_with_units[1]
        for unit in units_for_grade:
            if student_test_score[unit] == 'K':
                student_test_score[unit] = '0'

            if student_test_score[unit] <= grade:
                path = path + ',' + str(grade) + '.' + unit
                units_per_student += 1

            if units_per_student == MAX_UNITS_PER_STUDENT:
                path = path.replace('0', 'K')
                return path

    path = path.replace('0', 'K')
    return path


def create_student_learning_paths(domains_ordered_by_grade, student_test_scores):
    """Creates an individual learning path for a list of students based on the domains passed.
    """
    student_learning_paths = []
    for student_test_score in student_test_scores:
        student_units = create_individual_learning_path(domains_ordered_by_grade, student_test_score)
        student_learning_paths.append(student_units)
    return student_learning_paths


def write_student_learning_paths_to_file(student_learning_paths):
    """Writes a list of student learning paths(as string) to the output file.
    """
    with open(OUTPUT_FILE, 'w') as data_file:
        for path in student_learning_paths:
            data_file.write('{}\n'.format(path))


def main():
    """Reads ordered domains and student test scores from two files, passed as command line arguments.
    Creates individual learning paths for each student and writes them to a new file.
    """
    domain_order_file = sys.argv[1]
    student_test_scores_file = sys.argv[2]

    domains_ordered_by_grade = read_domains_ordered_by_grade_from_file(domain_order_file)    
    student_test_scores = read_student_test_scores_from_file(student_test_scores_file)
    student_learning_paths = create_student_learning_paths(domains_ordered_by_grade, student_test_scores)
    write_student_learning_paths_to_file(student_learning_paths)


if __name__ == '__main__':
    main()
