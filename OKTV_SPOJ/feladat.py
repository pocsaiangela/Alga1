def picad():
    time_of_crime = input().split(' ')
    start_of_crime = int(time_of_crime[0])
    end_of_crime = int(time_of_crime[1])

    scotland_yard_interrogations = int(input())
    count_of_people = []
    appearances = []

    for _ in range(scotland_yard_interrogations):
        appeared_and_left = input().split(' ')
        appeared = int(appeared_and_left[0])
        left = int(appeared_and_left[1])
        appearances.append((appeared, left))

    for time in range(start_of_crime, end_of_crime+1):
        people = 0
        for appearance in appearances:
            if appearance[0] <= time <= appearance[1]:
                people += 1

        count_of_people.append(people)

    print(min(count_of_people), max(count_of_people))


if __name__ == '__main__':
    for _ in range(10):
        picad()
