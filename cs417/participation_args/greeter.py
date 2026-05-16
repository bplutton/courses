import argparse

# 1. Set up the parser
parser = argparse.ArgumentParser(description="A script that greets you!")

# 2. Add arguments
parser.add_argument("--name", type=str, default="Stranger", help="Your name")
parser.add_argument("--shout", action="store_true", help="Print in ALL CAPS")
parser.add_argument("--repeat", type=int, default=1, help="Number of times to repeat the greeting")

# 3. Parse the arguments
args = parser.parse_args()

# 4. Use the arguments in the program
message = f"Hello there, {args.name}!"

if args.shout:
    print(message.upper())
else:
    for _ in range(args.repeat):
        print(message)