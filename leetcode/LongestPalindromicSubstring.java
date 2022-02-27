class Solution {
    public String longestPalindrome(String s) {
        int len = s.length();
        int maxLen = 1;
        int stIndx = 0;
        for(int i=0; i<len; i++){
            int slen1 = getPalindromeLenght(s,i,i);
            int slen2 = getPalindromeLenght(s,i,i+1);
            int slen = slen1>slen2 ? slen1 : slen2;
            int k = slen1>slen2 ? i-(slen1-1)/2 :i-(slen2/2 - 1);
            if(maxLen<slen){
                maxLen=slen;
                stIndx = k;
            }
        }
        return s.substring(stIndx, stIndx+maxLen);
    }
    private int getPalindromeLenght(String s, int mid1, int mid2){
        int len = s.length();
        while((mid1>=0) && (mid2<len) && (s.charAt(mid1) == s.charAt(mid2))){
            mid1--;
            mid2++;
        }
        return mid2-mid1-1;
    }
}
