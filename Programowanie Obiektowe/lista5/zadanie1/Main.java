// Bartosz Kruszewski
// PO lista 5 zadanie 1 Listy
// 25.03.2023 Wersja 1.
// Program prezentujący klasę OrderedList

// javac Main.java <- kompilacja
// java Main <- uruchomienie programu

// Pliki OrderedList.java, Card.java, Rank.java, Alcohol.java 
// i Country.java muszą znajdować się w folderze zadanie1,
// który musi znajdować się w folderze z plikiem Main.java


import zadanie1.OrderedList;
import zadanie1.Card;
import zadanie1.Rank;
import zadanie1.Alcohol;
import zadanie1.Country;

public class Main {
    public static void main(String[] args) throws Exception {
        //testy listy z klasą Card
        OrderedList<Card> cardList = new OrderedList<>();
        cardList.add(new Card("7"));
        cardList.add(new Card("queen"));
        cardList.add(new Card("4"));
        cardList.add(new Card("jack"));
        System.out.println("Lista z kartami: " + cardList);

        //testy listy z klasa Rank
        OrderedList<Rank> rankList = new OrderedList<>();
        rankList.add(new Rank("general"));
        rankList.add(new Rank("private"));
        rankList.add(new Rank("colonel"));
        rankList.add(new Rank("major"));
        System.out.println("Lista ze stopniami wojskowymi: " + rankList);

        //testy listy z klasa Alcohol
        OrderedList<Alcohol> alcoholList = new OrderedList<>();
        alcoholList.add(new Alcohol("wine"));
        alcoholList.add(new Alcohol("vodka"));
        alcoholList.add(new Alcohol("beer"));
        alcoholList.add(new Alcohol("spirit"));
        System.out.println("Lista z alkoholami: " + alcoholList);

        //testy listy z klasa Country
        OrderedList<Country> countryList = new OrderedList<>();
        countryList.add(new Country("Poland"));
        countryList.add(new Country("USA"));
        countryList.add(new Country("Island"));
        countryList.add(new Country("France"));
        System.out.println("Lista z państwami: " + countryList);
    }
}