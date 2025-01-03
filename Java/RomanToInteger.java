import java.util.ArrayList;
import java.util.LinkedHashMap;


public class RomanToInteger {

    static int convert(String s){
        LinkedHashMap<Character,Integer> map = new LinkedHashMap<>();
        map.put('I',1);
        map.put('V',5);
        map.put('X',10);
        map.put('L',50);
        map.put('C',100);
        map.put('D',500);
        map.put('M',1000);
        ArrayList<Integer> list = new ArrayList<>();
        for(Character i: s.toCharArray()){
            list.add(map.get(i));
        }
        System.out.println(list);

        int result = list.getFirst();

        for (int i = 1; i < list.size(); i++) {
            if(list.get(i) > list.get(i-1)){
                result+=list.get(i)-2*list.get(i-1);
            }else{
            result+=list.get(i);
            }
        }
        return  result;
    }

    public static void main(String[] args) {
        String s = "MCM";
        System.out.println(convert(s));
    }
}
