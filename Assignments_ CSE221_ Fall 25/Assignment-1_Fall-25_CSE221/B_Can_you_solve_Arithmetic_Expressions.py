T = int(input())
for _ in range(T):
    s = input().strip()
    expr = s[10:]
 
    for op in '+-*/':
        if op in expr:
            a_str, b_str = expr.split(op)
            a = float(a_str)
            b = float(b_str)
 
            if op == '+':
                res = a + b
            elif op == '-':
                res = a - b
            elif op == '*':
                res = a * b
            elif op == '/':
                res = a / b
            print(f"{res:.6f}")
            break