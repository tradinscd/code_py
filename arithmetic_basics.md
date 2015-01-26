
# Basic Arithmetic

- **Author:** [Chris Albon](http://www.chrisalbon.com/),
[@ChrisAlbon](https://twitter.com/chrisalbon)
- **Date:** -
- **Repo:** [Python 3 code snippets for data
science](https://github.com/chrisalbon/code_py)
- **Note:** -

### Create some simulated variables


    x = 6
    y = 9

### x plus y


    print(x + y)

    15


### x minus y


    print(x - y)

    -3


### x times y


    print(x * y)

    54


### the remainder of x divided by y


    print(x % y)

    6


### x divided by y


    print(x / y)

    0.6666666666666666


### x divided by y (floor) (i.e. the quotient)


    print(x // y)

    0


### x raised to the y power


    print(x ** y)

    10077696


### x plus y, then divide by x


    print((x + y) / x)

    2.5


## Classics vs. floor division. This varies between 2.x and 3.x.

### Classic divison of 3 by 5


    print(3 / 5)

    0.6


### Floor divison of 3 by 5. This means it truncates any remainder down the its
"floor"


    print(3 // 5)
