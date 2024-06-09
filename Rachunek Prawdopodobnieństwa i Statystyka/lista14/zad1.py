from scipy.stats import norm
from driver import get_data, get_mean, get_z

if __name__ == '__main__':

    data_x, data_y = get_data('rpr-1403.csv')
    print(f'Mean-X: {get_mean(data_x):.4f}')
    print(f'N-X: {len(data_x)}')
    print(f'Mean-Y: {get_mean(data_y):.4f}')
    print(f'N-Y: {len(data_y)}') 
    print(f'Z: {get_z(data_x, data_y, 4, 9)}')
    print(f'P-value: {norm.cdf(get_z(data_x, data_y, 4, 9)) * 2}')