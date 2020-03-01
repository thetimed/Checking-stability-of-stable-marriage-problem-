# Name: <TODO: replace with your name>
# Section: <TODO: replace with your section>

# p1q2
# A marriage between m and w is stable if and only if whenever m prefers a woman k over his wife w,
# k also happens to prefer her own husband over m so that m and w have no reason to part.

# With this logic, we infer that any man or woman who has gotten their first preference has no reason
# to part

#Given n men and n women, where each person has ranked all members of the opposite sex
#in order of preference, marry the men and women together such that there are no
#two people of opposite sex who would both rather have each other than their current partners.
#When there are no such pairs of people, the set of marriages is deemed stable.

#Check first male,aka his wife, and his current satisfaction, if 1 just skip
#else change to another female and see the new score, if higher, gtfo,
#if lower, see if the female would benefit,
#if not, gtfo

# All statements should only be in functions. Do not include statements outside functions in this file.
# You may insert additional helper functions into this file if desired.

# 1st step: Build a table with the scores first of male and female
# From the choice, run the algorithm
def is_stable(n, pref, solution):
    k = []
    gh = []
    fh = []
    for i in solution:
        wife = i[1]
        husband = i[0]
        x = [x for x in pref if husband in x][0]
        y = [y for y in pref if wife in y][0]
        access_wife = pref.index(y)
        access_husband = pref.index(x)
        current_status_husband = pref[access_husband][int(wife[1])]
        current_status_wife = pref[access_wife][int(husband[1])]
        gh.append(husband)
        fh.append(wife)
        for q in range(n):
            if pref[access_husband][q+1] < current_status_husband:
                gh.append("f" + str(q+1))
        k.append(gh)
        gh = []
        for qq in range(n):
            if pref[access_wife][qq+1] < current_status_wife:
                fh.append("m" + str(qq+1))
        k.append(fh)
        fh = []

    k.sort()
    female = k[0:n]
    male = k[n:2*n]
    for i in female:
        for ma in male:
            count = 0
            for gg in range(len(i)):
                if i[gg] in ma:
                    count += 1
                if count >=2:
                    return False
    return True
