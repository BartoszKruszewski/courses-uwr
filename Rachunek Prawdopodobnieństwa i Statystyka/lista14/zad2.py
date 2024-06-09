from scipy.stats import t
from driver import get_data, get_mean, get_s2, get_sp2, get_t

if __name__ == '__main__':

    data_x, data_y = get_data('rpr-1402.csv')
    print(f'Mean-X: {get_mean(data_x):.4f}')
    print(f'N-X: {len(data_x)}')
    print(f'S2-X: {get_s2(data_x):.4f}')
    print(f'Mean-Y: {get_mean(data_y):.4f}')
    print(f'N-Y: {len(data_y)}')
    print(f'S2-Y: {get_s2(data_y):.4f}')
    print(f'SP2: {get_sp2(data_x, data_y)}')
    print(f'T: {get_t(data_x, data_y)}')
    print(f'P-value: {t.cdf(get_t(data_x, data_y), len(data_x) + len(data_y) - 2) * 2}')