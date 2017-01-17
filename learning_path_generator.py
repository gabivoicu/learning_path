import csv, sys


def read_domains_ordered_by_grade_from_file(domain_order_file):
    domains_ordered_by_grade = ()
    with open(domain_order_file, 'r') as data_file:
        for row in data_file:
            row = row.strip()
            row_elements = row.split(',')
            class_name = row_elements.pop(0)
            row_units = ((class_name, tuple(row_elements)), )
            domains_ordered_by_grade = domains_ordered_by_grade + row_units
    return domains_ordered_by_grade

def read_student_test_scores_from_file(student_test_scores_file):
    student_test_scores = []
    with open(student_test_scores_file, 'r') as data_file:
        file_reader = csv.DictReader(data_file)
        for row in file_reader:
            student_test_scores.append(row)
    return student_test_scores

def create_student_learning_paths(domains_ordered_by_grade, student_test_scores):
    student_learning_paths = []
    for student_test_score in student_test_scores:
        student_units = ()
        for grade_with_units in domains_ordered_by_grade:
            grade = grade_with_units[0]
            units_for_grade = grade_with_units[1]
            for unit in units_for_grade:
                if student_test_score[unit] == 'K':
                    student_test_score[unit] = 0
                else:
                    student_test_score[unit] = int(student_test_score[unit])
                if student_test_score[unit] <= grade:
                    student_units = student_units + ((grade, unit), )
                else:
                    pass
        print student_units[:5]
        print student_test_score['Student Name']
        student_learning_paths.append(student_units)
    return student_learning_paths

def main():

    domain_order_file = sys.argv[1]
    student_test_scores_file = sys.argv[2]

    domains_ordered_by_grade = read_domains_ordered_by_grade_from_file(domain_order_file)    
    student_test_scores = read_student_test_scores_from_file(student_test_scores_file)
    student_learning_paths = create_student_learning_paths(domains_ordered_by_grade, student_test_scores)
    # write_student_learning_paths_to_file(student_learning_paths)

if __name__ == '__main__':
    main()
