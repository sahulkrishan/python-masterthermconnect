"""Constants used by the module."""
APP_CLIENTINFO = "os=android&osversion=7.0&ver=8&info=Google%2CAndroid"
APP_OS = "android"
APP_VERSION = "1"

COOKIE_TOKEN = "PHPSESSID"
HEADER_TOKEN_EXPIRES = "Date"
DATE_FORMAT = "%a, %d %b %Y %H:%M:%S %Z"
SUPPORTED_ROLES = ["400"]

URL_BASE = "https://mastertherm.vip-it.cz"
URL_LOGIN = "/plugins/mastertherm_login/client_login.php"
URL_PUMPINFO = "/plugins/get_pumpinfo/get_pumpinfo.php"
URL_GET = "/mt/PassiveVizualizationServlet"
URL_POST = "/mt/ActiveVizualizationServlet"

# Used to setup the pad name, for some reason they don't like the letter Q
CHAR_MAP = [
    "-",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

DEVICE_SWITCH_MAP = {
    0: "D_348",
    1: "D_433",
    2: "D_326",
    3: "D_316",
    4: "D_307",
    5: "D_298",
    6: "D_436",
    7: "D_278",
    8: "D_182",
}

PAD_MAP = {
    0: "heating",
    1: "cooling",
    2: "padf",
    3: "pade",
    4: "padd",
    5: "padc",
    6: "padb",
    7: "pada",
    8: "padz",
}

DEVICE_INFO_MAP = {
    "name": "givenname",
    "surname": "surname",
    "country": "localization",
    "language": "lang",
    "hp_type": "type",
    "controller": "regulation",
    "exp": "exp",
    "output": "output",
    "reservation": "reservation",
    "place": "city",
    "latitude": "password9",
    "longitude": "password10",
    "notes": "notes",
    "pada": "pada",
    "padb": "padb",
    "padc": "padc",
    "padd": "padd",
    "pade": "pade",
    "padf": "padf",
    "padz": "padz",
}

DEVICE_DATA_PADMAP = {
    "pada": {
        "enabled": ["fixed", False],
        "name": ["string", ["I_211", "I_212", "I_213", "I_214", "I_215", "I_216"]],
        "on": ["bool", "D_212"],
        "pump_running": ["bool", ""],
        "water_temp": ["float", "A_126"],
        "water_requested": ["decimal", ""],
        "ambient_temp": ["float", ""],
        "ambient_requested": ["float", ""],
        "control_curve": {
            "setpoint_a_outside": ["float", "A_101"],
            "setpoint_a_requested": ["float", "A_106"],
            "setpoint_b_outside": ["float", "A_102"],
            "setpoint_b_requested": ["float", "A_107"],
        },
    },
    "padb": {
        "enabled": ["fixed", False],
        "name": ["string", ["I_221", "I_222", "I_223", "I_224", "I_225", "I_226"]],
        "on": ["bool", "D_216"],
        "pump_running": ["bool", ""],
        "water_temp": ["float", "A_91"],
        "water_requested": ["decimal", ""],
        "ambient_temp": ["float", ""],
        "ambient_requested": ["float", ""],
        "control_curve": {
            "setpoint_a_outside": ["float", "A_108"],
            "setpoint_a_requested": ["float", "A_84"],
            "setpoint_b_outside": ["float", "A_109"],
            "setpoint_b_requested": ["float", "A_85"],
        },
    },
    "padc": {
        "enabled": ["fixed", False],
        "name": ["string", ["I_231", "I_232", "I_233", "I_234", "I_235", "I_236"]],
    },
    "padd": {
        "enabled": ["fixed", False],
        "name": ["string", ["I_241", "I_242", "I_243", "I_244", "I_245", "I_246"]],
    },
    "pade": {
        "enabled": ["fixed", False],
        "name": ["string", ["I_251", "I_252", "I_253", "I_254", "I_255", "I_256"]],
    },
    "padf": {
        "enabled": ["fixed", False],
        "name": ["string", ["I_261", "I_262", "I_263", "I_264", "I_265", "I_266"]],
    },
}

# NOTES --------------------------------------------------
# pswitch_data_1: Cooling Curve
# a_outside: A_47
# b_outside: A_48
# a_requested: A_49
# b_requested: A_50
#
# heating (0) / cooling (1) / auto (2) mode: I_52
# --------------------------------------------------------
DEVICE_DATA_MAP = {
    "on": ["bool", "D_3"],
    "heating": ["bool", ""],
    "compressor_running": ["bool", ""],
    "circulation_pump_running": ["bool", ""],
    "defrost_mode": ["bool", ""],
    "outside_temp": ["float", "A_3"],
    "requested_temp": ["float", "A_1"],
    "actual_temp": ["float", "A_90"],
    "compressor_run_time": ["int", "I_11"],
    "compressor_start_counter": ["int", "I_12"],
    "pump_runtime": ["int", "I_13"],
    "heating_curve": {
        "setpoint_a_outside": ["float", "A_35"],
        "setpoint_a_requested": ["float", "A_37"],
        "setpoint_b_outside": ["float", "A_36"],
        "setpoint_b_requested": ["float", "A_38"],
    },
    "pads": DEVICE_DATA_PADMAP,
}

DATA_MAP = {
    "alarm": "D_20",
    "alarm2": "D_21",
    "alarmA": "I_20",
    "alarmB": "I_21",
    "alarmC": "I_22",
    "alarmD": "I_23",
    "alarmE": "I_24",
    "alarmF": "I_25",
    "alarmG": "I_26",
    "alarmH": "I_27",
    "alarmI": "I_28",
    "alarmJ": "I_39",
    "alarmK": "I_40",
    "alarmL": "I_41",
    "alarmM": "I_42",
    "clockComp": "I_11",
    "clockEc1": "I_100",
    "clockEc2": "I_101",
    "clockHp": "I_13",
    "compStatus": "D_5",
    "ek1Status": "D_6",
    "ek2Status": "D_7",
    "fanStatus": "D_8",
    "function": "D_4",
    "functionSet": "I_51",
    "functionTuv": "D_66",
    "hdo": "D_15",
    "hpEqAirA": "A_35",
    "hpEqAirB": "A_36",
    "hpEqCoolingAirA": "A_47",
    "hpEqCoolingAirB": "A_48",
    "hpEqCoolingWatA": "A_49",
    "hpEqCoolingWatB": "A_50",
    "hpEqWatA": "A_37",
    "hpEqWatB": "A_38",
    "hpId": "I_72",
    "hpStatus": "D_10",
    "isPAD_sw10": "D_182",
    "isPAD_sw11": "D_242",
    "outdoor": "A_3",
    "power": "D_3",
    "season": "D_24",
    "seasonSet": "I_50",
    "seasonSummer": "A_83",
    "seasonWinter": "A_82",
    "startsComp": "I_12",
    "toAActive": "D_212",
    "toAActive_v": "D_245",
    "toAEnabled": "D_278",
    "toAEqAirAC": "A_314",
    "toAEqAirAH": "A_101",
    "toAEqAirBC": "A_316",
    "toAEqAirBH": "A_102",
    "toAEqWatAC": "A_315",
    "toAEqWatAH": "A_106",
    "toAEqWatBC": "A_317",
    "toAEqWatBH": "A_107",
    "toAName1": "I_211",
    "toAName2": "I_212",
    "toAName3": "I_213",
    "toAName4": "I_214",
    "toAName5": "I_215",
    "toAName6": "I_216",
    "toAReal": "A_216",
    "toASet": "A_215",
    "toASet_": "A_219",
    "toBActive": "D_216",
    "toBActive_v": "D_248",
    "toBEnabled": "D_436",
    "toBEqAirAC": "A_330",
    "toBEqAirAH": "A_108",
    "toBEqAirBC": "A_332",
    "toBEqAirBH": "A_109",
    "toBEqWatAC": "A_331",
    "toBEqWatAH": "A_84",
    "toBEqWatBC": "A_333",
    "toBEqWatBH": "A_85",
    "toBName1": "I_221",
    "toBName2": "I_222",
    "toBName3": "I_223",
    "toBName4": "I_224",
    "toBName5": "I_225",
    "toBName6": "I_226",
    "toBReal": "A_222",
    "toBSet": "A_221",
    "toBSet_": "A_225",
    "toCActive": "D_220",
    "toCActive_v": "D_251",
    "toCEnabled": "D_298",
    "toCEqAirAC": "A_346",
    "toCEqAirAH": "A_113",
    "toCEqAirBC": "A_348",
    "toCEqAirBH": "A_114",
    "toCEqWatAC": "A_347",
    "toCEqWatAH": "A_86",
    "toCEqWatBC": "A_349",
    "toCEqWatBH": "A_87",
    "toCName1": "I_231",
    "toCName2": "I_232",
    "toCName3": "I_233",
    "toCName4": "I_234",
    "toCName5": "I_235",
    "toCName6": "I_236",
    "toCReal": "A_228",
    "toCSet": "A_227",
    "toCSet_": "A_231",
    "toDActive": "D_50",
    "toDActive_v": "D_254",
    "toDEnabled": "D_307",
    "toDEqAirAC": "A_362",
    "toDEqAirAH": "A_122",
    "toDEqAirBC": "A_364",
    "toDEqAirBH": "A_88",
    "toDEqWatAC": "A_363",
    "toDEqWatAH": "A_120",
    "toDEqWatBC": "A_365",
    "toDEqWatBH": "A_121",
    "toDName1": "I_241",
    "toDName2": "I_242",
    "toDName3": "I_243",
    "toDName4": "I_244",
    "toDName5": "I_245",
    "toDName6": "I_246",
    "toDReal": "A_234",
    "toDSet": "A_233",
    "toDSet_": "A_238",
    "toEActive": "D_51",
    "toEActive_v": "D_257",
    "toEEnabled": "D_316",
    "toEEqAirAC": "A_379",
    "toEEqAirAH": "A_387",
    "toEEqAirBC": "A_381",
    "toEEqAirBH": "A_389",
    "toEEqWatAC": "A_380",
    "toEEqWatAH": "A_388",
    "toEEqWatBC": "A_382",
    "toEEqWatBH": "A_390",
    "toEName1": "I_251",
    "toEName2": "I_252",
    "toEName3": "I_253",
    "toEName4": "I_254",
    "toEName5": "I_255",
    "toEName6": "I_256",
    "toEReal": "A_241",
    "toESet": "A_240",
    "toESet_": "A_247",
    "toFActive": "D_52",
    "toFActive_v": "D_259",
    "toFEnabled": "D_326",
    "toFEqAirAC": "A_405",
    "toFEqAirAH": "A_402",
    "toFEqAirBC": "A_407",
    "toFEqAirBH": "A_404",
    "toFEqWatAC": "A_406",
    "toFEqWatAH": "A_401",
    "toFEqWatBC": "A_408",
    "toFEqWatBH": "A_403",
    "toFName1": "I_261",
    "toFName2": "I_262",
    "toFName3": "I_263",
    "toFName4": "I_264",
    "toFName5": "I_265",
    "toFName6": "I_266",
    "toFReal": "A_250",
    "toFSet": "A_249",
    "toFSet_": "A_277",
    "toPoolActive": "D_238",
    "toPoolEnabled": "D_348",
    "toPoolReal": "A_262",
    "toPoolSet": "A_15",
    "toRealA": "A_90",
    "toRealB": "A_91",
    "toRealC": "A_92",
    "toRealD": "A_93",
    "toRealZ": "A_211",
    "toSetA": "A_96",
    "toSetB": "A_97",
    "toSetC": "A_98",
    "toSetD": "A_99",
    "toSetZ": "A_191",
    "toSetZ_": "A_191",
    "toSolar1": "A_259",
    "toSolar2": "A_260",
    "toSolarEnabled": "D_433",
    "toSolarPanel": "A_258",
    "toTypeA": "I_62",
    "toTypeB": "I_65",
    "toTypeC": "I_68",
    "toTypeD": "I_69",
    "toZEnabled": "D_242",
    "tuvMax": "A_297",
    "tuvMin": "A_296",
    "tuvReal": "A_126",
    "tuvSet": "A_129",
    "tvReal": "A_1",
    "tvSet": "A_5",
    "version": "I_104",
}
