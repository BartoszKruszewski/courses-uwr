# Bartosz Kruszewski
# PO lista 9 zadania 1 i 3
# Funkcje matematyczne
# i rysowanie ich wykresów
# 28.04.2023 Wersja 1.
# ruby zadania1-3.rb

class Function
  def initialize(&block)
    @function = block
  end

  def value(x)
    @function.call(x)
  end

  def zero(a, b, e)
    # ustawienie przedziałów na początkowe wartości
    x1 = a
    x2 = b
    # powatrzanie obliczeń, aż osiągniemy zadeklarowaną precyzję
    while (x2 - x1).abs > e
      # ustalanie środka przedziału
      s = (x1 + x2) / 2.0
      # sprawdzanie czy środek przedziału jest miejscem zerowym
      if value(s).abs < e
        return s
        # zmiejszenie przedzialu poszukiwań o połowę
      elsif value(s) * @function.call(x1) < 0
        x2 = s
      else
        x1 = s
      end
    end
    # jeżeli nie udało się znaleźć miejsca zerowego zwracamy nil
    nil
  end

  def field(a, b)
    # ustalenie dokładności obliczeń
    n = 10000
    # obliczenie wysokości trapezów do szacowania pola
    dx = (b - a) * 1.0 / n
    # utworzenie zmiennej przechowującej sumę pól trapezów
    sum = 0.0
    (0..n).each do |i|
      # obliczanie długości podstaw trapezu
      y1 = value(a + i * dx)
      y2 = value(a + (i + 1) * dx)
      # obliczanie pola trapezu i dodanie go do sumy
      sum += ((y1 + y2) / 2) * dx
    end
    sum
  end

  def deriv(x)
    # ustalenie h jako bardzo małej wartości,
    # będącej przybliżeniem ujemnej nieskończoności
    h = 0.0001
    (value(x + h) - value(x)) / h
  end

  def plot(ax, bx, ay, by, precision = 0.5)
    # rysowanie górnej części ramki
    puts "o]" + "=" * (bx - ax + 1) + "[o"
    # iteracja po wierszach wykresu
    (ay..by).reverse_each do |y|
      # rysowanie lewego boku ramki
      print "| "
      # iteracja po kolumnach wykresu
      (ax..bx).each do |x|
        begin
          # jeżeli wartość zmiennej dla x jest równa w przybliżeniu y
          # to rysujemy *, jeżeli nie to rysujemy albo osie układu
          # współrzędnych, albo pustą przestrzeń (spację)
          if (value(x) - y).abs < precision
            print "*"
          elsif x == 0 and y == 0
              print "+"
          elsif x == 0
            print "|"
          elsif y == 0
            print "-"
          else
            print " "
          end
        rescue Exception
          if x == 0 and y == 0
            print "+"
          elsif x == 0
            print "|"
          elsif y == 0
            print "-"
          else
            print " "
          end
        end
      end
      # rysowanie prawego boku ramki
      puts " |"
    end
    # rysowanie dolnej części ramki
    puts "o]" + "=" * (bx - ax + 1) + "[o"
  end
end

# przykładowe funkcje
funcs = [
  ["f(x) = x^2*sin(x)", Function.new { |x| x * x * Math.sin(x) }],
  ["f(x) = x^3-5x^2+10x-5",
   Function.new { |x| x * x * x - 5 * x * x + 10 * x - 5 }],
  ["f(x) = 1/x", Function.new { |x| 1.0 / x }],
  ["f(x) = e^(-x^2)", Function.new { |x| Math.exp(-x * x) }],
  ["f(x) = sin(x)/x", Function.new { |x| Math.sin(x) / x }]
]

# wypisywanie tabelki
puts "======================================================================"
puts "|        Funkcja        | x | f(x) | f(x) = 0 | Pole [1 - 2] | f'(x) |"
puts "======================================================================"

funcs.each do |name, f|
  x = 2.0
  fx = f.value(x).round(2).to_s.ljust(4)
  zero = f.zero(-5, 5, 0.0001)
  if zero == nil
    zero = "-".ljust(8)
  else
    zero = zero.round(6).to_s.ljust(8)
  end
  area = f.field(1, 2).round(10).to_s.ljust(12)
  deriv = f.deriv(x).round(2).to_s.ljust(5)
  x = x.round(0).to_s
  puts "| #{name.ljust(21)} |" +
         " #{x.ljust(1)} | #{fx} | #{zero} | #{area} | #{deriv} |"
end
puts "======================================================================"

# wypisywanie wykresów
puts
Function.new { |x| Math.sin(x) }.plot(-20, 20, -2, 2)
puts
Function.new { |x| Math.cos(x) }.plot(-20, 20, -2, 2)
puts
Function.new { |x| x*x/10 }.plot(-20, 20, -2, 5)
puts
Function.new { |x| x*x*x/20 }.plot(-20, 20, -5, 4)
puts
Function.new { |x| 1/x }.plot(-20, 20, -2, 2)
puts
Function.new { |x| Math.sqrt(x) }.plot(-20, 20, -2, 4)