class Pet:
    def __init__(self, name='None', animal_type='None', age=0):

        assert age >= 0, f"Age {age} is greater than or equal to zero"

        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def animal_type(self):
        return self.__animal_type

    @property
    def age(self):
        return self.__age

    @name.setter
    def name(self, value):
        self.__name = value

    @animal_type.setter
    def animal_type(self, value):
        self.__animal_type = value

    @age.setter
    def age(self, value):
        self.__age = value

    def __str__(self):
        return f"{self.__name} is a {self.__age} year-old {self.animal_type}"


def main():
    print('This programs tests the Pet class.\n')

    myPet = Pet()

    myPet.name = input('Animal name: ')
    myPet.animal_type = input('Animal type: ')
    myPet.age = input('Animal age: ')

    print('\nAnimal name: ', myPet.name)
    print('Animal type: ', myPet.animal_type)
    print('Animal age: ', myPet.age)

    print(myPet)

if __name__ == "__main__":
    main()