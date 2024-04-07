import math

shape_choice = input('Программа вычисляет площадь фигуры. Введите цифру для выбора и нажмите Enter:\n'
                     '1 — круг\n'
                     '2 — треугольник\n')


# Заведём класс для вычисления площадей разных фигур
class shape_area:
    # Функция вычисления площади круга
    def s_circ(R_sirc):
        print('S круга = ', math.pi * R_circ * R_circ)

    # Функция вычисления площади треугольника
    def s_triang(a_side, b_side, c_side, is_triag_right, triag_hyp):
        # Проверим неравенство треугольника, чтобы понять, существует ли фигура
        if (a_side + b_side > c_side) and (a_side + c_side > b_side) and (b_side + c_side > a_side):

            # Проверим наличие прямого угла: сначала найдём гипотенузу,
            # потом воспользуемся теоремой Пифагора
            if (a_side > b_side) and (a_side > c_side):
                triag_hyp = a_side
                fir_cat = b_side
                sec_cat = c_side
            elif (b_side > a_side) and (b_side > c_side):
                triag_hyp = b_side
                fir_cat = a_side
                sec_cat = c_side
            elif (c_side > a_side) and (c_side > b_side):
                triag_hyp = c_side
                fir_cat = a_side
                sec_cat = b_side
            else:
                is_triag_right = False

            if triag_hyp != 0:
                if triag_hyp ** 2 == fir_cat ** 2 + sec_cat ** 2:
                    S_triang = (fir_cat * sec_cat) / 2
                    print('Это прямоугольный треугольник. S = ', round(S_triang, 2))
                else:
                    is_triag_right = False
            else:
                is_triag_right = False
        else:
            print(
                'Ошибка: не выполнено неравенство треугольника, фигура не существует.'
                'Подробнее https://ru.wikipedia.org/wiki/Неравенство_треугольника')

        if is_triag_right == False:
            p_triang = (a_side + b_side + c_side) / 2
            S_triang = math.sqrt(p_triang * (p_triang - a_side) * (p_triang - b_side) * (p_triang - c_side))
            print('S = ', round(S_triang, 2))


if shape_choice == '1':
    R_circ = float(input('Введите радиус фигуры, R: '))
    shape_area.s_circ(R_circ)
elif shape_choice == '2':
    a_side, b_side, c_side = (int(input('Введите три стороны треугольника, после ввода каждой нажимайте Enter: ')),
                              int(input()), int(input()))
    # Вспомогательные переменные. Помогают избежать ошибок, к примеру, когда треугольник оказался правильным
    is_triag_right, triag_hyp = True, 0

    shape_area.s_triang(a_side, b_side, c_side, is_triag_right, triag_hyp)
else:
    print('Ошибка: фигуры нет в списке. Пожалуйста, введите цифру вашей фигуры согласно инструкции. ')