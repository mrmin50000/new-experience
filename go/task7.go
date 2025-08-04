package main

import "fmt"

var Global = 5

func UseGlobal() {
	defer func(a int) {
		Global = a
	}(Global)
	Global = 42
	fmt.Println(Global)
}

func main() {
	fmt.Println(Global)
	UseGlobal()
	fmt.Println(Global)
}
