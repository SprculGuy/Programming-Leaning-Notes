class Team:
    def __init__(self,teamRanking, teamConf,teamName):
        self.teamRanking=teamRanking
        self.teamConf = teamConf
        self.teamName = teamName

class Tournament:
    def __init__(self,teamList,tournDetails):
        self.teamList=teamList
        self.tournDetails=tournDetails
    def confCount(self):
        ans={}
        for i in self.teamList:
            if(i.teamConf in ans):
                ans[i.teamConf]+=1
            else:
                ans[i.teamConf]= 1
        return ans

def tCount(n,tournList):
    matchedtoulist=[]
    for i in tournList:
        if n==i.tournDetails["Time"]:
            matchedtoulist.append(i)
    finalTeamDict={}
    for i in matchedtoulist:
        for o in i.teamList:
            finalTeamDict[o.teamRanking]=o.teamName
    ansList=[]
    ansDict=dict(sorted(finalTeamDict.items()))
    for i in ansDict.keys():
        ansList.append(ansDict[i])
    if(ansList==[]):
        return None
    else:
        return ansList


tournList=[]
ntourn=int(input())
for i in range(ntourn):
    teamList=[]
    nteam=int(input())
    for i in range(nteam):
        teamRanking=int(input())
        teamConf = input()
        teamName =input()
        teamList.append(Team(teamRanking,teamConf,teamName))
    detailDict={}
    detailDict["Name"]=input()
    detailDict["Host"]=input()
    detailDict["Edition"]=int(input())
    detailDict["Year"]=int(input())
    detailDict["Participants"]=int(input())
    detailDict["Time"]=int(input())
    tournList.append(Tournament(teamList,detailDict))

ninput=int(input())
ans1=tournList[0].confCount()
for i in ans1.keys():
    print(i,"-",ans1[i])
ans2=tCount(ninput,tournList)
if ans2==None:
    print("No Team Found")
else:
    for i in ans2:
        print(i)