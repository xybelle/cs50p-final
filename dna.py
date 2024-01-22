import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) < 3:
        print("Usage ./dna.py database_file sequence_file")
        return

    # TODO: Read database file into a variable
    dna_db = []
    with open(sys.argv[1]) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dna_db.append(row)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2]) as txtfile:
        seq = txtfile.read()

    # TODO: Find longest match of each STR in DNA sequence
    keys_list = list(dna_db[0].keys())[1:]
    subseq = dict()

    for key in keys_list:
        subseq[f"{key}"] = 0

    for i in range(len(keys_list)):
        subseq[f"{keys_list[i]}"] = longest_match(seq, keys_list[i])

    # TODO: Check database for matching profiles
    common_keys = set(dna_db[0].keys()) & set(subseq.keys())
    match = False
    for row in dna_db:
        row_values = {key: int(value) if isinstance(value, str) and value.isdigit() else value
                      for key, value in row.items()}
        if all(subseq[key] == row_values[key] for key in common_keys):
            if 'name' in row:
                print(f"{row['name']}")
            match = True
    if not match:
        print("No match")

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
