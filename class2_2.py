# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 12:13:06 2022

@author: 이세인
"""

# 리스트의 복사
nums = list(range(10)) #range 함수를  사용해서 0부터 9까지의 정수를 요소로 갖는 리스트 생성
nums1 = nums # nums1에 nums를 복사하는것 같지만 사실 같은 객체를 가리키는 것
nums2 = nums[:] # 복사

nums[0] = "a"

print(nums)

print(nums1)
print(nums2)

# 리스트에서뿐 아니라 이와 같은 상황에서 쓸수 있는것은 copy 라이브러리의 deepcopy 함수 이다.
import copy
nums = list(range(10))
nums3 = copy.deepcopy(nums)
nums[0] = "a"
print(nums3)



id(nums)
id(nums1) #메모리 주소가 같음을 알 수 있다. 같은 녀석을 가리키고 있음을 알 수 있다.
id(nums2)
id(nums3)


# =============================================================================
# 튜플, 집합, 딕셔너리
# =============================================================================
# 튜플은 리스트와 비슷하게 데이터 저장을 담당하지만 요소들을 변경할 수 없다.
tpl = (0, 1, 2, 3, 4, 5, 6 ,7,8,9)

tpl[1]
tpl[3:5]

tpl[1] = 0 # 변경 불가능 하다.


# 튜플의 용도는 변경이 안되어야 하는 데이터 저장


tpl.count(2) # 튜플 안에 2가 몇개가 있는가
tpl.index(3) # 튜플 안에 3의 위치는 ?

# =============================================================================
# 
# 집합
# 집합은 {} 를 사용해서 선언하는 자료형으로 중복을 허용하지 않음
# 집합 연산 (교집합, 합집합, 차집합, 대칭 차집합) 을 위한 자료형
# 중복된 원소는 하나만 제외하고 모두 무시됨
# 원소의 순서가 의미가 없으므로 인덱싱/슬라이싱 불가
# 순서가 의미 없기 때문에 []로 만들고 순서가 붙는(인덱싱) 리스트는 원소로 못넣는다
# =============================================================================

#집합은 {}를 사용해서 만들 수 있다.
name = {'이정재', '박해수', '오영수', '위하준', '정호연', '허성태', '미주령'}
type(name)
#공집합을 만들떄는 {} 로 하면 안되고 딕셔너리가 되므로 set을 이용한다
name1 = {} #이렇게 하면 공집합이 아닌, dict(딕셔너리)가 된다.
type(name1)
#공집합
name2 = set()
type(name2)

#집합안에 원소로 포함되어 있는지 여부 검사
"오영수" in name
"이상훈" in name

names = {'이정재', '이정재', '박해수'}
len(names) #'이정재'가 중복이 되기에 하나만 들어가져서 len은 2가 나온다.
print(names)
#중복되는 원소는 하나만 남는다.

names = {'이정재', [1,2]}
#[1,2] 라는 리스트는 순서 0번째, 1번째 가 있기 때문에 set 이 될 수 없다.

# =============================================================================
# 원소의 추가
# =============================================================================
#하나의 원소 추가 .add()
name = {'이정재', '박해수', '오영수', '위하준', '정호연', '허성태', '미주령'}
name.add('압둘 알리')
print(name)
 
#여러개의 원소 추가, 리스트, 튜플, 틱셔너리를 넣을 수 있는데 다 원소로 분해되서 들어감

name.update([1,2,3,4,5])
print(name)


# =============================================================================
# 원소의 제거 
# =============================================================================
#1. remove() 함수, 집합에 없는 원소를 지우려 시도하면 에러 발생
name = {'이정재', '박해수', '오영수', '위하준', '정호연', '허성태', '미주령'}
name.remove('이상훈')

#2. discard() 함수, 집합에 없는 원소를 제거하려 시도해도 에러 발생하지 않음
name.discard('이상훈')

#그렇다면 무조건 remove가 아닌 discard가 좋은 것일까 ?? #무엇이 더 좋다고는 할 수 없다.

#3. pop()함수는 랜덤하게 요소 제거 후 반환
name.pop()
print(name)


#4. clear() 공집합으로 만듬
name.clear()
print(name)


# =============================================================================
# 집합의 연산
# 합집합: |(or) 또는 union 메소드
# 교집합: &(and) 또는 intersection 메소드
# 차집합: - 또는 difference 메소드 사용
# 대칭 차집합: ^ 또는 symmetric_difference 메소드 사용
# =============================================================================
a = {1,2,3,4}
type(a)
b = set([3,4,5,6])
type(b)

#합집합
a|b
a.union(b)

#교집합
a&b
a.intersection(b)

#차칩합
a-b
b-a
a.difference(b)

#대칭차집합
a^b
a.symmetric_difference(b)






# =============================================================================
# 딕셔너리는 key와 value의 매칭으로 구성된다.
# 뒤에서 배울 pandas의 dataframe과 비슷한 구조이다.
# value에는 하나의 원소가 들어갈수도 있으며 리스트 등 다양하게 들어갈 수 있다.
# =============================================================================

information = {"이름" : "이상훈", "나이":"32", "키":"170"}
type(information)


information.items()
information.keys()
information.values()

#KEY가 중복되면 안된다.
information = {"이름" : "이상훈", "나이":"32", "키":"170", "이름":"비밀"}
information.keys()
information['이름']

#기존에 있는 KEY에 해당하는 값 변경
information = {"이름" : "이상훈", "나이":"32", "키":"170"}
information["나이"] = "30"
information

#기존에 KEY가 없다면 새로운 쌍 추가
information['지역'] = "서울"
information


# GET 함수의 사용. 찾는 KEY에 해당하는 값을 출력. KEY가 없다면 미리 정해둔 값 출력 가능
information['성별'] # 성별이라는 key가 없다
information.get('성별') # 에러는 발생하지 않음
information.get('성별',"key error") # key가 없으니 원하는 출력 문자 설정


#KEY가 있는지 확인하는 방법
type(information.keys())
lst = list(information.keys())
"나이" in lst

"나이" in information # 딕셔너리에서 바로 in을 사용하면 key 의 존재 확인 가능






# 과제
# 튜플은 값을 변경할 수 없는것이 가장 큰 특징이다.
# 하지만 만약 튜플의 값을 변경해야 한다면 ??
# tpl = (0,1,2,3) 을 선언 한 다음, tpl = (0,1,2,3,4)로 수정해본다.
# 힌트는 list를 이용하는 것
tpl = (0,1,2,3)


tpl = list(tpl)
tpl = [0,1,2,3,4]
tpl =tuple(tpl)





# 답안지
temp = list(tpl)
temp.append(4)
tpl1 = tuple(temp)