class Person:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # member function, method
    def introduce(self):
        print(f'My name is {self.name}, and I\'m {self.age} years old.')


a_person = Person("SooYoung", 20)
a_person.introduce()


class FamilyMember:
    last_name = 'Lee'

    def __init__(self, name, age):
        self.name, self.age = name, age

    # 파이썬의 생성자 오버로딩.
    @classmethod
    def from_age(cls, age = 0):
        return cls('NoName', age)

    @classmethod
    def from_name(cls, name = 'NoName'):
        return cls(name, 0)

    def introduce(self):
        print(f'My name is {self.name} {FamilyMember.last_name}, and I\'m {self.age} years old.')

    @classmethod
    def change_last_name(cls, new_last_name):
        cls.last_name = new_last_name


# 멤버 변수를 실시간으로 추가하거나 지울 수 있음.
# 따라서, 객체 별로 멤버 변수를 다르게 할 수 있음.
father = FamilyMember()
father.name = 'Tom'
father.age = 60
father.address = 'Seoul'

son = FamilyMember()
son.name = 'John'
son.age = 10
son.school = 'TU Korea'
del son.school

# 클래스 자체에 멤버 변수를 추가하면, 생성되어 있는 모든 객체에 그 멤버를 추가함.
FamilyMember.last_name = 'Lee'

# father.introduce() ===> type(father).introduce(father)
father.introduce()
FamilyMember.introduce(father)
type(father).introduce(father)


# 멤버 함수도 실시간으로 추가, 삭제 가능.
def identify(self):
    if self.age >= 10:
        print("I'm adult.")
    else:
        print("I'm child.")


def introduce_in_korean(self):
    print(f'저는 {self.name}입니다.')