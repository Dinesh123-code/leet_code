// Last updated: 7/14/2026, 9:55:51 AM
class Solution {
    public int mostWordsFound(String[] sentences) {
        int maxWords = 0;
        for (String s : sentences) {
            int count = s.split(" ").length;
            if (count > maxWords) {
                maxWords = count;
            }
        }
        return maxWords;
    }
}