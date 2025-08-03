package main

type figures int

const (
	square figures = iota
	circle
	triangle
)

func area(f figures) (func(float64) float64, bool) {
	switch f {
	case square:
		return func(x float64) float64 { return x * x }, true
	case circle:
		return func(x float64) float64 { return 3.14 * x * x }, true
	case triangle:
		return func(x float64) float64 { return 0.43 * x * x }, true
	default:
		return nil, false
	}

}
