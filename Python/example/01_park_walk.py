# test용
park = 	["OSO", 
         "OOO", 
         "OXO", 
         "OOO"]
routes = ["E 2", "S 3", "W 1"]

# park와 routes의 조건
PARK_LONG_MAX = 50
PARK_LONG_MIN = 3
ROUTES_LONG_MAX = 50
ROUTES_LONG_MIN = 1


# park의 크기가 조건에 만족하는지 확인
# 조건에 만족하면 높이와 가로의 길이를 반환하고, 아니면 -1 반환
def park_long_check(park_arr):

    if not (PARK_LONG_MIN <= len(park_arr) <= PARK_LONG_MAX):
        return -1
    
    for park in park_arr:
        if not (PARK_LONG_MIN <= len(park) <= PARK_LONG_MAX):
            return -1

    for i in range(len(park_arr)-1):
        if len(park_arr[i]) != len(park_arr[i+1]):
            return -1
        
    park_size = [ len(park_arr), len(park_arr[0]) ]
    return park_size


# routes의 크기가 조건에 만족하는지 확인
# 조건에 만족하지 않으면 -1 반환
def routes_long_check(routes):
    if not (ROUTES_LONG_MIN <= len(routes) <= ROUTES_LONG_MAX):
        return -1
    
    for route in routes:
        if not (ROUTES_LONG_MIN <= len(route) <= ROUTES_LONG_MAX):
            return -1

    for route in routes:
        if not (1 <= int(route[2]) <= 9):
            return -1
     
    routes_size = [ len(routes), len(routes[0]) ]
    return routes_size


# start지점의 위치 반환 함수
def search_s(park):
    H = -1
    W = -1

    for p in park:
        find_start = p.find("S")
        H = H + 1

        if find_start != -1:
            W = find_start
            break

    sPoint = [ H, W ]
    return sPoint
    

def solution(park, routes):
    # park 조건 확인 / 조건 불만족 시 문구 출력
    park_size = park_long_check(park)
    if park_size == -1:
        return print("Park Size Error!!")

    # routes 조건 확인 / 조건 불만족 시 문구 출력
    routes_long = routes_long_check(routes)
    if routes_long == -1:
        return print("routes Long Error!!")

    start_point = search_s(park)

    for route in routes:
        move_point = [ 0, 0 ]
        cnt = 0

        # 방위, 움직일 방향이 park크기 밖인지, 움직인 후 park크기 밖인지 확인
        if (route[0] == "N") and (start_point[0] > 0) and\
            (start_point[0] - int(route[2]) >= 0):
            for i in range(int(route[2])):
                cnt = cnt + 1
                if park[ start_point[0] - cnt ][ start_point[1] ] == "X": 
                    move_point = [ 0, 0 ]
                    break
                else: 
                    move_point[0] = move_point[0] - 1
        elif (route[0] == "S") and (start_point[0] < park_size[0]) and\
            (start_point[0] + int(route[2]) < park_size[0]):
            for i in range(int(route[2])):
                cnt = cnt + 1
                if park[ start_point[0] + cnt ][ start_point[1] ] == "X": 
                    move_point = [ 0, 0 ]
                    break
                else: 
                    move_point[0] = move_point[0] + 1
        elif (route[0] == "W") and (start_point[1] > 0) and\
            (start_point[1] - int(route[2]) >= 0):
            for i in range(int(route[2])):
                cnt = cnt + 1
                if park[ start_point[0] ][ start_point[1] - cnt ] == "X": 
                    move_point = [ 0, 0 ]
                    break
                else: 
                    move_point[1] = move_point[1] - 1
        elif (route[0] == "E") and (start_point[1] < park_size[1]) and\
            (start_point[1] + int(route[2]) < park_size[1]):
            for i in range(int(route[2])):
                cnt = cnt + 1
                if park[ start_point[0] ][ start_point[1] + cnt ] == "X": 
                    move_point = [ 0, 0 ]
                    break
                else: 
                    move_point[1] = move_point[1] + 1
        
        start_point[0] = start_point[0] + move_point[0]
        start_point[1] = start_point[1] + move_point[1]

    answer = start_point
    return answer


if __name__ == "__main__":
    # print(park_long_check(park))
    # # print(routes_long_check(routes))
    # print(search_s(park))
    
    # print(solution(park, routes))

    # print(routes[0].split(" "))

    test = [
                "OSO", 
                "OOO", 
                "OXO", 
                "OOO"
            ]
    
    # b = [i[1] for i in test[2:4]]
    b = list(test)
    b[0] = list(b[0])
    b[0][1] = "O"
    b[0] = ''.join(b[0])
    print(b)
