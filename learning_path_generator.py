import csv, sys


def main():

    domain_order_file = sys.argv[1]
    student_test_scores_file = sys.argv[2]

    domains_ordered_by_class = ()
    with open(domain_order_file, 'r') as data_file:
        for row in data_file:
            row = row.strip()
            row_elements = row.split(',')
            class_name = row_elements.pop(0)
            row_units = ((class_name, tuple(row_elements)), )
            domains_ordered_by_class = domains_ordered_by_class + row_units
            
    student_test_scores = []
    with open(student_test_scores_file, 'r') as data_file:
        file_reader = csv.DictReader(data_file)
        for row in file_reader:
            student_test_scores.append(row)

    for student_test_score in student_test_scores:
        student_units = ()
        for grade in range(0, len(domains_ordered_by_class)):
            units_for_grade = domains_ordered_by_class[grade][1]
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

if __name__ == '__main__':
    main()
