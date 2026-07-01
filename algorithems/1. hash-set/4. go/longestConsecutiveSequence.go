package main

import (
    "container/heap"
    "fmt"
)

// ---------- Longest Consecutive Sequence ----------

// GetLongestConsecutiveSequenceLength calculates length of longest consecutive sequence
// Time: O(n), Space: O(n)
func GetLongestConsecutiveSequenceLength(nums []int) int {
    numSet := make(map[int]bool)
    for _, num := range nums {
        numSet[num] = true
    }

    maxLength := 0

    for num := range numSet {
        // Only start if this is the beginning of a sequence
        if !numSet[num-1] {
            current := num
            length := 1

            for numSet[current+1] {
                current++
                length++
            }

            if length > maxLength {
                maxLength = length
            }
        }
    }

    return maxLength
}

// ---------- Main ----------

func main() {
    nums := []int{0, 4, 9, 0, 8, 2, 8, 4, 8, 0}

    fmt.Println(GetLongestConsecutiveSequenceLength(nums)) // 3
}