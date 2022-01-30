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
int_Box_A = 127462

print("0(+65)\t{} = {}".format(chr(int_A), chr(int_Box_A)))

for i in range(1, 26):
    print("{}\t{} = {}".format(i, chr(int_A+i), chr(int_Box_A+i)))

flag_SE = "{}{}".format(chr(int_Box_A+18), chr(int_Box_A+4))
print_flag(flag_SE)

flag_ES = flag_SE[::-1]
print_flag(flag_ES)

for y in range(26):
    for x in range(26):
        print("{}{} ".format(chr(int_Box_A+y), chr(int_Box_A+x)), end='')
    print()