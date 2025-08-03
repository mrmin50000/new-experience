package main

import (
	"encoding/json"
	"fmt"
	"time"
)

type Person struct {
	Name        string `json:"HOHOHOHO"`
	Email       string
	DateOfBirth time.Time
}

func main() {
	a := Person{Name: "leha", Email: "penis@asdsad.ri"}
	yo, _ := json.Marshal(a)
	fmt.Println(string(yo))
}
