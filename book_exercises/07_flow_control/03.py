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


# Product2 - The first case that matches '113' prints out 'Product2'
# Product not found! - The number 142 does not match any case statement, so the 
# default case prints out 'Product not found'

