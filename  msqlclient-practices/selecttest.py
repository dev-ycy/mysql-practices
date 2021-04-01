from MySQLdb import connect, OperationalError
from MySQLdb.cursors import DictCursor

try:
    # 연결
    db = connect(
        user='webdb',
        password='webdb',
        host='localhost',
        port=3306,
        db='webdb',
        charset='utf8')

    # cursor 생성
    # DictCursor: row 별로 dict 형태로 리스트로 담음 [{}, ..., {}]
    cursor = db.cursor(DictCursor)


    # SQL 실행  (쿼리를 날리겠다)
    sql = 'select no, first_name, last_name, email from emaillist order by no desc'
    cursor.execute(sql)

    # 결과 받아오기
    results = cursor.fetchall()

    # 자원 정리
    cursor.close()
    db.close()

    # 결과 보기
    for result in results:
        print(result)

except OperationalError as e:
    print(f'error: {e}')