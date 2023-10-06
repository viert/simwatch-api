# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: camden.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x63\x61mden.proto\x12\x06\x63\x61mden\"!\n\x05Point\x12\x0b\n\x03lat\x18\x01 \x01(\x01\x12\x0b\n\x03lng\x18\x02 \x01(\x01\"\xa1\x02\n\nController\x12\x0b\n\x03\x63id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08\x63\x61llsign\x18\x03 \x01(\t\x12\x0c\n\x04\x66req\x18\x04 \x01(\r\x12\"\n\x08\x66\x61\x63ility\x18\x05 \x01(\x0e\x32\x10.camden.Facility\x12\x0e\n\x06rating\x18\x06 \x01(\x05\x12\x0e\n\x06server\x18\x07 \x01(\t\x12\x14\n\x0cvisual_range\x18\x08 \x01(\r\x12\x11\n\tatis_code\x18\t \x01(\t\x12\x11\n\ttext_atis\x18\n \x01(\t\x12\x1b\n\x0ehuman_readable\x18\x0b \x01(\tH\x00\x88\x01\x01\x12\x14\n\x0clast_updated\x18\x0c \x01(\x04\x12\x12\n\nlogon_time\x18\r \x01(\x04\x42\x11\n\x0f_human_readable\"\xc4\x01\n\rControllerSet\x12 \n\x04\x61tis\x18\x01 \x01(\x0b\x32\x12.camden.Controller\x12$\n\x08\x64\x65livery\x18\x02 \x01(\x0b\x32\x12.camden.Controller\x12\"\n\x06ground\x18\x03 \x01(\x0b\x32\x12.camden.Controller\x12!\n\x05tower\x18\x04 \x01(\x0b\x32\x12.camden.Controller\x12$\n\x08\x61pproach\x18\x05 \x01(\x0b\x32\x12.camden.Controller\"\xe2\x01\n\x08\x41ircraft\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0b\n\x03wtc\x18\x03 \x01(\t\x12\x0b\n\x03wtg\x18\x04 \x01(\t\x12\x12\n\ndesignator\x18\x05 \x01(\t\x12\x19\n\x11manufacturer_code\x18\x06 \x01(\t\x12+\n\raircraft_type\x18\x07 \x01(\x0e\x32\x14.camden.AircraftType\x12\x14\n\x0c\x65ngine_count\x18\x08 \x01(\r\x12\'\n\x0b\x65ngine_type\x18\t \x01(\x0e\x32\x12.camden.EngineType\"\x89\x03\n\x05Pilot\x12\x0b\n\x03\x63id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08\x63\x61llsign\x18\x03 \x01(\t\x12\x0e\n\x06server\x18\x04 \x01(\t\x12\x14\n\x0cpilot_rating\x18\x05 \x01(\x05\x12\x1f\n\x08position\x18\x06 \x01(\x0b\x32\r.camden.Point\x12\x10\n\x08\x61ltitude\x18\x07 \x01(\x05\x12\x13\n\x0bgroundspeed\x18\x08 \x01(\x05\x12\x13\n\x0btransponder\x18\t \x01(\t\x12\x0f\n\x07heading\x18\n \x01(\x05\x12\x10\n\x08qnh_i_hg\x18\x0b \x01(\r\x12\x0e\n\x06qnh_mb\x18\x0c \x01(\r\x12\'\n\x0b\x66light_plan\x18\r \x01(\x0b\x32\x12.camden.FlightPlan\x12\x14\n\x0clast_updated\x18\x0e \x01(\x04\x12\x12\n\nlogon_time\x18\x0f \x01(\x04\x12\'\n\raircraft_type\x18\x10 \x01(\x0b\x32\x10.camden.Aircraft\x12!\n\x05track\x18\x11 \x03(\x0b\x32\x12.camden.TrackPoint\"\xeb\x01\n\nFlightPlan\x12\x14\n\x0c\x66light_rules\x18\x01 \x01(\t\x12\x10\n\x08\x61ircraft\x18\x02 \x01(\t\x12\x11\n\tdeparture\x18\x03 \x01(\t\x12\x0f\n\x07\x61rrival\x18\x04 \x01(\t\x12\x11\n\talternate\x18\x05 \x01(\t\x12\x12\n\ncruise_tas\x18\x06 \x01(\r\x12\x10\n\x08\x61ltitude\x18\x07 \x01(\r\x12\x0f\n\x07\x64\x65ptime\x18\x08 \x01(\t\x12\x14\n\x0c\x65nroute_time\x18\t \x01(\t\x12\x11\n\tfuel_time\x18\n \x01(\t\x12\x0f\n\x07remarks\x18\x0b \x01(\t\x12\r\n\x05route\x18\x0c \x01(\t\"X\n\nTrackPoint\x12\x0b\n\x03lat\x18\x01 \x01(\x01\x12\x0b\n\x03lng\x18\x02 \x01(\x01\x12\x0b\n\x03\x61lt\x18\x03 \x01(\x05\x12\x0b\n\x03hdg\x18\x04 \x01(\x05\x12\n\n\x02gs\x18\x05 \x01(\x05\x12\n\n\x02ts\x18\x06 \x01(\x03\"\xef\x01\n\x06Runway\x12\x0c\n\x04icao\x18\x01 \x01(\t\x12\x11\n\tlength_ft\x18\x02 \x01(\r\x12\x10\n\x08width_ft\x18\x03 \x01(\r\x12\x0f\n\x07surface\x18\x04 \x01(\t\x12\x0f\n\x07lighted\x18\x05 \x01(\x08\x12\x0e\n\x06\x63losed\x18\x06 \x01(\x08\x12\r\n\x05ident\x18\x07 \x01(\t\x12\x10\n\x08latitude\x18\x08 \x01(\x01\x12\x11\n\tlongitude\x18\t \x01(\x01\x12\x14\n\x0c\x65levation_ft\x18\n \x01(\x05\x12\x0f\n\x07heading\x18\x0b \x01(\x05\x12\x11\n\tactive_to\x18\x0c \x01(\x08\x12\x12\n\nactive_lnd\x18\r \x01(\x08\"\x97\x02\n\x0bWeatherInfo\x12\x18\n\x0btemperature\x18\x01 \x01(\x01H\x01\x88\x01\x01\x12\x16\n\tdew_point\x18\x02 \x01(\x01H\x02\x88\x01\x01\x12\x17\n\nwind_speed\x18\x03 \x01(\x04H\x03\x88\x01\x01\x12\x16\n\twind_gust\x18\x04 \x01(\x04H\x04\x88\x01\x01\x12!\n\x17wind_direction_variable\x18\x05 \x01(\tH\x00\x12\x1c\n\x12wind_direction_deg\x18\x06 \x01(\rH\x00\x12\x0b\n\x03raw\x18\x07 \x01(\t\x12\n\n\x02ts\x18\x08 \x01(\x04\x42\x10\n\x0ewind_directionB\x0e\n\x0c_temperatureB\x0c\n\n_dew_pointB\r\n\x0b_wind_speedB\x0c\n\n_wind_gust\"\xb3\x02\n\x07\x41irport\x12\x0c\n\x04icao\x18\x01 \x01(\t\x12\x0c\n\x04iata\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x1f\n\x08position\x18\x04 \x01(\x0b\x32\r.camden.Point\x12\x0e\n\x06\x66ir_id\x18\x05 \x01(\t\x12\x11\n\tis_pseudo\x18\x06 \x01(\x08\x12-\n\x07runways\x18\x07 \x03(\x0b\x32\x1c.camden.Airport.RunwaysEntry\x12\x1f\n\x02wx\x18\x08 \x01(\x0b\x32\x13.camden.WeatherInfo\x12*\n\x0b\x63ontrollers\x18\t \x01(\x0b\x32\x15.camden.ControllerSet\x1a>\n\x0cRunwaysEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1d\n\x05value\x18\x02 \x01(\x0b\x32\x0e.camden.Runway:\x02\x38\x01\"*\n\tPointList\x12\x1d\n\x06points\x18\x01 \x03(\x0b\x32\r.camden.Point\"\xc8\x01\n\nBoundaries\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06region\x18\x02 \x01(\t\x12\x10\n\x08\x64ivision\x18\x03 \x01(\t\x12\x12\n\nis_oceanic\x18\x04 \x01(\x08\x12\x1a\n\x03min\x18\x05 \x01(\x0b\x32\r.camden.Point\x12\x1a\n\x03max\x18\x06 \x01(\x0b\x32\r.camden.Point\x12\x1d\n\x06\x63\x65nter\x18\x07 \x01(\x0b\x32\r.camden.Point\x12!\n\x06points\x18\x08 \x03(\x0b\x32\x11.camden.PointList\"\xd4\x01\n\x03\x46IR\x12\x0c\n\x04icao\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06prefix\x18\x03 \x01(\t\x12\x31\n\x0b\x63ontrollers\x18\x04 \x03(\x0b\x32\x1c.camden.FIR.ControllersEntry\x12&\n\nboundaries\x18\x05 \x01(\x0b\x32\x12.camden.Boundaries\x1a\x46\n\x10\x43ontrollersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.camden.Controller:\x02\x38\x01\"[\n\rAirportUpdate\x12\'\n\x0bupdate_type\x18\x01 \x01(\x0e\x32\x12.camden.UpdateType\x12!\n\x08\x61irports\x18\x02 \x03(\x0b\x32\x0f.camden.Airport\"U\n\x0bPilotUpdate\x12\'\n\x0bupdate_type\x18\x01 \x01(\x0e\x32\x12.camden.UpdateType\x12\x1d\n\x06pilots\x18\x02 \x03(\x0b\x32\r.camden.Pilot\"O\n\tFirUpdate\x12\'\n\x0bupdate_type\x18\x01 \x01(\x0e\x32\x12.camden.UpdateType\x12\x19\n\x04\x66irs\x18\x02 \x03(\x0b\x32\x0b.camden.FIR\"\xa0\x01\n\x06Update\x12/\n\x0e\x61irport_update\x18\x01 \x01(\x0b\x32\x15.camden.AirportUpdateH\x00\x12+\n\x0cpilot_update\x18\x02 \x01(\x0b\x32\x13.camden.PilotUpdateH\x00\x12\'\n\nfir_update\x18\x03 \x01(\x0b\x32\x11.camden.FirUpdateH\x00\x42\x0f\n\robject_update\"O\n\tMapBounds\x12\x19\n\x02sw\x18\x01 \x01(\x0b\x32\r.camden.Point\x12\x19\n\x02ne\x18\x02 \x01(\x0b\x32\r.camden.Point\x12\x0c\n\x04zoom\x18\x03 \x01(\x01\"\x9a\x01\n\x11MapUpdatesRequest\x12#\n\x06\x62ounds\x18\x01 \x01(\x0b\x32\x11.camden.MapBoundsH\x00\x12\x10\n\x06\x66ilter\x18\x02 \x01(\tH\x00\x12\x11\n\x07show_wx\x18\x03 \x01(\x08H\x00\x12\x16\n\x0csubscribe_id\x18\x04 \x01(\tH\x00\x12\x18\n\x0eunsubscribe_id\x18\x05 \x01(\tH\x00\x42\t\n\x07request\"\x1e\n\x0e\x41irportRequest\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\"3\n\x0f\x41irportResponse\x12 \n\x07\x61irport\x18\x01 \x01(\x0b\x32\x0f.camden.Airport\" \n\x0cPilotRequest\x12\x10\n\x08\x63\x61llsign\x18\x01 \x01(\t\"-\n\rPilotResponse\x12\x1c\n\x05pilot\x18\x01 \x01(\x0b\x32\r.camden.Pilot\"2\n\x11PilotListResponse\x12\x1d\n\x06pilots\x18\x01 \x03(\x0b\x32\r.camden.Pilot\"\x1d\n\x0cQueryRequest\x12\r\n\x05query\x18\x01 \x01(\t\"L\n\rQueryResponse\x12\r\n\x05valid\x18\x01 \x01(\x08\x12\x1a\n\rerror_message\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x10\n\x0e_error_message\"W\n\x11\x42uildInfoResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x12\n\nrepository\x18\x03 \x01(\t\x12\x0f\n\x07license\x18\x04 \x01(\t\"\n\n\x08NoParams\"\xbf\x02\n\x06Metric\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04help\x18\x02 \x01(\t\x12\'\n\x0bmetric_type\x18\x03 \x01(\x0e\x32\x12.camden.MetricType\x12\x0e\n\x06single\x18\x04 \x01(\x08\x12\x10\n\x08is_float\x18\x05 \x01(\x08\x12\x35\n\x0c\x66loat_values\x18\x06 \x03(\x0b\x32\x1f.camden.Metric.FloatValuesEntry\x12\x31\n\nint_values\x18\x07 \x03(\x0b\x32\x1d.camden.Metric.IntValuesEntry\x1a\x32\n\x10\x46loatValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\x1a\x30\n\x0eIntValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x04:\x02\x38\x01\"\xf1\x02\n\tMetricSet\x12-\n\x15vatsim_objects_online\x18\x01 \x01(\x0b\x32\x0e.camden.Metric\x12.\n\x16\x64\x61tabase_objects_count\x18\x02 \x01(\x0b\x32\x0e.camden.Metric\x12=\n%database_objects_count_fetch_time_sec\x18\x03 \x01(\x0b\x32\x0e.camden.Metric\x12\x31\n\x19vatsim_data_load_time_sec\x18\x04 \x01(\x0b\x32\x0e.camden.Metric\x12+\n\x13processing_time_sec\x18\x05 \x01(\x0b\x32\x0e.camden.Metric\x12+\n\x13\x64\x62_cleanup_time_sec\x18\x06 \x01(\x0b\x32\x0e.camden.Metric\x12\x1d\n\x15vatsim_data_timestamp\x18\x07 \x01(\x04\x12\x1a\n\x12process_started_at\x18\x08 \x01(\x04\"%\n\x15MetricSetTextResponse\x12\x0c\n\x04text\x18\x01 \x01(\t\".\n\x11QuerySubscription\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05query\x18\x02 \x01(\t\"\x87\x01\n\x18QuerySubscriptionRequest\x12:\n\x0crequest_type\x18\x01 \x01(\x0e\x32$.camden.QuerySubscriptionRequestType\x12/\n\x0csubscription\x18\x02 \x01(\x0b\x32\x19.camden.QuerySubscription\"\x8a\x01\n\x17QuerySubscriptionUpdate\x12\x17\n\x0fsubscription_id\x18\x01 \x01(\t\x12\x38\n\x0bupdate_type\x18\x02 \x01(\x0e\x32#.camden.QuerySubscriptionUpdateType\x12\x1c\n\x05pilot\x18\x03 \x01(\x0b\x32\r.camden.Pilot*^\n\x08\x46\x61\x63ility\x12\n\n\x06REJECT\x10\x00\x12\x08\n\x04\x41TIS\x10\x01\x12\x0c\n\x08\x44\x45LIVERY\x10\x02\x12\n\n\x06GROUND\x10\x03\x12\t\n\x05TOWER\x10\x04\x12\x0c\n\x08\x41PPROACH\x10\x05\x12\t\n\x05RADAR\x10\x06*\x88\x01\n\x0c\x41ircraftType\x12\x0b\n\x07\x41T_NONE\x10\x00\x12\x10\n\x0c\x41T_AMPHIBIAN\x10\x01\x12\x11\n\rAT_GYROCOPTER\x10\x02\x12\x11\n\rAT_HELICOPTER\x10\x03\x12\x10\n\x0c\x41T_LANDPLANE\x10\x04\x12\x0f\n\x0b\x41T_SEAPLANE\x10\x05\x12\x10\n\x0c\x41T_TILTROTOR\x10\x06*f\n\nEngineType\x12\x0b\n\x07\x45T_NONE\x10\x00\x12\x0f\n\x0b\x45T_ELECTRIC\x10\x01\x12\n\n\x06\x45T_JET\x10\x02\x12\r\n\tET_PISTON\x10\x03\x12\r\n\tET_ROCKET\x10\x04\x12\x10\n\x0c\x45T_TURBOPROP\x10\x05*.\n\nUpdateType\x12\x0b\n\x07UT_NONE\x10\x00\x12\x07\n\x03SET\x10\x01\x12\n\n\x06\x44\x45LETE\x10\x02*M\n\nMetricType\x12\x0b\n\x07MT_NONE\x10\x00\x12\x0b\n\x07\x43OUNTER\x10\x01\x12\t\n\x05GAUGE\x10\x02\x12\x0b\n\x07SUMMARY\x10\x03\x12\r\n\tHISTOGRAM\x10\x04*d\n\x1cQuerySubscriptionRequestType\x12\x15\n\x11SUBSCRIPTION_NONE\x10\x00\x12\x14\n\x10SUBSCRIPTION_ADD\x10\x01\x12\x17\n\x13SUBSCRIPTION_DELETE\x10\x02*E\n\x1bQuerySubscriptionUpdateType\x12\r\n\tQSUT_NONE\x10\x00\x12\n\n\x06ONLINE\x10\x01\x12\x0b\n\x07OFFLINE\x10\x02\x32\xc0\x04\n\x06\x43\x61mden\x12;\n\nMapUpdates\x12\x19.camden.MapUpdatesRequest\x1a\x0e.camden.Update(\x01\x30\x01\x12=\n\nGetAirport\x12\x16.camden.AirportRequest\x1a\x17.camden.AirportResponse\x12\x37\n\x08GetPilot\x12\x14.camden.PilotRequest\x1a\x15.camden.PilotResponse\x12=\n\nListPilots\x12\x14.camden.QueryRequest\x1a\x19.camden.PilotListResponse\x12\x39\n\nCheckQuery\x12\x14.camden.QueryRequest\x1a\x15.camden.QueryResponse\x12\x38\n\tBuildInfo\x12\x10.camden.NoParams\x1a\x19.camden.BuildInfoResponse\x12\x31\n\nGetMetrics\x12\x10.camden.NoParams\x1a\x11.camden.MetricSet\x12\x41\n\x0eGetMetricsText\x12\x10.camden.NoParams\x1a\x1d.camden.MetricSetTextResponse\x12W\n\x0eSubscribeQuery\x12 .camden.QuerySubscriptionRequest\x1a\x1f.camden.QuerySubscriptionUpdate(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'camden_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _AIRPORT_RUNWAYSENTRY._options = None
  _AIRPORT_RUNWAYSENTRY._serialized_options = b'8\001'
  _FIR_CONTROLLERSENTRY._options = None
  _FIR_CONTROLLERSENTRY._serialized_options = b'8\001'
  _METRIC_FLOATVALUESENTRY._options = None
  _METRIC_FLOATVALUESENTRY._serialized_options = b'8\001'
  _METRIC_INTVALUESENTRY._options = None
  _METRIC_INTVALUESENTRY._serialized_options = b'8\001'
  _globals['_FACILITY']._serialized_start=4949
  _globals['_FACILITY']._serialized_end=5043
  _globals['_AIRCRAFTTYPE']._serialized_start=5046
  _globals['_AIRCRAFTTYPE']._serialized_end=5182
  _globals['_ENGINETYPE']._serialized_start=5184
  _globals['_ENGINETYPE']._serialized_end=5286
  _globals['_UPDATETYPE']._serialized_start=5288
  _globals['_UPDATETYPE']._serialized_end=5334
  _globals['_METRICTYPE']._serialized_start=5336
  _globals['_METRICTYPE']._serialized_end=5413
  _globals['_QUERYSUBSCRIPTIONREQUESTTYPE']._serialized_start=5415
  _globals['_QUERYSUBSCRIPTIONREQUESTTYPE']._serialized_end=5515
  _globals['_QUERYSUBSCRIPTIONUPDATETYPE']._serialized_start=5517
  _globals['_QUERYSUBSCRIPTIONUPDATETYPE']._serialized_end=5586
  _globals['_POINT']._serialized_start=24
  _globals['_POINT']._serialized_end=57
  _globals['_CONTROLLER']._serialized_start=60
  _globals['_CONTROLLER']._serialized_end=349
  _globals['_CONTROLLERSET']._serialized_start=352
  _globals['_CONTROLLERSET']._serialized_end=548
  _globals['_AIRCRAFT']._serialized_start=551
  _globals['_AIRCRAFT']._serialized_end=777
  _globals['_PILOT']._serialized_start=780
  _globals['_PILOT']._serialized_end=1173
  _globals['_FLIGHTPLAN']._serialized_start=1176
  _globals['_FLIGHTPLAN']._serialized_end=1411
  _globals['_TRACKPOINT']._serialized_start=1413
  _globals['_TRACKPOINT']._serialized_end=1501
  _globals['_RUNWAY']._serialized_start=1504
  _globals['_RUNWAY']._serialized_end=1743
  _globals['_WEATHERINFO']._serialized_start=1746
  _globals['_WEATHERINFO']._serialized_end=2025
  _globals['_AIRPORT']._serialized_start=2028
  _globals['_AIRPORT']._serialized_end=2335
  _globals['_AIRPORT_RUNWAYSENTRY']._serialized_start=2273
  _globals['_AIRPORT_RUNWAYSENTRY']._serialized_end=2335
  _globals['_POINTLIST']._serialized_start=2337
  _globals['_POINTLIST']._serialized_end=2379
  _globals['_BOUNDARIES']._serialized_start=2382
  _globals['_BOUNDARIES']._serialized_end=2582
  _globals['_FIR']._serialized_start=2585
  _globals['_FIR']._serialized_end=2797
  _globals['_FIR_CONTROLLERSENTRY']._serialized_start=2727
  _globals['_FIR_CONTROLLERSENTRY']._serialized_end=2797
  _globals['_AIRPORTUPDATE']._serialized_start=2799
  _globals['_AIRPORTUPDATE']._serialized_end=2890
  _globals['_PILOTUPDATE']._serialized_start=2892
  _globals['_PILOTUPDATE']._serialized_end=2977
  _globals['_FIRUPDATE']._serialized_start=2979
  _globals['_FIRUPDATE']._serialized_end=3058
  _globals['_UPDATE']._serialized_start=3061
  _globals['_UPDATE']._serialized_end=3221
  _globals['_MAPBOUNDS']._serialized_start=3223
  _globals['_MAPBOUNDS']._serialized_end=3302
  _globals['_MAPUPDATESREQUEST']._serialized_start=3305
  _globals['_MAPUPDATESREQUEST']._serialized_end=3459
  _globals['_AIRPORTREQUEST']._serialized_start=3461
  _globals['_AIRPORTREQUEST']._serialized_end=3491
  _globals['_AIRPORTRESPONSE']._serialized_start=3493
  _globals['_AIRPORTRESPONSE']._serialized_end=3544
  _globals['_PILOTREQUEST']._serialized_start=3546
  _globals['_PILOTREQUEST']._serialized_end=3578
  _globals['_PILOTRESPONSE']._serialized_start=3580
  _globals['_PILOTRESPONSE']._serialized_end=3625
  _globals['_PILOTLISTRESPONSE']._serialized_start=3627
  _globals['_PILOTLISTRESPONSE']._serialized_end=3677
  _globals['_QUERYREQUEST']._serialized_start=3679
  _globals['_QUERYREQUEST']._serialized_end=3708
  _globals['_QUERYRESPONSE']._serialized_start=3710
  _globals['_QUERYRESPONSE']._serialized_end=3786
  _globals['_BUILDINFORESPONSE']._serialized_start=3788
  _globals['_BUILDINFORESPONSE']._serialized_end=3875
  _globals['_NOPARAMS']._serialized_start=3877
  _globals['_NOPARAMS']._serialized_end=3887
  _globals['_METRIC']._serialized_start=3890
  _globals['_METRIC']._serialized_end=4209
  _globals['_METRIC_FLOATVALUESENTRY']._serialized_start=4109
  _globals['_METRIC_FLOATVALUESENTRY']._serialized_end=4159
  _globals['_METRIC_INTVALUESENTRY']._serialized_start=4161
  _globals['_METRIC_INTVALUESENTRY']._serialized_end=4209
  _globals['_METRICSET']._serialized_start=4212
  _globals['_METRICSET']._serialized_end=4581
  _globals['_METRICSETTEXTRESPONSE']._serialized_start=4583
  _globals['_METRICSETTEXTRESPONSE']._serialized_end=4620
  _globals['_QUERYSUBSCRIPTION']._serialized_start=4622
  _globals['_QUERYSUBSCRIPTION']._serialized_end=4668
  _globals['_QUERYSUBSCRIPTIONREQUEST']._serialized_start=4671
  _globals['_QUERYSUBSCRIPTIONREQUEST']._serialized_end=4806
  _globals['_QUERYSUBSCRIPTIONUPDATE']._serialized_start=4809
  _globals['_QUERYSUBSCRIPTIONUPDATE']._serialized_end=4947
  _globals['_CAMDEN']._serialized_start=5589
  _globals['_CAMDEN']._serialized_end=6165
# @@protoc_insertion_point(module_scope)
