# Напишите на C# или Python библиотеку для поставки внешним клиентам,
# которая умеет вычислять площадь круга по радиусу и треугольника по трем сторонам

from ShapeArea import ShapeArea

shape_choice = input('Программа вычисляет площадь фигуры. Введите цифру для выбора и нажмите Enter:\n'
                     '1 — круг\n'
                     '2 — треугольник\n')

if shape_choice == '1':
    r_circ = float(input('Введите радиус фигуры, R: '))
    ShapeArea.sSirc(r_circ)
elif shape_choice == '2':
    a_side, b_side, c_side = (int(input('Введите три стороны треугольника, после ввода каждой нажимайте Enter: ')),
                              int(input()), int(input()))

    ShapeArea.sTriang(a_side, b_side, c_side)
else:
    print('Ошибка: фигуры нет в списке. Пожалуйста, введите цифру вашей фигуры согласно инструкции. ')