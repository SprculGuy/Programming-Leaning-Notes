

def function(clist, cvote):

    Winner = clist[0]
    win = 0
    for candidate in clist:
        count = 0
        invalidVotes = 0
        for vote in cvote:
            if vote not in clist:
                invalidVotes = invalidVotes + 1
            if vote == candidate:
                count = count + 1
                if count > win:
                    win = count
                    Winner = vote
        print(f"{candidate}={count} ", end="")
    
    print(f"invalidVotes={invalidVotes} ", end="")
    print(f"Winner = {Winner}")

function(["A","B","C"], ["A","F","A","B","A","B","A","C","E","B","B","B"])
            