

class Operations:
    """
    Add documentation
    """

    @staticmethod
    def convert_to_int_or_float(val):
        if '.' in val:
            new_val = float(val)
        else:
            new_val = int(val)
        return new_val

    @staticmethod
    def add(val1, val2):
        if isinstance(val1, str) and isinstance(val2, str):
            val1 = Operations.convert_to_int_or_float(val1)
            val2 = Operations.convert_to_int_or_float(val2)
            return val1 + val2



