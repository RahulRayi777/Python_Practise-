# Input: ["bat", "tab", "tap", "pat", "cat"]
# Output: [['bat', 'tab'], ['tap', 'pat'], ['cat']]

# Input: ["flower", "flow", "flight"]
# Output: "fl"

 
def lcs(words):
    prefix=words[0]
    for i in range(len(prefix)):
        for word in words[1:]:
            if i>len(word) or  word[i]!=prefix[i]:
                return prefix[:i]
    return prefix
        
words=["flower", "flow", "flight"]   
print(lcs(words))
