import json
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class RecordConfig:
    record_id: Optional[str]
    name: str
    type: str  # A, AAAA, CNAME, MX, NS, PTR, SOA, SRV, TXT
    prefer_ip: str
    fallback_ip: str
    ttl: int
    proxied: bool
    interval_override_seconds: Optional[int] = None


@dataclass
class ZoneConfig:
    name: str
    cloudflare_api_token: str
    zone_id: str
    records: List[RecordConfig]


@dataclass
class GeneralConfig:
    version: int
    interval_seconds: int
    http_timeout_connect: float
    http_timeout_read: float
    http_retries: int
    http_backoff_base: float
    ipify_ipv4_url: str
    ipify_ipv6_url: str
    zones: List[ZoneConfig] = field(default_factory=list)


def load_config(config_path: str = "/etc/nok-dns/config.json") -> GeneralConfig:
    with open(config_path, "r") as f:
        data = json.load(f)

    return GeneralConfig(
        version=data["version"],
        interval_seconds=data["interval_seconds"],
        http_timeout_connect=data["http"]["timeout_connect_seconds"],
        http_timeout_read=data["http"]["timeout_read_seconds"],
        http_retries=data["http"]["retries"],
        http_backoff_base=data["http"]["backoff_base_seconds"],
        ipify_ipv4_url=data["ipify"]["ipv4_url"],
        ipify_ipv6_url=data["ipify"]["ipv6_url"],
        zones=[
            ZoneConfig(
                name=z["name"],
                cloudflare_api_token=z["cloudflare_api_token"],
                zone_id=z["zone_id"],
                records=[
                    RecordConfig(
                        record_id=r.get("record_id"),
                        name=r["name"],
                        type=r["type"],
                        prefer_ip=r["prefer_ip"],
                        fallback_ip=r["fallback_ip"],
                        ttl=r["ttl"],
                        proxied=r["proxied"],
                        interval_override_seconds=r.get("interval_override_seconds"),
                    )
                    for r in z["records"]
                ],
            )
            for z in data["zones"]
        ],
    )

