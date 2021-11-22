ans=['5', '3', '2']
print(int(''.join(ans)))  # 이거를 가지고 배열 안에 있는 string 혹은 char 값을 더해서 출력할 수 있다.
i=[1,2]
tmp=(lambda x: x*2)(i)  # 앞에서 바로 식을 만들고, 뒤에서 바로 실행한다. 이렇게 하면, [1,2,1,2] 가 생성된다.

#정규식
n='5.2n'
re.match(r'^[0-9\.]+$', n)  # r 은 \n 같은 것을 무시하겠다는 것이고, ^은 무조건 시작이 저거여야한다는 것, $는 끝도 저거여야 한다는 것
# 기본적으로 .은 모든 문자를 뜻하는데, . 자체를 인식하기 위에 \사용. \는 뒤에 있는 특수 문자를 그대로 인식한다는 뜻
# 참고 링크: https://sysops.tistory.com/174

# 이런식으로 lambda와 map을 사용해 배열 전체를 해준다.
fn = lambda n : float(n) if re.match(r'^[0-9]+$', n) else n
cols = list(map(fn, cols))
