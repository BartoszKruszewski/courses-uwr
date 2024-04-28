0;

% Bartosz Kruszewski
% 26.04.2024
% Wyznaczanie wartości dystrybuanty rozkładu normalnego

function result = cdf(u, v, x, n = 1000000)
    % Funkcja obliczająca wartość dystrybuanty rozkładu normalnego.
    % - u: wartość oczekiwana
    % - v: odchylenie standardowe
    % - x: argument dystrybuanty
    % - n: liczba węzłów

    % Mozemy obliczyc wczesniej
    a = (x - u) / sqrt(2) / v;

    % Pierwsze dwa elementy sumy
    s = (exp(-(-1 * a)^2) + exp(-((-1 + 2 / n) * a)^2)) / 2;

    % Sumowanie kolejnych wyrazów sumy
    s += sum(arrayfun(@(t) exp(-(t / n * a)^2), -n + 4:2:n));

    % Obliczenie końcowego wyniku
    result = (1 + (x - u) / sqrt(2 * pi) / v * 2 / n  * s) / 2;
endfunction

% testy
fprintf('\n');
fprintf('    Test    |        Wyniki         |      WolframAlpha    \n');
fprintf('------------|-----------------------|----------------------\n');
fprintf('0.0 1.0 0.5 | %.19f | 0.6914624612740131036\n', cdf(0.0, 1.0, 0.5));
fprintf('2.0 1.7 0.3 | %.19f | 0.1586552539314570514\n', cdf(2.0, 1.7, 0.3));
fprintf('1.1 1.2 0.9 | %.19f | 0.4338161673890963463\n', cdf(1.1, 1.2, 0.9));
fprintf('0.1 0.2 0.4 | %.19f | 0.9331927987311419339\n', cdf(0.1, 0.2, 0.4));
fprintf('8.0 5.4 0.6 | %.19f | 0.0852856581920806146\n', cdf(8.0, 5.4, 0.6));
fprintf('\n');
