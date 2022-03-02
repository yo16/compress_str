"""ハッシュ化してその文字列をzip圧縮する
"""

import io
from sys import byteorder
import zipfile

from hashing import do_hashing


def do_compress(str_hex:str)->str:
    """文字列の16進数をバイナリ値にそのまま変換し、zip圧縮して返す

    Args:
        str_hex (str): 16進数の文字列(先頭にbはない)

    Returns:
        str: zip圧縮したバイナリ値を16進数にした文字列
    """
    ret = ''
    
    # 16進数文字列をそのままバイナリ化
    b = bytes.fromhex(str_hex)
    
    # バイナリをzip化
    zip_stream = io.BytesIO()
    with zipfile.ZipFile(zip_stream, 'w', compression=zipfile.ZIP_DEFLATED) as new_zip:
        new_zip.writestr('_', b)
    
    # zipしたバイナリ値をそのまま取得
    h = zip_stream.getvalue()

    # 16進数にして返す
    return h.hex()


if __name__=='__main__':
    test_str = 'test123'
    ret = do_hashing(test_str, ret_type='Hex', hash_method='SHA3_512')
    print(ret)
    print(f'{len(ret)/2} bytes')        # 16進数1文字=4bit=0.5byte
    
    ret2 = do_compress(ret)
    print(ret2)
    print(f'{len(ret2)/2} bytes')
