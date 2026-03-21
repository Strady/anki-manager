import base64
import edge_tts
from io import BytesIO


def base64_encode(bytes_data: bytes) -> str:
    return base64.b64encode(bytes_data).decode()


def generate_audio_from_text(text: str, rate: int = -10) -> bytes:
    communicate = edge_tts.Communicate(text=text, rate=f'{rate}%')
    audio_bytes = BytesIO()
    for chunk in communicate.stream_sync():
        if 'data' in chunk:
            audio_bytes.write(chunk['data'])
    return audio_bytes.getvalue()
