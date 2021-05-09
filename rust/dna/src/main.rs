use std::collections::HashMap;
use std::env;
use std::fs::File;
use std::io::{self, BufRead};

fn main() {
    // Get commandline arguments
    let args: Vec<String> = env::args().collect();
    if args.len() != 2 {
        panic!("expect exactly 1 argument")
    }

    let file = File::open(args[1].as_str()).unwrap();
    let sequence = load_sequence(file).unwrap();
    let counter = count_nucleotides(&sequence);
    println!("{}", format_output(counter));
}

/// Count the number of "A", "C", "G", and "T" in a given sequence
///
/// # Arguments:
///
/// * `sequence` - a DNA sequence
///
fn count_nucleotides(sequence: &str) -> HashMap<char, i32> {
    let mut counter = HashMap::new();
    for base in sequence.chars() {
        let base_count = counter.entry(base).or_insert(0);
        *base_count += 1;
    }

    counter
}

/// Format output
///
/// # Arguments
///
/// * `counter` - counter returned by `count_nucleotides`
fn format_output(counter: HashMap<char, i32>) -> String {
    let output = format!(
        "{} {} {} {}",
        counter.get(&'A').unwrap_or(&0),
        counter.get(&'C').unwrap_or(&0),
        counter.get(&'G').unwrap_or(&0),
        counter.get(&'T').unwrap_or(&0),
    );

    output
}

/// Load sequence
///
/// # Arguments
///
/// * `reader` - reader for a fasta file
fn load_sequence<R>(reader: R) -> io::Result<String>
where
    R: io::Read,
{
    let mut sequence = String::new();
    let mut buffered_reader = io::BufReader::new(reader);
    buffered_reader.read_line(&mut sequence)?;

    Ok(sequence)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_count_nucleotides() {
        let sequence = "AAAACCGT";
        let counter = count_nucleotides(sequence);

        assert_eq!(counter[&'A'], 4);
        assert_eq!(counter[&'C'], 2);
        assert_eq!(counter[&'G'], 1);
        assert_eq!(counter[&'T'], 1);
    }

    #[test]
    fn test_format_output() {
        let mut counter = HashMap::new();
        counter.insert('A', 3);
        counter.insert('G', 100);
        counter.insert('T', 2);

        let actual = format_output(counter);
        assert_eq!(actual, "3 0 100 2".to_string());
    }

    #[test]
    fn test_load_sequence() {
        let data: &'static [u8] = b"AAACCGGTT";
        let sequence = load_sequence(data);

        assert_eq!(sequence.unwrap(), "AAACCGGTT".to_string());
    }
}
