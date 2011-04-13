unknown = []
for lin in open('fn_builtin.txt'):
    ident = lin.split()[0]
    try:
        fn = eval(ident)
    except:
        unknown.append(ident)
    else:
        print(fn.__doc__.split('\n')[0])
print(unknown)
