public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        //value -> index
        Dictionary<int,int> prevMap = new Dictionary <int,int> ();

        for (int i = 0; i<nums.Length;i++)
        {
            int n = nums[i];
            int diff = target - n;

            if  (prevMap.ContainsKey(diff))
            {
                return new int[] {prevMap[diff],i};
            } 
            prevMap[n]=i;
        }

        return new int[0];

    }
}
