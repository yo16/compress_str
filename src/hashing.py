"""ハッシュ化

適当なハッシュ値がほしかったので作った。
ハッシュ用ライブラリと、圧縮用ライブラリは区別したかったので
別ファイルにした。
"""
import hashlib
import math

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal
HashingMethod = Literal[
    'SHA256',
    'SHA3_512'
]
ReturnType = Literal[
    'Hexa',  # 16進数
    'Bin'   # 2進数
]


def do_hashing(original_str:str, hash_method:HashingMethod='SHA256', ret_type:ReturnType='Bin') -> str:
    """_summary_

    Args:
        hash_method (HashingMethod): ハッシュ化方法
        original_str (str): ハッシュ化前の文字列
        ret_type (ReturnType): ハッシュ後の文字列の型[Bin:2進数, Hexa:16進数]

    Returns:
        str: ハッシュ化後の文字列
    """
    m = None
    if hash_method=='SHA256':
        m = hashlib.sha256()
    elif hash_method=='SHA3_512':
        m = hashlib.sha3_512()
    
    ret_str = m.hexdigest()
    if ret_type=='Bin':
        # 16進数を2進数へ変換する
        pool_str = ''
        # 桁あふれ対応のため、下から8文字ずつ
        base_len = len(ret_str)
        for i in range(math.ceil(base_len/8)):
            idx_from = (-8)*(i+1)
            idx_to = None
            if i>0:
                idx_to = (-8)*i
            part_str = ret_str[idx_from:idx_to]
            num_10 = int(part_str,16)
            pool_str += format(num_10, '032b')
        ret_str = pool_str
    
    return ret_str


if __name__=='__main__':
    original_str = 'test1'
    
    hash_method: HashingMethod = 'SHA3_512'
    hash_bin = do_hashing(original_str, ret_type='Bin', hash_method=hash_method)
    hash_hex = do_hashing(original_str, ret_type='Hex', hash_method=hash_method)
    
    print(f'original: {original_str}')
    print(f'hash_str: {hash_bin}')
    print(f'hash_str: {hash_hex}')
