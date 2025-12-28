import httpx

class CloudflareClient:
    def __init__(self, token: str):
        self.token = token
        self.http = httpx.Client(
            timeout=10.0,
            headers={"Authorization": f"Bearer {token}"}
        )
        self.base_url = "https://api.cloudflare.com/client/v4"

    def get_dns_record(self, zone_id: str, record_id: str) -> dict:
        response = self.http.get(f"{self.base_url}/zones/{zone_id}/dns_records/{record_id}")
        response.raise_for_status()
        return response.json()["result"]

    def update_dns_record(self, zone_id: str, record_id: str, payload: dict) -> dict:
        response = self.http.patch(f"{self.base_url}/zones/{zone_id}/dns_records/{record_id}", json=payload)
        response.raise_for_status()
        return response.json()["result"]

    def find_record_id(self, zone_id: str, record_name: str, record_type: str) -> Optional[str]:
        response = self.http.get(f"{self.base_url}/zones/{zone_id}/dns_records",
                                 params={"type": record_type, "name": record_name})
        response.raise_for_status()
        records = response.json()["result"]
        for record in records:
            if record["name"] == record_name and record["type"] == record_type:
                return record["id"]
        return None
