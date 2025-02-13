# d_s_p = {"위스키" : ['초콜릿', 50000]}
# print(d_s_p["위스키"][1])

drinks_foods = ["초콜릿","치즈","삼겹살","양꼬치"]
drinks = ["위스키", "와인", "소주", "고량주"]
prices = [50000, 30000, 5000, 7500]

import random
import math


def how_bout_this(drinks, drinks_food, menu):
    print(f'{drinks[menu - 1]} 에는 {drinks_foods[menu - 1]} 이거지 ㅋㅋ')
    print()


def delete(drink, food) :
    print_menu(drink,food)

    try :
        num = math.floor(float(input("몇번 술이랑 안주를 삭제할까요?\n-->").strip()))
        del drink[num-1]
        del food[num-1]

    except Exception :
        print("올바르게 입력해주세요!")
        return


def print_menu(drink, food) :
    print_list = [(a, b) for a, b in zip(drink, food)]

    for j, doprint in enumerate(print_list):
        print(f'{j + 1}번 메뉴 :', end =" ")
        print(doprint)

    print()


def ask_modify(drink, food) :
    print_menu(drink, food)
    try :
        pick = math.floor(float(input("몇 번 술의 안주를 수정할까요? : ").strip()))
        if pick < 1 or pick > len(drinks) :
            print("해당 번호가 없습니다")
            return

    except Exception :
        print("해당 번호가 없습니다.")
        return

    modify(drink, food, pick-1)


def modify(drink, food, pick) :
    anjoo = input("뭘로 수정할까요? : ").strip()
    food[pick] = anjoo
    print(f"{drink[pick]}엔 역시 {food[pick]} 이지~")
    print()


def add(drink, food) :
    alcohol = input("어떤 술을 추가하실껀가요 ? : ").strip()
    if alcohol in drink :
        menu = input("이미 술이 존재합니다, 수정하시겠어요? Y/N : ").strip().upper()
        if menu == 'Y' :
            modify(drink, food, drink.index(alcohol))
        else :
            return
    else :
        drink.append(alcohol)
        anjoo = input("어떤 안주를 추가하실껀가요 ? : ").strip()
        food.append(anjoo)


while True:
    print(f'다음 선택지 중에 고르세요. ')


    menu_list = ""
    j = 0
    for i, drink in enumerate(drinks) :
        menu_list += f'{i+1}. {drink} '
        j = i
    menu_list += f'\n{j+2}. 아무거나, {j+3}.이건 아니지! 수정 {j+4}. 이게 없네~ 추가 {j+5}. 넌 나가라~ 제거 {j+6}. 전체 출력! {j+7}. 종료'

    try :
        menu = math.floor(float(input(menu_list + "\n-->")))

    except Exception :
        print("다시 입력해주세요!")
        continue

    if menu >= 1 and menu <= len(drinks):
        how_bout_this(drinks, drinks_foods, menu)

    elif menu == j+2 :
        num = random.randint(0, len(drinks)-1)
        how_bout_this(drinks, drinks_foods, num)

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
        print("올바른 번호를 입력해주세요!")

