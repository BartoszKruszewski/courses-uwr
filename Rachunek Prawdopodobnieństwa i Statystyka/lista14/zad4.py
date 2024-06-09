from driver import get_confidence_interval, get_data

if __name__ == '__main__':

    data_x, data_y = get_data('rpr-1402.csv')
    print(f'Confidence interval for X: {get_confidence_interval(1.96, 2, data_x)}')
    print(f'Confidence interval for Y: {get_confidence_interval(1.96, 3, data_y)}')