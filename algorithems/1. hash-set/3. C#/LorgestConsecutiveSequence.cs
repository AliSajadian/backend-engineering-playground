using System;
using System.Collections.Generic;
using System.Linq;

public class ConsecutiveSequencesUtils
{
    public static int GetLongestConsecutiveSequenceLength(int[] nums)
    {
        var numSet = new HashSet<int>(nums);
        int maxLength = 0;

        foreach (int num in numSet)
        {
            if (!numSet.Contains(num - 1))
            {
                int current = num;
                int length = 1;

                while (numSet.Contains(current + 1))
                {
                    current++;
                    length++;
                }

                maxLength = Math.Max(maxLength, length);
            }
        }

        return maxLength;
    }
}