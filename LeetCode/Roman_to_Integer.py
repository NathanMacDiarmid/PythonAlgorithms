def roman_to_integer(s: str) -> int:
    """
    Returns the coresponding integer from inputed Roman Numerals.

    This function assumes the input is in proper Roman Numeral form.

    >>> III
    3

    >>> IV
    4

    >>> XL
    40
    """
    lst = []
    lst2 =[]
    count = 0
    temp = 0

    for i in s:
        if i == 'I':
            i = 1
            lst.append(i)
        if i == 'V':
            i = 5
            lst.append(i)
        if i == 'X':
            i = 10
            lst.append(i)
        if i == 'L':
            i = 50
            lst.append(i)
        if i == 'C':
            i = 100
            lst.append(i)
        if i == 'D':
            i = 500
            lst.append(i)
        if i == 'M':
            i = 1000
            lst.append(i)

    for i in lst:
        if i > temp:
            i -= temp
            lst2.append(i)
        else:
            lst2.append(i)
        temp = i

    temp = 0
    
    for i in lst2:
        if i < temp:
            lst2.remove(i)
        temp = i

    for i in lst2:
        count += i

    return count