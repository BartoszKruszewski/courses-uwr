# Bartosz Kruszewski
# PO lista 10 zadania 1
# Sortowania
# 05.05.2023 Wersja 1.
# ruby zadanie1.rb

class Collection
  def initialize(data)
    # kolekcja jest tworzona na podstawie listy wbudowanej w ruby
    @data = data
  end

  def swap(i, j)
    @data[i], @data[j] = @data[j], @data[i]
  end

  def length
    @data.length
  end

  def get(i)
    @data[i]
  end

  def to_s
    @data.to_s
  end
end

class Sorter
  # sortowanie bąbelkowe
  def self.sort1(collection, compare_f = ->(a, b) { a > b })
    # ustalanie długości kolekcji
    n = collection.length
    # "przejście" po kolekcji n razy zaczynając od i-tego elementu
    # i "cofanie się" do pierwszego elementu zamieniając elementy
    # w złej kolejności po drodze
    (1...n).each do |i|
      j = i
      while j > 0 && compare_f.call(collection.get(j - 1), collection.get(j))
        collection.swap(j, j - 1)
        j -= 1
      end
    end
  end

  # sortowanie szybkie
  def self.sort2(collection, compare_f = ->(a, b) { a > b })
    quicksort(collection, 0, collection.length - 1, compare_f)
  end

  def self.quicksort(collection, left, right, compare_f)
    # Rekurencyjne dzielenie kolekcji przy użyciu pivota i sortowanie podkolekcji
    if left < right
      pivot_index = partition(collection, left, right, compare_f)
      quicksort(collection, left, pivot_index - 1, compare_f)
      quicksort(collection, pivot_index + 1, right, compare_f)
    end
  end

  def self.partition(collection, left, right, compare_f)
    # Podział kolekcji na dwie części względem pivota i zwracanie indeksu pivota
    pivot = collection.get(right)
    i = left
    (left...right).each do |j|
      if compare_f.call(pivot, collection.get(j))
        collection.swap(i, j)
        i += 1
      end
    end
    collection.swap(i, right)
    i
  end

end

# testy

puts
puts "Sortowanie domyślne:"
a = Collection.new([7, 8, 12, 0, 2, 2, 4, -9, 1])
puts "Nieposortowana kolekcja a: " + a.to_s
Sorter.sort2(a)
puts "Kolekcja a posortowana algorytmem sort1: " + a.to_s

b = Collection.new([10, 12, 6, 15, 2, 15, -18, 10, 0])
puts "Nieposortowana kolekcja b: " + b.to_s
Sorter.sort2(b)
puts "Kolekcja b posortowana algorytmem sort2: " + b.to_s

puts
puts "Sortowanie z kluczem e1 < e2:"
a = Collection.new([7, 8, 12, 0, 2, 2, 4, -9, 1])
puts "Nieposortowana kolekcja a: " + a.to_s
Sorter.sort2(a, ->(a, b) { a < b })
puts "Kolekcja a posortowana algorytmem sort1: " + a.to_s

b = Collection.new([10, 12, 6, 15, 2, 15, -18, 10, 0])
puts "Nieposortowana kolekcja b: " + b.to_s
Sorter.sort2(b, ->(a, b) { a < b })
puts "Kolekcja b posortowana algorytmem sort2: " + b.to_s

puts
puts "Sortowanie z kluczem e1 % 5 < e2 % 5:"
a = Collection.new([7, 8, 12, 0, 2, 2, 4, -9, 1])
puts "Nieposortowana kolekcja a: " + a.to_s
Sorter.sort2(a, ->(a, b) { a % 5 < b % 5 })
puts "Kolekcja a posortowana algorytmem sort1: " + a.to_s

b = Collection.new([10, 12, 6, 15, 2, 15, -18, 10, 0])
puts "Nieposortowana kolekcja b: " + b.to_s
Sorter.sort2(b, ->(a, b) { a % 5 < b % 5 })
puts "Kolekcja b posortowana algorytmem sort2: " + b.to_s


