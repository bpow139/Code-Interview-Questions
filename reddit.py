"""
function thats takes two args 'string' and int

abc, 123 returns TRUE

aaa, 111 returns TRUE

bbf, 222 returns FALSE
"""


def Match(group1, group2):

    group1 = str(group1)
    group2 = str(group2)

    mem = []
    ref = {}

    # check if in memory
    # check this number with the dict.
    for i in range(len(group1)):
        if group1[i] in mem:
            if group2[i] == ref[group1[i]]:
                pass
            else:
                return print("False")
        else:
            mem.append(group1[i])
            ref[group1[i]] = group2[i]

            for k in range(i):
                if ref[group1[i]] == ref[group1[k]]:
                    return print("False")
            else:
                continue
            break

    return print("True")


if __name__ == "__main__":

    a = input("Enter the first string/int:  ")
    b = input("Enter the second string/int:  ")

    Match(group1=a, group2=b)
