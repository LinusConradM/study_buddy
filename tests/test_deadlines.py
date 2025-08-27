from datetime import datetime

from deadlines import extract_deadlines


def test_extract_deadlines_simple():
    text = (
        "Homework 1: due September 20, 2023\n"
        "Final Exam – December 15, 2023"
    )
    deadlines = extract_deadlines(text)
    # Two deadlines should be found
    assert len(deadlines) == 2

    titles = [d['title'] for d in deadlines]
    dates = [d['due'].date().isoformat() for d in deadlines]

    assert titles == ['Homework 1', 'Final Exam']
    assert dates == ['2023-09-20', '2023-12-15']


def test_extract_deadlines_ignores_non_date_lines():
    text = (
        "Welcome to the course!\n"
        "Project proposal - due October 5, 2023\n"
        "See you soon."
    )
    deadlines = extract_deadlines(text)
    assert len(deadlines) == 1
    assert deadlines[0]['title'] == 'Project proposal'
    assert deadlines[0]['due'].date().isoformat() == '2023-10-05'