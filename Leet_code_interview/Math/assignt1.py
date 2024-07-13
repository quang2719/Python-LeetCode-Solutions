#Fizz Buzz


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = [str(i+1) for i in range(n)]
        f = 3
        while(f-1<n):
            res[f-1] = 'Fizz'
            f+=3
        b = 5
        while(b-1<n):
            if res[b-1] == 'Fizz':
                res[b-1] = 'FizzBuzz'
            else:
                res[b-1] = 'Buzz'
            b+=5
        return res