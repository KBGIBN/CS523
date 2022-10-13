from math import ceil, log2
 
# A utility function to get the
# middle index from corner indexes.
def getMid(s, e) :
    return s + (e -s) // 2
 
""" A recursive function to get the sum of values
    in the given range of the array. The following
    are parameters for this function.
 
    st --> Pointer to segment tree
    si --> Index of current node in the segment tree.
           Initially 0 is passed as root is always at index 0
    ss & se --> Starting and ending indexes of the segment
                represented by current node, i.e., st[si]
    qs & qe --> Starting and ending indexes of query range """
def getSumUtil(st, ss, se, qs, qe, si) :
 
    # If segment of this node is a part of given range,
    # then return the sum of the segment
    if (qs <= ss and qe >= se) :
        return st[si]
 
    # If segment of this node is
    # outside the given range
    if (se < qs or ss > qe) :
        return 0
 
    # If a part of this segment overlaps
    # with the given range
    mid = getMid(ss, se)
     
    return getSumUtil(st, ss, mid, qs, qe, 2 * si + 1) + getSumUtil(st, mid + 1, se, qs, qe, 2 * si + 2)

 
# Return sum of elements in range from
# index qs (query start) to qe (query end).
# It mainly uses getSumUtil()
def getSum(st, n, qs, qe) :
 
    # Check for erroneous input values
    if (qs < 0 or qe > n - 1 or qs > qe) :
 
        print("Invalid Input", end = "")
        return -1
     
    return getSumUtil(st, 0, n - 1, qs, qe, 0)
 
# A recursive function that constructs
# Segment Tree for array[ss..se].
# si is index of current node in segment tree st
def constructSTUtil(arr, ss, se, st, si) :
 
    # If there is one element in array,
    # store it in current node of
    # segment tree and return
    if (ss == se) :
     
        st[si] = arr[ss]
        return arr[ss]
     
    # If there are more than one elements,
    # then recur for left and right subtrees
    # and store the sum of values in this node
    mid = getMid(ss, se)
     
    st[si] = constructSTUtil(arr, ss, mid, st, si * 2 + 1) + constructSTUtil(arr, mid + 1, se, st, si * 2 + 2)

    return st[si]
 

def constructST(arr, n) :
    # Height of segment tree
    x = (int)(ceil(log2(n)))
 
    # Maximum size of segment tree
    max_size = 2 * (int)(2**x) - 1
     
    # Allocate memory
    st = [0] * max_size
 
    # Fill the allocated memory st
    constructSTUtil(arr, 0, n - 1, st, 0)
 
    # Return the constructed segment tree
    return st
 

if __name__ == "__main__" :
    inp = list(map(int,input().split())) # Get input
    n = inp[0]
    arr = inp[1:-2]
    start_range = inp[-2]
    end_range = inp[-1]

    # Build segment tree from given array
    st = constructST(arr, n)
 
    # Print sum of values in array from index 1 to 3
    print("Sum in range [" + str(start_range) + "," + str(end_range) + "] = ", getSum(st, n, 1, 3))