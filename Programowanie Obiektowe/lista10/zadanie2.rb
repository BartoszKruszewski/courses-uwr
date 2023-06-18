# Bartosz Kruszewski
# PO lista 10 zadania 2
# Wyszukiwania
# 05.05.2023 Wersja 1.
# ruby zadanie2.rb

class Collection
  def initialize(data = nil)
    # dlugość kolekcji
    @length = 0

    # sprawdzanie, czy podano listę z wartościami początkowymi dla kolekcji
    if data.nil?
      # referencje do pierwszego i ostatniego elementu kolekcji
      @first = nil
      @last = nil
    else
      # dodawanie każdego elementu z listy do kolekcji
      data.each do |e|
        add(e)
      end
    end
  end

  def length
    @length
  end

  def add(element)
    # utworzenie nowego elementu
    node = Node.new(element)
    # sprawdzanie, czy kolekcja jest pusta
    if @length == 0
      @first = node
      @last = node
      # sprawdzanie, czy nowy element jest mniejszy od obecnie najmniejszego
    elsif element <= @first.value
      node.next = @first
      @first.prev = node
      @first = node
      # sprawdzanie, czy nowy element jest większy od obecnie największego
    elsif element >= @last.value
      @last.next = node
      node.prev = @last
      @last = node
      # "przejscie" po elementach listy, do momentu aż następny element listy
      # będzie większy
    else
      current = @first.next
      while current != nil
        if element <= current.value
          node.prev = current.prev
          node.next = current
          current.prev.next = node
          current.prev = node
          break
        end
        current = current.next
      end
    end
    @length += 1
  end

  # zwracanie wartości elementu o podanym indeksie
  def [](index)
    # sprawdzanie czy indeks jest poprawny
    if index < @length
      # ustawienie aktualnego elementy na pierwszy
      current = @first
      # "przejście" na następny element indeks razy
      (index).times do
        current = current.next
      end
    else
      raise IndexError.new("Nie ma elementu o indeksie #{index} w kolekcji!")
    end
    current.value
  end

  def to_s
    # utworzenie łańcucha znaków przechowującego reprezentację kolekcji
    result = "["
    # rozpoczęcie od pierwszego elementu
    current = @first
    # dopisywanie kolejnych wartości elementów
    while current
      result += current.value.to_s
      unless current.next.nil?
        result += ", "
      end
      current = current.next
    end
    result + "]"
  end

  # klasa elementu kolekcji
  private class Node
            # możliwość bezpośredniego używania pól klasy
            attr_accessor :prev, :next, :value

            def initialize(value)
              # wartość elementu
              @value = value
              # referencja następny element
              @prev = nil
              # referencja na poprzedni element
              @next = nil
            end
          end
end

class Search
  # wyszukiwanie binarne
  def self.bin_search(collection, element)
    # ustalanie końców przedziałów
    l = 0
    r = collection.length - 1
    # szukanie dopóki końce przedziałów nie "przetną się"
    while l <= r
      # ustalanie pozycji na środek
      pos = (l + r) / 2
      # zmiana końców przedziału w zależności,
      # czy szukany element jest większy, czy mniejszy od sprawdzanego
      if collection[pos] == element
        return pos
      elsif collection[pos] < element
        l = pos + 1
      else
        r = pos - 1
      end
    end
    # zwracanie -1 jeżeli nie znaleziono elementu
    -1
  end

  # wyszukiwanie interpolacyjne
  def self.interpolation_search(collection, element)
    # ustalanie końców przedziałów
    l = 0
    r = collection.length - 1
    # szukanie dopóki końce przedziałów nie "przetną się"
    while l <= r
      # ustalanie pozycji według wzoru
      pos = l + (element - collection[l]) * (r - l) /
        (collection[r] - collection[l])
      # zmiana końców przedziału w zależności,
      # czy szukany element jest większy, czy mniejszy od sprawdzanego
      if collection[pos] == element
        return pos
      elsif collection[pos] < element
        l = pos + 1
      else
        r = pos - 1
      end
    end
    # zwracanie -1 jeżeli nie znaleziono elementu
    -1
  end
end

# testy

a = Collection.new([7, 9, 21, 18, 12, 5])
puts "Kolekcja: " + a.to_s
puts
puts "Indeks elementu 18 szukany za pomocą bin_search(): " +
       Search.bin_search(a, 18).to_s
puts "Indeks elementu 18 szukany za pomocą bin_search(): " +
       Search.interpolation_search(a, 18).to_s
puts
puts "Indeks elementu 5 szukany za pomocą bin_search(): " +
       Search.bin_search(a, 5).to_s
puts "Indeks elementu 5 szukany za pomocą bin_search(): " +
       Search.interpolation_search(a, 5).to_s
puts
puts "Indeks elementu 21 szukany za pomocą bin_search(): " +
       Search.bin_search(a, 21).to_s
puts "Indeks elementu 21 szukany za pomocą bin_search(): " +
       Search.interpolation_search(a, 21).to_s