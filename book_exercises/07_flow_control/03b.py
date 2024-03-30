def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')

bar_code_scanner('113')
bar_code_scanner(142)

"""
Product2
Product not found!, because we were passing in an integer 147 comparing it to
different cases with strings as the value.
"""