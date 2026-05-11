class Solution:
    def defangIPaddr(self, address: str) -> str:
      
        find = "."
        find=address.replace(".","[.]")
        return find

        