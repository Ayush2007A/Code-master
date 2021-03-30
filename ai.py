def self_(method_sign):
    global sign
    x=input(':: ')
    signs = ['+','-']
    sign=signs
    if method_sign == '+':
        x = int(float(x))
    return self_