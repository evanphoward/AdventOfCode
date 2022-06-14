package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	file, err := os.Open("Day2/input")
	if err != nil {
		fmt.Printf("Error opening file: %v\n", err)
		os.Exit(1)
	}
	scanner := bufio.NewScanner(file)
	var lines []string

	twos, threes := 0, 0

	for scanner.Scan() {
		lines = append(lines, scanner.Text())
		counts := make(map[string]int)
		for _, letter := range scanner.Text() {
			counts[string(letter)]++
		}
		two, three := false, false
		for _, count := range counts {
			switch {
			case count == 2:
				two = true
			case count == 3:
				three = true
			default:
			}
		}
		if two {
			twos++
		}
		if three {
			threes++
		}
	}

	fmt.Println("Part 1: ", twos*threes)

	for _, line_1 := range lines {
		for _, line_2 := range lines {
			diffs := 0
			for k := 0; k < len(line_1); k++ {
				if line_1[k] != line_2[k] {
					diffs++
					if diffs > 1 {
						break
					}
				}
			}
			if diffs == 1 {
				line := ""
				for k := 0; k < len(line_1); k++ {
					if line_1[k] == line_2[k] {
						line += string(line_1[k])
					}
				}
				fmt.Println("Part 2: ", line)
				os.Exit(0)
			}
		}
	}
}
