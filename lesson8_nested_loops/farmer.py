subsidy = int(input('Enter the subsidy amount: '))
animals = int(input('Enter the number of animals: '))
bulls = subsidy // 20
cows = subsidy // 10
calves = subsidy // 5

for bull in range(1, bulls + 1):
    for cow in range(0, cows + 1):
        for calf in range(0, calves + 1):
            if bull + cow + calf == animals:
                if bull*20 + cow*10 + calf*5 == subsidy:
                    print('Bulls:', bull, 'Cows:', cow, 'Calves:', calf)
