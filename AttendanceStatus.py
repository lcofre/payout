from dateutil.relativedelta import relativedelta
import datetime
import math
from CSVParser import CSVParser

# Rates are gathered here in case they need to be changed
RATES = {
    'basic_<_18': 72.5,
    'basic_18_24>': 81,
    'basic_25': 85.9,
    'basic_26+': 90.5,
    'meal': 5.5,
    'travel_per_km_to/from': 1.09,
    'fuel': 1
}


class AttendanceStatus:
    """
    Default behaviour for all categories of attendance.
    Specific categories may overwrite the methods as needed.
    """

    def __init__(self):
        self.ages = {}  # To calculate age only once per student
        self.workplaces = None
        self.basic_rates = {
            18: RATES['basic_<_18'],
            25: RATES['basic_18_24>'],
            26: RATES['basic_25'],
            120: RATES['basic_26+']
        }

    def basic_rate(self, attendance_entry):
        if attendance_entry["dob"] not in self.ages:
            dob = datetime.datetime.strptime('1985-06-25', '%Y-%m-%d')
            today = datetime.date.today()
            self.ages[attendance_entry["dob"]] = relativedelta(today, dob).years

        for top_age, rate in sorted(self.basic_rates.items()):
            if self.ages[attendance_entry["dob"]] < top_age:
                return rate

    def meal_rate(self):
        return 0

    def travel_rate(self, attendance_entry):
        return 0

    def fuel_rate(self):
        return 0

    def total_allowance(self, attendance_entry):
        return self.basic_rate(attendance_entry) \
               + self.meal_rate() \
               + self.travel_rate(attendance_entry) \
               + self.fuel_rate()


class Attending(AttendanceStatus):
    def meal_rate(self):
        return RATES['meal']

    def travel_rate(self, attendance_entry):
        if not self.workplaces:
            self.workplaces = CSVParser('workplaces.csv').all_as_dict()

        workplace = self.workplaces[attendance_entry['workplace_id']]
        distance = self.distance(attendance_entry['location'], workplace['location'])
        if distance >= 5:
            # Payment is per full km, 5.9 km is 5 complete kms.
            # Distance is doubled because payment is to/from work
            return int(distance) * RATES['travel_per_km_to/from'] * 2
        return 0

    def fuel_rate(self):
        return RATES['fuel']

    @staticmethod
    def distance(start_point, end_point):
        start = eval(start_point)
        end = eval(end_point)

        return math.sqrt(pow(end[0] - start[0], 2) + pow(end[1] - start[1], 2))


class AnnualLeave(AttendanceStatus):
    """Behaves as default"""


class CertifiedSickLeave(AttendanceStatus):
    """Behaves as default"""


class UncertifiedSickLeave(AttendanceStatus):
    """Uncertified Sick leave gets no allowance"""

    def basic_rate(self, attendance_entry):
        return 0
