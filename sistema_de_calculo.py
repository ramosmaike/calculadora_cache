import streamlit as st

st.divider()
def calcular_cache(cache_por_hora, horas, minutos):
  """Calcula o valor total do cachê, considerando horas e minutos.

  Args:
    cache_por_hora: Valor do cachê por hora.
    horas: Número de horas trabalhadas.
    minutos: Número de minutos trabalhados.

  Returns:
    Valor total do cachê.
  """

  # Convertendo minutos para uma fração de hora
  horas_decimais = horas + minutos / 60
  valor_total = cache_por_hora * horas_decimais

  return valor_total

st.title('Calculadora de Cachê')

cache_por_hora = st.number_input('Valor do cachê por hora (R$):', min_value=0.01, step=0.01)
horas = st.number_input('Horas trabalhadas:', min_value=1, step=1)
minutos = st.number_input('Minutos trabalhados:', min_value=0, max_value=59, step=1)

if st.button('Calcular'):
  valor_total = calcular_cache(cache_por_hora, horas, minutos)
  st.success(f'O valor total a ser pago é: R$ {valor_total:.2f}')
  st.balloons()
st.divider()

        