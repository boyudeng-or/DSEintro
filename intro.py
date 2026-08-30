# Boyu Deng
# Fun fact: I learned to cook mapo tofu from a roommate during my MSc — still my go-to comfort food after long study days.

"""Small background script for DSE511 Virtual Index Card."""

import math
from typing import Iterable


def haversine_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Great-circle distance in km between two WGS84 points."""
    r = 6371.0
    p = math.pi / 180.0
    dlat = (lat2 - lat1) * p
    dlon = (lon2 - lon1) * p
    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1 * p) * math.cos(lat2 * p) * math.sin(dlon / 2) ** 2
    )
    return 2 * r * math.asin(math.sqrt(a))


# Four-stop academic path: hometown -> undergrad -> MSc -> PhD
PLACES: Iterable[tuple[str, float, float]] = (
    ("Huludao, CN (hometown)", 40.711, 120.837),
    ("Jinan University, Guangzhou (undergrad)", 23.129, 113.348),
    ("CUHK, Hong Kong (MSc Math)", 22.419, 114.206),
    ("UTK ISE, Knoxville, TN (PhD)", 35.961, -83.926),
)


def main() -> None:
    stops = tuple(PLACES)
    print("Boyu Deng — four-stop academic path (km per leg):\n")

    segments: list[float] = []
    for i in range(len(stops) - 1):
        origin, destination = stops[i], stops[i + 1]
        km = haversine_km(origin[1], origin[2], destination[1], destination[2])
        segments.append(km)
        print(f"  {origin[0]} -> {destination[0]}: {km:,.0f} km")

    print(f"\nMean hop length ({len(segments)} segments): {sum(segments) / len(segments):,.0f} km")


if __name__ == "__main__":
    main()
