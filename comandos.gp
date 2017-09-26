set title "Gráfico de número de operações em função do tamanho n."
set xlabel "Dimensão da matriz"
set ylabel "Número de operações"
f(x) = a*(x**3) + b
fit f(x) "operacoes.dat" using 1:2 via a,b
plot f(x), "operacoes.dat" 
