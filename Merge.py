#"" https://www.hackerrank.com/challenges/merge-the-tools  ""


print("Enter any string")
s = raw_input()
print("Enter the Number")
k = int(raw_input())
num_subsegments = int(len(s) / k)

for index in range(num_subsegments):
    # Subsegment string
    t = s[index * k : (index + 1) * k]
    
    # Subsequence string having distinct characters
    u = ""
    
    # If a character is not already in 'u', append
    for c in t:
        if c not in u:
            u += c

    # Print final converted string
    print(u)