## 조건에 부합하는 중고거래 댓글 조회하기

> https://school.programmers.co.kr/learn/courses/30/lessons/164673



### 문제 설명

- 다음은 어느 자동차 대여 회사의 자동차 대여 기록 정보를 담은 `CAR_RENTAL_COMPANY_RENTAL_HISTORY` 테이블입니다. `CAR_RENTAL_COMPANY_RENTAL_HISTORY` 테이블은 아래와 같은 구조로 되어있으며, `HISTORY_ID`, `CAR_ID`, `START_DATE`, `END_DATE` 는 각각 자동차 대여 기록 ID, 자동차 ID, 대여 시작일, 대여 종료일을 나타냅니다.

  | Column name | Type    | Nullable |
  | ----------- | ------- | -------- |
  | HISTORY_ID  | INTEGER | FALSE    |
  | CAR_ID      | INTEGER | FALSE    |
  | START_DATE  | DATE    | FALSE    |
  | END_DATE    | DATE    | FALSE    |

---



### 문제

- `CAR_RENTAL_COMPANY_RENTAL_HISTORY` 테이블에서 대여 시작일이 2022년 9월에 속하는 대여 기록에 대해서 대여 기간이 30일 이상이면 '장기 대여' 그렇지 않으면 '단기 대여' 로 표시하는 컬럼(컬럼명: `RENT_TYPE`)을 추가하여 대여기록을 출력하는 SQL문을 작성해주세요. 결과는 대여 기록 ID를 기준으로 내림차순 정렬해주세요.

------



### 예시

- 예를 들어 `CAR_RENTAL_COMPANY_RENTAL_HISTORY` 테이블이 다음과 같다면

  | HISTORY_ID | CAR_ID | START_DATE | END_DATE   |
  | ---------- | ------ | ---------- | ---------- |
  | 1          | 4      | 2022-09-27 | 2022-11-27 |
  | 2          | 3      | 2022-10-03 | 2022-11-04 |
  | 3          | 2      | 2022-09-05 | 2022-09-05 |
  | 4          | 1      | 2022-09-01 | 2022-09-30 |
  | 5          | 3      | 2022-09-16 | 2022-10-15 |

  2022년 9월의 대여 기록 중 '장기 대여' 에 해당하는 기록은 대여 기록 ID가 1, 4인 기록이고, '단기 대여' 에 해당하는 기록은 대여 기록 ID가 3, 5 인 기록이므로 대여 기록 ID를 기준으로 내림차순 정렬하면 다음과 같이 나와야 합니다.

  | HISTORY_ID | CAR_ID | START_DATE | END_DATE   | RENT_TYPE |
  | ---------- | ------ | ---------- | ---------- | --------- |
  | 5          | 3      | 2022-09-16 | 2022-10-13 | 단기 대여 |
  | 4          | 1      | 2022-09-01 | 2022-09-30 | 장기 대여 |
  | 3          | 2      | 2022-09-05 | 2022-09-05 | 단기 대여 |
  | 1          | 4      | 2022-09-27 | 2022-10-26 | 장기 대여 |

------



### 주의사항

- `START_DATE`와 `END_DATE`의 경우 예시의 데이트 포맷과 동일해야 정답처리 됩니다.

---



### 풀이

- 기존 `column`에 없는 `RENT_TYPE`이 추가되어야 함
  - `START_DATE`가 2022-09인 대여기록들 중
    - `WHERE` 사용
    - `2022-09`를 확인하는데는 `DATE_FORMAT(START_DATE, '%Y-%m')` 사용
  - `START_DATE`로부터 `END_DATE`가 30일 이상이면 `장기 대여`, 아니면 `단기 대여`로 표시
    - `CASE WHEN ~ THEN ~ ELSE ~ END AS ~` 사용
    - 새 컬럼의 값으로 장기대여 / 단기대여 2가지가 있음
    - 조건으로는 대여시작일이 `2022-09`중, 대여기간이` 30일 이상 / 30일 미만` 인 경우
    - 날짜 차이를 확인하는데는 `TIMESTAMPDIFF(DAY, START_DATE, END_DATE)` 사용
- 이는 `HISTORY_ID`기준으로 `내림차순`으로 정렬
  - `ORDER BY HISTORY_ID DESC`

```mysql
SELECT HISTORY_ID, CAR_ID, 
    DATE_FORMAT(START_DATE, '%Y-%m-%d') AS START_DATE, 
    DATE_FORMAT(END_DATE, '%Y-%m-%d') AS END_DATE,
    CASE
        WHEN TIMESTAMPDIFF(DAY, START_DATE, END_DATE) + 1 >= 30 THEN '장기 대여'
        ELSE '단기 대여'
    END AS RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE DATE_FORMAT(START_DATE, '%Y-%m') = '2022-09'
ORDER BY HISTORY_ID DESC;
```

