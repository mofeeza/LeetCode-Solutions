class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        fizzbizz = []
        
        for i in range(1,n+1):
            if (i%3 == 0):
                if (i%3 == 0 and i%5 == 0):
                    fizzbizz.append("FizzBuzz")
                else:
                    fizzbizz.append("Fizz")
                
            elif (i%5 == 0):
                fizzbizz.append("Buzz")
                
            else:
                fizzbizz.append(str(i))
                
        return fizzbizz