import httpx


class IPController:
    def __init__(self, ipv4_url: str, ipv6_url: str):
        self.ipv4_url = ipv4_url
        self.ipv6_url = ipv6_url

    def get_ip(self, prefer: str, fallback: str) -> str:
        try:
            return self.fetch_ip(self.ipv4_url if prefer == "ipv4" else self.ipv6_url)
        except Exception:
            return self.fetch_ip(self.ipv4_url if fallback == "ipv4" else self.ipv6_url)

    def fetch_ip(self, url: str) -> str:
        response = httpx.get(url, timeout=5)
        response.raise_for_status()
        return response.text.strip()

