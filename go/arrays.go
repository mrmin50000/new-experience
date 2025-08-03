package main

func main() {
	arr := [3]int{1, 2, 3}
	for a, b := range &arr {
		println(a, b)
	}
}
