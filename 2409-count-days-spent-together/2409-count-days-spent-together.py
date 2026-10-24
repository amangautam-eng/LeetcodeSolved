class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:

        days=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        daysum=[0]
        total=0

        for x in days:
            daysum.append(x+total)
            total+=x
        

        def convday(date):
            d=date.split('-')
            day=daysum[int(d[0])-1]+int(d[1])

            return day
        alicecome=convday(arriveAlice)
        alicego=convday(leaveAlice)

        bobcome=convday(arriveBob)
        bobgo=convday(leaveBob)

        if alicecome>bobgo or bobcome>alicego:
            return 0
        elif alicecome<bobcome and alicego<bobgo:
            return alicego-bobcome+1
        elif bobcome<alicecome and bobgo<alicego:
            return bobgo-alicecome+1
        else:
            return min(alicego-alicecome,bobgo-bobcome)+1

        


        