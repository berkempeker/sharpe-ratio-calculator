import yfinance as yf
import numpy as np
from datetime import datetime

def calculate_sharpe_ratio():
    # get user inputs
    ticker = input("Enter stock ticker symbol: ")
    risk_free_rate = float(input("Enter annual risk-free rate (as decimal, e.g., 0.44 for 44%): "))
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    # download stock data
    stock = yf.Ticker(ticker)
    df = stock.history(start=start_date, end=end_date)
    
    # calculate daily returns
    daily_returns = df['Close'].pct_change().dropna()
    
    # calculate metrics
    daily_avg_return = daily_returns.mean()
    daily_std = daily_returns.std()
    
    # annualize metrics (assuming 252 trading days)
    annual_avg_return = daily_avg_return * 252
    annual_std = daily_std * np.sqrt(252)
    
    # calculate Sharpe Ratio
    monthly_rf_rate = risk_free_rate / 12
    sharpe_ratio = (annual_avg_return - risk_free_rate) / annual_std
    
    # print results
    print(f"\nResults for {ticker.upper()}:")
    print(f"How many days of data: {len(daily_returns)}")
    print(f"Risk-free rate (annual): {risk_free_rate:.2%}")
    print(f"Daily average return: {daily_avg_return:.2%}")
    print(f"Daily standard deviation: {daily_std:.2%}")
    print(f"Annual average return: {annual_avg_return:.2%}")
    print(f"Annual standard deviation: {annual_std:.2%}")
    print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
    
    # Add standard deviation interpretation
    print("\nVolatility Interpretation:")
    print(f"The daily standard deviation of {daily_std:.2%} indicates that on any given day,")
    print(f"the stock's return typically fluctuates within {daily_std*2:.2%} of its mean return")
    print(f"(covering about 95% of all daily movements).")
  
    
    # Interpret Sharpe Ratio
    print("\nSharpe Ratio Interpretation:")
    if sharpe_ratio < 0:
        print("Negative Sharpe Ratio: The investment's return is worse than the risk-free rate.")
    elif sharpe_ratio < 0.5:
        print("Low Sharpe Ratio: Poor risk-adjusted returns.")
    elif sharpe_ratio < 1:
        print("Below-average Sharpe Ratio: Moderate risk-adjusted returns.")
    elif sharpe_ratio < 2:
        print("Good Sharpe Ratio: Good risk-adjusted returns.")
    else:
        print("Excellent Sharpe Ratio: Very good risk-adjusted returns.")

if __name__ == "__main__":
    try:
        calculate_sharpe_ratio()
    except Exception as e:
        print(f"An error occurred: {e}")
