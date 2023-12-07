from datetime import datetime
from sgp4.earth_gravity import wgs84
from sgp4.io import twoline2rv

def calculate_azimuth_elevation(observer_lat, observer_lon, observer_alt, tle_line1, tle_line2):
    # Gözlemci konumu
    observer = ephem.Observer()
    observer.lat = str(observer_lat)
    observer.lon = str(observer_lon)
    observer.elev = observer_alt

    # TLE objesi oluşturma
    satellite = twoline2rv(tle_line1, tle_line2, wgs84)

    # Şu anki tarih ve saat
    now = datetime.utcnow()

    # Uydu pozisyonunu hesaplama
    position, velocity = satellite.propagate(now.year, now.month, now.day, now.hour, now.minute, now.second)

    # Gözlemcinin uyduya olan açısı
    topocentric = observer.compute(observer)
    azimuth = math.degrees(topocentric.az)
    elevation = math.degrees(topocentric.alt)

    return azimuth, elevation

def main():
    # TLE parametreleri
    line1 = "ISS (ZARYA)"
    line2 = "1 25544U 98067A   21292.47037037  .00000725  00000+0  24610-4 0  9992"
    line3 = "2 25544  51.6416 289.5233 0007985   5.6366  82.6783 15.48811595504709"

    # Gözlemci konumu (örneğin, İstanbul için)
    observer_lat = 41.0082
    observer_lon = 28.9784
    observer_alt = 100  # Gözlemcinin yüksekliği (metre cinsinden)

    # Yönelim hesaplamaları
    azimuth, elevation = calculate_azimuth_elevation(observer_lat, observer_lon, observer_alt, line1, line2)

    print(f"Uydu Yönelimi: Azimuth={azimuth}, Elevation={elevation}")

if __name__ == "__main__":
    main()
