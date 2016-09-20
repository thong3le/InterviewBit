class Solution:
    # @param dividend : integer
    # @param divisor : integer
    # @return an integer
    def divide(self, dividend, divisor):
        return dividend / divisor if (dividend, divisor) != (-2147483648, -1) else 2147483647
       