package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	file, err := os.Open("Day3/input")
	if err != nil {
		fmt.Printf("Error opening file: %v\n", err)
		os.Exit(1)
	}
	scanner := bufio.NewScanner(file)
	numClaims := make(map[string][]int)
	overlap := make(map[int]bool)

	for scanner.Scan() {
		var id, x, y, width, height int
		fmt.Sscanf(scanner.Text(), "#%d @ %d,%d: %dx%d", &id, &x, &y, &width, &height)
		overlap[id] = false
		for r := x; r < x+width; r++ {
			for c := y; c < y+height; c++ {
				posString := fmt.Sprintf("%d,%d", r, c)
				numClaims[posString] = append(numClaims[posString], id)
			}
		}
	}

	counter := 0
	for _, val := range numClaims {
		if len(val) >= 2 {
			counter++
			for _, id := range val {
				overlap[id] = true
			}
		}
	}
	fmt.Println("Part 1: ", counter)

	for id, overlaps := range overlap {
		if overlaps {
			continue
		}
		fmt.Println("Part 2: ", id)
	}

}
