class AccountHolderService:
    def __init__(self, document):
        self._document = document
        self._document_nine_digits = self._document[:9]


    def document_is_valid(self):
        if not self._document_is_11_digits():
            return False
        digit1 = self._calculate_first_digit()
        digit2 = self._calculate_second_digit(digit1)
        if self._document[-2:] != f'{digit1}{digit2}':
            return False
        return True


    def _document_is_11_digits(self):
        return len(self._document) == 11


    def _calculate_first_digit(self):
        total = sum([int(digit) * (10 - i) for i, digit in enumerate(self._document_nine_digits)]) % 11
        if total < 2:
            return 0
        return 11 - total


    def _calculate_second_digit(self, first_digit):
        total = sum([int(digit) * (11 - i) for i, digit in enumerate(self._document_nine_digits + str(first_digit))]) % 11
        if total < 2:
            return 0
        return 11 - total




