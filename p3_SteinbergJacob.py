# Find duplicated substrings

def find_dup_str(s, n):
  for i in range(len(s) - n + 1):
    sub1 = s[i:i+n]

    for j in range(i + n, len(s) - n + 1):
      sub2 = s[j:j+n]

    if sub1 == sub2:
      return sub1

  return ""

def find_max_dup(s):
  max_dup = ""

  for n in range(1, len(s)//2 + 1):
    dup = find_dup_str(s, n)

    if dup != '':
        max_dup = dup

  return max_dup

# Part A test
s = input("Enter a string: ")
n = int(input("Enter the substring length: "))

answer = find_dup_str(s, n)
print("Duplicated substring:", answer)

# Part B test
s = input("Enter a string to find the longest duplicate: ")
answer = find_max_dup(s)
print("Longest duplicated substring:", answer)
