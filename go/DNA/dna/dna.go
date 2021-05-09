// Counting DNA Nucleotides
//
// http://rosalind.info/problems/dna/
package dna

import (
	"bufio"
	"fmt"
	"io"
)

func LoadDataset(reader io.Reader) (string, error) {
	bufReader := bufio.NewReader(reader)
	sequence, err := bufReader.ReadString('\n')
	if err == io.EOF {
		err = nil
	}

	return sequence, err
}

func CountNucleotides(sequence string) map[rune]int {
	counter := map[rune]int{'A': 0, 'C': 0, 'G': 0, 'T': 0}
	for _, base := range sequence {
		if _, found := counter[base]; found {
			counter[base] += 1
		}
	}
	return counter
}

func FormatOutput(counter map[rune]int) {
	bases := []rune{'A', 'C', 'G', 'T'}
	for _, base := range bases {
		fmt.Printf("%d ", counter[base])
	}
	fmt.Println()
}
