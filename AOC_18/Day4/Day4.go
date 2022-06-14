package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"sort"
	"strconv"
	"time"
)

type Action int

const (
	Wake Action = iota
	Asleep
	Shift
)

type Obsv struct {
	action Action
	guard  int
	date   time.Time
}

func main() {
	file, err := os.Open("Day4/input")
	if err != nil {
		fmt.Printf("Error opening file: %v\n", err)
		os.Exit(1)
	}
	scanner := bufio.NewScanner(file)

	observations := []Obsv{}
	guard_data := make(map[int][]int)

	for scanner.Scan() {
		obsv := scanner.Text()
		date, _ := time.Parse("2006-01-02 15:04", obsv[1:17])

		var action Action
		switch obsv[19] {
		case 'G':
			action = Shift
		case 'w':
			action = Wake
		case 'f':
			action = Asleep
		}

		obsvStruct := Obsv{date: date, action: action}
		if action == Shift {
			r := regexp.MustCompile(`\d+`)
			obsvStruct.guard, _ = strconv.Atoi(r.FindString(obsv[26:]))
			if _, present := guard_data[obsvStruct.guard]; !present {
				guard_data[obsvStruct.guard] = make([]int, 60)
			}
		}

		observations = append(observations, obsvStruct)
	}

	sort.Slice(observations, func(i, j int) bool {
		return observations[i].date.Before(observations[j].date)
	})

	curr_guard := observations[0].guard
	asleep := false
	minute := 0
	for _, obsv := range observations {
		if asleep {
			for i := minute; i < obsv.date.Minute(); i++ {
				guard_data[curr_guard][i]++
			}
		}
		if obsv.action == Asleep {
			asleep = true
		} else if obsv.action == Wake {
			asleep = false
		} else {
			curr_guard = obsv.guard
		}
		minute = obsv.date.Minute()
	}

	most_sleep_total_guard := -1
	most_sleep_total_val := 0
	most_sleep_minute_guard := -1
	most_sleep_minute := 0
	most_sleep_minute_val := 0
	for guard, minutes := range guard_data {
		sum := 0
		for i, min := range minutes {
			sum += min
			if min > most_sleep_minute_val {
				most_sleep_minute_val = min
				most_sleep_minute = i
				most_sleep_minute_guard = guard
			}
		}
		if sum > most_sleep_total_val {
			most_sleep_total_val = sum
			most_sleep_total_guard = guard
		}
	}

	max := 0
	for i, min := range guard_data[most_sleep_total_guard] {
		if min > guard_data[most_sleep_total_guard][max] {
			max = i
		}
	}
	fmt.Println("Part 1:", max*most_sleep_total_guard)
	fmt.Println("Part 2:", most_sleep_minute*most_sleep_minute_guard)
}
