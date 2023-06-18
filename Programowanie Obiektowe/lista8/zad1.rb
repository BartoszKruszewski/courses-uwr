# Bartosz Kruszewski
# PO lista 8 zadanie 1
# Zamiana jednostek
# 22.04.2023 Wersja 1.
# ruby main.rb

class Mass
  def initialize(value)
    @kilograms = value
  end

  def kilograms
    @kilograms
  end

  def kilograms=(value)
    @kilograms = value
  end

  def pounds
    @kilograms * 2.20462262
  end

  def pounds=(value)
    @kilograms = value * 0.45359237
  end

  def to_s
    "#{kilograms} kg, #{pounds} lb"
  end
end

class Length
  def initialize(value)
    @meters = value
  end

  def meters
    @meters
  end

  def meters=(value)
    @meters = value
  end

  def yards
    @meters * 1.0936133
  end

  def yards=(value)
    @yards = value * 0.9144
  end

  def to_s
    "#{meters} m, #{yards} yd"
  end
end

class Area
  def initialize(length1, length2)
    @hectares = length1.meters * length2.meters * 0.0001
  end

  def hectares
    @hectares
  end

  def hectares=(args)
    @hectares = args[0].meters * args[1].meters * 0.0001
  end

  def square_inches
    @hectares * 15500000
  end

  def square_inches=(args)
    @hectares = args[0].yards * args[1].yards * 1296
  end

  def to_s
    "#{hectares} ha, #{square_inches} in2"
  end
end

class Pressure
  def initialize(mass, area)
    @psi = mass.pounds / area.square_inches
  end

  def psi
    @psi
  end

  def psi=(args)
    @psi = args[0].pounds / args[1].square_inches
  end

  def bars
    @psi * 0.068947573
  end

  def bars=(args)
    @psi = args[0].pounds / args[1].square_inches * 14.50377375865
  end

  def to_s
    "#{bars} bar, #{psi} psi"
  end

end

# główne wywołanie programu
if __FILE__ == $0
  # precyzja wyświetlania wyników
  PRECISION = 3

  # utworzenie obietktów przechowujących informacje
  # o długości i polu powierzchni
  side_length = Length.new(1)
  area = Area.new(side_length, side_length)

  # rysowanie tabelki
  puts "Tabela powierzchni:"
  puts "Metry : Hektary : Cale kwadratowe"
  (1..10).each do |x|
    side_length.meters = x
    area.hectares = [side_length, side_length]
    puts side_length.meters.round(PRECISION).to_s + "x" +
           side_length.meters.round(PRECISION).to_s + " : " +
           area.hectares.round(PRECISION).to_s + " : " +
           area.square_inches.round(PRECISION).to_s
  end
  puts

  # utworzenie obietktów przechowujących informacje
  # o długości, polu powierzchni i ciśnieniu
  mass = Mass.new(1)
  area = Area.new(side_length, side_length)
  pressure = Pressure.new(mass, area)

  puts "Tabela ciśnienia:"
  puts "Funty : Cale kwadratowe : PSI : Bary"
  (1..10).each do |x|
    # przemnożenie wartości, żeby dane były bardziej widoczne
    mass.pounds = x * 1000
    side_length.meters = x * 0.0001
    area.square_inches = [side_length, side_length]
    pressure.psi = [mass, area]
    puts mass.pounds.round(PRECISION).to_s + " : " +
           area.square_inches.round(PRECISION).to_s + " : " +
           pressure.psi.round(PRECISION).to_s + " : " +
           pressure.bars.round(PRECISION).to_s
  end
end