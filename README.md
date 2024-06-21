# pyne
A Python one-liner tool that works similar to "perl -ne" (hence the name pyne, "py -ne"). This tool filters and transforms stdin line-by-line. Pyne aims to replace awk scripts with simple Python one-liners.

# Examples with numbers

The content of the sample input file is:

```
$ cat test/input.txt
1 2 3
4 5 6
7 8 9
```

1. Print the sum of the last column in the input file. 

```
$ cat test/input.txt | ./pyne  --begin 'sum = 0' 'sum += int(F[NF-1])' --end 'P(f"sum: {sum}")'
sum: 18
```

2. Print the last column in the input file.

```
$ cat test/input.txt | ./pyne  'P(F[NF-1])'
3
6
9
```

3. Print the first column in the input file:

```
$ cat test/input.txt | ./pyne  'P(F[0])'
1
4
7
```

4. Print only the odd lines from the file.

```
$ cat test/input.txt | ./pyne 'if NR%2 == 1: P(L)'
1 2 3
7 8 9
```

5. Print all the lines that have a value 8 in the second column. Not the double quote around the
   value being compared.

```
$ cat test/input.txt | ./pyne 'if F[1] == "8": P(L)'
7 8 9
```

# Examples with strings

Examples in this section make use of the following input file.

```
$ cat test/input2.txt
Winslet,Kate
Thurman,Uma
Portman,Natalie
Stone,Sharon
```

1. Print all lines with first names starting with "U". Use "," as separator.

```
$ cat test/input2.txt | ./pyne --sep="," 'if F[1].startswith("U"): P(L)'
Thurman,Uma
```


2. Print all lines that have "o" in the last name.

```
$ cat test/input2.txt | ./pyne --sep="," 'if "o" in F[1]: P(L)'
Stone,Sharon
```

3. Print all lines that match the regex "man". Note that you can compile the regex so that it is
   performant.

```
$ cat test/input2.txt | ./pyne --sep="," --begin 'cre=R.compile("man")' 'if cre.search(F[0]): P(L)'
Thurman,Uma
Portman,Natalie
```

# BODY from input file
Sometimes one-liners are not really one-liners and may need to be folded into multiple lines for
readability and reusability. In such cases, you can store the BODY part of the one-liner in a file
and provide the file name as BODY. You need to prefix the file name with an "@". Following script
prints each line with "man" in last name with "match" prefix and others with "NO match" prefix.

```
$ cat /tmp/script.py
if cre.search(F[0]):
    P("match    :", L)
else:
    P("NO match :", L)

$ cat test/input2.txt | ./pyne --sep="," --begin 'cre=R.compile("man")' "@/tmp/script.py"
NO match : Winslet,Kate
match    : Thurman,Uma
match    : Portman,Natalie
NO match : Stone,Sharon
```

You can cut down a lot of boilerplate and just write your script to process input and produce
output.

