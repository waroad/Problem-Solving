from matplotlib.projections import axes
import math
import numpy as np
import matplotlib.pyplot as plt
import sys
import sympy as sym
# %matplotlib inline


def derivative():
    a1 = math.cos(math.pi / 3)
    prev=0
    fig, ax = plt.subplots()
    x1 = np.arange(0, 10, 1)
    y1=[0 for _ in x1]
    for i in range(7):
        xx = sym.Symbol('x')
        aa = sym.diff((sym.cos(xx)), xx, i)
        aa=str(aa)
        if aa=='cos(x)':
            a=(math.cos(math.pi /4)* ((math.pi / 12))**i)/math.factorial(i)
            for ind,xx in enumerate(x1):
                y1[ind]+=(math.cos(xx) * ((math.pi / 12)) ** i) / math.factorial(i)

        elif aa=='-cos(x)':
            a=(math.cos(math.pi /4)* ((math.pi / 12))**i)/math.factorial(i)*-1
            for ind,xx in enumerate(x1):
                y1[ind]+=(math.cos(xx) * ((math.pi / 12)) ** i) / math.factorial(i)*-1
        elif aa=='sin(x)':
            a=(math.sin(math.pi /4)* ((math.pi / 12))**i)/math.factorial(i)
            for ind,xx in enumerate(x1):
                y1[ind]+=(math.sin(xx) * ((math.pi / 12)) ** i) / math.factorial(i)
        else:
            a=(math.sin(math.pi /4)* ((math.pi / 12))**i)/math.factorial(i)*-1
            for ind,xx in enumerate(x1):
                y1[ind]+=(math.sin(xx) * ((math.pi / 12)) ** i) / math.factorial(i)*-1
        prev+=a
        print(prev,"{:.10f}".format(((a1 - prev) / a1) * 100))

        ax.plot(x1,y1)
    plt.show()


def graphical_approach():
    xx = []
    yy = []
    for i in range(5):
        x = 4 * i + 4
        fx = (667.38 / x) * (1 - math.e ** (-0.146843 * x)) - 40
        xx.append(x)
        yy.append(fx)
    # 라인 스타일로는 '-', ':', '-.', '--' 등이 사용될 수 있습니다.
    plt.figure(figsize=(3, 4))
    plt.plot(xx, yy, marker="*")
    plt.xlim(0, 20)
    plt.ylim(-10, 40)
    plt.xticks(xx)
    plt.tick_params(axis='x', direction='in')
    plt.tick_params(axis='y', direction='inout')
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    # X축 및 Y축에서 특정 범위를 자를 수도 있습니다.
    plt.show()
# graphical_approach()


def falling():
    # 컴퓨터
    def f1(c):
        ff = 53.39 * (1 - np.exp((-0.18355) * c))
        return ff

    # 수치적
    def f2(vi):
        ff = vi + (9.8 - 12.5 * vi / 68.1) * h
        return ff

    h = 2

    x1 = np.arange(0, 1000, 0.1)
    y1 = [f1(xx) for xx in x1]

    x2, y2 = [0], [0]
    for i in range(1000):
        # 2,4,6,,,
        x2.append((i + 1) * h)
        y2.append(f2(y2[i]))

    print('%5s %10s' % ('t, s', 'v, m/s'))
    for i in range(7):
        print('%5d %10.2f' % (x1[i * 20], y1[i * 20]))
    print('%5s %10.2f' % ('oo', f1(sys.maxsize)))
    print("")

    print('%5s %10s' % ('t, s', 'v, m/s'))
    for i in range(7):
        print('%5d %10.2f' % (x2[i], y2[i]))
    print('%5s %10.2f' % ('oo', y2[-1]))

    fig, ax = plt.subplots()
    ax.plot(x1, y1)
    ax.plot(x2, y2, linestyle=':', marker="*")
    ax.set_xlim([0, 13])

    plt.show()

# e 1/2승
def mac():
    x = 1 / 2
    es = 0.00001
    maxit = 1000

    true_answer = np.exp(1 / 2)
    sol = 1
    yy=[1]*9
    ea = 100
    fac = 1
    xx = np.arange(1, 10)
    print('%5s %10.7s %10.7s %10.7s' % ('Terms', 'Result', 'Et', 'Ea'))

    print('%5d %10d %10f' % (1, 1, (true_answer - 1) / true_answer * 100))
    for i in range(1, 20):
        solold = sol
        sol = sol + x ** i/ math.factorial(i)
        if sol != 0:
            ea = abs((sol - solold) / sol) * 100
        print('%5d %10.7f %10.7f %10.7f' % (i + 1, sol, (true_answer - sol) / true_answer * 100, ea))
        plt.plot(xx, yy)
        yy+=xx**i/ math.factorial(i)
    plt.show()


# e 10승
def mac10():
    x = int(input("e의 지수값을 입력하시오 : "))
    sum = 1
    term = 1
    test = 0
    i = 0
    while True:
        if sum == test:
            break
        i = i + 1
        test = sum
        term = (x ** i) / math.factorial(i)
        sum = sum + term
        print("i=", i, "  term=", term, "  sum=", sum)
        # print("exact value = ", math.exp(x));
    print("exact value = ", sum)


# e -10승
def macminus10():
    x = int(input("e의 지수값을 입력하시오 : "))
    sum = 1
    term = 1
    test = 0
    i = 0
    minusx = -x
    while True:
        if sum == test:
            break
        i = i + 1
        test = sum
        term = (minusx ** i) / math.factorial(i)
        sum = sum + term
        # print("exact value = ", math.exp(x));
    print("exact value = ", 1 / sum)


# Taylor Seies
# cos
def draw_cos():
    def func_cos(x, n):
        cos_approx = 0
        for i in range(n):
            coef = (-1) ** i
            num = x ** (2 * i)
            denom = math.factorial(2 * i)
            cos_approx += (coef) * ((num) / (denom))
        return cos_approx

    # x 좌표
    angles = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
    # 실제 코사인 y 좌표
    p_cos = np.cos(angles)
    true_value=np.cos(np.pi/2)
    print(true_value)
    fig, ax = plt.subplots()
    # 실제 코사인 그래프 그리기
    ax.plot(angles, p_cos)
    # add lines for between 1 and 6 terms in the Taylor Series
    for i in range(1, 6):
        #####[]빠뜨리지 말자
        # 실험 코사인 y좌표
        t_cos = [func_cos(angle, i) for angle in angles]
        # 실험 코사인 그리기
        ax.plot(angles, t_cos)
        print(func_cos(np.pi / 2, i))

    ax.set_ylim([-7, 4])

    # set up legend
    '''
    legend_lst = ['cos() function']
    for i in range(1,6):
        legend_lst.append(f'Taylor Series - {i} terms')
    ax.legend(legend_lst,3)
    '''

    plt.show()


# sin
def draw_sin():
    def func_sin(x, n):
        sin_approx = 0
        for i in range(n):
            coef = (-1) ** i
            num = x ** (2 * i + 1)
            denom = math.factorial(2 * i + 1)
            sin_approx += (coef) * ((num) / (denom))
        return sin_approx

    angles = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
    true_sin = np.sin(angles)

    fig, ax = plt.subplots()
    # 실제 코사인 그래프 그리기
    ax.plot(angles, true_sin)
    ax.set_ylim([-7, 4])

    for i in range(6):
        mac_sin = [func_sin(angle, i) for angle in angles]
        ax.plot(angles, mac_sin)

    plt.show()


def poly():
    def f(x):
        return -0.1 * x ** 4 - 0.15 * x ** 3 - 0.5 * x ** 2 - 0.25 * x + 1.2
    def ff(x):
        return -0.4 * x ** 3 - 0.45 * x ** 2 - x - 0.25
    def fff(x):
        return -1.2 * x ** 2 - 0.9 * x - 1
    def ffff(x):
        return -2.4 * x - 0.9
    xi = 0
    h = 0.25
    xx = np.arange(-100, 1000, 0.1)
    yy = [f(x) for x in xx]
    x = [xi]
    fx = f(xi)
    zero = [fx]
    first = [fx]
    second = [fx]
    third = [fx]
    for i in range(4):
        x.append(xi + h)
        zero.append(zero[i])
        first.append(zero[i] + ff(xi) * h)
        second.append(zero[i] + ff(xi) * h + fff(xi) * h ** 2 / math.factorial(2))
        third.append(zero[i]+ff(xi)*h + fff(xi) * h ** 2 / math.factorial(2) + ffff(xi) * h ** 3 / math.factorial(3))
        xi += h
    fig, ax = plt.subplots()
    # original
    # ax.plot(xx, yy)
    # zero order
    ax.plot(x, zero)
    # first order
    ax.plot(x, first)
    # second order
    ax.plot(x, second)
    # third order
    ax.plot(x, third)

    ax.set_xlim([-0.1, 1.2])
    ax.set_ylim([0, 1.5])
    plt.show()
poly()


# 두 점 사이의 기울기를 통해 미분값을 구하는 코드 Round off and Truncation errors in numerical differentiation.
def inclination():
    def f1(x):
        return - 0.1 * x ** 4 - 0.15 * x ** 3 - 0.5 * x ** 2 - 0.25 * x + 1.25

    def f2(x):
        return - 0.4 * (x ** 3) - 0.45 * (x ** 2) - 1 * x - 0.25

    h = 1
    x = 0.5
    xx = []
    yy = []
    real_answer = f2(x)

    print("%20s %20s %20s" % ('step size', 'finite difference', 'true error'))

    for i in range(11):
        xx.append(h)
        centered = (f1(x + h) - f1(x - h)) / (2 * h)
        tr = abs(real_answer - centered)
        yy.append(tr)
        print('%20.10f %20.15f %20.15f' % (h, centered, tr))
        h /= 10

    plt.plot(xx, yy)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel("Step size")
    plt.ylabel("Error")
    plt.show()


# bisection
def bisection():
    def func_f(c):
        ff = (667.38 / c) * (1 - np.exp(-0.146843 * c)) - 40
        return ff
    def func_f2(x):
        ff = x ** 10 - 1
        return ff
    xl = 0
    xu = 1.3
    xr = xu
    es = 0.5
    imax = 100
    iter = 0
    true_answer = 1
    true_error_list = []
    iter_list = []
    for i in range(7):
        xrold = xr
        xr = (xl + xu) / 2
        true_error = abs((true_answer - xr)) / true_answer * 100
        true_error_list.append(true_error)
        iter = iter + 1
        iter_list.append(iter)
        temp = xl
        if xr != 0:
            ea = abs((xr - xrold) / xr) * 100
        test = func_f2(xl) * func_f2(xr)
        print("iter[{}] {:10.5f}, {:10.3f}, {:10.5f}, {:10.1f}, {:10.1f}".format(iter, temp, xu, xr, ea, true_error))
        if test < 0:
            xu = xr
        elif test > 0:
            xl = xr
        else:
            ea = 0


        if ea < es or iter >= imax:
            break;

    Bisect = xr
    print(">>> Bisect", Bisect)

    fig, ax = plt.subplots()
    ax.plot(iter_list, true_error_list)


# modi false position
def modi_falsePosition():
    def func_f(c):
        ff = (667.38 / c) * (1 - np.exp(-0.146843 * c)) - 40
        return ff
    def func_f2(x):
        ff = x ** 10 - 1
        return ff
    # false position
    xl = 0
    xu = 1.3
    xr = xl
    fxl = func_f2(xl)
    fxu = func_f2(xu)
    es = 0.5
    imax = 100
    iter = 0
    true_answer = 1
    true_error_list = []
    iter_list = []
    il = 0
    iu = 0
    for i in range(7):
        xrold = xr
        xr = xu - ((fxu) * (xl - xu) / (fxl - fxu))
        true_error = abs((true_answer - xr)) / true_answer * 100
        true_error_list.append(true_error)
        iter = iter + 1
        iter_list.append(iter)
        temp = xl
        if xr != 0:
            ea = abs((xr - xrold) / xr) * 100
        test = func_f2(xr) * func_f2(xl)
        print("iter[{}] {:10.5f}, {:10.3f}, {:10.5f}, {:10.1f}, {:10.1f}".format(iter, temp, xu, xr, ea, true_error))
        if test < 0:
            xu = xr
            fxu = func_f2(xu)
            iu = 0
            il = il + 1
            if (il >= 2):
                fxl = fxl / 2
        elif test > 0:
            xl = xr
            fxl = func_f2(xl)
            il = 0
            iu = iu + 1
            if (iu >= 2):
                fxu = fxu / 2
        else: ea = 0
        if ea < es or iter >= imax:
            break
    modifiedfalsePosition = xr
    print(">>> modifiedfalsePosition", modifiedfalsePosition)

    # fig, ax = plt.subplots()
    # ax.plot(iter_list, true_error_list)
    # plt.yscale('log')
    # plt.show()


# fixed point
def fixed():
    def f1(c):
        return np.exp(-c) - c

    def f2(c):
        return np.exp(-c)

    xr = 0
    iter = 0
    es = 0.5
    imax = 100
    true_answer = 0.6

    print("%5s %10s %10s %10s" % ('i', 'xi', 'ea', 'et'))
    while True:
        xrold = xr
        xr = f2(xrold)
        iter += 1
        et = abs((true_answer - xr)) / true_answer * 100
        if xr != 0:
            ea = abs((xr - xrold) / xr) * 100
        print("%5d %10.7f %10.2f %10.2f" % (iter, xr, ea, et))

        if ea < es or iter >= imax:
            break
    fixed = xr


# newton
def newton():
    def f1(c):
        return np.exp(-c) - c
    # 미분
    def f2(c):
        return -np.exp(-c) - 1
    xr = 0
    iter = 0
    es = 0.5
    imax = 100
    true_answer = 0.6
    print("%5s %10s %10s" % ('i', 'xi', 'et'))
    while True:
        xrold = xr
        xr = xrold - f1(xrold) / f2(xrold)
        iter += 1
        et = abs((true_answer - xr)) / true_answer * 100
        if xr != 0:
            ea = abs((xr - xrold) / xr) * 100
        print("%5d %10.7f %10.2f" % (iter, xr, et))

        if ea < es or iter >= imax:
            break
    fixed = xr


# newton raphson
def newton2():
    def func_f(x):
        ff = x ** 10 - 1
        return ff

    def func_g(x):
        ff = x - ((x ** 10 - 1) / (10 * (x ** 9)))
        return ff

    x0 = 0.5
    xr = x0
    es = 0.0001
    imax = 10000
    iter = 0

    while True:
        xrold = xr
        xr = func_g(xrold)
        iter = iter + 1
        if xr != 0:
            ea = abs((xr - xrold) / xr) * 100
        print("iter[{}], xr[{}], ea[{}], es[{}]".format(iter, xr, ea, es))
        if ea < es or iter >= imax:
            break

    NewtonRaphson = xr

    print(">>> NewtonRaphson", NewtonRaphson)


# secant
def secant():
    def f1(c):
        return np.exp(-c) - c

    def f2(c):
        return np.exp(-c)

    x1 = 0
    x2 = 1
    x3 = x2

    es = 0.5
    imax = 100
    iter = 0

    true_answer = 0.567
    true_error_list = []
    iter_list = []

    print('%10s %10s %10s %10s' % ('iteration', 'x1', 'x2', 'x3'))
    for i in range(7):
        x3old = x3
        x3 = x2 - (f1(x2) * (x1 - x2) / (f1(x1) - f1(x2)))

        true_error = abs((true_answer - x3)) / true_answer * 100
        true_error_list.append(true_error)

        iter = iter + 1
        iter_list.append(iter)

        print('%10d %10.2f %10.5f %10.5f' % (iter, x1, x2, x3))
        x1 = x2
        x2 = x3


# modified secant
def modi_secant():
    delta = 0.01

    def func_f(x):
        ff = np.exp(-x) - x
        return ff

    # 함수의 정의에 대해 생각해보자!!!
    def func_g(x):
        ff = x - (x + delta) * func_f(x) / (func_f(x + (x + delta)) - func_f(x))
        return ff

    x0 = 1
    xr = x0
    es = 0.0000005
    imax = 1000
    iter = 0
    while True:
        xrold = xr
        xr = func_g(xrold)
        iter = iter + 1
        if xr != 0:
            ea = abs((xr - xrold) / xr) * 100
        print("iter[{}], xr[{}], ea[{}], es[{}]".format(iter, xr, ea, es))
        if ea < es or iter >= imax:
            break;

    Secant = xr
    print(">>> secant", Secant)


# 뮐러
def muller():
    def func_f(x):
        ff = x ** 3 - 13 * x - 12
        return ff
    xr = 5
    h = 0.1
    eps = 0.00000000001
    maxit = 100
    x2 = xr
    x1 = xr + h * xr
    x0 = xr - h * xr
    print("---------------------------------")
    print(f"x0 : {x0}, x1 : {x1}, x2 : {x2}")
    print("---------------------------------")
    iter = 0
    while True:
        iter = iter + 1
        h0 = x1 - x0
        h1 = x2 - x1
        d0 = (func_f(x1) - func_f(x0)) / h0
        d1 = (func_f(x2) - func_f(x1)) / h1
        a = (d1 - d0) / (h1 + h0)
        b = a * h1 + d1
        c = func_f(x2)
        rad = math.sqrt(b * b - 4 * a * c)
        if abs(b + rad) > abs(b - rad):
            den = b + rad
        else:
            den = b - rad
        dxr = -2 * c / den
        xr = x2 + dxr
        print(f"Iter : {iter}, xr : {xr}, dxr : {dxr}, {abs(dxr/xr)*100}")
        if abs(dxr) < eps * xr or iter >= maxit:
            break
        x0 = x1
        x1 = x2
        x2 = xr
    print("")
    print(f"xr : {xr}")