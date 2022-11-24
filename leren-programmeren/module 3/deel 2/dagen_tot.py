DagVandaag = input("Welke dag is het vandaag ")

week = ['maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag', 'zondag']
x = 0
while True:
    print(week[x])
    if week[x] == DagVandaag:
        break
    x += 1