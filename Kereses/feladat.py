import os


#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    # Write your code here
    arr.sort()
    
    min_diff = float('inf')
    result = []
    
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i - 1]

        if diff < min_diff:
            min_diff = diff
            result = [arr[i - 1], arr[i]] 
        elif diff == min_diff:
            result.extend([arr[i - 1], arr[i]])
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()