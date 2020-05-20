from AttendanceStatus import *

CATEGORIES = {
    'AT': Attending(),
    'AL': AnnualLeave(),
    'CSL': CertifiedSickLeave(),
    'USL': UncertifiedSickLeave()
}

payouts = {}

if __name__ == "__main__":
    parser = CSVParser('attendance.csv')

    next_line = parser.next_line()
    while next_line:
        student_id = int(next_line['id'])
        if next_line['id'] not in payouts:
            payouts[student_id] = 0
        payouts[student_id] += CATEGORIES[next_line['status']].total_allowance(next_line)
        next_line = parser.next_line()

    for student_id, total_allowance in sorted(payouts.items()):
        print(str(student_id) + ', ' + str(round(total_allowance, 2)))
