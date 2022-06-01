from insertionsort import insertionSort
from shuffle import merge

"""
No. of transactions = 2*N-3 for N cows for N>=2 (always)
split : N-1 from A to B , N-2 from B to A
Basic algos
2 algos :
a) 1 - Min 1,2 is sent first from A to B 
   2 - Max 1,2 is sent next from A to B
   3 - Min of all values in B is sent from B to A

b) 1 - Min 1 and Max 2 is sent first from A to B 
   2 - Min of all values in B is sent from B to A

"""

"""



"""


class Crossing_Bridge:
    def __init__(self, cows):
        # this list will contain a)cows in side a b)cows in side b c)total time taken for all transactions that has occured
        self.temptransaction = []
        insertionSort(cows)
        shuffled = merge()
        cows = shuffled.shuffle(cows.copy())
        self.transaction = self.crossing(self.temptransaction, cows)

    def show_crossing(self):
        sum = 0
        print("\nSTART:")
        for i in range(0, len(self.transaction)):
            if len(self.transaction[i-1][0]) == 0 and i != 0:
                sum += self.transaction[i-1][2]+self.transaction[0][0][0]
                print("\nNEXT GROUP:")
            print(self.transaction[i][0], "  |_______________|  ", self.transaction[i]
                  [1], "\t total time taken = ", self.transaction[i][2]+sum, "minutes")
        print("\nEND")

    def sequence1(self, cows):
        # uses algo 1
        # basically runs until location A is empty
        # based on the princi that we move the slowest two cows together , this happens only when the fastest two cows are not on the same side
        # if the fastest two cows are on the same side , we move them from A to B
        # also , only the minimum value moves from B to A. Thus sorting proves to be essential.
        a = cows  # side a has the initial list of cows
        min1, min2 = a[0], a[1]
        b = []  # side b is empty initially
        time_taken = 0  # time taken will be added each time we make a transaction
        side_select = 'A'
        sequence = [[a.copy(), b.copy(), time_taken]]
        while len(a) > 0:
            if side_select == 'A':
                if (min1 in a and min2 in a) or len(b) == 0:
                    insertionSort(b, a.pop(1))
                    time_taken += b[0]
                    insertionSort(b, a.pop(0))
                else:
                    insertionSort(b, a.pop(-2))
                    insertionSort(b, a.pop(-1))
                    time_taken += b[-1]
                side_select = 'B'
                sequence.append([a.copy(), b.copy(), time_taken])
            elif side_select == 'B':
                time_taken += b[0]
                insertionSort(a, b.pop(0))
                side_select = 'A'
                sequence.append([a.copy(), b.copy(), time_taken])
        return sequence

    def sequence2(self, cows):
        # uses algo 2
        # basically runs until location A is empty
        # based on the princi that we move the slowest and fastest together from A to B
        # The fastest cow enjoys being in every single transaction a) from A to B along with the slowest cow in A , b) from B to A (returning to repeat said process)
        # also , only the minimum value moves from B to A. Thus sorting proves to be essential.
        a = cows  # side a has the initial list of cows
        b = []  # side b is empty initially
        time_taken = 0  # time taken will be added each time we make a transaction
        side_select = 'A'
        sequence = [[a.copy(), b.copy(), time_taken]]
        while len(a) > 0:
            if side_select == 'A':
                insertionSort(b, a.pop())
                time_taken += b[0]
                insertionSort(b, a.pop(0))
                side_select = 'B'
                sequence.append([a.copy(), b.copy(), time_taken])
            elif side_select == 'B':
                time_taken += b[0]
                insertionSort(a, b.pop(0))
                side_select = 'A'
                sequence.append([a.copy(), b.copy(), time_taken])
        return sequence

    def crossing(self, temptransaction, cows):
        if len(cows) < 4:
            temptransaction = self.sequence2(cows.copy())
        elif len(cows) == 4:
            s1 = self.sequence1(cows.copy())
            s2 = self.sequence2(cows.copy())
            temptransaction = s1 if s1[-1][2] < s2[-1][2] else s2
        else:
            copyCows = []
            i = 0
            while i in range(0, len(cows)):
                if i == 0:
                    copyCows.append(cows.copy()[i:i+4])
                    i += 4
                else:
                    next_group = cows.copy()[i:i+3]
                    next_group.append(cows.copy()[0])
                    copyCows.append(next_group)
                    i += 3
            print("The cows can be grouped into {} groups with maximum four cows as such :".format(
                len(copyCows)))
            for i in copyCows:
                i.sort()
                print(i)
                temptransaction.extend(self.crossing(temptransaction, i))
        return temptransaction
