# 자동차 평균 대여 기간

> https://school.programmers.co.kr/learn/courses/30/lessons/157342



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

`CAR_RENTAL_COMPANY_RENTAL_HISTORY` 테이블에서 평균 대여 기간이 7일 이상인 자동차들의 자동차 ID와 평균 대여 기간(컬럼명: `AVERAGE_DURATION`) 리스트를 출력하는 SQL문을 작성해주세요. 평균 대여 기간은 소수점 두번째 자리에서 반올림하고, 결과는 평균 대여 기간을 기준으로 내림차순 정렬해주시고, 평균 대여 기간이 같으면 자동차 ID를 기준으로 내림차순 정렬해주세요.

------



## 예시

예를 들어 `CAR_RENTAL_COMPANY_RENTAL_HISTORY` 테이블이 다음과 같다면

| HISTORY_ID | CAR_ID | START_DATE | END_DATE   |
| ---------- | ------ | ---------- | ---------- |
| 1          | 1      | 2022-09-27 | 2022-10-01 |
| 2          | 1      | 2022-10-03 | 2022-11-04 |
| 3          | 2      | 2022-09-05 | 2022-09-05 |
| 4          | 2      | 2022-09-08 | 2022-09-10 |
| 5          | 3      | 2022-09-16 | 2022-10-15 |
| 6          | 1      | 2022-11-07 | 2022-12-06 |

자동차 별 평균 대여 기간은

- 자동차 ID가 1인 자동차의 경우, 대여 기간이 각각 5일, 33일, 30일인 기록이 존재하므로 평균 22.7일
- 자동차 ID가 2인 자동차의 경우, 대여 기간이 각각 1일, 3일인 기록이 존재하므로 평균 2일
- 자동차 ID가 3인 자동차의 경우, 대여 기간이 30일인 기록만 존재하므로 평균 30일 입니다. 평균 대여 기간이 7일 이상인 자동차는 자동차 ID가 1, 3인 자동차이고, 평균 대여 기간 내림차순 및 자동차 ID를 기준으로 내림차순 정렬하면 다음과 같이 나와야 합니다.

| CAR_ID | AVERAGE_DURATION |
| ------ | ---------------- |
| 3      | 30.0             |
| 1      | 22.7             |

---



## 풀이

- `CAR_RENTAL_COMPANY_RENTAL_HISTORY` 테이블에서 평균 대여 기간이 7일 이상인 자동차들의 자동차 ID
  - `CAR_ID`에 중복된 번호가 있음으로 그룹화 해야함
    - `GROUP BY` 사용
  - `START_DATE`와 `END_DATE`의 차를 구해야 함
    - `TIMESTAMPDIFF(DAY, START_DATE, END_DATE)` 사용
  - 대여 기간이 7일 이상
    - 그룹에 조건을 걸때는 `HAVING`사용
    - `HAVING ~ >= 7`
- 평균 대여 기간(컬럼명: `AVERAGE_DURATION`)
  - 평균을 구하라고 하였으니 `AVG` 사용
- 평균 대여 기간은 소수점 두번째 자리에서 반올림
  - `ROUND(COLUMN_NAME, 1)` 사용
    - 컬럼명 다음의 숫자는 출력할 소수점 자리
    - 위에 쿼리는 첫번째 자리까지 표기한다는 뜻
      - => 두번째에서 반올림 한다
- 평균 대여 기간을 기준으로 내림차순 정렬해주시고, 평균 대여 기간이 같으면 자동차 ID를 기준으로 내림차순 정렬
  - `ORDER BY`사용
  - 평균 대여기간으로 먼저 내림차순 정렬
  - 편균 대여기간이 같다면  `CAR_ID`로 정렬

```mysql
SELECT CAR_ID, 
    ROUND(AVG(TIMESTAMPDIFF(DAY, START_DATE, END_DATE) + 1), 1) AS AVERAGE_DURATION
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
HAVING AVERAGE_DURATION >= 7
ORDER BY AVERAGE_DURATION DESC, CAR_ID DESC;
```

