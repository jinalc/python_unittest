from log import logger


class TestLog:
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        try:
            result = x / y
        except ZeroDivisionError:
            logger.exception('Tried to divide by zero')
        else:
            return result

    num_1 = 10
    num_2 = 0

    add_result = add(num_1, num_2)
    logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

    sub_result = subtract(num_1, num_2)
    logger.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

    mul_result = multiply(num_1, num_2)
    logger.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

    div_result = divide(num_1, num_2)
    logger.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))
