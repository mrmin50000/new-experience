package main

import "fmt"

func main() {
	slice := make([]int, 100)
	for i := 1; i <= 100; i++ {
		slice[i-1] = i
	}
	ans := slice[:10]
	for i := 89; i < 100; i++ {
		ans = append(ans, slice[i])
	}
	fmt.Println(ans)
}
