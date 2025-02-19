import hashlib

def generate_hash(timestamp: str, private_key: str, public_key: str) -> str:
    """
    Generate an MD5 hash required for Marvel API authentication.
    
    :param timestamp: Current timestamp as a string
    :param private_key: Marvel private API key
    :param public_key: Marvel public API key
    :return: MD5 hash string
    """
    hash_input = timestamp + private_key + public_key
    return hashlib.md5(hash_input.encode('utf-8')).hexdigest()