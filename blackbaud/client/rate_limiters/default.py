from limits import parse_many, storage

STANDARD_TIER = parse_many("10/second; 25000/day")

UPGRADED_TIER_1 = parse_many("10/second; 100000/day")

UPGRADED_TIER_2 = parse_many("10/second; 250000/day")

DEFAULT_STORAGE = storage.MemoryStorage()
