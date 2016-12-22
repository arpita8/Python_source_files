#"" https://www.hackerrank.com/challenges/compare-the-triplets?h_r=next-challenge&h_v=legacy  ""
import sys
print("Enter the triplet for Alice")
a_triplet = map(int, raw_input().split())
print("Enter the triplet Bob")
b_triplet = map(int, raw_input().split())
alice_points = 0
bob_points = 0
for a_val, b_val in zip(a_triplet, b_triplet):
    if a_val < b_val:
        bob_points += 1
    elif a_val > b_val:
        alice_points += 1
print(alice_points, bob_points)