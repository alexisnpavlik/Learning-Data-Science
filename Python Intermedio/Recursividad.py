def factorial(n):
    """[Genera el fatorial de un numero]
(
    Args:
        n ([int]): [numero elegido]

    Returns:
        [int]: [retorna el resultado]
    """

    if n==1:
      return 1
    
    return n* factorial(n-1)

print(factorial(3))
