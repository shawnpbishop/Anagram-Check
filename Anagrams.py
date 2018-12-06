#This program is written by Shawn Bishop.

def main():

    s1 = input("What is the first string? ").strip()
    s2 = input("What is the second string? ").strip()

    if sort(s1) == sort(s2):
        print("They are anagrams of each other. ")
    else:
        print("They are not anagrams of each other.")



def sort(s):
    r = list(s)
    r.sort()
    t = ""
    for ch in r:
        t += ch
    return t

main()
