class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans=0
        for i in range(len(sentences)):
           
            words=sentences[i].split(' ')
            count=len(words)
            ans=max(ans,count)
        return(ans)

        