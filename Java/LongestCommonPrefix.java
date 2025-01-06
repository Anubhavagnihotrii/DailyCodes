import java.util.Arrays;

public class LongestCommonPrefix {
    public static void main(String[] args) {
        String[] strs = {"flower","flow","flight"};
        Arrays.sort(strs);
        // System.out.println(Arrays.toString(strs));
        String first=strs[0];
        String last =strs[strs.length-1];
        // System.out.println(first+" "+last);
        String prefix="";

        for(int i=0;i<first.length();i++){
            if(first.charAt(i)==last.charAt(i)){
                prefix+=first.charAt(i);
            }
        }
        System.out.println(prefix);
    }
}
