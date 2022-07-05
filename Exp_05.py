def countOccurrences(str, word):
     
    # split the string by spaces in a
    a = str.split(" ")
 
    # search for pattern in a
    count = 0
    for i in range(0, len(a)):
         
        # if match found increase count
        if (word == a[i]):
           count = count + 1
            
    return count      
 
# Driver code
str ="GeeksforGeeks A computer science portal for geeks  "
word ="portal"
print(countOccurrences(str, word))