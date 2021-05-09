package main

import (
	"os"

	"github.com/mimikwang/rosalind/go/DNA/dna"
)

func main() {
	args := os.Args
	if len(args) < 2 {
		panic("not enough arguments")
	}

	filePath := args[1]
	file, err := os.Open(filePath)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	sequence, err := dna.LoadDataset(file)
	if err != nil {
		panic(err)
	}

	counter := dna.CountNucleotides(sequence)
	dna.FormatOutput(counter)
}
