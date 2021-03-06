import xlrd
from pandas_ods_reader import read_ods

path = "./allgames.ods"

# load a sheet based on its index (1 based)
sheet_idx = 1
df = read_ods(path, sheet_idx)
losses = ['Florida State 1.04', 'Florida 1.04', 'Los Angeles Rams 1.03', 'Manchester City 1.05', 'Pittsburgh Steelers 1.05',
 'Milwaukee Bucks 1.06', 'Dayton 1.06', 'Dayton 1.08', 'Pittsburgh 4.25 vs Syracuse 1.09', 'Army (1.08)', 'Top Esports (1.03)',
 'Reynor (1.09)']

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
                highrisk+=1
                t+=10000*1.01
            if '1.02' in j:
                highrisk+=1
                t+=10000*1.02
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
sbAfterDiscount = (tokens+20*10000)*.9

print()
print('Since December 4th, 2020')
print('There are '+str(totalGames) +' total games listed as high risk with 1.0x multiplier')
print('There are '+ str(highrisk)+ ' games listed as 1.01 & 1.02')
print('There are '+ str(wins)+ ' wins')
print('There are '+ str(totalGames-wins)+ ' losses')
print()
print('Assuming you spent '+str(bets)+ ' tokens on each game')
print('spending '+ str(tokens+20*10000)+ ' tokens evenly on all '+str(totalGames) +' games with extra 10k on 1.01 and 1.02')
print('you spent '+ str(spenttokens+20*10000) + ' on all the winning games ')
print('you won '+ str(t)+ ' in winnings at the end together')
print('you lost '+str(tokens-spenttokens)+ ' in tokens')
print('you gained '+ str(t-sbAfterDiscount) + ' in winnings')
print('That is a total of '+ str(((t-sbAfterDiscount)/sbAfterDiscount)*100) +"% profit!")

