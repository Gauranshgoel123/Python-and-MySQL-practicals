input1=input("FOR LINEAR SEARCH TYPE LINEAR")
if input1=="LINEAR":
    def search(arr, n, x):
        for i in range(0, n):
            if (arr[i] == x):
              return i

# Driver Code
arr = [2, 3, 4, 10, 40]
x = 10
n = len(arr) 
# Function call
result = search(arr, n, x)
print("Element is present at index", result)

input2=input("FOR BINARY SEARCH TYPE BINARY")
if input2=="BINARY":
    def binarySearch (arr, l, r, x):
        # Check base case
        if r >= l:   
            mid = l + (r - l) // 2
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
          
        # If element is smaller than mid, then it 
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
      
# Driver Code
arr = [ 2, 3, 4, 10, 40 ]
x = 10  
# Function call
result = binarySearch(arr, 0, len(arr)-1, x)
if result != -1:
    print ("Element is present at index % d" % result)
else:
    print ("Element is not present in array")
