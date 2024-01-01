class Solution(object):
    def fizzBuzz(self, n):
        divisors = {
            3: "Fizz",
            5: "Buzz",
        }
        l = []
        for i in range(1, n + 1):
            to_add = ""
            for divisor, translate in divisors.items():
                if i % divisor == 0:
                    to_add += translate
            l.append(to_add if to_add != "" else str(i))
        return  l
