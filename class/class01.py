# 객체 지향 프로그래밍 Object-Oriented Programing

# 프로그램을 단순히 데이터와 처리 방법으로 나누지 않과, 프로그램을 객체 단위로 생각하고 객체끼리 상호 작용을 표현하는 방식 
## 코드의 재사용, 코드 중복 방지, 유지보수 등을 위해 사용함 

# 처음엔 함수 중심으로 개발할 수 있지만, 점점 구조가 복잡해지면 개선이 어려움 
#  항상 객체 지향이 최선은 아니며 프로젝트의 규모 등에 따라 다름
# 객체 지향 프롲그래밍 외에 절파 지향 프로그래밍도 존재 

# 절차 지향 프로그래밍 예시

# 순차적으로 진행되는 프로그래밍 
# Jupyter Notebook,Google Colabe등 에서 라인 바이 라인으로 실해하는 경우 절차 지향으로 볼수 있음

# 절차 지향 방식으로 구현하고, 점점 객체 지향으로 구현해보기 
# 일반적인 코딩 

# 객체 업이 그냥 변수를 생성
# 추가 요소를 만들 떄는 숫자와 값만 변경하고 계속 증가시킴
# 스마트폰과 스마트본 정보를 출력하려면 두 변수를 같이 프린트 해야함 

smaartphone_1 = 'Iphone'

smaartphone_information = [
    {'color':'white'},
    {'price':100000}
]

print(smaartphone_1)
print(smaartphone_information)

# Dictionary를 사용해 스마트폰과 스마토폰 정보를 저장하는 방법 
# 딕셔너리의 ket는 중복 불가능한 문제가 존재 
# 정렬 문제 = > OreeredDict을 사용하면 해경
# Key가 만약 없을 경우 예외 처리를 해야함 => DeafaultDict을 사용하면 해결 
# 스마트폰, 스마트폰 정보를 출력할 경우엔 딕셔너리만 출력하면 됨 

smaartphone_dicts = [
    {'brand':'Iphone','smartphone_information':{'color':'white','price':10000}},
    {'brand':'Galaxy','smartphone_information':{'color':'Blue','price':8000}}
]

print(smaartphone_dicts[0].get('smartphone_information'))

# 객체 지향 프로그래밍 살펴보기 

# 코드의 중복 사용이 최소하되서 재사용성이 증가 
# 클래스의 매직 메소드를 사용할 수 있음 
# # 네암스페이스
# 프로그래밍 언어에서 객체를 구분할수 있는 공간
# 변수를 샛체에 할당하면 해당 객체는 딕셔너리 형태로 연결되서 네임스페이스에 저장됨 
# 파이썬의 클래스는 새로운 타입(객체)을 정의하기 위해사용되고, 모듈과 마찬가지로 하나의 네임스페이스를 가짐
# globals()를 사용하면 전역 네임스페이스를 확인할 수 있음 
# 함수는 전역과 별개의 네임스페이스를 가짐 
# temp_variable = a
print(globals()) 

# __init__: 클래스 인스턴스 생성시 초기화하며 실행되는 부분
# class의 값을 보고 싶으면 __dict__ 을 사용

# python class magic method - str 
# str 매직 메소드가 구현되어 있지 않은 상태에서 인스턴그를 print하면 object가 나옴
# print 또는 str 함수가 호출될 때 사용 - 기본적으로 str 메소드가 먼저 실행되며 , str 메소드가 없으면 repr 메소드를 실행함 

# # python class magic method - repr
# __repr__: str 과 비슷 
# 개발, 엔지니어 레벨에서 객체의 엄격한 타입을 표현시 사용 
# 객체 표현을 반환함 
# repr() 함수가 호출될 떄 사용 

## python class magiv method - doc
# # __doc__
# docstring을 출력

class Smartphone:
    """
    Smartphone class
    """
    def __init__(self,brand,informations):
        self._brand = brand
        self._informations = informations
    def __str__(self):
        return f'str: {self._brand}-{self._informations}'

    def __repr__(self):
        return f'repr : {self._brand} - {self._informations}'

Smartphone1 = Smartphone('Iphone',{'color':'white','price':10000});
Smartphone2 = Smartphone('Galaxy',{'color':'Black','price':8000})

print(Smartphone1)
print(Smartphone1.__dict__)

print(Smartphone1._brand == Smartphone2._brand)
print(Smartphone1 is Smartphone2)

print(Smartphone.__doc__)

# self 란 
# self는 인스턴스 자기 자신을 뜻함 
# 인스턴스 : 클래스에 의해 만들어진 객체 
# self가 있는 것이 인스턴스 변수 
# 인자에 self를 받는것은 인스턴스 메소드 : get_informaiton 함수 
# 인스턴스의 __class__는 사용된 클래스를 출력함 

class Smartphone:
    """
    Smartphone Class
    """

    def __init__(self,brand,details):
        self._brand = brand
        self._infomations = infomations
    def __str__(self):
        return f'str : {self._brand} - {self._infomations}'
    def __repr__ (self):
        return f'repr : {self._brand} - {self._infomations}'
    def get_infomation(self):
        print(f'Current ID: {id(self)}')
        print(f'Smartphone Detail Info : {self._brand} {self._infomations.get("price")}')

        Smartphone1 = Smartphone('Iphone',{'color':'White','price':10000})
        Smartphone2 = Smartphone('Galaxy',{'color':'Black','price':8000})

        Smartphone1.detail_info()

        print(Smartphone1.__class__,Smartphone2.__class__)
        # 부모는 같음 
        print(id(Smartphone1.__class__)== id(Smartphone2.__class__))

# 클래스 변수ㅡ 
# 클래스 내부에 선언된 변수 
# 클래스 변수는 클래스의 네임스페이스에 위치함 
# 모든 인스턴스거 공유하는 변수
# Smartphone1.__dict__ 를 출력하면 클래스 변수는 보이지 않음 
# dir(Smartphone1)를 출력할 떄는 클래스 변수가 보임 

# 인스턴스 변수 
# self.name 같이 self가 붙은 변수 
# 인스턴스 변수는 인스턴스의 네임스페이스에 위치함 
# 인스턴스 네임스페이스에서 없으면 상위에서 검색 
# 즉 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 => 상위 클래스, 부모 클래스 변수)

class Smartphone:
    """
    Smartphone Class
    """
    # 클래스 변수ㅡ 
    smartphone_count = 0

    def __init__(self,brand,infomations):
        self._brand = brand
        self.infomations = infomations
        Smartphone.smartphone_count += 1

    def __str__(self):
        return f'str : {self._brand} - {self._infomations}'
    def __repr__(self):
        return f'repr: {self._brand} - {self.infomations}'
    def infomation(self):
        print(f'Current Id: {id(self)}')
        print(f'Smartphone Deatail Info : {self._brand} {self._infomations}')

    def __del__(self):
        Smartphone.smartphone_count -=1

    Smartphone1 = Smartphone('Iphone',{'color':'White','price':10000})
    Smartphone2 = Smartphone('Galaxy',{'color':'Black','price':8000})

print(Smartphone.__dict__)
print(Smartphone1.__dict__)
print(Smartphone2.__dict__)
print(dir(Smartphone1))

print(Smartphone1.smartphone_count)
print(Smartphone.smartphone_count)

# 메소드의 종류 

# 1) 클래스 메소드(Python Class Method)
# @classmethod 데코레이터를 사용
# cls 인자를 받음
# cls 는 Smartphone를 뜻함(인스턴스 말고 클래스)
# 클래스 변수 컨트롤할 떄 사용

# 2) 인스턴스 메소드(pythone Instance Method)
# Sekf가 들어간 경우 
# 객체의 고유한 속성 값을 사용 

# 스태틱 메소드(Python Static Method)
# 아무것도 인자를 받지 않음(self, cls등)

class Smartphone:
    """
    Smartphone Class
    """
    smartphone_count = 0 

    def __init__(self,brand,informations):
        self._brand = brand
        self._informations = informations
        Smartphone.smartphone_count += 1

    def __str__(self):
        return f'str :{self._brand} - {self._informations}'
    def __repr__ (self): 
        return f'repr : {self._brand} - {self._informations}'

    def detail_info(self):
        print(f'Current Id : {id(self)}')
        print(f'Smartphone Detail Info : {self._brand} {self._informations.get("price")}')

    def get_price(self):
        return f'Before Smartphone Price -> brand : {self._brand}, price : {self._informations.get("price")}'     
    
    def get_price_culc(self):
        return f'After Smartphone Price -> brand : {self._brand}, price : {self._informations.get("price") * Smartphone.price_per_raise}'
    
    @classmethod 
    def raise_price(cls,per):
        if per <= 1 :
            print('Please Enter 1 or More')
            return 
        cls.pricer_per_raise = per 
        return 'Succeed! price increased.'
    @staticmethod
    def is_phone(inst):
        if inst._brand == 'Iphone':
            return f'Ok! this Smartphone is an {inst._brand}.'
        return 'Sorry. This Smartphone isnt an Iphone'
    
Smartphone1 = Smartphone('Iphone',{'color':'White','price':10000})
Smartphone2 = Smartphone('Galaxy',{'color' : 'Black','price':8000})
# 기본정보 
print(Smartphone1)
print(Smartphone2)

Smartphone1.information()
Smartphone2.information()

print(Smartphone1.get_price())
print(Smartphone2.get_price())

# 가격 인상(클래스 메소드 미상용)
# 이렇게 직접 접근은 좋지 않아요 

Smartphone.pricer_per_raise = 1.2 

# 가격 정보 

print(Smartphone1.get_price_culc())
print(Smartphone2.get_price_culc())

# 가격인상 
Smartphone.raise_price(1.6)

# 가격 정보 
print(Smartphone1.get_price_culc())
print(Smartphone2.get_price_culc())

def is_iphone(inst):
    if inst._brand == 'Iphone':
        return f'OK! This Smartphon is an {inst._brand}.'
    return 'Sorry. thos smartphone isnt an Iphone.'

print(is_iphone(Smartphone2))

print('static : ',Smartphone.is_phone(Smartphone1))
print('static : ',Smartphone.is_phone(Smartphone2))

# 상속 

# class는 상속을 통해 자식 클래스에세 부모 클래스의 속성과 메소드를 물려줌 
# 예를 들어 Smartphone Class가 있고, Iphone Class, Galaxy Class등이 있는 상황 
# Iphone 과 Galaxy가 가치는 속성(attribute)는 다를 수 있음 
# 다중 상속도 가능함 

class Smartphone: 
    def __init__(self,brand,price):
        self._brand = brand
        self._price = price

    def __str__(self):
        return f'str :{self._brand} - {self._price}'
class Galaxy(Smartphone):
    def __init__(self,brand,price,country):
        self._brand = brand 
        self._price = price
        self._country = country 

    def __str__(self):
        return f'str : {self,__class__.__name__} 스마트폰은 {self._brand}에서 출시되었고, {self._country}에서 생산되었습니다. 가격은 {self._price}입니다'           

iphone = Smartphone('Iphone',7000)
print(iphone)
galaxy = Galaxy('Galaxy',5000,'South Korea')
print(galaxy)

# # Setter 와 GEtter, Property
# 객체의 속성(attribute)를 다룰 떄 사용 
# getter,setter는 객체의 속성을 읽고 변경할 떄 사용함 
# 참고로 객체 +(Object)는 속성(Attribute)와 Method로 구현 

# 자바 같은 객체 지향 언어에서 외부에서 바로 접근할 수 없는 Private 객체 속성을 지원함 
# 이런 언어에선 private 속성의 값을 읽고(get) 변경(set) 하기 위해 Getter dhk setter를 사용함 
# 파이썬은 모든 메소드가 public 이기 떄문에 getter 와 setter메소드가 없지만 사용할 수는 있음 

class SmartphoneL:
    def __init__(self,brand,price):
        self._brand = brand
        self._price = price

    def get_price(self):
        return self._price 

    def set_price(self,price):
        self._price = price

# property 
# #파이선은 속성에직접 접근을 막기 위해 property를 사용함 
# 데코레이ㅓㅌ로 깜싸서 사용함 

class Smartphone:
    def __init__(self,brand,price):
        self._brand = brand
        self._price = price

    @property
    def price(self):
        return self._price

    @property
    def price(self):
        return self._price


    @price.setter
    def price(self,price):
        print(f"뱐걍 전 가격 : {self._price}")
        self._price = price
        print(f"변경 후 가격 : {self._price}")
Smartphone1 = Smartphone("Iphone",1000)
Smartphone1.price = 10000
Smartphone1.price = -1000

# 추상 메소드 
# class를 만들었다면 class에서 정의된 메소드를 그대로 사용하지 않을 수 있음 
# 상속받고, 어떤 메소드는 추가하고 어떤 메소드는 오버라이드할 수있음 
# 통일된 Class 체계를 구축하며 확장 기능을 가능하게 만드는 것이 Class

# 이런 개념을 토대로, Class를 만들떄 반드시 구현해야 할 메소드를 명시할 수 있음 
# 아래 코드는 Smartphone 에서 func1 함수를 구현하지 않아 오류가 발생함

class Smartphone:
    def func1(cls):
        raise NotImplementedError()

class Iphone(Smartphone):

# iphone = Iphone()
# iphone.func1() # Error 발생   

# 조금 더 Strict하고 세련된 방법은 @abc.abstractmethod 를 사용하는 방법
# abc는 absstract base class 의 약자 
# Class의 인자로 metaclass=abc.ABCMeta를 지정하고,
# Class에 데코레이텉로 abc.abstractmethod 를 사용하면, class가 호출되는 순간구현해야 하는 메소드가 구현되있는지를 확인함 
# 참고 : metaclass는 단순히 클래스를 만들 떄 사용됨 클래스의 클래스 
# 바로 에러가 발생하기 떄문에 인슨턴스화시키지 않고, 푸상화에 이점이 존재 

# import abc

# class Smartphone(metaclass=abc.ABCMeta):
#     @abc.abstractclassmethod
#     def func1(cls):
#         raise NotImplementedError()
    
# class Iphone(Smartphone):
#     def func2(self):
#         pass
# iphone = iphone() # Error 발생 

# slots 

# 파이썬의 클래스들은 인스턴스 속성을 저장함 
# 파이썬에서 객체의 인스ㅓㄴ스 속성을 저장하기 위해 dictionary를 사용함 
# 이런 방식은 속성을추가하거나 삭제할 때 유용함 
# obj.__dict__으로 접근하는 경우 
# 그러나 dictionary 자료 구조는메모리를 많이 낭비함
# 파이썬 객체 생성시 모든 솟ㄱ성을 메모리에 할당하려고 함 
# 메모리 할당량이 많으면 많은 RAM을 낭비하게 됨 

# 이런 문제를 해결하기 위해 __slots__ 를 사용해 특정 속성에만 메모리를 할당하도록 함 
# ipython memory usage 를 사용하면 __slots__를 사용해서 메모리 사용량이 얼마나 개선되는지 확인할 수 있음 

# __slots__ 없이 짠 코드 

class smartphone:
    def __init__(self,brand,price):
        self._brand = brand
        self._price = price
        self.set_up()

    # 코드 생략 
    # set_up은 init시 실행하는 함수 

# __slots__를 사용해 짠 코드 

class Smartphone:
    __slots__ = ['_brand','_price']

    def __init__(self,brand,price) :
        self._brand = brand
        self._price = price
        self.set_up()

    # 코드 생략 
    # set_up은 init시 실행하는 함수 


# 결론 : CLass 란  객페를 만들어내기 위한 츨



