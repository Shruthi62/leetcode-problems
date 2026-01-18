class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string res="";
        string top=strs[0];
        int x=strs[0].length();
        
        for (int j= 0;j<x;j++)
            {bool flag=false;    
         for (int i = 0;i<strs.size();i++)
       {
           if (strs[i][j]!=top[j])
               return res;
        flag=true;
           
       }
        if(flag)  
            res+=top[j];  
            }
        return res;
 }

};