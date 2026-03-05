/* 
Problem: Two Sum
Platform: LeetCode
Pattern: Hash Map
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)
*/

package dsa_with_dedication.two_pointer;
/* 
import java.util.HashMap;
import java.util.Map;

public class two_sum {
    public static int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int compliment = target - nums[i];
            if (map.containsKey(compliment)) {
                return new int[] { map.get(compliment), i };
            }
            map.put(nums[i], i);
        }
        throw new IllegalArgumentException("No two sum pair");
    }

    public static void main(String[] args) {
        int[] nums = { 5, 7, 11, 2 };
        int target = 9;
        int[] result = twoSum(nums, target);
        System.out.println("Indices: " + result[0] + ", " + result[1]);
    }
}
*/

/*Problem: Two Sum
Platform: LeetCode
Pattern: two pointer
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1) */

public class two_sum{
    public static int[] twosum (int nums[], int target)
    {
        int first=0 ,last=nums.length - 1 ;
        while(first < last)
        {
            if(nums[first]+nums[last]== target)
            {
                return new int[]{first,last};
            }
            else if(nums[first] + nums[last] > target)
                last--;
            else 
                first++;
        }
        throw new IllegalArgumentException("no two sum pair available ");
    }
    public static void main(String[] args) {
        int nums[]=new int[]{2,4,6,15};
        int target=9;
        int soln[]= twosum(nums, target);
        System.out.println("Indices: " + soln[0] + ", " + soln[1]);
    }
}