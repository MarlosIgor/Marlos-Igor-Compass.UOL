esta_chuvendo = True
print('Hoje estou com as roupas ' + ('secas.', 'molhadas.')[esta_chuvendo])
print('Hoje estou com as roupas ' + ('secas.' if esta_chuvendo else 'molhadas.'))

