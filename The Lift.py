people_waiting = int(input())
current_state_of_lift = list(map(int, input().split(" ")))


for i in current_state_of_lift:
    while current_state_of_lift[i] <= 4:
        if current_state_of_lift[i] == 4:
            i +=1
            continue

        people_waiting -= 1
        current_state_of_lift[i] += 1

        if people_waiting > 0 and current_state_of_lift.count(4) == len(current_state_of_lift):
            print(f"There isn't enough space! {people_waiting} people in a queue!")
            more_people = True
            break

        if people_waiting <= 0 and current_state_of_lift.count(4) != len(current_state_of_lift):
            no_people = True
            print("The lift has empty spots!")
            break

    break

print(*current_state_of_lift)