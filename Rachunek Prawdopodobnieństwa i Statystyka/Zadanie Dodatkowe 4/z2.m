function result = z2(x, u, v, max_iter = 20)
    % Funkcja obliczająca wartość dystrybuanty rozkładu normalnego.
    %
    % - u: wartość oczekiwana
    % - v: odchylenie standardowe
    % - x: argument dystrybuanty
    % - max_iter: liczba iteracji
    %
    % Funkcja wykorzystuje tablice Romberga wypełnianą
    % z pomocą złożonego wzoru trapezów.

    % utworzenie oszczędnej tablicy Romberga
    % (utrzymujemy jednocześnie tylko jedną kolumnę)
    R = zeros(1, max_iter);

    % wypełnienie pierwszej kolumny z pomocą wzoru trapezów
    for k = 0:max_iter-1

        n = 2^k;
        a = (x - u) / sqrt(2) / v;

        % dwa pierwsze wyrazy dzielimy przez 2
        s = (exp(-(-1 * a)^2) + exp(-((-1 + 2 / n) * a)^2)) / 2;

        % sumowanie kolejnych wyrazów sumy
        for t = -n+4:2:n
            s += exp(-(t / n * a)^2);
        end

        % obliczanie koncowego wyniku
        R(k + 1) = (1 + (x - u) / sqrt(2 * pi) / v * 2 / n * s) / 2;
    end

    % wypełnienie pozostałych kolumn
    p1 = R(1);
    p2 = R(2);
    for k = 1:max_iter-1
        for j = 1:k
            p2 = p1;
            p1 = R(k + 1);
            R(k + 1) = (4^j * p1 - p2) / (4^j - 1);
        end
    end

    % odczytanie wyniku z ostatniej kolumny
    result = R(max_iter);
end
