class Solution:
    def numberToWords(self, num):
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
               'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        threes = 'Billion Million Thousand'.split()

        def words(n):
            if n < 20:
                return to19[n-1:n]
            if n < 100:
                idx = (n//10)
                return tens[idx-2:idx-1] + words(n % 10)
            if n < 1000:
                idx = n//100
                return to19[idx-1:idx]+['Hundred', ]+words(n % 100)
            if n >= 1000000000:
                return words(n//1000000000) + ['Billion', ] + words(n % 1000000000)
            if n >= 1000000:
                return words(n//1000000) + ['Million', ] + words(n % 1000000)
            if n >= 1000:
                return words(n//1000) + ['Thousand', ] + words(n % 1000)
        return ' '.join(words(num)) or 'Zero'
