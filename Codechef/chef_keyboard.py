
"""
Chef and Keyboard
https://www.codechef.com/OCT16/problems/CHEFKEY
"""

def chef_keyboard_N_2(n, m, k):
	count = 0
	for ii in range(1, n+1):
		for jj in range(1, m+1):
			if ii * jj == k:
				count += 1

	return count

def chef_keyboard_N(n,m,k):
	count = 0
	for ii in range(1, min(n,m)+1):
		if k%ii == 0 and k/ii <= max(n,m):
			count += 1

	return count


T = input()
for ll in range(T):
	test_cases = raw_input().split()
	print chef_keyboard_N_2(int(test_cases[0]), int(test_cases[1]), int(test_cases[2]))
	print chef_keyboard_N(int(test_cases[0]), int(test_cases[1]), int(test_cases[2]))