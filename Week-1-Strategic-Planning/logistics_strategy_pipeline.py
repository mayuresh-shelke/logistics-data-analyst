"""
Logistics Data Analysis & Route Optimization Strategy
Module: Week 1 Strategic Planning & Exploratory Pipeline
Author: Mayuresh (Logistics Data Analyst Intern)
"""

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


# ==============================================================================
# STEP 1: SYNTHETIC DATA INGESTION & FEATURE SIMULATION
# ==============================================================================
def generate_logistics_data(n_samples: int = 1500, random_seed: int = 42):
    """Simulates realistic metropolitan last-mile delivery order data."""
    np.random.seed(random_seed)

    # Geographic coordinates (Simulating a dense metropolitan area)
    latitude = np.random.uniform(18.90, 19.25, n_samples)
    longitude = np.random.uniform(72.80, 73.05, n_samples)

    # Operational metrics
    transit_distance_km = np.random.uniform(1.5, 30.0, n_samples)
    traffic_density_index = np.random.uniform(
        1.0, 10.0, n_samples
    )  # 1 = clear, 10 = gridlock
    weather_severity_score = np.random.choice(
        [0, 1, 2, 3], p=[0.60, 0.25, 0.10, 0.05], size=n_samples
    )  # 0: Clear, 3: Storm
    package_weight_kg = np.random.uniform(0.5, 25.0, n_samples)
    num_parcels = np.random.randint(1, 6, n_samples)
    hour_of_day = np.random.randint(8, 20, n_samples)

    # True delivery duration calculation with non-linear real-world noise
    base_speed_kmh = 24.0  # Urban average speed
    transit_time_minutes = (transit_distance_km / base_speed_kmh) * 60

    delay_penalty = (
        (traffic_density_index * 3.2)
        + (weather_severity_score * 8.5)
        + (package_weight_kg * 0.4)
        + (num_parcels * 2.1)
    )

    noise = np.random.normal(0, 3.5, n_samples)
    actual_delivery_time_min = np.maximum(
        10.0, transit_time_minutes + delay_penalty + noise
    )

    df = pd.DataFrame(
        {
            "order_id": [f"ORD_{i:05d}" for i in range(1, n_samples + 1)],
            "dest_latitude": latitude,
            "dest_longitude": longitude,
            "transit_distance_km": np.round(transit_distance_km, 2),
            "traffic_density_index": np.round(traffic_density_index, 2),
            "weather_severity_score": weather_severity_score,
            "package_weight_kg": np.round(package_weight_kg, 2),
            "num_parcels": num_parcels,
            "hour_of_day": hour_of_day,
            "actual_delivery_time_min": np.round(actual_delivery_time_min, 2),
        }
    )

    return df


# ==============================================================================
# STEP 2: UNSUPERVISED SPATIAL CLUSTERING (DISPATCH ZONING)
# ==============================================================================
def create_delivery_clusters(df: pd.DataFrame, num_vehicles: int = 6):
    """Clusters delivery locations into balanced micro-zones using K-Means."""
    coords = df[["dest_latitude", "dest_longitude"]]
    kmeans = KMeans(n_clusters=num_vehicles, random_state=42, n_init=10)
    df["assigned_zone_cluster"] = kmeans.fit_predict(coords)
    return df, kmeans


# ==============================================================================
# STEP 3: PREDICTIVE MODELING FOR DELIVERY DURATION (ETA)
# ==============================================================================
def train_eta_predictor(df: pd.DataFrame):
    """Trains a Random Forest Regressor to predict actual delivery duration."""
    features = [
        "transit_distance_km",
        "traffic_density_index",
        "weather_severity_score",
        "package_weight_kg",
        "num_parcels",
        "hour_of_day",
        "assigned_zone_cluster",
    ]
    target = "actual_delivery_time_min"

    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=150, max_depth=12, random_state=42, n_jobs=-1
    )
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    r2 = r2_score(y_test, predictions)

    print("================ MODEL EVALUATION ================")
    print(f"Mean Absolute Error (MAE):     {mae:.2f} minutes")
    print(f"Root Mean Squared Error (RMSE): {rmse:.2f} minutes")
    print(f"R-Squared Score (R2):          {r2:.4f}")
    print("==================================================")

    # Feature Importance Analysis
    importances = pd.Series(model.feature_importances_, index=features)
    print("\nFeature Importances:")
    print(importances.sort_values(ascending=False))

    return model


# ==============================================================================
# STEP 4: ROUTE OPTIMIZATION OUTLINE (PSEUDOCODE CONCEPT)
# ==============================================================================
def route_sequencing_pseudocode():
    """
    Conceptual pseudocode illustrating how stop sequencing will be executed
    using distance matrix formulations and Google OR-Tools.
    """
    pseudocode = """
    ALGORITHM: OptimizeDeliveryRoute(ClusterLocations, VehicleCapacity, HubLocation):
        1. Initialize Graph G = (V, E) where V = {HubLocation} U {ClusterLocations}
        2. Construct Distance Matrix D[i][j] representing true road network travel times.
        3. Define Constraints:
            a. Each customer stop must be visited exactly once.
            b. Sum of parcel weights on vehicle <= VehicleCapacity.
            c. Delivery time must satisfy Customer Time Windows (TW_start, TW_end).
        4. Objective Function:
            Minimize Total Cost = SUM(D[i][j] * DistanceWeight + Penalty(LateDelivery))
        5. Solve using Guided Local Search / Tabu Search heuristics via OR-Tools.
        6. Return Ordered Sequence of Waypoints: [Hub -> Stop_k -> Stop_m -> ... -> Hub]
    """
    print(pseudocode)


# ==============================================================================
# EXECUTION ENTRY POINT
# ==============================================================================
if __name__ == "__main__":
    print("[1/4] Simulating Logistics Dataset...")
    logistics_data = generate_logistics_data(n_samples=1500)
    print(f"Generated {len(logistics_data)} records successfully.\n")

    print("[2/4] Clustering Deliveries into 6 Geographic Vehicle Zones...")
    clustered_data, cluster_model = create_delivery_clusters(
        logistics_data, num_vehicles=6
    )
    print(clustered_data["assigned_zone_cluster"].value_counts().sort_index())
    print("\n[3/4] Training Predictive ETA Model...")
    trained_model = train_eta_predictor(clustered_data)

    print("\n[4/4] Strategic Route Sequencing Framework:")
    route_sequencing_pseudocode()
