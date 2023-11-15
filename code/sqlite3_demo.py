import sqlite3


def create_portfolio_table():
    with sqlite3.connect("data/stocks.db") as db:
        cursor = db.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS portfolio (
                symbol TEXT,
                shares INTEGER,
                price REAL
            )
            """
        )


def insert_stocks(stocks):
    with sqlite3.connect("data/stocks.db") as db:
        cursor = db.cursor()
        cursor.executemany("INSERT INTO portfolio VALUES (?,?,?)", stocks)


def display_portfolio():
    with sqlite3.connect("data/stocks.db") as db:
        cursor = db.cursor()
        for row in cursor.execute("SELECT * FROM portfolio"):
            print(row)


def display_expensive_stocks(price):
    with sqlite3.connect("data/stocks.db") as db:
        cursor = db.cursor()
        results = cursor.execute("SELECT * FROM portfolio WHERE price > ?", (price,))
        for row in results:
            print(row)


def main():
    """"""
    create_portfolio_table()

    # stocks = [
    #     ("AAPL", 50, 189.03),
    #     ("FB", 150, 332.58),
    #     ("GOOG", 100, 136.05),
    #     ("MSFT", 100, 368.97),
    #     ("NVDA", 100, 487.00),
    #     ("TSLA", 100, 242.79),
    # ]
    # insert_stocks(stocks)

    # display_portfolio()

    # print("\nExpensive Stocks:")
    # min_price = 300
    # display_expensive_stocks(min_price)


if __name__ == "__main__":
    main()
