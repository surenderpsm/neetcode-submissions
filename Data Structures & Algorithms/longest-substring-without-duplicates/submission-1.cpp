class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int maxLen = 0;
        int beg = 0;
        unordered_map<char, int> recentIndex;
        for (int i = 0; i < s.length(); i++) {
            if (recentIndex.find(s[i]) != recentIndex.end()) {
                // we use max cause it ensures we dont check old index records of characters outside the window.
                beg = std::max(recentIndex[s[i]]+1, beg);
                //recent index values are logically always lower than i. because we traverse it linearly.
            }
            recentIndex[s[i]] = i;
            maxLen = std::max(maxLen, i-beg+1);
        }
        return maxLen;
    }
};


/**

    abba

    i 3
    ml 2
    bg 2

    ri
    a 0
    b 2



    max len 0
    begin 0

    map tracks recent index in window

    iterate the loop
        if recent index has current char
            update begin of window to after recent index of current char
        recend index insert/update
        track max length.
    return maxlen

    s
    zxyzxyz
    
    we iterate the entire string. 

    we check if the window has the current i character if it does take the character's last found index and increment the start of the window to one + that index.
    at each update on the window, we track the maximum lenght of the window witnessed till that iteration.

*/