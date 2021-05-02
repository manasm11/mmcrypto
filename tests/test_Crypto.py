from mmcrypto import Crypto
from mmcrypto.Crypto import Price
from datetime import datetime
import os
import requests_cache
from pytest import mark

requests_cache.install_cache(expire_after=360)


# @mark.xfail(reason="Will Complete After Testing Price")
def test_crypto(data_directory_, test):
    assert "data" not in data_directory_, "Check the data_directory_ fixture"

    # Crypto.update TESTS

    Crypto.update(data_directory=data_directory_)
    assert os.path.exists(data_directory_), f"{data_directory_} not created"
    btc_file = os.path.join(data_directory_, "btc.csv")
    assert os.path.exists(btc_file), f"{btc_file} not created"
    assert os.stat(btc_file).st_size > 0, f"{btc_file} FILE IS EMPTY"

    # HELPER FUNCTIONS
    raw = Crypto._get_data_from_api()
    assert isinstance(raw, dict)
    data = Crypto._parse_data_from_api(raw)
    assert isinstance(data, dict)
    assert len(data.keys()) > 0, "data is empty"
    assert isinstance(data["win"], Price)
    assert data["doge"], "data['doge'] is empty"
    assert data["doge"] > 0
    assert data["doge"] >= 0
    assert data["doge"] < int("9" * 22)
    assert data["doge"] <= int("9" * 22)
    assert data["doge"] == data["doge"]

    # SYMBOLS
    symbols = Crypto.SYMBOLS
    crypto = Crypto(symbol="btc", data_directory=data_directory_)
    test.assertRaisesRegex(
        TypeError, ".*must be a str.*", Crypto, symbol={}, data_directory=""
    )
    test.assertRaisesRegex(
        TypeError, ".*must be a str.*", Crypto, symbol="win", data_directory=[]
    )
    price = Price(
        time=datetime.now().timestamp(),
        low=1,
        high=2,
        value=1.2,
        vol=1000,
        open_=1.1,
        sell=1.12,
        buy=1.13,
    )


def test_crypto_add_price(crypto, price):
    crypto.add_price(price)
    with open(crypto.filename) as f:
        line = f.readlines()[-1]
        for attr in price.attrs:
            assert str(price[attr]) in line
    prices = crypto.get_prices()
    prices_list = [_ for _ in prices]
    assert len(prices_list) > 0
    assert isinstance(prices_list[0], Price)
    try:
        for p in prices:
            p._validate()
    except Exception:
        assert False, "Invalid Price"


def test_crypto_all(data_directory_):
    Crypto.update(data_directory_)
    all_ = Crypto.all(data_directory_)
    assert len(all_) > 0
    assert isinstance(all_[0], Crypto)
    assert "btc" in [c.symbol for c in all_]
    assert "win" in [c.symbol for c in all_]
    assert "doge" in [c.symbol for c in all_]
