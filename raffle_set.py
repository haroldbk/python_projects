# Write your code here :-)
raffle = {'James','Denis','Simon'}

raffle.add('Daniel')
raffle.add("Denis")
print(raffle)
raffle.discard('Simon')
print(raffle)
winner =raffle.pop()
print(winner)

raffle2={'Kyle','Denis','Jason'}
prev_winners = frozenset({'Denis','Simon'})

raffle2-=prev_winners
print(raffle2)

winner =raffle2.pop()
print(winner)
