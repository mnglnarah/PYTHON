
def heading(title):
    """Small helper to print a nice heading for each topic."""
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


heading("1. CREATING AND STORING STRINGS")

s1 = 'Hello'
s2 = "Python"
s3 = "This is a\nmulti-line string"
s4 = """Triple double quotes
also work for multiple lines"""

print("s1 =", s1)
print("s2 =", s2)
print("s3 =", s3)
print("s4 =", s4)

q1 = "It's a nice day"
q2 = 'He said "Hi"'
q3 = 'It\'s a nice day'

print(q1)
print(q2)
print(q3)

print("Line1\nLine2")
print("Name\tAge")
print("C:\\Users\\BCA")
print(r"C:\Users\BCA")

name = "Rahul"
print("Stored string:", name)
print("Type of name:", type(name))

empty = ""
print("Empty string length:", len(empty))

word = "Python"
print("First character  :", word[0])
print("Last character   :", word[-1])
print("Third character  :", word[2])

word = "J" + word[1:]
print("New string:", word)

print("Characters of 'BCA':")
for ch in "BCA":
    print(ch)


heading("2. BUILT-IN FUNCTIONS FOR STRINGS")

text = "Hello World"

print("len(text)     :", len(text))
print("max(text)     :", max(text))
print("min(text)     :", repr(min(text)))
print("sorted('bca') :", sorted("bca"))
print("ord('A')      :", ord("A"))
print("chr(97)       :", chr(97))
print("str(100)      :", str(100), type(str(100)))


s = "python programming"

print("\n--- Case methods ---")
print("upper()       :", s.upper())
print("lower()       :", s.lower())
print("title()       :", s.title())
print("capitalize()  :", s.capitalize())
print("swapcase()    :", s.swapcase())


s = "welcome to python, python is easy"

print("\n--- Searching methods ---")
print("find('python')      :", s.find("python"))
print("rfind('python')     :", s.rfind("python"))
print("find('java')        :", s.find("java"))
print("index('to')         :", s.index("to"))
print("count('python')     :", s.count("python"))
print("startswith('wel')  :", s.startswith("wel"))
print("endswith('easy')    :", s.endswith("easy"))


print("\n--- Checking methods ---")
print("'hello'.isalpha()       :", "hello".isalpha())
print("'12345'.isdigit()        :", "12345".isdigit())
print("'abc123'.isalnum()       :", "abc123".isalnum())
print("'hello'.islower()        :", "hello".islower())
print("'HELLO'.isupper()        :", "HELLO".isupper())
print("' '.isspace()            :", " ".isspace())
print("'Hello World'.istitle()  :", "Hello World".istitle())


s = "  Hello Python  "

print("\n--- Modifying methods ---")
print("strip()   :", repr(s.strip()))
print("lstrip()  :", repr(s.lstrip()))
print("rstrip()  :", repr(s.rstrip()))
print("replace() :", s.replace("Python", "Java"))
print("center()  :", "BCA".center(11, "*"))
print("ljust()   :", "BCA".ljust(8, "-"))
print("rjust()   :", "BCA".rjust(8, "-"))
print("zfill()   :", "42".zfill(5))


data = "apple,banana,mango"
fruits = data.split(",")

print("split(',')       :", fruits)
print("split() words    :", "I love Python".split())
print("splitlines()     :", "line1\nline2\nline3".splitlines())
print("partition('=')   :", "name=Rahul".partition("="))


heading("3. STRING OPERATORS")

a = "Hello"
b = "World"

print("a + b          :", a + b)
print("a + ' ' + b    :", a + " " + b)
print("a * 3          :", a * 3)

print("'ell' in a     :", "ell" in a)
print("'xyz' in a     :", "xyz" in a)
print("'xyz' not in a :", "xyz" not in a)

print('"abc" == "abc"     :', "abc" == "abc")
print('"abc" != "abd"     :', "abc" != "abd")
print('"apple" < "banana" :', "apple" < "banana")
print('"z" < "a"          :', "z" < "a")
print('"Hello" == "hello" :', "Hello" == "hello")

x = "python"
y = "python"

print("x is y           :", x is y)
print("x == y           :", x == y)

msg = "Hi"
msg += " there"

print("msg after +=     :", msg)

msg *= 2
print("msg after *=     :", msg)


heading("4. STRING SLICING AND JOINING")

# index :  0  1  2  3  4  5  6  7  8  9 10
# char  :  P  R  O  G  R  A  M  M  I  N  G

s = "PROGRAMMING"

print("s             :", s)
print("s[0:4]        :", s[0:4])
print("s[4:7]        :", s[4:7])
print("s[:4]         :", s[:4])
print("s[4:]         :", s[4:])
print("s[:]          :", s[:])
print("s[::2]        :", s[::2])
print("s[1::2]       :", s[1::2])
print("s[::-1]       :", s[::-1])
print("s[-3:]        :", s[-3:])
print("s[:-3]        :", s[:-3])
print("s[-2:-1]      :", s[-2:-1])
print("s[-2::-1]     :", s[-2::-1])
print("s[20:30]      :", repr(s[20:30]))


word = "madam"

if word == word[::-1]:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")


print("\n--- Joining ---")

first = "Data"
second = "Science"

print("Using +       :", first + " " + second)

words = ["Python", "is", "fun"]

print("join(' ')    :", " ".join(words))
print("join('-')    :", "-".join(words))
print("join('')     :", "".join(words))
print("join(',')    :", ",".join(["red", "green", "blue"]))

sentence = "I am a BCA student"

print("Result        :", " ".join(sentence.split()))
print("Reversed words:", " ".join(sentence.split()[::-1]))


heading("5. FORMATTING STRINGS")

name = "Anita"
age = 20
marks = 87.456

print("\n--- (a) % formatting ---")
print("Name: %s, Age: %d" % (name, age))
print("Marks: %f" % marks)
print("Marks: %.2f" % marks)


print("\n--- (b) format() method ---")
print("Name: {}, Age: {}".format(name, age))
print("Name: {1}, Age: {0}, Again: {1}".format(age, name))
print("Name: {n}, Age: {a}".format(n=name, a=age))
print("Marks: {:.2f}".format(marks))


print("\n--- (c) f-strings ---")
print(f"Name: {name}, Age: {age}")
print(f"Marks: {marks:.2f}")
print(f"Next year {name} will be {age + 1}")
print(f"Name in capitals: {name.upper()}")
print(f"{name = }")


print("\n--- (d) Alignment and width ---")
print(f"[{name:10}]")
print(f"[{name:<10}]")
print(f"[{name:>10}]")
print(f"[{name:^10}]")
print(f"[{name:*^10}]")
print(f"[{name:*^11}]")
print(f"[{age:05}]")


print("\n--- (e) Number formatting ---")

big = 1234567.891

print(f"Comma separator : {big:,.2f}")
print(f"Percentage      : {0.756:.1%}")
print(f"Binary of 10    : {10:b}")
print(f"Octal of 10     : {10:o}")
print(f"Hex of 255      : {255:x}")
print(f"Scientific      : {big:e}")


print("\n--- (f) Student report ---")

students = [
    ("Rahul", 85.5),
    ("Anita", 92.25),
    ("Kiran", 78.0)
]

print(f"{'Name':<10}{'Marks':>8}")
print("-" * 18)

for stu_name, stu_marks in students:
    print(f"{stu_name:<10}{stu_marks:>8.2f}")


# ------------------------------------------------------------
# MINI PROGRAM : putting everything together
# ------------------------------------------------------------

heading("MINI PROGRAM : Count vowels, consonants and digits")

sample = "BCA 3rd Semester 2026"
vowels = consonants = digits = spaces = 0

for ch in sample.lower():
    if ch in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1

print(f"Text       : {sample}")
print(f"Length     : {len(sample)}")
print(f"Vowels     : {vowels}")
print(f"Consonants : {consonants}")
print(f"Digits     : {digits}")
print(f"Spaces     : {spaces}")
print(f"Reversed   : {sample[::-1]}")
print(f"Uppercase  : {sample.upper()}")
