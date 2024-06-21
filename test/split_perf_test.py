#!/usr/bin/env python3

import re
import timeit
import sys

input_str = " ".join([chr(x) for x in range(ord('a'), ord('z') + 1)]) * 1000
cre = re.compile(" ")
num_fields = 25001

def raw_split():
    fields = input_str.split(" ") 
    if len(fields) != num_fields:
        print(f"Expected the length of fields to be {num_fields} but found {len(fields)}")
        sys.exit(1)
    " ".join(fields)

def regex_split():
    fields = cre.split(input_str) 
    if len(fields) != num_fields:
        print(f"Expected the length of fields to be {num_fields} but found {len(fields)}")
        sys.exit(1)
    " ".join(fields)

print(timeit.timeit("raw_split()", number=10000, globals=globals()))
print(timeit.timeit("regex_split()", number=10000, globals=globals()))

