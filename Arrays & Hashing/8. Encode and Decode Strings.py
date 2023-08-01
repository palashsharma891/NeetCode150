class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        ans = ''
        for s in strs:
            ans += str(len(s)) + ':;' + s
        return ans

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        # "lint:;code:;love:;you"
        #lenghtstring "4:;lint4:;code4:;love3:;you"
        ans = []
        curr = ''
        i = 0
        l = ''
        while i < len(str):
            curr += str[i]
            if str[i:i+2] == ':;':
                print(curr)
                l = int(curr[:-1])
                ans += [str[i+2:i+2+l]]
                i += l + 1 # +1, not +2 because we are incrementing i during every iteration of the while loop
                curr = ''
                print(ans)
            i += 1

        return ans

# OR

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        ans = ''
        for s in strs:
            ans += str(len(s)) + ':;' + s
        return ans

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        # "lint:;code:;love:;you"
        #lenghtstring "4:;lint4:;code4:;love3:;you"
        ans = []
        curr = ''
        i = 0
        l = ''
        while i < len(str):
            curr += str[i]
            if str[i:i+2] == ':;':
                print(curr)
                l = int(curr[:-1])
                ans += [str[i+2:i+2+l]]
                i += l + 1 # +1, not +2 because we are incrementing i during every iteration of the while loop
                curr = ''
                print(ans)
            i += 1

        return ans
