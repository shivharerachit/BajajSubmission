import requests

payload = {
    "name": "Rachit Shivhare",
    "regNo": "0827CS221213",
    "email": "rachitshivhare221089@acropolis.in"
}

gen_url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"
response = requests.post(gen_url, json=payload)
x = response.json()
webhookURL = x['webhook']
accessToken = x['accessToken']

print("Webhook URL:", webhookURL)
print("Access Token:", accessToken)

SQL_QUERY = """SELECT
    p.AMOUNT AS SALARY,
    CONCAT(e.FIRST_NAME, ' ', e.LAST_NAME) AS NAME,
    FLOOR(DATEDIFF(CURDATE(), e.DOB) / 365.25) AS AGE,
    d.DEPARTMENT_NAME
FROM
    PAYMENTS p
JOIN EMPLOYEE e ON p.EMP_ID = e.EMP_ID
JOIN DEPARTMENT d ON e.DEPARTMENT = d.DEPARTMENT_ID
WHERE
    DAY(p.PAYMENT_TIME) != 1
    AND p.AMOUNT = (
        SELECT MAX(AMOUNT)
        FROM PAYMENTS
        WHERE DAY(PAYMENT_TIME) != 1
    );"""

headers = {
    "Authorization": accessToken,
    "Content-Type": "application/json"
}

body = {
    "finalQuery": SQL_QUERY,
}

response = requests.post(webhookURL, headers=headers, json=body)
print("Status Code:", response.status_code)
print("Response:", response.json())