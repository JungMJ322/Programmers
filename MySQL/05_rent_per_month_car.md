# 대여 횟수가 많은 자동차들의 월별 대여 횟수 구하기

> https://school.programmers.co.kr/learn/courses/30/lessons/151139



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

`CAR_RENTAL_COMPANY_RENTAL_HISTORY` 테이블에서 대여 시작일을 기준으로 2022년 8월부터 2022년 10월까지 총 대여 횟수가 5회 이상인 자동차들에 대해서 해당 기간 동안의 월별 자동차 ID 별 총 대여 횟수(컬럼명: `RECORDS`) 리스트를 출력하는 SQL문을 작성해주세요. 결과는 월을 기준으로 오름차순 정렬하고, 월이 같다면 자동차 ID를 기준으로 내림차순 정렬해주세요. 특정 월의 총 대여 횟수가 0인 경우에는 결과에서 제외해주세요.

------



## 예시

예를 들어 `CAR_RENTAL_COMPANY_RENTAL_HISTORY` 테이블이 다음과 같다면

| HISTORY_ID | CAR_ID | START_DATE | END_DATE   |
| ---------- | ------ | ---------- | ---------- |
| 1          | 1      | 2022-07-27 | 2022-08-02 |
| 2          | 1      | 2022-08-03 | 2022-08-04 |
| 3          | 2      | 2022-08-05 | 2022-08-05 |
| 4          | 2      | 2022-08-09 | 2022-08-12 |
| 5          | 3      | 2022-09-16 | 2022-10-15 |
| 6          | 1      | 2022-08-24 | 2022-08-30 |
| 7          | 3      | 2022-10-16 | 2022-10-19 |
| 8          | 1      | 2022-09-03 | 2022-09-07 |
| 9          | 1      | 2022-09-18 | 2022-09-19 |
| 10         | 2      | 2022-09-08 | 2022-09-10 |
| 11         | 2      | 2022-10-16 | 2022-10-19 |
| 12         | 1      | 2022-09-29 | 2022-10-06 |
| 13         | 2      | 2022-10-30 | 2022-11-01 |
| 14         | 2      | 2022-11-05 | 2022-11-05 |
| 15         | 3      | 2022-11-11 | 2022-11-11 |

대여 시작일을 기준으로 총 대여 횟수가 5회 이상인 자동차는 자동차 ID가 1, 2인 자동차입니다. 월 별 자동차 ID별 총 대여 횟수를 구하고 월 오름차순, 자동차 ID 내림차순으로 정렬하면 다음과 같이 나와야 합니다.

| MONTH | CAR_ID | RECORDS |
| ----- | ------ | ------- |
| 8     | 2      | 2       |
| 8     | 1      | 2       |
| 9     | 2      | 1       |
| 9     | 1      | 3       |
| 10    | 2      | 2       |

---



## 풀이

- **대여 시작일**을 기준으로 **2022년 8월부터 2022년 10월**까지

  - `START_DATE`를 기준으로 2022-08 ~ 2022-10까지의 조건
  - 조건을 생성하는 `WHERE` 사용
  - 날짜 형식을 정하는 `DATE_FORMAT(START_DATE, '%Y-%m')` 사용

- 총 대여 횟수가 **5회 이상**인 자동차들

  - 개수를 세는 집계 함수인 `COUNT()`를 사용

  - `CAR_ID`별로 집계해야 함으로 `GROUP BY CAR_ID` 해야 함

  - 집계된 `COUNT(HISTORY_ID)`가 5보다 큰 경우 임으로 `HAVING`으로 조건을 생성함

    - ```mysql
      -- 2022-08 ~ 2022-10이 대여시작일 인 것들을 CAR_ID로 집계해 
      -- HISTORY_ID의 개수를 집계한 것중 5보다 큰것
      SELECT CAR_ID 
      FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
      WHERE DATE_FORMAT(START_DATE, '%Y-%m') BETWEEN '2022-08' AND '2022-10'
      GROUP BY CAR_ID
      HAVING COUNT(HISTORY_ID) >= 5
      ```

  - 위를 Sub Query로 사용하여 `CAR_RENTAL_COMPANY_RENTAL_HISTORY`와 `CAR_ID`가 일치하는 것들을 찾음

- **해당 기간 동안**의 **월별** **자동차 ID 별** 총 대여 횟수

  - 날짜에서 월의 값만 표기하는 `MONTY(START_DATE)`을 이용
  -  `COUNT()`를 사용하여 월 별로 `CAR_ID` 대여 횟수를 구함
    - `월`별로 `CAR_ID` 대여 횟수를 구해야 함
    - `GROUP BY MONTH, CAR_ID`

- 결과는 월을 기준으로 오름차순 정렬하고, 월이 같다면 자동차 ID를 기준으로 내림차순 정렬

  - `ORDER BY MONTH ASC, CAR_ID DESC`



```mysql
SELECT MONTH(START_DATE) AS MONTH, CAR_ID, COUNT(*) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE CAR_ID IN (
    SELECT CAR_ID 
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE DATE_FORMAT(START_DATE, '%Y-%m') BETWEEN '2022-08' AND '2022-10'
    GROUP BY CAR_ID
    HAVING COUNT(HISTORY_ID) >= 5)
    AND DATE_FORMAT(START_DATE, '%Y-%m') BETWEEN '2022-08' AND '2022-10'
GROUP BY MONTH, CAR_ID
ORDER BY MONTH ASC, CAR_ID DESC;
```



```mysql
SELECT MONTH(START_DATE) AS MONTH, CAR_ID, COUNT(*) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY A JOIN (
	SELECT CAR_ID 
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
    GROUP BY CAR_ID
    HAVING COUNT(HISTORY_ID) >= 5) B
    ON A.CAR_ID = B.CAR_ID
WHERE START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
GROUP BY MONTH, CAR_ID
ORDER BY MONTH ASC, CAR_ID DESC;
```

- 함수 사용 줄이고 `JOIN`해서 사용하는 것이 더 효율적이라고 하여 변경



```mysql
SELECT MONTH, CAR_ID, RECORDS
FROM (
    SELECT DISTINCT MONTH(START_DATE) AS MONTH
        , CAR_ID
        , COUNT(*) OVER(PARTITION BY MONTH(START_DATE), CAR_ID) AS RECORDS
        , COUNT(*) OVER(PARTITION BY CAR_ID) AS FILTER
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
    )A
WHERE FILTER >= 5 
ORDER BY MONTH ASC, CAR_ID DESC
```

- `JOIN`도 사용하지 않음 <참고>