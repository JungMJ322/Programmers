## 신고 결과 받기

> https://school.programmers.co.kr/learn/courses/30/lessons/92334



### 문제 설명

신입사원 무지는 게시판 불량 이용자를 신고하고 처리 결과를 메일로 발송하는 시스템을 개발하려 합니다. 무지가 개발하려는 시스템은 다음과 같습니다.

- 각 유저는 한 번에 한 명의 유저를 신고할 수 있습니다.
  - 신고 횟수에 제한은 없습니다. 서로 다른 유저를 계속해서 신고할 수 있습니다.
  - 한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.
- k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송합니다.
  - 유저가 신고한 모든 내용을 취합하여 마지막에 한꺼번에 게시판 이용 정지를 시키면서 정지 메일을 발송합니다.

다음은 전체 유저 목록이 ["muzi", "frodo", "apeach", "neo"]이고, k = 2(즉, 2번 이상 신고당하면 이용 정지)인 경우의 예시입니다.

| 유저 ID  | 유저가 신고한 ID | 설명                               |
| -------- | ---------------- | ---------------------------------- |
| "muzi"   | "frodo"          | "muzi"가 "frodo"를 신고했습니다.   |
| "apeach" | "frodo"          | "apeach"가 "frodo"를 신고했습니다. |
| "frodo"  | "neo"            | "frodo"가 "neo"를 신고했습니다.    |
| "muzi"   | "neo"            | "muzi"가 "neo"를 신고했습니다.     |
| "apeach" | "muzi"           | "apeach"가 "muzi"를 신고했습니다.  |

각 유저별로 신고당한 횟수는 다음과 같습니다.

| 유저 ID  | 신고당한 횟수 |
| -------- | ------------- |
| "muzi"   | 1             |
| "frodo"  | 2             |
| "apeach" | 0             |
| "neo"    | 2             |

위 예시에서는 2번 이상 신고당한 "frodo"와 "neo"의 게시판 이용이 정지됩니다. 이때, 각 유저별로 신고한 아이디와 정지된 아이디를 정리하면 다음과 같습니다.

| 유저 ID  | 유저가 신고한 ID  | 정지된 ID        |
| -------- | ----------------- | ---------------- |
| "muzi"   | ["frodo", "neo"]  | ["frodo", "neo"] |
| "frodo"  | ["neo"]           | ["neo"]          |
| "apeach" | ["muzi", "frodo"] | ["frodo"]        |
| "neo"    | 없음              | 없음             |

따라서 "muzi"는 처리 결과 메일을 2회, "frodo"와 "apeach"는 각각 처리 결과 메일을 1회 받게 됩니다.

이용자의 ID가 담긴 문자열 배열 `id_list`, 각 이용자가 신고한 이용자의 ID 정보가 담긴 문자열 배열 `report`, 정지 기준이 되는 신고 횟수 `k`가 매개변수로 주어질 때, 각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 return 하도록 solution 함수를 완성해주세요.

------



### 제한사항

- 2 ≤

   

  ```
  id_list
  ```

  의 길이 ≤ 1,000

  - 1 ≤ `id_list`의 원소 길이 ≤ 10
  - `id_list`의 원소는 이용자의 id를 나타내는 문자열이며 알파벳 소문자로만 이루어져 있습니다.
  - `id_list`에는 같은 아이디가 중복해서 들어있지 않습니다.

- 1 ≤

   

  ```
  report
  ```

  의 길이 ≤ 200,000

  - 3 ≤ `report`의 원소 길이 ≤ 21
  - `report`의 원소는 "이용자id 신고한id"형태의 문자열입니다.
  - 예를 들어 "muzi frodo"의 경우 "muzi"가 "frodo"를 신고했다는 의미입니다.
  - id는 알파벳 소문자로만 이루어져 있습니다.
  - 이용자id와 신고한id는 공백(스페이스)하나로 구분되어 있습니다.
  - 자기 자신을 신고하는 경우는 없습니다.

- 1 ≤ `k` ≤ 200, `k`는 자연수입니다.

- return 하는 배열은 `id_list`에 담긴 id 순서대로 각 유저가 받은 결과 메일 수를 담으면 됩니다.

------



### 입출력 예

| id_list                              | report                                                       | k    | result    |
| ------------------------------------ | ------------------------------------------------------------ | ---- | --------- |
| `["muzi", "frodo", "apeach", "neo"]` | `["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]` | 2    | [2,1,1,0] |
| `["con", "ryan"]`                    | `["ryan con", "ryan con", "ryan con", "ryan con"]`           | 3    | [0,0]     |

------



### 입출력 예 설명

**입출력 예 #1**

문제의 예시와 같습니다.

**입출력 예 #2**

"ryan"이 "con"을 4번 신고했으나, 주어진 조건에 따라 한 유저가 같은 유저를 여러 번 신고한 경우는 신고 횟수 1회로 처리합니다. 따라서 "con"은 1회 신고당했습니다. 3번 이상 신고당한 이용자는 없으며, "con"과 "ryan"은 결과 메일을 받지 않습니다. 따라서 [0, 0]을 return 합니다.

------



### 제한시간 안내

- 정확성 테스트 : 10초

----



### 풀이

- 각 유저는 한 번에 한 명의 유저를 신고할 수 있고, 서로다른 유저를 계속 신고할 수 있으며, 한 유저가 다른유저를 중복 신고할 경우 신고 횟수는 1회로 처리

  - `dictionary`로 신고한 유저를 `key`로
  - 신고한 유저가 신고한(신고당한 유저)를 신고한 유저의 `value`로 한다
    - 신고한 유저가 다른 유저를 중복신고 하더라도 중복되지 않음
      - but 신고한 유저가 서로 다른 여러 유저를 신고한다면?
      - `dict`안에 `dict`로 해서 중복이 없도록? / 일딴 해보자

- k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송

  - `유저A`가 `유저B`를 신고했는데 `유저B`가 정지를 당했다면 `유저A`에게 `유저B`가 신고되었다는 메일을 발송

- ```json
  // 이런 형식으로 신고한 유저, 그 유저가 신고한 유저가 되로록 dict 구성해서 만듬
  // 이때 k = 2
  {
      'A': {
          'B': 1, 'C': 1
      },
      'B': {
          'C': 1, 'D': 1
      },
      'D': {
          'B': 1, 'C': 1
      }
  }
  ```

  - 위와 같다면 A는 B, C를 신고하였고, B는 C, D를 신고하였고, C는 아무도 신고하지 않았고, D는 B, C를 신고 하였다면
  - 신고를 2번 이상 당한 B, C는 정지
  - B, C유저를 신고한 A, D유저에게 신고한 유저가 정지되었다는 사실을 메일로 발송
    - 유저 id가 `['A', 'B', 'C', 'D']`라면
    - `result == [2, 0, 0, 2]`가 되도록 함
  
- [02_report_result.py]()



- 다른사람의 풀이

  - ```python
    def solution(id_list, report, k):
        answer = [0] * len(id_list)    
        reports = {x : 0 for x in id_list}
    
        for r in set(report):
            reports[r.split()[1]] += 1
    
        for r in set(report):
            if reports[r.split()[1]] >= k:
                answer[id_list.index(r.split()[0])] += 1
    
        return answer
    ```

  - `set`은 중복이 허용되지 않는다는 특징을 이용하여 문제를 해결한 것으로 보임

  - 짧고 간결하다

  - `dict`는 생각났지만 `set`은 생각나지 않아 더 어렵게 문제를 해결한 것 같음

  - 속도는 내 코드가 좀더 빠른거 같음

    - |              | 다른사람 풀이             | 내 풀이                  |
      | ------------ | ------------------------- | ------------------------ |
      | 테스트 1 〉  | 통과  (0.01ms, 10.3MB)    | 통과  (0.03ms, 10.3MB)   |
      | 테스트 2 〉  | 통과  (0.03ms, 10.4MB)    | 통과  (0.04ms, 10.3MB)   |
      | 테스트 3 〉  | 통과  (1532.73ms, 39.5MB) | 통과  (456.71ms, 45.4MB) |
      | 테스트 7 〉  | 통과  (3.51ms, 10.6MB)    | 통과  (4.15ms, 10.7MB)   |
      | 테스트 8 〉  | 통과  (3.54ms, 10.7MB)    | 통과  (4.22ms, 10.8MB)   |
      | 테스트 9 〉  | 통과  (411.90ms, 23.9MB)  | 통과  (140.57ms, 26.1MB) |
      | 테스트 11 〉 | 통과  (601.03ms, 39.6MB)  | 통과  (268.54ms, 44.9MB) |
      | 테스트 18 〉 | 통과  (0.93ms, 10.3MB)    | 통과  (2.89ms, 10.1MB)   |
      | 테스트 19 〉 | 통과  (1.48ms, 10.3MB)    | 통과  (3.24ms, 10.4MB)   |
      | 테스트 20 〉 | 통과  (381.66ms, 20.3MB)  | 통과  (259.79ms, 23.6MB) |
      | 테스트 21 〉 | 통과  (746.16ms, 31.6MB)  | 통과  (340.96ms, 34.8MB) |

    - 일반적인 상황에서는 내 코드가 조금 느리지만 큰단위의 처리에서는 빠른것 같음



- 내가 만든 코드의 `report_to_dict`함수에 `self.report`를 `set`하여 중복을 제거하면 풀이속도가 좀더 빨라지지 않을까?

  - ```python
    report_set = set(self.report)
    self.report = report_set
    ```

    - 위와 같이 추가

  - 속도

    - |              | 다른사람 풀이             | 내 풀이                  | set을 추가한 풀이       |
      | ------------ | ------------------------- | ------------------------ | ----------------------- |
      | 테스트 1 〉  | 통과  (0.01ms, 10.3MB)    | 통과  (0.03ms, 10.3MB)   | 통과 (0.02ms, 10.5MB)   |
      | 테스트 2 〉  | 통과  (0.03ms, 10.4MB)    | 통과  (0.04ms, 10.3MB)   | 통과 (0.04ms, 10.4MB)   |
      | 테스트 3 〉  | 통과  (1532.73ms, 39.5MB) | 통과  (456.71ms, 45.4MB) | 통과 (494.86ms, 53.1MB) |
      | 테스트 7 〉  | 통과  (3.51ms, 10.6MB)    | 통과  (4.15ms, 10.7MB)   | 통과 (1.78ms, 10.7MB)   |
      | 테스트 8 〉  | 통과  (3.54ms, 10.7MB)    | 통과  (4.22ms, 10.8MB)   | 통과 (2.57ms, 11MB)     |
      | 테스트 9 〉  | 통과  (411.90ms, 23.9MB)  | 통과  (140.57ms, 26.1MB) | 통과 (166.48ms, 30MB)   |
      | 테스트 11 〉 | 통과  (601.03ms, 39.6MB)  | 통과  (268.54ms, 44.9MB) | 통과 (321.99ms, 53.2MB) |
      | 테스트 18 〉 | 통과  (0.93ms, 10.3MB)    | 통과  (2.89ms, 10.1MB)   | 통과 (2.84ms, 10.3MB)   |
      | 테스트 19 〉 | 통과  (1.48ms, 10.3MB)    | 통과  (3.24ms, 10.4MB)   | 통과 (6.31ms, 10.4MB)   |
      | 테스트 20 〉 | 통과  (381.66ms, 20.3MB)  | 통과  (259.79ms, 23.6MB) | 통과 (293.20ms, 25.7MB) |
      | 테스트 21 〉 | 통과  (746.16ms, 31.6MB)  | 통과  (340.96ms, 34.8MB) | 통과 (314.51ms, 38.8MB) |

    - 다른 사람의 풀이보단 빨라졌지만 처음에 풀었던 풀이에서 시간이 오래걸린 테스트 들은 대부분 지연되었음

    - `set`함수를 실행하면서 시간이 더 지연된 것 같음

    - 테스트 케이스를 제공해 주지 않아서 정확히 알기 어렵다



- `set`과정을 거치면 `dict`로 중복된 신고를 없애는 과정이 필요 없어짐

  - 유저가 신고한 유저들을 `dict`에 저장하는 것이 아닌 신고당한 유저의 `dict`에 신고자 이름을 `list`형태로 넣으면?

    - A, B, C 유저가 있을 때 B유저를 A, C가 신고 했다면

    - ```json
      {
          'B':{
              '신고자': ['A', 'C']
          }
      }
      ```

    - 의 형태로 신고자가 2명이상일 때 메일을 발송한다면 `dict`에 B `key`의 신고자 `key`의 유저들에게만 메일을 보내면 된다.

    - |              | 다른사람 풀이             | 내 풀이                  | set을 추가하고 수정한 풀이 |
      | ------------ | ------------------------- | ------------------------ | -------------------------- |
      | 테스트 1 〉  | 통과  (0.01ms, 10.3MB)    | 통과  (0.03ms, 10.3MB)   | 통과 (0.03ms, 10.3MB)      |
      | 테스트 2 〉  | 통과  (0.03ms, 10.4MB)    | 통과  (0.04ms, 10.3MB)   | 통과 (0.03ms, 10.3MB)      |
      | 테스트 3 〉  | 통과  (1532.73ms, 39.5MB) | 통과  (456.71ms, 45.4MB) | 통과 (183.31ms, 46.6MB)    |
      | 테스트 7 〉  | 통과  (3.51ms, 10.6MB)    | 통과  (4.15ms, 10.7MB)   | 통과 (1.90ms, 10.8MB)      |
      | 테스트 8 〉  | 통과  (3.54ms, 10.7MB)    | 통과  (4.22ms, 10.8MB)   | 통과 (2.93ms, 11.1MB)      |
      | 테스트 9 〉  | 통과  (411.90ms, 23.9MB)  | 통과  (140.57ms, 26.1MB) | 통과 (100.76ms, 27.1MB)    |
      | 테스트 11 〉 | 통과  (601.03ms, 39.6MB)  | 통과  (268.54ms, 44.9MB) | 통과 (178.71ms, 46.7MB)    |
      | 테스트 18 〉 | 통과  (0.93ms, 10.3MB)    | 통과  (2.89ms, 10.1MB)   | 통과 (0.50ms, 10.2MB)      |
      | 테스트 19 〉 | 통과  (1.48ms, 10.3MB)    | 통과  (3.24ms, 10.4MB)   | 통과 (0.59ms, 10.4MB)      |
      | 테스트 20 〉 | 통과  (381.66ms, 20.3MB)  | 통과  (259.79ms, 23.6MB) | 통과 (59.27ms, 24.5MB)     |
      | 테스트 21 〉 | 통과  (746.16ms, 31.6MB)  | 통과  (340.96ms, 34.8MB) | 통과 (89.16ms, 36.9MB)     |

    - 메일 보낼 사람을 확인하는`check_mail()` 함수 과정을 거치지 않아도 되어 속도가 매우 빨라진것을 볼 수 있음

      - 신고당한 횟수를 따로 카운팅 하지 않아도 됨
      - 신고자를 찾는 과정이 없어짐

  - [02_report_result_2.py]()
