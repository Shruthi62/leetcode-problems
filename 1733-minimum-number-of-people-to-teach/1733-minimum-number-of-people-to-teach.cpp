#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minimumTeachings(int n, vector<vector<int>>& languages, vector<vector<int>>& friendships) {
        vector<unordered_set<int>> userLang(languages.size());
        for (int i = 0; i < languages.size(); i++)
            for (int l : languages[i]) userLang[i].insert(l);

        unordered_set<int> needTeach;
        for (auto &f : friendships) {
            int u = f[0]-1, v = f[1]-1;
            bool ok = false;
            for (int l : userLang[u]) if (userLang[v].count(l)) { ok = true; break; }
            if (!ok) { needTeach.insert(u); needTeach.insert(v); }
        }
        if (needTeach.empty()) return 0;

        int ans = INT_MAX;
        for (int lang = 1; lang <= n; lang++) {
            int cnt = 0;
            for (int u : needTeach) if (!userLang[u].count(lang)) cnt++;
            ans = min(ans, cnt);
        }
        return ans;
    }
};
