from binance.client import Client
from secrets import api_secret, api_key

client = Client("bGGhPSsx9ZzgnnS2ZYclBsVjW1l7raAmnoN7VDZ3XWhOK2qC2Ttr7djpoyJVxmEm", "qAK1ZuQ2gS4XMao6psqG0NsPmsjinyFnW9M8NtmjYDtVBwoCHb2fDu6gWkTUBB5p")

# pegar informações da nossa conta
info = client.get_account()
for item in info:
    print(item)

# ver os saldos dos ativos que temos na conta
lista_ativos = info["balances"]
# print(lista_ativos)
# ativos que temos algum saldo
for ativo in lista_ativos:
    if float(ativo["free"]) > 0:
        print(ativo)

# criar uma ordem dentro da binance
from binance.enums import *
order = client.create_order(
    symbol='BNBBRL',
    side=SIDE_SELL,
    type=ORDER_TYPE_MARKET,
    quantity=0.01,
    )
print(order)

# visualizar as ordens executadas
print(client.get_all_orders(symbol='BNBBRL'))
print(client.get_my_trades(symbol='BNBBRL'))

# te mostrar as referências de cada par de moedas
print(client.get_symbol_info('BNBBRL'))

# pegar as cotações em tempo real
transacoes = client.get_recent_trades(symbol="BNBBRL", limit=1)
print(transacoes)