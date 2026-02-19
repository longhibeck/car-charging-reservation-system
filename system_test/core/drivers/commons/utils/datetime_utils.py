from datetime import datetime, timezone, timedelta


class DateTimeUtils:
    ZULU_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"

    @staticmethod
    def to_zulu_format(dt: datetime) -> str:
        return dt.strftime(DateTimeUtils.ZULU_FORMAT)

    @staticmethod
    def parse_zulu_time(zulu_str: str) -> datetime:
        return datetime.strptime(zulu_str, DateTimeUtils.ZULU_FORMAT).replace(
            tzinfo=timezone.utc
        )

    @staticmethod
    def now_utc() -> datetime:
        return datetime.now(timezone.utc)

    @staticmethod
    def get_current_zulu_time() -> str:
        return DateTimeUtils.to_zulu_format(DateTimeUtils.now_utc())
    
    @staticmethod
    def add_hours_to_zulu_time(zulu_str: str, hours: int) -> str:
        dt = DateTimeUtils.parse_zulu_time(zulu_str)
        dt += timedelta(hours=hours)
        return DateTimeUtils.to_zulu_format(dt)