package main

import "fmt"

func main() {
	m := make(map[string]string)
	m["foo"] = "bar"
	fmt.Println(m)
	order := []string{"bread", "cheese", "cucumber"}
	sum := 0
	yo := map[string]int{
		"bread":    50,
		"milk":     100,
		"butter":   200,
		"sausage":  500,
		"salt":     20,
		"cucumber": 200,
		"cheese":   600,
		"ham":      700,
		"hamon":    1500,
	}

	for k, v := range yo {
		if v >= 500 {
			fmt.Println(k)
		}
	}

	for _, a := range order {
		sum += yo[a]
	}
	fmt.Println(sum)
}
