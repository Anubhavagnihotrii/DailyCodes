public class MergeStringsAlternately {
    public static String mergeAlternately(String word1, String word2) {
        StringBuilder word3 = new StringBuilder();
        int len1 = word1.length();
        int len2 = word2.length();
        int i=0;
        while(i<len1 || i<len2){
            if(i<len1){
                word3.append(word1.charAt(i));
            }
            if(i<len2){
                word3.append(word2.charAt(i));
            }
            i++;
        }

        return word3.toString();
    }
    public static void main(String[] args) {
        String word1 = "abc";
        String word2 = "pqr";
        System.out.println(mergeAlternately(word1,word2));
    }
}
