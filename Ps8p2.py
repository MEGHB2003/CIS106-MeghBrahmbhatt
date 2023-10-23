def calcbatavg(hits, atbats):
  if atbats == 0:
    return 0.0
  else:
    return hits / atbats

players = []
count = 0
while True:
  player = {}
  player['name'] = input("Enter player name: ")
  player['hits'] = int(input("Enter hits: "))
  player['atbats'] = int(input("Enter at bats: "))
  player['batavg'] = calcbatavg(player['hits'], player['atbats'])
  players.append(player)
  count += 1
  if input("Do you want to continue? (y/n): ") == 'n':
    break

print("\nPlayer Data:")
for player in players:
  print(player['name'], player['batavg'])
  
print("\nTotal Players:", count)