"""Given an array of positive integers, 
return the number of elements that are strictly greater than the average of all previous elements. 
Skip the first element"""




"""

100 => First element ignore

200 > avg(100) => count is 1

150 vs avg(100, 200) => not greater than 150 count is 1

300 > avg(100, 200, 150) = 450/3 = 150 is 300 > 150 count is 2 True then return 2

"""

def countResponseTimeRegressions(responseTimes):
    n = 0
    # Write your code here
    
    #skip the first element in the array

    for i in range(1, len(responseTimes)):


    #loop through starting from the second element

        previous_avg = sum(responseTimes[0:i])/i

        if responseTimes[i] > previous_avg:

            # if the element is greater than the avg of the previous element add 1

            n +=1

    return n

result=countResponseTimeRegressions([100, 200, 150,300])

print(result)


    
