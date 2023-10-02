from pydantic import BaseModel, Field
from typing import Optional, Dict, List
from app.proto.camden_pb2 import MapUpdatesRequest, MapBounds, Point as GRPCPoint


class Point(BaseModel):
    lat: float = 0.0
    lng: float = 0.0

    def to_grpc_point(self) -> GRPCPoint:
        return GRPCPoint(lat=self.lat, lng=self.lng)


class MapBaseRequest(BaseModel):
    request_type: str

    def to_grpc(self) -> MapUpdatesRequest: ...


class MapBoundsRequest(MapBaseRequest):
    sw: Point
    ne: Point
    zoom: float

    def to_grpc(self) -> MapUpdatesRequest:
        return MapUpdatesRequest(
            bounds=MapBounds(
                sw=self.sw.to_grpc_point(),
                ne=self.ne.to_grpc_point(),
                zoom=self.zoom
            )
        )


class MapFilterRequest(MapBaseRequest):
    filter: str

    def to_grpc(self) -> MapUpdatesRequest:
        return MapUpdatesRequest(
            filter=self.filter
        )


class MapWeatherRequest(MapBaseRequest):
    show_wx: bool

    def to_grpc(self) -> MapUpdatesRequest:
        return MapUpdatesRequest(
            show_wx=self.show_wx
        )


class MapSubscribeIDRequest(MapBaseRequest):
    subscribe_id: str

    def to_grpc(self) -> MapUpdatesRequest:
        return MapUpdatesRequest(
            subscribe_id=self.subscribe_id
        )


class MapUnsubscribeIDRequest(MapBaseRequest):
    unsubscribe_id: str

    def to_grpc(self) -> MapUpdatesRequest:
        return MapUpdatesRequest(
            unsubscribe_id=self.unsubscribe_id
        )


class Runway(BaseModel):
    icao: str
    length_ft: Optional[int] = None
    width_ft: Optional[int] = None
    surface: Optional[str] = None
    lighted: bool = False
    closed: bool = False
    ident: str
    latitude: float = 0.0
    longitude: float = 0.0
    elevation_ft: int = 0
    heading: int = 0
    active_to: bool = False
    active_lnd: bool = False


class WeatherInfo(BaseModel):
    temperature: Optional[float]
    dew_point: Optional[float]
    wind_speed: Optional[int]
    wind_gust: Optional[int]
    wind_direction_variable: Optional[str]
    wind_direction_deg: Optional[int]
    raw: str
    ts: int


class Controller(BaseModel):
    cid: int
    name: str
    callsign: str
    freq: int
    facility: str
    rating: int
    server: str
    visual_range: int
    atis_code: Optional[str] = None
    text_atis: Optional[str] = None
    human_readable: str
    last_updated: int
    logon_time: int


class ControllerSet(BaseModel):
    atis: Optional[Controller] = None
    delivery: Optional[Controller] = None
    ground: Optional[Controller] = None
    tower: Optional[Controller] = None
    approach: Optional[Controller] = None


class Airport(BaseModel):
    icao: Optional[str] = None
    iata: Optional[str] = None
    name: Optional[str] = None
    position: Point = Field(default_factory=Point)
    fir_id: Optional[str] = None
    is_pseudo: bool = False
    runways: Dict[str, Runway] = Field(default_factory=dict)
    wx: Optional[WeatherInfo] = None
    controllers: ControllerSet = Field(default_factory=ControllerSet)


class FlightPlan(BaseModel):
    flight_rules: Optional[str] = None
    aircraft: Optional[str] = None
    departure: Optional[str] = None
    arrival: Optional[str] = None
    alternate: Optional[str] = None
    deptime: Optional[str] = None
    enroute_time: Optional[str] = None
    fuel_time: Optional[str] = None
    remarks: Optional[str] = None
    route: Optional[str] = None
    cruise_tas: Optional[int] = None
    altitude: Optional[int] = None


class TrackPoint(BaseModel):
    lat: float = 0.0
    lng: float = 0.0
    alt: int = 0
    hdg: int = 0
    gs: int = 0
    ts: int = 0


class Pilot(BaseModel):
    cid: int
    name: Optional[str] = None
    callsign: Optional[str] = None
    server: Optional[str] = None
    pilot_rating: Optional[int] = None
    position: Point = Field(default_factory=Point)
    altitude: int = 0
    groundspeed: int = 0
    transponder: Optional[str] = None
    heading: int = 0
    qnh_i_hg: Optional[int] = None
    qnh_mb: Optional[int] = None
    flight_plan: Optional[FlightPlan] = None
    last_updated: Optional[int] = None
    logon_time: Optional[int] = None
    track: List[TrackPoint]


class QueryResponse(BaseModel):
    valid: bool
    error: Optional[str] = None


class GRPCBuildInfo(BaseModel):
    name: str
    version: str
    repository: str
    license: str
