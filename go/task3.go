package main

import "fmt"

func main() {
	arr := [10]int{1, 3, 4, 5, 6, 2, 56, 4, 5, 8}
	k := 11
	for a, _ := range arr {
		for j := a; j < len(arr); j++ {
			if arr[a]+arr[j] == k {
				fmt.Printf("%d : %d\n", a, j)
			}
		}
	}
}
