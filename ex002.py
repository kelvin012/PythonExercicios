algo = input('Digite algo: ')
print(type(algo))
print(f'Só tem espaços ? {algo.isspace()}')
print(f'Isso pode ser transformado em numero ? {algo.isnumeric()}')
print(f'É alfabetico ? {algo.isalpha()}')
print(f'Isso é um caractere alfanumerico ? {algo.isalnum()}')
print(f'Isso esta em caixa alta ? {algo.isupper()}')
print(f'Isso esta em caixa baixa ? {algo.islower()}')
print(f'Está Capitalizada ? {algo.istitle()}')
