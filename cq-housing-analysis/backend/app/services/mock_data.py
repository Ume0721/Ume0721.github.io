import random
import uuid
from datetime import datetime, timedelta

DISTRICTS = {
    "渝中区": {"price_range": (12000, 25000), "area_range": (40, 150)},
    "江北区": {"price_range": (10000, 22000), "area_range": (50, 160)},
    "南岸区": {"price_range": (9000, 20000), "area_range": (50, 170)},
    "渝北区": {"price_range": (8000, 18000), "area_range": (60, 180)},
    "沙坪坝区": {"price_range": (9000, 19000), "area_range": (50, 160)},
    "九龙坡区": {"price_range": (7000, 16000), "area_range": (50, 170)},
    "两江新区": {"price_range": (9000, 20000), "area_range": (60, 200)},
    "高新区": {"price_range": (8000, 18000), "area_range": (60, 180)},
}

COMMUNITIES = ["融创欧麓花园城", "龙湖两江新宸", "保利观澜", "万科城", "恒大中央广场"]
LAYOUTS = ["1室1厅", "2室1厅", "2室2厅", "3室1厅", "3室2厅", "4室2厅"]
DECORATIONS = ["毛坯", "简装", "精装", "豪装"]
ORIENTATIONS = ["南", "南北", "东南", "西南", "东", "西", "北"]
FLOORS = ["低楼层", "中楼层", "高楼层"]


def generate_mock_records(count: int = 10000) -> list[dict]:
    records: list[dict] = []
    districts = list(DISTRICTS.keys())
    now = datetime.now()

    for _ in range(count):
        district = random.choice(districts)
        cfg = DISTRICTS[district]

        unit_price = random.uniform(*cfg["price_range"])
        area = random.uniform(*cfg["area_range"])
        total_price = round(unit_price * area / 10000, 2)

        crawled_at = now - timedelta(days=random.randint(0, 90))

        records.append(
            {
                "source": "mock",
                "source_id": f"cq{uuid.uuid4().hex[:12]}",
                "title": f"{district}{random.choice(COMMUNITIES)}{random.choice(LAYOUTS)}",
                "district": district,
                "community": random.choice(COMMUNITIES),
                "total_price": round(total_price, 2),
                "unit_price": round(unit_price, 2),
                "area": round(area, 2),
                "layout": random.choice(LAYOUTS),
                "floor": random.choice(FLOORS),
                "orientation": random.choice(ORIENTATIONS),
                "decoration": random.choice(DECORATIONS),
                "building_year": random.randint(1998, 2024),
                "tags": "近地铁,电梯房",
                "listing_date": (crawled_at - timedelta(days=random.randint(1, 180))).date(),
                "crawled_at": crawled_at,
            }
        )

    return records
