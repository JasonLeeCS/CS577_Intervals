#
# Intervals
# Assignment: HW 7 CS577
# Author: Jason Lee (jlee967@wisc.edu)
#


def binarySearch(end, target):
    l, r = 0, len(end) - 1
    middle = 0

    while l <= r:
        #Edge case
        if target >= end[r]:
            return r + 1

        middle = (l + r) // 2
        middleNum = end[middle]

        if target < middleNum:
            if target >= end[middle - 1]:
                return middle
            r = middle - 1

        elif target >= middleNum:
            l = middle + 1

    return 0


def interval(jobs, end, n):
    # Wow! Look at this dymanic programming!
    dynamicP = [0] + [0] * n

    for i, job in enumerate(jobs):
        j = i + 1

        # Find closed request
        prev = binarySearch(end[:i], job[0])

        # Max of adding or not
        dynamicP[j] = max(dynamicP[prev] + job[2], dynamicP[i])

    return dynamicP[j]


def main():
    instances = int (input())
    result = ""

    for _ in range(instances):
        numJobs = int(input())
        jobs = []
        end = []

        for _ in range (numJobs):
            jobs.append(tuple(map(int, input().split())))

        # Sort by increasing time
        jobs = sorted(jobs, key = lambda job: job[1])
        end = [job[1] for job in jobs]

        value = interval(jobs, end, numJobs)

        result += f"{value}\n"

    return result.rstrip()


    
if __name__ == "__main__":
     print(main())   


