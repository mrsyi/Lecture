#!/usr/bin/env ipython

'''
    mysolution_integral.py

    Minimun realization,
    but in the Object-Oriented Programming way

    这次作业旨在编写能够独立维护的功能模块，即在脱离该代码文件的上下文后，其
    功能依旧能够运行。即对功能进行 _封装_。
    在 `class` 域之外定义的函数，为只在该文件内可见的方法。脱离本文件后，函数
    将无法运行，必须修改调用该功能的地方，从而造成调用函数的文件中夹杂与其业务
    无关的内容，为双方的维护都增加了难度。
    解决方法为把所有在域外定义的方法移至域内，并前导下划线 `_`。
'''

__author__ = 'smdsbz'



import matplotlib.pyplot as plt


class Integral:
    '''
    The Solution Class

    Usage:
    下面的例子在 Python Shell 中直接运行（需要切换到文件所在目录）
    可以看到，对于基本使用，除参数定义之外，用户不需要知道 **任何** 
    其他关于 Integral 内部具体实现的知识

    > from mysolution_integral import Integral
    
    > f = '2 * (x ** 3)'
    > s = 0.0
    > e = 10.0

    > Integral(f, s, e)()
    4999.99xx   # a pretty accurate value

    > result = Integral(f, s, e)
    > result(max_epsilon=1E-1)
    4999.xxxx      # a less accurate value

    # also try...
    > result(plot_error=False)
    > result.result
    '''

    def __init__(self, equation, start, end,    # 一行控制在 79 字符
                                                # 函数调用间换行的对齐括号风格
                 default_step=1):   # 有默认值参数的等号前后不加空格
        '''
        Initialize the Solution class

        Args:
            equation        - `eval()`-able string like
                              "2 * (x ** 3) - 4 * (x ** 0.5)", where `x` is
                              the placeholder
            start           - integral start
            end             - integral end
            default_step    - float

        Return:
            the integral value
        '''
        self._equation = equation
        self._start = start
        self._end = end
        self._default_step = default_step
        # test if equation is valid
        try:
            eval(equation.replace('x', '123'))
        except SyntaxError: # equation not valid
            print("Unsupported expression!")
        
        # 简单的用户输入合法性纠正
        # NOTE: 你永远不知道用户会输入什么
        # - 反向积分
        if self._start > self._end:
            self._start, self._end = self._end, self._start # 交换上下限
            self._equation = '-( ' + self._equation + ' )'  # 反号

        # - 参数假设修正
        if self._default_step > self._end - self._start:
            self._default_step = -0.5 * (self._end - self._start)


    def __call__(self, *args, **kwargs):
        '''
        Do the calculation and return the value

        在调用时才计算表达式的值，即 lazy 模式，在某些时候可以极大地优化单线程
        非异步程序的 _用户体验_
        '''
        return self.calculate_itermethod(*args, **kwargs)

    
    @property
    def result(self):
        # 直接取值的调用多半不需要 debug，故不画图
        return self.calculate_itermethod(plot_error=False)


    def _get_value_under_x(self, x):
        '''
        [Hidden] get value of equation under specified x
        前导下划线的“私有方法”
        '''
        # NOTE: 这里的括号是必须的，根据 Python 优先级，先乘方，再加负号
        #       当然即使不是必须的，也建议加括号
        return eval(self._equation.replace('x', '(' + str(x) + ')'))


    def _integral(self, current_step):
        '''
        [Hidden] (calculate_itermethod)
        Iterate over range (with step at `current_step`) once

        Args:
            current_step    - ie $$ dx $$

        Return:
            Integral value under `current_step`
        '''
        start = self._start # 不直接使用原值，保证重用性
        summation = 0 
        while start < self._end:
            summation += self._get_value_under_x(start) * current_step
            start += current_step
        print("[LOG] under current iteration: {}".format(summation))
        return summation


    def calculate_itermethod(self, max_epsilon=1E-3, plot_error=True):
        '''
        Calculate the production-ready value of integral

        Method:
            Calculate the value over and over again, until it meets the
            precision requirement

        NOTE:
            This method does **NOT** reuse results from last iteration

        Args:
            max_epsilon - precision requirement (default is 1E-3)
            plot_error  - if True, plot the descending trend of error

        Return:
            production-ready result value
        '''
        curr_step = self._default_step
        last_value = self._integral(curr_step)
        curr_step *= 0.5
        curr_value = self._integral(curr_step)
        statistics = {
            "iter_time": [1, ],
            "delta": [abs(last_value - curr_value), ]
        }
        # NOTE: 算法应当可以自动判别结果是否收敛，而不需要人为指定 dx
        #       尽量对全输入空间保证结果正确性
        while abs(curr_value - last_value) > max_epsilon:
            curr_step *= 0.5    # exponential speed
            last_value, curr_value = curr_value, self._integral(curr_step)
            # logging calculation process
            statistics["iter_time"].append(statistics["iter_time"][-1] + 1)
            statistics["delta"].append(abs(last_value - curr_value))
        if plot_error:
            plt.plot(statistics["iter_time"], statistics["delta"])
            plt.show()
        return curr_value

