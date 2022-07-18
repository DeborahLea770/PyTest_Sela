class Date:
    def __init__(self, day: int, month: int, year: int):
        """
        function __init__ initiates parameters
        :param day:
        :param month:
        :param year:
        """
        if not 32 > day > 0:
            raise TypeError("DAY ERROR")
        if not 13 > month > 0:
            raise TypeError("MONTH ERROR")
        if not 10000 > year > 999:
            raise TypeError("YEAR ERROR")

        self._day = day
        self._month = month
        self._year = year
        self.day_count_for_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self._year % 4 == 0 and (self._year % 100 != 0 or self._year % 400 == 0):
            self.day_count_for_month[2] = 29

    def __str__(self):
        """
        function __str__ gets a parameter self:Date
        :return: a format string as "day/month/year"
        """
        return f"{self._day}/{self._month}/{self._year}"

    def __sub__(self, other):
        """
        function __sub__ gets self:Date and other:Date
        function return how many days separates between self and other
        """
        number_of_days = 0
        if isinstance(other, Date):
            flag = True
            d = self
            if self > other:
                d = other
                other = self
            while flag:
                d = d.getNextDay()
                number_of_days += 1
                if d == other:
                    flag = False
        return number_of_days

    def isValid(self):
        """
        Function isvalid except parameter self : Date
        and check if isValid or if invalid
                requirements:
                    1) Leap year, february has 29 days else hase 28 days.
                    2) months 4,6,9,11 has 30 days during the month
                    3) months 1,3,7,8,10,12 has 31 Days during the month
        param: self: Date
        return: Date
        """
        return 1 <= self._month <= 12 and 1 <= self._day <= self.day_count_for_month[self._month]

    def getNextDay(self):
        """
        Function getNextDay gets a parameter self: Date
        and returns the next day.
        param self: Date
        return: Date
        """

        if self.day_count_for_month[self._month] > self._day:
            return Date(self._day + 1, self._month, self._year)
        if self.day_count_for_month[self._month] < self._day + 1 and self._month < 12:
            return Date(1, self._month + 1, self._year)
        else:
            return Date(1, 1, self._year + 1)

    def getNextDays(self, day_to_add: int):
        """
        Function getNextDays gets parameters self: Date day_to_add: int
        and returns the future Date after x amount of days.
        param self: Date
        param daysToAdd: int
        return: Date
        """
        d = self
        for x in range(day_to_add):
            d = d.getNextDay()
        return d

    def __eq__(self, other) -> bool:
        if isinstance(other, Date):
            return self._day == other._day and self._month == other._month and self._year == other._year

    def __ne__(self, other) -> bool:
        if isinstance(other, Date):
            return not self.__eq__(other)

    def __gt__(self, other) -> bool:
        if isinstance(other, Date):
            return self._year > other._year or (self._year == other._year and self._month > other._month) or \
                   (self._year == other._year and self._month == other._month and self._day > other._day)

    def __lt__(self, other) -> bool:
        if isinstance(other, Date):
            return self._year < other._year or (self._year == other._year and self._month < other._month) or \
                   (self._year == other._year and self._month == other._month and self._day < other._day)

    def __ge__(self, other) -> bool:
        if isinstance(other, Date):
            return self.__gt__(other) or self.__eq__(other)

    def __le__(self, other) -> bool:
        if isinstance(other, Date):
            return self.__lt__(other) or self.__eq__(other)


def main():
    d1 = Date(7, 12, 2000)
    d2 = Date(17, 12, 2000)
    print(d1 < d2)
    print(d1)
    print(d2)
    print(d1.isValid())
    print(d2.isValid())
    print(d1.getNextDay())
    print(d2.getNextDay())
    print(d1.getNextDays(23))
    print(d2.getNextDays(23))
    print(d2 > d1)
    print(d2 < d1)
    print(d2 == d1)
    print(d2 != d1)
    print(d2 <= d1)
    print(d2 >= d1)


if __name__ == "__main__":
    main()
