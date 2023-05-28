# park와 routes의 조건
PARK_LONG_MAX = 50
PARK_LONG_MIN = 3
ROUTES_LONG_MAX = 50
ROUTES_LONG_MIN = 1

class Dog:
    def __init__(self, park, routes):
        self.park = park
        self.routes = routes
        self.__g = { "N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1) }

    # park의 크기가 조건에 만족하는지 확인
    # 조건에 만족하면 높이와 가로의 길이를 반환하고, 아니면 -1 반환
    def get_park_size(self):
        check = len(self.park[0])
        
        if not (PARK_LONG_MIN <= len(self.park) <= PARK_LONG_MAX):
            return -1
        
        for p in self.park:
            if not (PARK_LONG_MIN <= len(p) <= PARK_LONG_MAX)\
                or (check != len(p)):
                return -1

        park_size = [ len(self.park), len(self.park[0]) ]
        return park_size


    # routes의 크기가 조건에 만족하는지 확인
    # 조건에 만족하지 않으면 -1 반환
    def check_routes_rule(self):
        if not (ROUTES_LONG_MIN <= len(self.routes) <= ROUTES_LONG_MAX):
            return -1
        
        for route in self.routes:
            if not (ROUTES_LONG_MIN <= len(route) <= ROUTES_LONG_MAX)\
                or not (1 <= int(route[2]) <= 9):
                return -1

        routes_size = [ len(self.routes), len(self.routes[0]) ]
        return routes_size


    # start지점의 위치 반환 함수
    def get_start_point(self):
        H = -1
        W = -1

        for p in self.park:
            find_start = p.find("S")
            H = H + 1

            if find_start != -1:
                W = find_start
                break

        sPoint = [ H, W ]
        return sPoint
    

    def move(self, direction, distance):
        # str로 들어온 이동거리를 int로 변경
        distance = int(distance)

        # get_park_size 함수로 park 크기를 찾기
        park_size = self.get_park_size()

        # get_start_point 함수로 출발지점 찾기
        start_p = self.get_start_point()

        move_h = start_p[0] + (self.__g[direction][0] * distance)
        move_w = start_p[1] + (self.__g[direction][1] * distance)

        # 현재 위치와 이동할 위치의 min, max를 구해 list에서 슬라이스 하기 편하도록
        max_height = max(start_p[0], move_h)
        min_height = min(start_p[0], move_h)
        max_width = max(start_p[1], move_w)
        min_width = min(start_p[1], move_w)

        # 시작 지점과 이동할 위치가 park의 크기를 벗어날 경우 동작하지 않고 기존의 park 반환
        if not (0 <= start_p[0] < park_size[0]) \
            or not (0 <= start_p[1] < park_size[1]) \
            or not (0 <= (move_h) < park_size[0]) \
            or not (0 <= (move_w) < park_size[1]):
            return self.park
        # 특정 열 또는 행에 X가 있는 경우 동작하지 않고 기존의 park 반환
        elif "X" in [height[start_p[1]] for height in self.park[min_height:max_height+1]]\
            or "X" in self.park[start_p[0]][min_width:max_width+1]:
            return self.park

        # str은 항목할당을 지원하지 않음
        # park의 특정 행을 str에서 list로 변경후 S위치를 변경
        self.park[start_p[0]] = list(self.park[start_p[0]])
        self.park[move_h] = list(self.park[move_h])

        self.park[start_p[0]][start_p[1]] = "O"
        self.park[move_h][move_w] = "S"

        self.park[start_p[0]] = ''.join(self.park[start_p[0]])
        self.park[move_h] = ''.join(self.park[move_h])

        return self.park


def solution(park, routes):

    dog = Dog(park, routes)

    # park 조건 확인 / 조건 불만족 시 문구 출력
    park_size = dog.get_park_size()
    if park_size == -1:
        return print("Park Size Error!!")

    # routes 조건 확인 / 조건 불만족 시 문구 출력
    routes_long = dog.check_routes_rule()
    if routes_long == -1:
        return print("routes Long Error!!")

    # routes의 정보를 순서대로 Dog class의 객체 dog의 함수 move로 전달
    for route in routes:
        h, w = route.split(" ")
        dog.move(h, w)
    
    answer = dog.get_start_point()
    return answer


if __name__ == "__main__":
    # test용
    park = 	["SOO", "OOO", "OOO"]
    routes = ["E 2", "S 2", "W 1"]


    print(solution(park, routes))