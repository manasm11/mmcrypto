# mmcrypto

Python package get and save crypto data from wazirx.

```py
pip3 install mmcrypto
python3
>>> from mmcrypto import Crypto
>>> directory_to_save_data = '/home/user/data/'
>>> Crypto.update(directory_to_save_data)
>>> Crypto.all()
>>> crypto = Crypto('btc', directory_to_save_data)
>>> crypto.get_prices()
>>> 


```
