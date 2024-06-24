PatternedPasswords
==================

This is a tool for generating Passwords in a certain Pattern.


Be warned: Depending on the length of the passwords, the output file can get huge and the script will take some time.


Example: ullnnnnn is 15 GB and takes around 12 minutes (depending on the hardware of course).

Usage
-----
> Patterned Passwords [-h] [-o OUTPUT] [-a | -c | -s CHARS] pattern

positional arguments:
  pattern               The Pattern for the password
***u: upper, l: lower, n: number, s: special character***

optional arguments:
 (-h, --help) show this help message and exit

  (-a, --all) use every special character in the entire ASCII Table (Default: False)


  (-c, --common)          Use only special characters commonly used in passwords: _ . - ! @ * $ ? & % (Default: True) Source: Mark Burnett @ xato.net


 ( -s CHARS, --special-characters CHARS) use these specific characters as special characters (Example: -s #!?-)

  (-o OUTPUT, --output OUTPUT) output file (Default: output.txt)


Example:
---------
Output of **uulln**(**u**pper + **u**pper + **l**ower + **l**ower + **n**umber):
>1. AAaa0
>2. AAaa1
>3. AAaa2

---SNIP---

>4569759\. ZZzz8
>
>4569760\. ZZzz9
(Yes there would be 4569760 combinations)

Example Usage:
--------
> PatternedPasswords.py -s "!$@" uulns -o sample-output.txt #creates the sample output provided in this repo


> PatternedPasswords.py --all lluullss -o wordlist.txt # use all special characters and the pattern lluullss
