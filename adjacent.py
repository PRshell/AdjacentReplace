# Python3 program for
# Function that replace all '?' with lowercase alphabets such that each adjacent character is different

def changeString(S):
     
    N = len(S)
    s = [' '] * (len(S))
     
    for i in range(len(S)):
        s[i] = S[i]
 
   
    if (s[0] == '?'):
        s[0] = 'a'
         
        if (s[0] == s[1]):
            s[0] = chr(ord(s[0]) + 1)
 
   
    for i in range(1, N - 1):
        if (s[i] == '?'):
            s[i] = 'a'
 
            if (s[i] == s[i - 1]):
                s[i] =  chr(ord(s[i]) + 1)
 
            if (s[i] == s[i + 1]):
                s[i] =  chr(ord(s[i]) + 1)
 
            if (s[i] == s[i - 1]):
                s[i] =  chr(ord(s[i]) + 1)
 
    if (s[N - 1] == '?'):
         
      
        s[N - 1] = 'a'
        
        if (s[N - 1] == s[N - 2]):
            s[N - 1] += chr(ord(s[N -1]) + 1)
 
    ans = ""
    for i in range(len(s)):
        ans += s[i]
         
    # Return the resultant String
    return ans
 
# Driver Code
if __name__ == '__main__':
     
    # Given String S
    S = input()
 
    # Function Call
    print(changeString(S))
