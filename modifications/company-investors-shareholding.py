import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


def get_institutional_holders(ticker):
    try:
        stock = yf.Ticker(ticker)
        holders = stock.institutional_holders

        if holders is None or holders.empty:
            print("\nNo institutional holder data available.")
            return None

        return holders

    except Exception as e:
        print(f"\nError: {e}")
        return None


def display_table(df):

    print("\nTop Institutional Holders:\n")

    columns = []

    for col in ["Holder", "Shares", "Date Reported"]:
        if col in df.columns:
            columns.append(col)

    print(df[columns].head(10))


def create_pie_chart(df, ticker):

    top_holders = df.head(10).copy()

    labels = top_holders["Holder"].tolist()
    shares = top_holders["Shares"].tolist()

    remaining_shares = df.iloc[10:]["Shares"].sum()

    if remaining_shares > 0:
        labels.append("Others")
        shares.append(remaining_shares)

    plt.figure(figsize=(12, 8))

    plt.pie(
        shares,
        labels=labels,
        autopct="%1.1f%%",
        pctdistance=0.8
    )

    plt.title(f"{ticker} - Institutional Ownership")
    plt.show()


def main():

    print("=" * 50)
    print("SHAREHOLDING VISUALIZER")
    print("=" * 50)

    ticker = input("\nEnter Company Ticker: ").upper()

    data = get_institutional_holders(ticker)

    if data is None:
        return

    while True:

        print("\nChoose Option")
        print("1. View Institutional Holders")
        print("2. Institutional Holders Pie Chart")
        print("3. Both")
        print("4. Exit")

        choice = input("\nEnter Choice: ")

        if choice == "1":

            display_table(data)

        elif choice == "2":

            create_pie_chart(data, ticker)

        elif choice == "3":

            display_table(data)
            create_pie_chart(data, ticker)

        elif choice == "4":

            print("\nExiting...")
            break

        else:

            print("\nInvalid choice.")


if __name__ == "__main__":
    main()