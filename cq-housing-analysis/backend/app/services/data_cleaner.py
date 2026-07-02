import re
import pandas as pd


class DataCleaner:
    VALID_DISTRICTS = [
        "渝中区", "江北区", "南岸区", "渝北区", "沙坪坝区", "九龙坡区",
        "大渡口区", "巴南区", "北碚区", "璧山区", "合川区", "永川区",
        "长寿区", "涪陵区", "万州区", "开州区", "两江新区", "高新区",
    ]

    @staticmethod
    def clean_price(raw) -> float | None:
        if raw is None or raw == "":
            return None
        nums = re.findall(r"[\\d.]+", str(raw))
        if not nums:
            return None
        value = float(nums[0])
        return value if 0 < value < 100000 else None

    @staticmethod
    def clean_area(raw) -> float | None:
        if raw is None or raw == "":
            return None
        nums = re.findall(r"[\\d.]+", str(raw))
        if not nums:
            return None
        value = float(nums[0])
        return value if 0 < value < 10000 else None

    @classmethod
    def clean_dataframe(cls, df: pd.DataFrame) -> pd.DataFrame:
        if df.empty:
            return df

        if "source" in df.columns and "source_id" in df.columns:
            df = df.drop_duplicates(subset=["source", "source_id"], keep="last")

        if "total_price" in df.columns:
            df["total_price"] = df["total_price"].apply(cls.clean_price)
        if "unit_price" in df.columns:
            df["unit_price"] = df["unit_price"].apply(cls.clean_price)
        if "area" in df.columns:
            df["area"] = df["area"].apply(cls.clean_area)
        if "district" in df.columns:
            df = df[df["district"].isin(cls.VALID_DISTRICTS)]

        if "unit_price" in df.columns and "area" in df.columns and "total_price" in df.columns:
            mask = df["unit_price"].isna() & df["area"].notna() & (df["area"] > 0)
            df.loc[mask, "unit_price"] = (df.loc[mask, "total_price"] * 10000 / df.loc[mask, "area"]).round(2)

        return df.reset_index(drop=True)
