def verificar_se_e_numero(num1, num2):
  if not isinstance(num1, (float,int)) or not isinstance(num2, (float,int)):
    raise ValueError('Alguns parâmetros são do tipo número')
  

def verificar_se_e_numero_1_parametro(num1):
  if not isinstance(num1, (float,int)):
    raise ValueError('Alguns parâmetros são do tipo número')