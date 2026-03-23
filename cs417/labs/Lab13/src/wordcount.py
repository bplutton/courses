"""Word counter using argparse."""
import argparse, sys
from collections import Counter


def build_parser():
    """Create and return the argument parser.

    Arguments to define:
        filename            - positional, the text file to analyze
        --ignore-case / -i  - store_true, lowercase all words
        --top / -t          - int, show top N most frequent words (default: None)
        --min-length / -m   - int, only count words with at least this many chars (default: 1)
        --sort-by / -s      - choices ["freq", "alpha"], how to sort top words (default: "freq")
        --reverse / -r      - store_true, reverse the sort order

    Returns:
        argparse.ArgumentParser
    """
    # ArgumentParser with description
    parser = argparse.ArgumentParser(description="Shows the words in a text file and " \
    "how often each word occurs")
    # Positional 'filename' argument
    parser.add_argument('filename', help = "text file to analyze")
    # --ignore-case / -i (action="store_true")
    parser.add_argument('-i', '--ignore-case', action="store_true", help="Converts all words to " \
                        "lowercase before counting")
    # --top / -t (type=int, default=None)
    parser.add_argument('-t', '--top', type=int, default=None, help='Show only the ' \
                        'N most frequent words')
    # --min-length / -m (type=int, default=1)
    parser.add_argument('-m', '--min-length', type=int, default=1, help='Only count words wi' \
                        'th at least this many characters')
    # --sort-by / -s (choices=["freq", "alpha"], default="freq")
    parser.add_argument('-s', '--sort-by', choices=["freq", "alpha"], default="freq")
    # --reverse / -r (action="store_true")
    parser.add_argument('-r', '--reverse', action = "store_true")
    
    return parser


def analyze(filepath, ignore_case=False, top=None, min_length=1,
            sort_by="freq", reverse=False):
    """Analyze a text file and return a formatted result string.

    Args:
        filepath: path to the text file
        ignore_case: if True, lowercase all words before counting
        top: if set, show the N most frequent words with counts
        min_length: only count words with at least this many characters
        sort_by: "freq" (by count) or "alpha" (alphabetical) when showing top words
        reverse: if True, reverse the sort order

    Returns:
        str: formatted result

    Raises:
        FileNotFoundError: if the file doesn't exist
    """
    # Read the file and split into words on whitespace
    try:
        with open(filepath, "r") as f:
            data = f.read()
            data = data.replace('\n', ' ')
            while data[-1] == " ":
                data = data[:-1]
            words = data.split(" ")
    except FileNotFoundError:
        print(f"Error: File {filepath} not found", file = sys.stderr)
        exit(1)
    # TODO: If ignore_case, lowercase all words
    # TODO: Filter out words shorter than min_length
    # TODO: Count total words
    # TODO: If top is None, return "<filename>: <count> words"
    if ignore_case:
        for i in range(len(words)):
            words[i] = words[i].lower()

    if top is None:
        return f"{filepath}: {len(words)} words"
        # elif sort_by == "alpha":
        # lines_to_return = ""
        # lines_to_return += f"{filepath}: {len(words)} words\n\n"
        # words_alphabetically = sorted(Counter(words))
    else:
        lines_to_return = ""
        counts = Counter(words)
        if min_length > 1:
            for word in list(counts):
                if len(word) < min_length:
                    del counts[word]
        most_common_words = counts.most_common(top)

        lines_to_return += f"{filepath}: {sum(counts.values())} words\n\n"
        lines_to_return += f"Top {top} words:\n"

        if sort_by == "alpha" and not reverse:
            sorted_az = sorted(counts.items(), key=lambda item: item[0])
            most_common_words = sorted_az[:top]
        elif reverse and sort_by == "freq":
            reversed_counts = list(counts.most_common())[::-1]
            most_common_words = reversed_counts[:top]
        elif reverse and sort_by == "alpha":
            sorted_za = sorted(counts.items(), key=lambda item: item[0], reverse=True)
            most_common_words = sorted_za[:top]
        
        for item in most_common_words:
            lines_to_return += f'  {item[0]}: {item[1]}\n'
        return lines_to_return
    # TODO: If top is set, find the most frequent words:
    #   - Use Counter(words).most_common() for frequency data
    #   - If sort_by == "alpha", sort alphabetically instead
    #   - If reverse, flip the order
    #   - Take the first 'top' entries
    #   - Return multi-line string:
    #       "<filename>: <count> words\n\nTop <N> words:\n  <word>: <count>\n  ..."
    


def main():
    """Build parser, parse args, analyze, print result."""
    # Build the parser
    parser = build_parser()
    # Parse args
    args = parser.parse_args() 
    # Call analyze with the parsed arguments
    result = analyze(args.filename, args.ignore_case, args.top, args.min_length, args.sort_by, args.reverse)
    # Print the result
    print(result)


if __name__ == "__main__":
    main()
