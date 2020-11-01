# 정렬된 리스트를 입력받으면, 가장 간격이 짧은 값의 쌍을 반환하는 함수 작성.

def find_shortest_way(sorted_list):
    length = len(sorted_list)
    shortest_way = [[sorted_list[0], sorted_list[1]]]

    for index in range(1, length - 1):
        current_location = [sorted_list[index], sorted_list[index + 1]]
        distance = current_location[1] - current_location[0]
        compare_distance = shortest_way[-1][1] - shortest_way[-1][0]

        if distance < compare_distance:
            shortest_way = []
            shortest_way.append(current_location)
        
        elif distance == compare_distance:
            shortest_way.append(current_location)
        
    return shortest_way

test_list = [1,3,6,9,10]
result = find_shortest_way(test_list)
print(result)