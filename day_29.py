from typing import Union, List, Tuple


def gpa_calculator(grades):
    """
    A simple gpa a calculator, based of the 5 point grading system of Nigerian Federal Universities
    :param grades: The grades gotten passed in as a tuple or list of 2-length tuples or lists of the grade gotten and
    the total credit unit of the given course
    :return: the gpa of the student as calculated from the grades passed in
    """
    assert isinstance(grades, list) or isinstance(grades,
                                                  tuple), f"Expected one parameter of type list or tuple you passed in a {grades.__class__}"
    assert all(isinstance(i, tuple) or isinstance(i, list) for i in
               grades), "This function only takes in a list or tuple of 2-length lists or tuples"
    assert all(len(i) == 2 for i in grades), "Please pass in a 2-length for the each grades"
    assert all(i[0] in ('A', 'B', 'C', 'D', 'F') for i in
               grades), "Please pass in "  # ensure that all grades passed is what is expected
    assert all(isinstance(i[1], int) for i in grades), ""
    grade_mapping = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'F': 0}
    gpa_total = 0
    total_units = sum(i[1] for i in grades)  # get the total units for all the courses
    for grade, unit_points in grades:
        gpa_total += grade_mapping[grade.upper()]  # update the total grade according to the grade
    return gpa_total / total_units


if __name__ == '__main__':
    print(gpa_calculator([("A", 3), ('A', 4), ('A', 3), ('A', 5)]))
