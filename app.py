import mymodule

x = mymodule.summa(1, 2)

print(x)

if __name__ == "__main__":
    print( __name__, "был запущен")
else:
    print(__name__, "был импортирован")