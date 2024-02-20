def get_number_of_platforms_required(train_arrival_times_list, train_depature_times_list,total_no_of_trains):
    train_arrival_times_list.sort()
    train_depature_times_list.sort()
    platforms_required = 1
    max_platforms_required = 1
    i=1
    j=0
    while (i < total_no_of_trains and j < total_no_of_trains):
        if (train_arrival_times_list[i] <= train_depature_times_list[j]):
            platforms_required += 1
            i+=1
        elif (train_arrival_times_list[i]> train_depature_times_list[j]):
            platforms_required -= 1
            j+=1
        if (platforms_required > max_platforms_required):
            max_platforms_required = platforms_required
    return max_platforms_required
def main():
    train_arrival_times_list = list(map(int, input().split()))
    train_depature_times_list = list(map(int, input().split()))
    total_no_of_trains= len(train_arrival_times_list)
    result=get_number_of_platforms_required(train_arrival_times_list, train_depature_times_list,total_no_of_trains)
    print(result)
main()
    
    
