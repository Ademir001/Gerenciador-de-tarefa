package main

import (
	"pic"
)

func Pic(dx, dy int) [][]uint8 {
	result := make([][]uint8, dy)
	for y := range result {
		row := make([]uint8, dx)
		for x := range row {
			row[x] = uint8((x + y) / 2)
		}
		result[y] = row
	}
	return result
}

func main() {
	pic.Show(Pic)
}
