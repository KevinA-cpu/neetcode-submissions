class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # array of triplets and target triplet
        # the operation is that choose the biggest number per element in the triplet
        # target positiion must be the same
        # 1, look through the triplets, spot the necessary number at the necessary location
        # 2 discard triplet that will sabotage this
    
# [2,5,6],[1,4,4],[5,7,5] <-- False
# [2,3,6],[1,4,4],[5,3,5] <-- True Target: [5,4,6]
# [2,3,6],[5,4,5]
# [5,4,6]
# [5,3,6],[1,4,4],[5,3,5] <--  Target: [5,4,6]

# [[2,6,6],[10,5,1],,,] [10,6,6]
        firstTarget = target[0]
        secondTarget = target[1]
        thirdTarget = target[2]
        newTriplets=[]
        for i in triplets:
            if i[0] == firstTarget and i[1] == secondTarget and i[2] == thirdTarget:
                return True
            elif i[0] <= firstTarget and i[1] <= secondTarget and i[2] <= thirdTarget:
                newTriplets.append(i)

        newLength = len(newTriplets)
        if newLength == 0:
            return False
        print(triplets)
        first=newTriplets[0][0]
        second=newTriplets[0][1]
        third=newTriplets[0][2]
        for i in range(1, len(newTriplets)):
            first = max(first, newTriplets[i][0])
            second = max(second, newTriplets[i][1])
            third = max(third, newTriplets[i][2])

        return firstTarget == first and secondTarget == second and thirdTarget == third

            