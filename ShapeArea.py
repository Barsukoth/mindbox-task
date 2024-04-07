import math

# Заведём класс для вычисления площадей разных фигур
class ShapeArea:
    # Функция вычисления площади круга
    def sSirc(self, r_circ):
        s_sirc = round(math.pi * r_circ * r_circ, 2)
        print('S круга = ', s_sirc)
        return s_sirc

    # Функция вычисления площади треугольника
    def sTriang(self, a_side, b_side, c_side):
        # Вспомогательные переменные. Помогают избежать ошибок, к примеру, когда треугольник оказался правильным
        is_triag_right, triag_hyp = True, 0

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
                    s_triang = round((fir_cat * sec_cat) / 2, 2)
                    print('Это прямоугольный треугольник. S = ', s_triang)
                    return s_triang
                else:
                    is_triag_right = False
            else:
                is_triag_right = False
        else:
            print(
                'Ошибка: не выполнено неравенство треугольника, фигура не существует.'
                'Подробнее https://ru.wikipedia.org/wiki/Неравенство_треугольника')
            return False

        if is_triag_right == False:
            p_triang = (a_side + b_side + c_side) / 2
            s_triang = round(math.sqrt(p_triang * (p_triang - a_side) * (p_triang - b_side) * (p_triang - c_side)), 2)
            print('S треугольника = ', s_triang)
            return s_triang