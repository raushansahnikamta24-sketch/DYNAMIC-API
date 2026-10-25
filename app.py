import os
import sys
import time
import json
import threading
import requests
import urllib3
import httpx
import SpecialFriend_pb2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
from google.protobuf import json_format
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
from google.protobuf.message import Message

urllib3.disable_warnings()

GUEST_UID = "4785573108"
GUEST_PASSWORD = "ADI-33FO9W0B"

AeSkEy = b'Yg&tc%DEuh6%Zc^8'
AeSiV  = b'6oyZDr22E3ychjM%'
BASE_URL = "https://client.ind.freefiremobile.com"

_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC, 6, 30, 0, "", "FreeFire.proto",
)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0e\x46reeFire.proto"c\n\x08LoginReq\x12\x0f\n\x07open_id\x18\x16 \x01(\t'
    b'\x12\x14\n\x0copen_id_type\x18\x17 \x01(\t\x12\x13\n\x0blogin_token\x18\x1d '
    b'\x01(\t\x12\x1b\n\x13orign_platform_type\x18\x63 \x01(\t"]\n\x10\x42lacklist'
    b'InfoRes\x12\x1e\n\nban_reason\x18\x01 \x01(\x0e\x32\n.BanReason\x12\x17\n'
    b'\x0f\x65xpire_duration\x18\x02 \x01(\r\x12\x10\n\x08\x62\x61n_time\x18\x03 '
    b'\x01(\r"f\n\x0eLoginQueueInfo\x12\r\n\x05\x61llow\x18\x01 \x01(\x08\x12'
    b'\x16\n\x0equeue_position\x18\x02 \x01(\r\x12\x16\n\x0eneed_wait_secs\x18'
    b'\x03 \x01(\r\x12\x15\n\rqueue_is_full\x18\x04 \x01(\x08"\xa0\x03\n\x08'
    b'LoginRes\x12\x12\n\naccount_id\x18\x01 \x01(\x04\x12\x13\n\x0block_region'
    b'\x18\x02 \x01(\t\x12\x13\n\x0bnoti_region\x18\x03 \x01(\t\x12\x11\n\tip_'
    b'region\x18\x04 \x01(\t\x12\x19\n\x11\x61gora_environment\x18\x05 \x01(\t'
    b'\x12\x19\n\x11new_active_region\x18\x06 \x01(\t\x12\x19\n\x11recommend_'
    b'regions\x18\x07 \x03(\t\x12\r\n\x05token\x18\x08 \x01(\t\x12\x0b\n\x03ttl'
    b'\x18\t \x01(\r\x12\x12\n\nserver_url\x18\n \x01(\t\x12\x16\n\x0e\x65mul'
    b'ator_score\x18\x0b \x01(\r\x12$\n\tblacklist\x18\x0c \x01(\x0b\x32\x11.'
    b'BlacklistInfoRes\x12#\n\nqueue_info\x18\r \x01(\x0b\x32\x0f.LoginQueue'
    b'Info\x12\x0e\n\x06tp_url\x18\x0e \x01(\t\x12\x15\n\rapp_server_id\x18'
    b'\x0f \x01(\r\x12\x0f\n\x07\x61no_url\x18\x10 \x01(\t\x12\x0f\n\x07ip_city'
    b'\x18\x11 \x01(\t\x12\x16\n\x0eip_subdivision\x18\x12 \x01(\t*\xa8\x01\n'
    b'\tBanReason\x12\x16\n\x12\x42\x41N_REASON_UNKNOWN\x10\x00\x12\x1b\n\x17'
    b'\x42\x41N_REASON_IN_GAME_AUTO\x10\x01\x12\x15\n\x11\x42\x41N_REASON_'
    b'REFUND\x10\x02\x12\x15\n\x11\x42\x41N_REASON_OTHERS\x10\x03\x12\x16\n'
    b'\x12\x42\x41N_REASON_SKINMOD\x10\x04\x12 \n\x1b\x42\x41N_REASON_IN_GAME'
    b'_AUTO_NEW\x10\xf6\x07\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "FreeFire_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals["_BANREASON"]._serialized_start = 738
    _globals["_BANREASON"]._serialized_end = 906
    _globals["_LOGINREQ"]._serialized_start = 18
    _globals["_LOGINREQ"]._serialized_end = 117
    _globals["_BLACKLISTINFORES"]._serialized_start = 119
    _globals["_BLACKLISTINFORES"]._serialized_end = 212
    _globals["_LOGINQUEUEINFO"]._serialized_start = 214
    _globals["_LOGINQUEUEINFO"]._serialized_end = 316
    _globals["_LOGINRES"]._serialized_start = 319
    _globals["_LOGINRES"]._serialized_end = 735

LoginReq = _globals["LoginReq"]
LoginRes = _globals["LoginRes"]

MAIN_KEY = base64.b64decode("WWcmdGMlREV1aDYlWmNeOA==")
MAIN_IV = base64.b64decode("Nm95WkRyMjJFM3ljaGpNJQ==")
RELEASEVERSION = "OB55"
USERAGENT = "UnityPlayer/2018.4.12f1 (UnityWebRequest/1.0, libcurl/8.5.0-DEV)"
LOGIN_URL = "https://loginbp.ppmainecoonghj.com/"

HTTP_LIMITS = httpx.Limits(max_keepalive_connections=20, max_connections=50)
HTTP_TIMEOUT = httpx.Timeout(15.0, connect=5.0)
_http_client = httpx.Client(limits=HTTP_LIMITS, timeout=HTTP_TIMEOUT, verify=False)

C = "\033[1;36m"
G = "\033[1;32m"
R = "\033[1;31m"
Y = "\033[1;33m"
W = "\033[1;37m"
B = "\033[1m"
S = "\033[0m"

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def draw_line():
    print(f"{C}═══════════════════════════════════════════════════════════{S}")

def banner():
    clear()
    ascii_art = f"""{C}
    ███████╗ ██████╗  ██╗ ██████╗  ███████╗ ██╗   ██╗
    ██╔════╝ ██╔══██╗ ██║ ██╔══██╗ ██╔════╝ ╚██╗ ██╔╝
    ███████╗ ██████╔╝ ██║ ██║  ██║ █████╗    ╚████╔╝ 
    ╚════██║ ██╔═══╝  ██║ ██║  ██║ ██╔══╝     ╚██╔╝  
    ███████║ ██║      ██║ ██████╔╝ ███████╗    ██║   
    ╚══════╝ ╚═╝      ╚═╝ ╚═════╝  ╚══════╝    ╚═╝   {S}"""
    print(ascii_art) 
    draw_line()
    print(f"{W}{B}               FF DYNAMIC DUO INFO EXTRACTOR{S}")
    draw_line()

def show_credits():
    draw_line()
    print(f"\n {C}[★] {W}Developer : {C}@spideyabd{S}")
    print(f" {C}[★] {W}Join      : {G}t.me/SPIDEYFREEFILES{S}")
    print(f" {C}[★] {W}Join      : {G}t.me/SPIDEYFREEAPI{S}\n")

def enc(d):
    return AES.new(AeSkEy, AES.MODE_CBC, AeSiV).encrypt(pad(d, 16))

def dec(d):
    try:
        return unpad(AES.new(AeSkEy, AES.MODE_CBC, AeSiV).decrypt(d), 16)
    except:
        return d

def pad_key(text):
    padding_length = AES.block_size - (len(text) % AES.block_size)
    return text + bytes([padding_length] * padding_length)

def aes_cbc_encrypt(key, iv, plaintext):
    return AES.new(key, AES.MODE_CBC, iv).encrypt(pad_key(plaintext))

def build_uid_protobuf(uid):
    def to_varint(n):
        res = bytearray()
        while n >= 0x80:
            res.append((n & 0x7f) | 0x80)
            n >>= 7
        res.append(n)
        return bytes(res)
    return enc(b"\x08" + to_varint(int(uid)))

def format_timestamp(ts):
    try:
        return time.strftime('%B %d, %Y at %I:%M %p', time.localtime(ts))
    except (ValueError, TypeError):
        return "Invalid Timestamp"

def json_to_proto(json_data, proto_message):
    json_format.ParseDict(json.loads(json_data), proto_message)
    return proto_message.SerializeToString()

def try_parse_login_res(data):
    try:
        msg = LoginRes()
        msg.ParseFromString(data)
        if msg.account_id and msg.account_id > 0:
            return json.loads(json_format.MessageToJson(msg))
    except Exception:
        pass
    return None

def extract_login_res(raw):
    parsed = try_parse_login_res(raw)
    if parsed:
        return parsed
    idx = 0
    while True:
        idx = raw.find(b"\x08", idx)
        if idx == -1:
            break
        parsed = try_parse_login_res(raw[idx:])
        if parsed:
            return parsed
        idx += 1
    jwt_marker = raw.find(b"eyJhbGciOiJIUzI1NiIs")
    if jwt_marker != -1:
        for i in range(jwt_marker - 1, max(jwt_marker - 300, -1), -1):
            if raw[i] == 0x42:
                parsed = try_parse_login_res(raw[i:])
                if parsed:
                    return parsed
                break
    return None

def get_access_token(uid, password):
    url = "https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant"
    payload = (
        f"uid={uid}&password={password}"
        "&response_type=token&client_type=2"
        "&client_secret=2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3"
        "&client_id=100067"
    )
    headers = {
        "User-Agent": USERAGENT,
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    try:
        resp = _http_client.post(url, data=payload, headers=headers)
        data = resp.json()
        return data.get("access_token", "0"), data.get("open_id", "0")
    except Exception:
        return "0", "0"

def perform_login(access_token, open_id, open_id_type="4", orign_platform_type="4"):
    body = json.dumps({
        "open_id": open_id,
        "open_id_type": open_id_type,
        "login_token": access_token,
        "orign_platform_type": orign_platform_type,
    })
    proto_bytes = json_to_proto(body, LoginReq())
    payload = aes_cbc_encrypt(MAIN_KEY, MAIN_IV, proto_bytes)
    headers = {
        "User-Agent": USERAGENT,
        "Accept": "*/*",
        "Accept-Encoding": "deflate, gzip",
        "X-Ga-Sv": "1789534056",
        "Authorization": "Bearer",
        "X-Ga": "v1 1",
        "Releaseversion": RELEASEVERSION,
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Unity-Version": "2018.4.12f1",
        "PlAy_VeR": "1.132.1",
        "Ob_VeR": RELEASEVERSION,
    }
    try:
        resp = _http_client.post(f"{LOGIN_URL}MajorLogin", data=payload, headers=headers)
        return extract_login_res(resp.content)
    except Exception:
        return None

def fetch_jwt_token():
    access_token, open_id = get_access_token(GUEST_UID, GUEST_PASSWORD)
    if access_token == "0" or open_id == "0":
        return None
    msg = perform_login(access_token, open_id, "4", "4")
    if not msg:
        return None
    return msg.get("token")

def decode_protobuf_data(binary_data):
    try:
        if not binary_data or len(binary_data) < 2:
            return None, "Empty Response"

        response = SpecialFriend_pb2.SpecialFriendResponse()
        response.ParseFromString(binary_data)

        if not response.HasField("duo_info"):
            return None, "No Dynamic Duo info found"

        duo = response.duo_info
        score = duo.score

        if score < 101: calc_level = 1
        elif score < 301: calc_level = 2
        elif score < 501: calc_level = 3
        elif score < 801: calc_level = 4
        elif score < 1201: calc_level = 5
        else: calc_level = 6

        calc_status = "Active" if getattr(duo, "status", 0) == 2 else "Inactive"

        result = {
            "partner_uid": str(duo.partner_uid),
            "level": calc_level,
            "score": score,
            "days_active": duo.days_active,
            "time_created": format_timestamp(duo.creation_timestamp),
            "creation_timestamp": duo.creation_timestamp,
            "status": calc_status
        }
        return result, "Success"
    except Exception as e:
        return None, f"Parsing Error: {str(e)}"



from flask import Flask, jsonify, request

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({
        "status": "online",
        "name": "Dynamic Duo API",
        "usage": "/api/duo?uid=PLAYER_UID"
    })

@app.get("/api/duo")
def duo_api():
    target_uid = (request.args.get("uid") or "").strip()
    if not target_uid or not target_uid.isdigit():
        return jsonify({
            "success": False,
            "error": "A numeric uid query parameter is required.",
            "example": "/api/duo?uid=123456789"
        }), 400

    # Optional API-key protection: set API_KEY in Vercel Environment Variables.
    expected_key = os.environ.get("API_KEY", "").strip()
    if expected_key:
        supplied_key = (
            request.headers.get("X-API-Key", "")
            or request.args.get("key", "")
        ).strip()
        if supplied_key != expected_key:
            return jsonify({"success": False, "error": "Invalid or missing API key."}), 401

    try:
        jwt = fetch_jwt_token()
        if not jwt:
            return jsonify({
                "success": False,
                "error": "Could not generate an upstream token. Check guest credentials and upstream service."
            }), 502

        headers = {
            "Authorization": f"Bearer {jwt}",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11)",
            "X-GA": "v1 1",
            "ReleaseVersion": "OB55",
            "Connection": "Keep-Alive"
        }
        payload = build_uid_protobuf(target_uid)
        upstream = requests.post(
            f"{BASE_URL}/GetSpecialFriendList",
            headers=headers,
            data=payload,
            timeout=15,
            verify=False
        )

        if upstream.status_code != 200:
            return jsonify({
                "success": False,
                "uid": target_uid,
                "error": "Upstream game service returned an error.",
                "upstream_status": upstream.status_code
            }), 502

        parsed_data, error_msg = decode_protobuf_data(dec(upstream.content))
        if not parsed_data:
            return jsonify({
                "success": False,
                "uid": target_uid,
                "error": error_msg or "No Dynamic Duo data found."
            }), 404

        # The generated JWT/access token is deliberately not exposed in the response.
        return jsonify({"success": True, "uid": target_uid, "data": parsed_data})

    except requests.Timeout:
        return jsonify({"success": False, "error": "Upstream request timed out."}), 504
    except Exception:
        app.logger.exception("Dynamic Duo API request failed")
        return jsonify({"success": False, "error": "Internal server error."}), 500
