# 테스트 케이스
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

# 제한사항
ID_LIST_LEN_MIN = 2
ID_LIST_LEN_MAX = 1000
REPORT_LEN_MIN = 1
REPORT_LEN_MAX = 200000
K_MIN = 1
K_MAX = 200


class ReportResult:
    def __init__(self, id_list, report, k):
        self.id_list = id_list
        self.report = report
        self.k = k
        self.__report_dict = {}


    # is_list에 있는 유저들의 id를 __report_dict의 key값으로 만들어 밑의 dict를 값으로 넣음
    def __insert_id_list(self):
        for id in self.id_list:
            self.__report_dict[id] = {'Declaration': 0, 'mail': 0}
        
        return 1


    # report에서 공백으로 split하여 신고자와 신고당한사람을 user, decl로 나눠 dict에 저장
    def report_to_dict(self):
        self.__insert_id_list()

        for report in self.report:
            user, decl = report.split(" ")
            self.__report_dict[user][decl] = 1

        return 1

    
    # private 변수인 __report_dict를 반환하는 함수
    def get_report_dict(self):
        report_dict = self.__report_dict
        return report_dict


    # user를 신고한 횟수를 카운트하여 key(Declaration)에 카운트
    def __check_report(self):
        for id in self.id_list:
            # 신고한 적이 있는 user들의 list를 만듬
            dict_id_list = self.__report_dict[id].keys()

            # Declaration, mail 두가지의 key만 있는경우 다음 반복문 진행
            if len(dict_id_list) == 2:
                continue
            
            # 신고한 적 있는 user들 반복
            for dict_id in dict_id_list:
                # dict_id가 Declaration, mail인 경우 무시
                if dict_id == 'Declaration' or dict_id == 'mail':
                    continue
                
                # id가 신고한 dict_id
                # dict_id의 dict의 key인 Declaration에 카운트
                self.__report_dict[dict_id]['Declaration'] += 1

        return 1
    

    # 신고 당한 사람의 신고 횟수가 k번 이상이 되어 정지됨
    # 정지된 사람을 신고한 사람들에게 메일을 발송해야 하는데 발송할 사람들을 확인하는 함수
    def check_mail(self):
        self.__check_report()

        for id in self.id_list:
            declaration = self.__report_dict[id]['Declaration']

            # k번 이상 신고 당한 user들만
            if declaration >= self.k:
                cnt = 0

                for id2 in self.id_list:
                    if id == id2:
                        continue
                
                    # id2(user)의 신고자 명단에 id(정지된 사람)의 id가 있다면
                    # KeyError가 발생하지 않음으로 카운트
                    # 신고당한 횟수(declaration)만큼 카운트 되면 다음 정지된 사람을 신고한 user를 찾음
                    try:
                        if self.__report_dict[id2][id]:
                            self.__report_dict[id2]['mail'] += 1
                            cnt += 1

                            if cnt == declaration:
                                break
                    except KeyError:
                        continue
        
        return 1


    # user가 몇번 메일을 받는지 확인하는 함수
    def send_mail(self):
        mail = []

        for id in self.id_list:
            mail.append(self.__report_dict[id]['mail'])
    
        return mail


def solution(id_list, report, k):
    report_re = ReportResult(id_list, report, k)

    report_re.report_to_dict()
    report_re.check_mail()

    answer = report_re.send_mail()

    return answer


if __name__ == '__main__':
    print(solution(id_list, report, k))