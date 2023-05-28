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
            self.__report_dict[id] = {'reporter': [], 'mail': 0}
        
        return 1


    # set을 사용하여 report의 중복되는 요소를 제거
    # 한 user가 다른 한 user를 여러번 신고한 것을 1번으로 적용하는 과정
    def report_to_dict(self):
        self.__insert_id_list()
        report_set = set(self.report)
        self.report = report_set

        for report in self.report:
            user, decl = report.split(" ")
            self.__report_dict[decl]['reporter'].append(user)

        return 1


    # private 변수인 __report_dict를 반환하는 함수
    def get_report_dict(self):
        report_dict = self.__report_dict
        return report_dict


    # k번 이상 신고되어 정지된 user를 신고한 user들에게 mail 보낼 횟수를 확인하는 함수
    def __check_report(self):
        for id in self.id_list:

            # user들을 신고한 user들(reporter)의 list가 k 이상일 때
            if len(self.__report_dict[id]['reporter']) >= self.k:

                # id user를 신고한 user들의 dict중 mail인 key의 값을 1 증가 시킴
                for reporter_id in self.__report_dict[id]['reporter']:
                    self.__report_dict[reporter_id]['mail'] += 1

        return 1


    # __report_dict에서 각각의 user의 key가 mail인 값을 mail list에 추가시켜 반환하는 함수
    def send_mail(self):
        self.__check_report()
        mail = []

        for id in self.id_list:
            mail.append(self.__report_dict[id]['mail'])
    
        return mail


def solution(id_list, report, k):
    report_re = ReportResult(id_list, report, k)

    report_re.report_to_dict()

    answer = report_re.send_mail()

    return answer


if __name__ == '__main__':

    print(solution(id_list, report, k))

