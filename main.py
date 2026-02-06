import numpy as np
import numpy_financial as npf


if __name__ == '__main__':
    
    rate = 0.05
    periods = 5
    pv = 120000

    freq = 12
    rate_invest = 0.12
    all_periods = periods*12
    rate_invest /= freq

pv_price = - np.around(npf.fv(rate, periods, 0, pv),2)

price_change = -npf.fv(rate, np.arange(0, periods+1), 0, pv)

pmt = np.around(-npf.pmt(rate_invest, all_periods, 0,  pv_price),2)

pmt_change = np.around(npf.fv(rate_invest, np.arange(1, all_periods + 1), -pmt, 0))
