package dna_test

import (
	"reflect"
	"strings"
	"testing"

	"github.com/mimikwang/rosalind/go/DNA/dna"
)

func TestCountNucleotides(t *testing.T) {
	sequence := "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
	expected := map[rune]int{'A': 20, 'C': 12, 'G': 17, 'T': 21}
	actual := dna.CountNucleotides(sequence)

	if !reflect.DeepEqual(actual, expected) {
		t.Error()
	}
}

func TestLoadDataset(t *testing.T) {
	input := "AAAAAAGGCC"
	reader := strings.NewReader(input)
	sequence, err := dna.LoadDataset(reader)

	if sequence != input {
		t.Error()
	}
	if err != nil {
		t.Error()
	}
}
