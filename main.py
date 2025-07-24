import time
import requests

url = "https://www.mcserverhost.com/api/servers/e364e533/subscription"

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6",
    "Connection": "keep-alive",
    "Content-Length": "0",
    "Cookie":
    "_ga=GA1.1.396852822.1753345015; twk_idm_key=SgKxgQM8fi9BelpDcqIMl; __stripe_mid=76036b5d-70ec-495f-933b-a146936c2d0d983e37; __stripe_sid=183bbe2c-d2af-43fb-bb54-98fe75dfe5a8f2bc4f; mcserverhost=875f1acd-463a-4aed-8e1e-70ee844e53ff; _ga_SRYKCFQGK0=GS2.1.s1753345015$o1$g1$t1753347642$j60$l0$h0; TawkConnectionTime=0; twk_uuid_674201982480f5b4f5a2f121=%7B%22uuid%22%3A%221.2Bj68KxR4FdR0tI1G8iFEmHUtHOne756Js1ybwzhbEq45hpZz3PpLqXUjGXHwe40yOpVkShBydKfe4rPytlZvrlDSsx1azHgDPX23KjpQwbxYB53jLqO7C0YEcd%22%2C%22version%22%3A3%2C%22domain%22%3A%22mcserverhost.com%22%2C%22ts%22%3A1753347644433%7D",
    "Host": "www.mcserverhost.com",
    "Origin": "https://www.mcserverhost.com",
    "Referer": "https://www.mcserverhost.com/servers/e364e533/dashboard",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua":
    '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"'
}

while True:
    try:
        r = requests.post(url, headers=headers)
        if r.status_code == 200:
            print("✅ Renew thành công!")
        else:
            print(f"❌ Lỗi: {r.status_code} | {r.text}")

        time.sleep(1)  # đợi 1 giờ mới bấm tiếp

    except Exception as e:
        print("❌ Exception:", e)
        time.sleep(1)
