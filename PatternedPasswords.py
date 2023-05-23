import argparse, string, time

#Argparse
parser = argparse.ArgumentParser(prog="Patterned Passwords", description="This is a tool for generating Passwords in a certain Pattern", 
epilog="""Pattern: u: upper, l: lower, n: number, s: special character\nExample: 
Output of uulln:\n1. AAaa0\n2. AAaa1\n3. AAaa2\n\n---SNIP---\n\n4569759. ZZzz8\n4569760. ZZzz9\n(Yes there would be 4569760 combinations)""", 
formatter_class=argparse.RawDescriptionHelpFormatter)

group = parser.add_mutually_exclusive_group(required=False)
group.add_argument("-a", "--all", help="use every special character in the entire ASCII Table (Default: %(default)s)",action="store_true", default=False)
group.add_argument("-c", "--common", help="Use only special characters commonly used in passwords: _ . - ! @ * $ ? & %% (Source in Readme)", action="store_true", default=True)
group.add_argument("-s", "--special-characters", help="use these specific characters as special characters (Example: --special-characters #!?-)", type=str, default='', dest='chars')
parser.add_argument("-o", "--output", help="output file (Default: output.txt)", type=str, default="output.txt")
parser.add_argument("pattern", help="The Pattern for the password", type=str)
args = parser.parse_args()

#Definitions
special_chars = list("_.-!@*$?&%")
if args.chars is not None:
    special_chars = list(args.chars)
if args.all:
    special_chars = [chr(char) for char in range(33, 48)] + [chr(char) for char in range(58, 65)] + [chr(char) for char in range(91, 97)] + [chr(char) for char in range(123, 127)]
rule = {"u": string.ascii_uppercase, "l": string.ascii_lowercase, "n": string.digits, "s": special_chars}
o = open(args.output, "w")

# main method
def generate_passwords(i, password):
    if i == len(args.pattern):
        o.write(password + "\n")
    else:
        for char in rule[args.pattern[i]]:
            password = password[:i] + char + password[i+1:]
            generate_passwords(i+1, password)
combinations = 1
for i in args.pattern:
    combinations = combinations * len(rule[i])
print(f"Generating {combinations} Passwords")
if len(args.pattern) > 5:
    print("This may take a few minutes! Please be patient.")
start_time = time.time()
generate_passwords(0, 'x' * len(args.pattern))
stop_time = time.time()
elapsed_time = stop_time - start_time
print(f"Elapsed Time: {elapsed_time/60:.2f} minutes")
print("Output file: " + str(args.output))

