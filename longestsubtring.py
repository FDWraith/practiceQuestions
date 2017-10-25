# String -> Sttring
# find the longest substring without repeating characters
def lengthOfLongestSubstring( s):
        longest_len = 0
        substr_so_far = ""
        substr_len = 0 
        for index in range(len(s)): 
            print substr_so_far	
            if( s[index] in substr_so_far ):
                substr_so_far = substr_so_far[substr_so_far.find(s[index])+1:] + s[index]
                substr_len = len(substr_so_far)
            else:
	        	substr_so_far += s[index]
	        	substr_len += 1
            longest_len = max(substr_len, longest_len)
        return( longest_len )

print lengthOfLongestSubstring("bpfbhmipx")
