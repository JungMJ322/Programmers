# 자동차 대여 기록에서 대여중 / 대여 가능 여부 구분하기

> https://school.programmers.co.kr/learn/courses/30/lessons/157340



## 문제 설명

다음은 어느 자동차 대여 회사의 자동차 대여 기록 정보를 담은 `CAR_RENTAL_COMPANY_RENTAL_HISTORY` 테이블입니다. `CAR_RENTAL_COMPANY_RENTAL_HISTORY` 테이블은 아래와 같은 구조로 되어있으며, `HISTORY_ID`, `CAR_ID`, `START_DATE`, `END_DATE` 는 각각 자동차 대여 기록 ID, 자동차 ID, 대여 시작일, 대여 종료일을 나타냅니다.

| Column name | Type    | Nullable |
| ----------- | ------- | -------- |
| HISTORY_ID  | INTEGER | FALSE    |
| CAR_ID      | INTEGER | FALSE    |
| START_DATE  | DATE    | FALSE    |
| END_DATE    | DATE    | FALSE    |

------



## 문제

`CAR_RENTAL_COMPANY_RENTAL_HISTORY` 테이블에서 2022년 10월 16일에 대여 중인 자동차인 경우 '대여중' 이라고 표시하고, 대여 중이지 않은 자동차인 경우 '대여 가능'을 표시하는 컬럼(컬럼명: `AVAILABILITY`)을 추가하여 자동차 ID와 `AVAILABILITY` 리스트를 출력하는 SQL문을 작성해주세요. 이때 반납 날짜가 2022년 10월 16일인 경우에도 '대여중'으로 표시해주시고 결과는 자동차 ID를 기준으로 내림차순 정렬해주세요.

------



## 예시

예를 들어 `CAR_RENTAL_COMPANY_RENTAL_HISTORY` 테이블이 다음과 같다면

| HISTORY_ID | CAR_ID | START_DATE | END_DATE   |
| ---------- | ------ | ---------- | ---------- |
| 1          | 4      | 2022-09-27 | 2022-09-27 |
| 2          | 3      | 2022-10-03 | 2022-10-04 |
| 3          | 2      | 2022-10-05 | 2022-10-05 |
| 4          | 1      | 2022-10-11 | 2022-10-16 |
| 5          | 3      | 2022-10-13 | 2022-10-15 |
| 6          | 2      | 2022-10-15 | 2022-10-17 |

2022년 10월 16일에 대여 중인 자동차는 자동차 ID가 1, 2인 자동차이고, 대여 가능한 자동차는 자동차 ID가 3, 4이므로, '대여중' 또는 '대여 가능' 을 표시하는 컬럼을 추가하고, 자동차 ID를 기준으로 내림차순 정렬하면 다음과 같이 나와야 합니다.

| CAR_ID | AVAILABILITY |
| ------ | ------------ |
| 4      | 대여 가능    |
| 3      | 대여 가능    |
| 2      | 대여중       |
| 1      | 대여중       |

---



## 풀이

- 테이블에서 2022년 10월 16일에 대여 중인 자동차인 경우
  - 반납 날짜가 2022년 10월 16일인 경우에도 '대여중'으로 표시
  - `START_DATE`가 2022-10-16보다 전이거나 같을 경우와
  - `END_DATE`가  2022-10-16보다 후이거나 같을 경우
  - 위 조건에 만족하는 `CAR_ID`
  - 이를 Sub Query로 사용 OR `WITH`를 사용해 가상테이블 생성
- 대여 중인 자동차인 경우 '대여중' 이라고 표시하고, 대여 중이지 않은 자동차인 경우 '대여 가능'을 표시
  - 대여중인 `CAR_ID`를 구했으나 이를 그냥 `JOIN`하면 `INNER JOIN`이 되어 대여가능한 `CAR_ID`는 표기가 안된다
  - `OUTTER JOIN`을 통해 가상테이블의 `CAR_ID`내용은 알고 모든 `CAR_ID`를 표기하도록 함
  - `CAST ~ WHEN ~ THEN ~ END`를 사용해 대여중 / 대여 가능을 표기 
  - 같은 `CAR_ID`의 다른 기간의 값도 같이 표기되어 `CAR_ID`가 중복되어 표기됨
    - `GRUOP BY CAR_ID`

```mysql
WITH RANTAL_CAR AS (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE START_DATE <= '2022-10-16' AND END_DATE >= '2022-10-16'
)

SELECT HIS.CAR_ID,
    CASE
        WHEN HIS.CAR_ID = RAN.CAR_ID THEN '대여중'
        ELSE '대여 가능'
    END AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY HIS
    LEFT JOIN RANTAL_CAR RAN ON HIS.CAR_ID = RAN.CAR_ID
GROUP BY CAR_ID
ORDER BY CAR_ID DESC
```



- 다른 사람 풀이

  ```mysql
  SELECT CAR_ID,
      MAX(IF("2022-10-16" BETWEEN START_DATE AND END_DATE, "대여중", "대여 가능")) AS AVAILABILITY
  FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
  GROUP BY CAR_ID
  ORDER BY CAR_ID DESC
  ```

  - `IF`문을 사용해 `조건`이 맞음 "대여중"을, 아니면 "대여 가능"을 값으로 넣도록 함
  - `MAX`를 사용한 이유는 '대여중'이 '대여 가능'보다 더 **큰 값(내림차순 정렬할 때 더 먼저 있는 값)**이기 때문에
    - 대여중/대여 가능 두가지 값을 모두 가질 수 있다면 `MAX`함수로 '대여중'이 표기 될수 있도록