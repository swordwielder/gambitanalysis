import xlrd
from pandas_ods_reader import read_ods

path = "./allgames.ods"

# load a sheet based on its index (1 based)
sheet_idx = 1
df = read_ods(path, sheet_idx)
losses = ['Florida State 1.04', 'Florida 1.04', 'Los Angeles Rams 1.03', 'Manchester City 1.05', 'Pittsburgh Steelers 1.05',
 'Milwaukee Bucks 1.06', 'Dayton 1.06', 'Dayton 1.08', 'Pittsburgh 4.25 vs Syracuse 1.09', 'Army (1.08)', 'Top Esports (1.03)',
 'Reynor (1.09)', 'Colorado (1.07)', 'Team Gamerlegion (1.09)', 'Georgetown (7.28) v. Creighton (1.08)', 'Houston (1.07) v. East Carolina (7.98)']

# load a sheet based on its name
# sheet_name = "allgames"
# df = read_ods(path, sheet_name)

# load a file that does not contain a header row
# if no columns are provided, they will be numbered



df = read_ods(path, 1, headers=False)
t=0
spenttokens=0
total=0
wins=0
totalGames=0
highrisk=0
highRiskGames = []
highRiskLosses = []
for i in range(1,10):
    highRiskGames.append(0)
    highRiskLosses.append(0)


for i in df:
    for j in df[i]:
        if j:
            if '1.' in j:
                totalGames+=1
tokens = 10000 * totalGames
bets = tokens/totalGames

for i in df:
    for j in df[i]:
        if j:
            if '1.01' in j:
                highRiskGames[0]+=1
                if '1.' in j and any(b in j for b in losses):
                    highRiskLosses[0]+=1
            if '1.02' in j:
                highRiskGames[1]+=1
                if '1.' in j and any(b in j for b in losses):
                    highRiskLosses[1]+=1
            if '1.03' in j:
                highRiskGames[2]+=1
                if '1.' in j and any(b in j for b in losses):
                    highRiskLosses[2]+=1
            if '1.04' in j:
                highRiskGames[3]+=1
                if '1.' in j and any(b in j for b in losses):
                    highRiskLosses[3]+=1
            if '1.05' in j:
                highRiskGames[4]+=1
                if '1.' in j and any(b in j for b in losses):
                    highRiskLosses[4]+=1
            if '1.06' in j:
                highRiskGames[5]+=1
                if '1.' in j and any(b in j for b in losses):
                    highRiskLosses[5]+=1
            if '1.07' in j:
                highRiskGames[6]+=1
                if '1.' in j and any(b in j for b in losses):
                    highRiskLosses[6]+=1
            if '1.08' in j:
                highRiskGames[7]+=1
                if '1.' in j and any(b in j for b in losses):
                    highRiskLosses[7]+=1
            if '1.09' in j:
                highRiskGames[8]+=1
                if '1.' in j and any(b in j for b in losses):
                    highRiskLosses[8]+=1

for i in df:
    for j in df[i]:
        if j:
            if '1.01' in j:
                highrisk+=1
            if '1.02' in j:
                highrisk+=1
            if '1.' in j and not any(b in j for b in losses):
                index = j.find('1.')
                print('betting '+str(bets) +' on ')
                print(j)
                
                total = float(j[index:index+4]) * bets
                print(total)
                t+=total
                wins+=1
                spenttokens+=bets

print()
sbAfterDiscount = tokens*.95

print()
print('Since December 4th, 2020')
print('There are '+str(totalGames) +' total games listed as high risk with 1.0x multiplier')
print('There are '+ str(highrisk)+ ' games listed as 1.01 & 1.02')
print('There are '+ str(wins)+ ' wins')
print('There are '+ str(totalGames-wins)+ ' losses')
print('With 10% discount you are going to get the following:')
print()
print('Assuming you spent '+str(bets)+ ' tokens on each game')
print('spending '+ str(tokens)+ ' tokens evenly on all '+str(totalGames) +' games')
print('you spent '+ str(spenttokens) + ' on all the winning games ')
print('you won '+ str(t)+ ' in winnings at the end together')
print('you lost '+str(tokens-spenttokens)+ ' in tokens')
print('you gained '+ str(t-sbAfterDiscount) + ' in winnings')
print('That is a total of '+ str(((t-sbAfterDiscount)/sbAfterDiscount)*100) +"% profit!")
# print(highRiskGames)
print()
for i in range(len(highRiskGames)):
    success = round((highRiskGames[i]-highRiskLosses[i])/highRiskGames[i]*100,1)
    print('There are '+str(highRiskGames[i])+ " 1.0"+str(i+1) + ' and there are '+ str(highRiskLosses[i]) +' losses in this group, ' +"success rate: " + str(success)+"%")