#   Copyright [2022] Chris J Daly (github user cjdaly)
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


flag_US = "🇺🇸"

def print_flag(flag):
    print (flag, [c for c in flag])

print_flag(flag_US)

int_A = 65
int_A_block = 127462

print("0(+{})\t{} = {} (+{})".format(
    int_A, chr(int_A), chr(int_A_block), int_A_block))

for i in range(1, 26):
    lt = chr(int_A+i) ; bl = chr(int_A_block+i)
    print("{}\t{} = {}".format(i, lt, bl))

letter_to_block = {chr(i+int_A):chr(i+int_A_block) for i in range(26)}
def L2B(letter):
    return letter_to_block[letter]
#
block_to_letter = {v:k for k,v in letter_to_block.items()}
def B2L(block):
    return block_to_letter[block]

flag_SE = "{}{}".format(letter_to_block['S'], L2B('E'))
print_flag(flag_SE)

flag_ES = flag_SE[::-1]
print_flag(flag_ES)

for y in range(26):
    for x in range(26):
        print("{}{} ".format(chr(int_A_block+y), chr(int_A_block+x)), end='')
    print()

