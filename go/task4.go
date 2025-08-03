package main

import "fmt"

func RemoveDuplicates(input []string) []string {
	yo := make(map[string]int)
	for j, i := range input {
		yo[i]++
		if yo[i] > 1 {
			copy(input[j:], input[j+1:])
			input[len(input)-1] = ""
			input = input[:len(input)-1]
			yo[i]--
		}
	}
	return input
}

func main() {
	input := []string{
		"cat",
		"dog",
		"bird",
		"dog",
		"parrot",
		"cat",
	}
	fmt.Println(RemoveDuplicates(input))
}
