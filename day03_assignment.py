drinks_foods = ["초콜릿","치즈","삼겹살","양꼬치"]
drinks = ["위스키", "와인", "소주", "고량주"]


import random
import math


def delete(drink, food) :
    print_menu(drink,food)
    num = math.floor(float(input("몇번 술이랑 안주를 삭제할까요?\n-->")))
    del drink[num-1]
    del food[num-1]



def print_menu(drink, food) :
    print_list = []
    for i in range(len(drink)):
        print_list.append((drink[i], food[i]))

    for j, doprint in enumerate(print_list):
        print(f'{j + 1}번 메뉴 :', end =" ")
        print(doprint)

    print()


def ask_modify(drink, food) :
    for i, alcohol in enumerate(drink) :
        print(f'{i+1}. {alcohol}', end = ' ')
    print()
    pick = math.floor(float(input("어떤 번호 술의 안주를 수정할까요? : ")))
    modify(drink, food, pick-1)


def modify(drink, food, pick) :
    anjoo = input("뭘로 수정할까요? : ")
    food[pick] = anjoo
    print(f"{drink[pick]}엔 역시 {food[pick]} 이지~")
    print()


def add(drink, food) :
    alcohol = input("어떤 술을 추가하실껀가요 ? : ")
    if alcohol in drink :
        menu = input("이미 술이 존재합니다, 수정하시겠어요? Y/N : ").upper()
        if menu == 'Y' :
            modify(drink, food, drink.index(alcohol))
        else :
            return
    else :
        drink.append(alcohol)
        anjoo = input("어떤 안주를 추가하실껀가요 ? : ")
        food.append(anjoo)


while True:
    print(f'다음 선택지 중에 고르세요. ')


    menu_list = ""
    j = 0
    for i, drink in enumerate(drinks) :
        menu_list += f'{i+1}. {drink} '
        j = i
    menu_list += f'\n{j+2}. 아무거나, {j+3}.이건 아니지! 수정 {j+4}. 이게 없네~ 추가 {j+5}. 넌 나가라~ 제거 {j+6}. 전체 출력! {j+7}. 종료'
    menu = math.floor(float(input(menu_list + "\n-->")))

    if menu >= 1 and menu <= len(drinks)+1:
        print(f'{drinks[menu-1]} 엔 {drinks_foods[menu-1]} 이거지 ㅋㅋ')
        print()

    elif menu == j+2 :
        num = random.randint(0, 3)
        print(f'{drinks[num]} 엔 {drinks_foods[num]} 이거지 ㅋㅋ')
        print()

    elif menu == j+3 :
        ask_modify(drinks, drinks_foods)

    elif menu == j+4 :
        add(drinks, drinks_foods)

    elif menu == j+5 :
        delete(drinks, drinks_foods)

    elif menu == j+6 :
        print_menu(drinks, drinks_foods)

    elif menu == j+7 :
        break

    else :
        pass


