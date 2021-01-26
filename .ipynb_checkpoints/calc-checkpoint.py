import xlrd
from pandas_ods_reader import read_ods

path = "./allgames.ods"

# load a sheet based on its index (1 based)
sheet_idx = 1
df = read_ods(path, sheet_idx)
losses = ['Florida State 1.04', 'Florida 1.04', 'Los Angeles Rams 1.03', 'Manchester City 1.05']

# load a sheet based on its name
# sheet_name = "allgames"
# df = read_ods(path, sheet_name)

# load a file that does not contain a header row
# if no columns are provided, they will be numbered
tokens = 10000
bets = tokens/47
df = read_ods(path, 1, headers=False)
t=0
spenttokens=0
total=0
wins=0
totalGames=0
for i in df:
    for j in df[i]:
        if j:
            if '1.' in j:
                totalGames+=1
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
print('There are '+str(totalGames) +' total games')
print('There are '+ str(wins)+ ' wins')
print()
print('you spent '+ str(spenttokens) + ' on all the winning games ')
print('you spent on average '+str(bets)+ ' tokens on each game')
print('you won '+ str(t)+ 'all together')
print('you lost '+str(10000-spenttokens)+ ' tokens')
print('you gained '+ str(t-9000) + ' tokens')
print('That is a total of '+ str(((t-9000)/9000)*100) +"%")

