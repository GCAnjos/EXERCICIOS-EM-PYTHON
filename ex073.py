times = ('Palmeiras', 'Botafogo', 'Grêmio', 'Bragantino',
         'Atletico-MG', 'Flamengo', 'Athletico-PR', 'Fluminense',
         'Cuiabá', 'São Paulo', 'Corinthias', 'Fortaleza',
         'Internacional', 'Santos', 'Vasco', 'Cruzeiro',
         'Bahia', 'Goiás', 'Coritiba', 'America-MG')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os cinco primeiros são: {times[0:4]}')
print('-=' * 15)
print(f'Os quatro ultimos são: {times[16:21]}')
print('-=' * 15)
print(f'Em ordem alfabetica: {sorted(times)}')
print('-=' * 15)
print(f'O Cruzeiro está na {times.index("Cruzeiro")} posição')
print('-=' * 15)
