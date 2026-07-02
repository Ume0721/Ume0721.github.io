import pandas as pd
from sklearn.cluster import KMeans
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error


class HousingAnalyzer:
    @staticmethod
    def district_overview(df: pd.DataFrame) -> list[dict]:
        stats = (
            df.groupby("district")
            .agg(
                count=("id", "size"),
                avg_total_price=("total_price", "mean"),
                avg_unit_price=("unit_price", "mean"),
                avg_area=("area", "mean"),
            )
            .round(2)
            .reset_index()
        )
        return stats.to_dict(orient="records")

    @staticmethod
    def price_prediction(df: pd.DataFrame) -> dict:
        features = ["area", "district", "layout", "decoration", "building_year"]
        target = "total_price"

        work_df = df[features + [target]].dropna().copy()
        if len(work_df) < 100:
            return {"error": "数据量不足，至少需要 100 条完整数据"}

        for col in ["district", "layout", "decoration"]:
            le = LabelEncoder()
            work_df[col] = le.fit_transform(work_df[col].astype(str))

        X = work_df[features].values
        y = work_df[target].values

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = GradientBoostingRegressor(n_estimators=200, max_depth=6, learning_rate=0.1, random_state=42)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        return {
            "r2_score": round(float(r2_score(y_test, y_pred)), 4),
            "mae": round(float(mean_absolute_error(y_test, y_pred)), 4),
            "train_samples": len(X_train),
            "test_samples": len(X_test),
            "feature_importance": dict(zip(features, model.feature_importances_.round(4).tolist())),
        }

    @staticmethod
    def kmeans_clustering(df: pd.DataFrame, n_clusters: int = 5) -> dict:
        cluster_df = df[["unit_price", "area"]].dropna().copy()
        if len(cluster_df) < n_clusters * 10:
            return {"error": "数据量不足"}

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(cluster_df)

        kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
        cluster_df["cluster"] = kmeans.fit_predict(X_scaled)

        summary = (
            cluster_df.groupby("cluster")
            .agg(count=("unit_price", "size"), avg_unit_price=("unit_price", "mean"), avg_area=("area", "mean"))
            .round(2)
            .reset_index()
        )

        return {
            "clusters": summary.to_dict(orient="records"),
            "scatter_data": cluster_df.sample(min(2000, len(cluster_df))).to_dict(orient="records"),
        }

    @staticmethod
    def correlation_analysis(df: pd.DataFrame) -> dict:
        num_cols = ["total_price", "unit_price", "area", "building_year"]
        corr_df = df[num_cols].dropna()
        if len(corr_df) < 50:
            return {"error": "数据量不足"}

        corr_matrix = corr_df.corr().round(4)
        return {"columns": num_cols, "matrix": corr_matrix.values.tolist()}
