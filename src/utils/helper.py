from datetime import timedelta, datetime
import string
import secrets
import hmac
import hashlib
import json
import os
import base64
import re
from fuzzywuzzy import fuzz
import requests
from datetime import datetime
import json


def remove_multiple_keys(dictionary: dict, keys_to_remove: list):
    [dictionary.pop(key, None) for key in keys_to_remove]


def replace_elements(array: list, value: dict, prop: str):
    for i, element in enumerate(array):
        if element.get(prop) == value.get(prop):
            array[i] = value


def hiden_document(document):
    # Remova caracteres não numéricos
    if not document:
        return
    number = "".join(filter(str.isdigit, document))

    if len(number) == 11:
        # Para CPF, substitua os dígitos não centrais por '*'
        return number[:3] + "*" * 4 + number[7:]
    elif len(number) == 14:
        # Para CNPJ, substitua os dígitos não centrais por '*'
        return number[:5] + "*" * 4 + number[9:]
    else:
        # Trate outros casos ou retorne None se o formato não for reconhecido
        return


def generate_random_key(length):
    alphabet = (
        string.ascii_letters + string.digits
    )  # Alfabeto de letras maiúsculas, minúsculas e dígitos
    random_key = "".join(secrets.choice(alphabet) for _ in range(length))
    return random_key


def add_days(data: datetime, day_to_add: int) -> datetime:
    try:
        new_date = data + timedelta(days=day_to_add)
        return new_date
    except Exception as ex:
        raise ex


def fuzziwuzzy_search(string_one: str, string_two: str, percent: float = 80) -> bool:
    try:
        result = fuzz.ratio(string_one, string_two) >= percent
        return result
    except Exception as ex:
        raise ex


def verify_signature(secret_key: str, headers: dict, payload: dict) -> bool:
    # Converta payload para string antes de calcular a hash
    payload_str = json.dumps(payload, separators=(",", ":"), sort_keys=True)

    # Certifique-se de que todos os dados estejam em bytes
    nonce = str(headers.get("nonce")).encode()
    timestamp = str(headers.get("timestamp")).encode()
    secret_key_bytes = secret_key.encode()
    payload_bytes = payload_str.encode()

    # Crie a string a ser hashada
    pre_hash_string = b"&".join([nonce, timestamp, payload_bytes])

    # Calcule a assinatura
    calculated_signature = hmac.new(
        secret_key_bytes, pre_hash_string, hashlib.sha256
    ).hexdigest()

    # Compare as assinaturas de forma segura
    if hmac.compare_digest(calculated_signature, headers.get("x-signature")):
        return True
    else:
        return False


def distinct_by_property(data, prop):
    unique_items = []
    seen_values = set()

    for item in data:
        if item.get(prop) not in seen_values:
            seen_values.add(item.get(prop))
            unique_items.append(item)

    return unique_items


def generate_random_hash(lenght=5):
    """Generate random base64 hash."""
    random_bytes = os.urandom(lenght)
    base64_string = base64.b64encode(random_bytes).decode("utf-8")[:lenght]
    return base64_string


def download_file(url: str) -> bytes:
    """Download files."""
    response = requests.get(url)
    returned = None
    if response.status_code not in [200, 201]:
        returned = None
    try:
        returned = base64.b64decode(response.content)
    except Exception as ex:
        returned = None

    return returned

def clear_value(value):
    """Remove all caracters not numerics"""
    clear_value = re.sub(r"\D", "", value)
    return clear_value


def remove_null_values_dict(data: dict):
    """Remove all values None."""
    response = {}
    for each in data.keys():
        if data.get(each):
            response[each] = data.get(each)
    return response


def verify_keys(keys: list, data: dict):
    """Validate keys not null."""
    dict_keys = list(data.keys())
    for each in keys:
        if not each in dict_keys or not data.get(each):
            return None
    return True


def remove_formatting(document):
    document = document.replace(".", "").replace("-", "")
    document = document.replace(".", "").replace("-", "").replace("/", "")
    return document





def converter_to_timestamp(data_string: str):
    try:
        data_hora = datetime.strptime(data_string, "%Y-%m-%dT%H:%M:%S")
    except:
        pass

    try:
        data_hora = datetime.strptime(data_string, "%d-%m-%YT%H:%M:%S")
    except Exception as ex:
        raise Exception(str(ex))
    return int(data_hora.timestamp())


def filter_process(encode_filter: str):
    try:
        decode_filter = json.loads(encode_filter)
        if type(decode_filter) != dict:
            decode_filter = json.loads(decode_filter)
        if not len(list(decode_filter.keys())):
            return {}
        if decode_filter.get("order") not in ["dcs", "asc"]:
            decode_filter["order"] = "dsc"
        query = {"order": decode_filter.get("order")}
        keys = {}
        for each in decode_filter.get("fields"):
            value = each.get("value")
            if each.get("operator") == "range":
                if len(each.get("value")) != 2:
                    keys.update({f'{each.get("key")}__in': value})
                elif each.get("type") == "datetime":
                    timestamps = list(map(converter_to_timestamp, value))
                    keys.update({f'{each.get("key")}__range': timestamps})
                elif each.get("type") == "string":
                    keys.update({f'{each.get("key")}__range': value})
            if each.get("key") in ["document", "phone"] and each.get("operator") != "range":
                keys.update({f'{each.get("key")}__contains': clear_value(value)})

            elif each.get("operator") == "<":
                keys.update({f'{each.get("key")}__lt': value})
            elif each.get("operator") == ">=":
                pass
            elif each.get("operator") == "<=":
                pass
            elif each.get("operator") == ">":
                keys.update({f'{each.get("key")}__gt': value})
            elif each.get("operator") == "==":
                keys.update({f'{each.get("key")}': value})
        query["keys"] = keys
        return query
    except Exception as e:
        raise Exception("Error in filter process")


def order_list(
    data_list: list, props: dict = {}, date_converted: bool = False, revert: bool = True
):
    """Order list by key and operator."""
    if not data_list:
        return []
    if not date_converted:
        ordened_list = sorted(
            data_list,
            key=lambda item: datetime.fromtimestamp(item.get("created_at")),
            reverse=props.get("order") != "asc",
        )
    else:
        ordened_list = sorted(
            data_list,
            key=lambda item: item.get("created_at"),
            reverse=props.get("order") != "asc" and not revert,
        )
    return ordened_list
