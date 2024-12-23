import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class FrequencyCount {
    public static List<Integer> frequencyCount(int[] arr) {
        List<Integer> countSum = new ArrayList<>();
        for (int i = 0; i < arr.length; i++) {
            countSum.add(0); // Initialize the list with zeros
        }

        for (int i : arr) {
            countSum.set(i - 1, countSum.get(i - 1) + 1); // Increment the count at the correct index
        }

        return countSum;
    }

    public static void main(String[] args) {
        List<Integer> result = frequencyCount(new int[]{1, 1, 1, 1});
        System.out.println(result);
    }
}