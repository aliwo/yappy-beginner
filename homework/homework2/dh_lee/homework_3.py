# 20190210
# TODO 1: 입력받은 수가 짝수인지 홀수인지 알려주는 프로그램 만들기

def evenorodd(x):
   x = int(input())
      if x / 2 = 0:
        print("짝수")
      else:
        print("홀수")
return x


# TODO 2: Iterable 의 의미
# iteration : 반복문을 활용해 객체의 여러 원소에 하나씩 차례데로 접근하는 것. 즉, 어떤 조건이 만족될 때까지 명령을 반복.
# iterable : iteration을 가능하게 하는 객체
# : 내부 원소에 하나씩 차례로 접근할 수 있다.
# : 예시) 시퀀스(list, str, tuple), 비시퀀스(dict), 파일 객체, getitem, iter 메서드
# : iter 메소드를 이용하면 iterator 객체를 반환할 수 있다.
# iterator : 직접 iteration을 수행한다.


# TODO 3: 인코딩이란?(UTF-8, 인코딩, 디코딩)
# 정의) 0과 1만으로 작업을 처리하는 컴퓨터가 언어들을 구현하기 위해 언어들을 일련의 문자 코드로 만들고 표준화하는 작업.
# 주요 문자 코드) ASCII코드: 기존 표준. 1바이트 크기라 다른 나라의 언어를 담기 어려웠음)
#  -> 유니코드: 2바이트의 넉넉한 크기와 65,536 개의 문자 표현 가능. BUT ASCII코드에게는 비효율적인 구조.
#  -> UTF-8: 유니코드 기반의 가변 길이 문자 인코딩 방식. 바이트를 가변적으로 조절해가면서 ASCII코드와 호환 가능.
#            ASCII 코드로 표현하지 못했던 세계 모든 문자들을 표현 가능. 가장 많이 이용됨
# 디코딩 : 인코딩과는 반대로, 기계어에서 글자로 변환하는 것.
# 예시) 인코딩 ord('꾹') => 44985
#      디코딩 chr(44985) => '꾹'