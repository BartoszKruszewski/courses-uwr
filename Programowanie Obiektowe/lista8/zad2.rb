# Bartosz Kruszewski
# PO lista 8 zadanie 2
# Zamiana jednostek 2
# 22.04.2023 Wersja 1.
# ruby main.rb

class Time
  def initialize(value)
    @seconds = value
  end

  def seconds
    @seconds
  end

  def seconds=(value)
    @seconds = value
  end

  def hours
    @seconds * 1.0 / 3600
  end

  def hours=(value)
    @seconds = value * 3600
  end

  def to_s
    "#{seconds} s, #{hours} h"
  end
end

class Length
  def initialize(value)
    @kilometers = value
  end

  def kilometers
    @kilometers
  end

  def kilometers=(value)
    @kilometers = value
  end

  def miles
    @kilometers * 0.621371192
  end

  def miles=(value)
    @kilometers = value * 1.609344
  end

  def to_s
    "#{kilometers} km, #{miles} m"
  end
end

class Velocity
  def initialize(length, time)
    @km_h = length.kilometers * 1.0 / time.hours
  end

  def km_h
    @km_h
  end

  def km_h=(args)
    @km_h = args[0].kilometers * 1.0 / args[1].hours
  end

  def knots
    @km_h * 0.5399
  end

  def knots=(args)
    @km_h = args[0].kilometers * 1.0 / args[1].hours * 1.852
  end

  def to_s
    "#{km_h} km/h, #{knots} knots"
  end
end

class Acceleration
  def initialize(velocity, time)
    @mm_h2 = velocity.km_h * 1000000.0 / time.hours
  end

  def mm_h2
    @mm_h2
  end

  def mm_h2=(args)
    @mm_h2 = args[0].km_h * 1000000.0 / args[1].hours
  end

  def km_s2
    @mm_h2 * 0.07716
  end

  def km_s2=(args)
    @mm_h2 = args[0].km_h * 12.96 * 1000000 / args[1].hours
  end

  def to_s
    "#{mm_h2} mm/h2, #{km_s2} km/s2"
  end

end

# główne wywołanie programu
if __FILE__ == $0
  # precyzja wyświetlania wyników
  PRECISION = 3

  # utworzenie obietktów przechowujących informacje
  # o długości, czasie i prędkośći
  length = Length.new(1)
  time = Time.new(3600)
  velocity = Velocity.new(length, time)

  # rysowanie tabelki
  puts "Tabela predkosci:"
  puts "Km/h : Węzły"
  (1..10).each do |x|
    length.kilometers = x
    velocity.km_h = [length, time]
    puts velocity.km_h.round(PRECISION).to_s + " : " +
           velocity.knots.round(PRECISION).to_s
  end
  puts

  # utworzenie obietktów przechowujących informacje
  # o długości, czasie, prędkośći i przyśpieszeniu
  length = Length.new(1)
  time = Time.new(3600)
  velocity = Velocity.new(length, time)
  acceleration = Acceleration.new(velocity, time)

  # rysowanie tabelki
  puts "Tabela przyśpieszenia:"
  puts "mm/h2 : km/s2"
  (1..10).each do |x|
    # przemnożenie wartości, żeby dane były bardziej widoczne
    length.kilometers = x * 0.001
    velocity.km_h = [length, time]
    acceleration.mm_h2 = [velocity, time]
    puts acceleration.mm_h2.round(PRECISION).to_s + " : " +
           acceleration.km_s2.round(PRECISION).to_s
  end
end