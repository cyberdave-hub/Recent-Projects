


class Honest_calc():

    def __init__(self):
        self.memory = 0.0
        self.msg_0 = "Enter an equation\n"
        self.msg_1 = "Do you even know what numbers are? Stay focused!"
        self.msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
        self.msg_3 = "Yeah... division by zero. Smart move..."
        self.msg_4 = "Do you want to store the result? (y / n):"
        self.msg_5 = "Do you want to continue calculations? (y / n):"
        self.msg_6 = " ... lazy"
        self.msg_7 = " ... very lazy"
        self.msg_8 = " ... very, very lazy"
        self.msg_9 = "You are"
        self.msg_10 = "Are you sure? It is only one digit! (y / n)"
        self.msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
        self.msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

    def get_input(self):
        while True:
            x, oper, y = input(self.msg_0).split()
            x = self.test_input(x)
            if x == 'M':
                x = self.memory
            y = self.test_input(y)
            if y == 'M':
                y = self.memory
            oper = self.test_oper(oper, x, y)
            break

    def test_input(self, test):
        while True:
            try:
                test = float(test)
            except (ValueError, AttributeError):
                try:
                    test == 'M'
                except (ValueError, AttributeError):
                    print(self.msg_1)
                    self.get_input()
            break
        return(test)

    def addition(self, x, y):
        try:
            result = float(x) + float(y)
        except ValueError:
            return
        self.check(x, y, "+")
        print(result)
        msg_4_answer = input(self.msg_4)
        if msg_4_answer == "y" and self.is_one_digit(result):
            msg_10_answer = input(self.msg_10)
            if msg_10_answer == "y":
                msg_11_answer = input(self.msg_11)
                if msg_11_answer == "y":
                    msg_12_answer = input(self.msg_12)
                    if msg_12_answer == "y":
                        self.memory = result
        elif msg_4_answer == "y":
            self.memory = result
        else:
            pass
        msg_5_answer = input(self.msg_5)
        if msg_5_answer == "y":
            self.get_input()
        else:
            return

    def subtraction(self, x, y):
        try:
            result = float(x) - float(y)
        except ValueError:
            return
        self.check(x, y, "-")
        print(result)
        msg_4_answer = input(self.msg_4)
        if msg_4_answer == "y" and self.is_one_digit(result):
            msg_10_answer = input(self.msg_10)
            if msg_10_answer == "y":
                msg_11_answer = input(self.msg_11)
                if msg_11_answer == "y":
                    msg_12_answer = input(self.msg_12)
                    if msg_12_answer == "y":
                        self.memory = result
        elif msg_4_answer == "y":
            self.memory = result
        else:
            pass
        msg_5_answer = input(self.msg_5)
        if msg_5_answer == "y":
            self.get_input()
        else:
            return

    def multiplication(self, x, y):
        try:
            result = float(x) * float(y)
        except ValueError:
            return
        self.check(x, y, "*")
        print(result)
        msg_4_answer = input(self.msg_4)
        if msg_4_answer == "y" and self.is_one_digit(result):
            msg_10_answer = input(self.msg_10)
            if msg_10_answer == "y":
                msg_11_answer = input(self.msg_11)
                if msg_11_answer == "y":
                    msg_12_answer = input(self.msg_12)
                    if msg_12_answer == "y":
                        self.memory = result
        elif msg_4_answer == "y":
            self.memory = result
        else:
            pass
        msg_5_answer = input(self.msg_5)
        if msg_5_answer == "y":
            self.get_input()
        else:
            return

    def division(self, x, y):
        try:
            result = float(x) / float(y)
        except ValueError:
            return
        self.check(x, y, "/")
        print(result)
        msg_4_answer = input(self.msg_4)
        if msg_4_answer == "y" and self.is_one_digit(result):
            msg_10_answer = input(self.msg_10)
            if msg_10_answer == "y":
                msg_11_answer = input(self.msg_11)
                if msg_11_answer == "y":
                    msg_12_answer = input(self.msg_12)
                    if msg_12_answer == "y":
                        self.memory = result
        elif msg_4_answer == "y":
            self.memory = result
        else:
            pass
        msg_5_answer = input(self.msg_5)
        if msg_5_answer == "y":
            self.get_input()
        else:
            return

    def test_oper(self, operator, x, y):
        if operator in ["+","-","*","/"]:
            if operator == "+":
                self.addition(x, y)
            elif operator == "-":
                self.subtraction(x, y)
            elif operator == "*":
                self.multiplication(x, y)
            elif (operator == "/") and (y != 0):
                self.division(x, y)
            elif  (operator == "/") and (y == 0):
                self.check(x, y, operator)
                print(self.msg_3)
                self.get_input()
            else:
                print(self.msg_3)
                self.get_input()
        else:
            print(self.msg_2)
            self.get_input()

    def is_one_digit(self, digit):
        if digit > -10:
            if digit < 10:
                if digit.is_integer():
                    return True
                else:
                    return False

    def check(self, v1, v2, v3):
        msg = ""
        if self.is_one_digit(v1) and self.is_one_digit(v2):
            msg = msg + self.msg_6
        if (v1 == 1 or v2 == 1) and v3 == "*":
            msg = msg + self.msg_7
        if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
            msg = msg + self.msg_8
        if msg != "":
            msg = self.msg_9 + msg
        print(msg)


def main():
    hc = Honest_calc()
    hc.get_input()

if __name__ == '__main__':
    main()

