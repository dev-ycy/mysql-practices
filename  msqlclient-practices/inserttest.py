from MySQLdb import connect, OperationalError

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
    cursor = db.cursor()


    # SQL 실행  (쿼리를 날리겠다)
    sql = 'insert into emaillist values(null, "마", "이콜", "michol@gmail.com")'
    count = cursor.execute(sql)

    # commit
    # insert / update / delete 후에 꼭 commit 해줘야함!
    db.commit()

    # 자원 정리
    cursor.close()
    db.close()

    # 결과 보기
    print(f'실행결과: {count==1}')

except OperationalError as e:
    print(f'error: {e}')