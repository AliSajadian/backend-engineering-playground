// longest-consecutive.utils.ts

/**
 * Calculate length of longest consecutive sequence
 * Time: O(n), Space: O(n)
 */
export function getLongestConsecutiveSequenceLength(nums: number[]): number {
    const numSet = new Set(nums);
    let maxLength = 0;

    for (const num of numSet) {
        // Only start if this is the beginning of a sequence
        if (!numSet.has(num - 1)) {
            let current = num;
            let length = 1;

            while (numSet.has(current + 1)) {
                current++;
                length++;
            }

            maxLength = Math.max(maxLength, length);
        }
    }

    return maxLength;
}
