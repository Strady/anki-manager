from enum import StrEnum

URL = 'http://localhost:8765'


class Fields(StrEnum):
    IMAGE = 'Image'
    AUDIO_FRONT = 'Audio Front'
    AUDIO_BACK = 'Audio Back'
    TEXT_FRONT = 'Text Front'
    TEXT_BACK = 'Text Back'
    TEXT_EXAMPLE = 'Text Example'

    @classmethod
    def as_tuple(cls) -> tuple[str, ...]:
        return [                    # type: ignore
            cls.IMAGE.value,
            cls.AUDIO_FRONT.value,
            cls.AUDIO_BACK.value,
            cls.TEXT_FRONT.value,
            cls.TEXT_BACK.value,
            cls.TEXT_EXAMPLE.value,
        ]
