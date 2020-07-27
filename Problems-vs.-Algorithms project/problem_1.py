def sqrt(low, high, N):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """ 
    if (low <= high):# If the range is still valid 
        mid = (low + high) // 2;# Find the mid-value of the range 
        if ((mid * mid <= N) and ((mid + 1) * (mid + 1) > N)) :# Base Case
            return mid;
        elif (mid * mid < N) :
            return sqrt(mid + 1, high, N);
        else :
            return sqrt(low, mid - 1, N);

        return low; 

 # Driver Code 
if __name__ == "__main__" :

    N = 36;
    print(sqrt(0,N,N))
    #expected output: 6
    print ("Pass" if  (6 == sqrt(0,N,N)) else "Fail")
    print('--------------------------------------')

    N = 4;
    print(sqrt(0,N,N))
    #expected output: 2
    print ("Pass" if  (2 == sqrt(0,N,N)) else "Fail")
    print('--------------------------------------')

    N = 18;
    print(sqrt(0,N,N))
    #expected output: 4
    print ("Pass" if  (4 == sqrt(0,N,N)) else "Fail")
    print('--------------------------------------')

    N = 49;
    print(sqrt(0,N,N))
    #expected output: 7
    print ("Pass" if  (7 == sqrt(0,N,N)) else "Fail")
    print('--------------------------------------')

    N=27
    print(sqrt(0,N,N))
    #expected output: 5
    print ("Pass" if  (5 == sqrt(0,N,N)) else "Fail")
    print('--------------------------------------')





