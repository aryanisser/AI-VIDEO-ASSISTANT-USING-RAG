import yt_dlp
from pydub import AudioSegment
import os
DOWNLOAD_DIR = 'downloades'
os.makedirs(DOWNLOAD_DIR, exist_ok=True)
def download_youtube_audio(url:str) -> str:
    output_path = os.path.join(DOWNLOAD_DIR, "%(title)s.%(ext)s")
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        "quiet": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info  = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info).replace('.webm', '.wav').replace('.m4a', '.mp3')
    return filename


        

def convert_to_wav(input_file:str) -> str:
    output_file = os.path.splitext(input_file)[0] + '.wav'
    audio = AudioSegment.from_file(input_file)
    audio = audio.set_frame_rate(16000).set_channels(1)
    audio.export(output_file, format='wav')
    return output_file  



def chunk_audio(wav_file:str, chunk_length:int=10) -> list:
    audio = AudioSegment.from_wav(wav_file)
    chunk_length_ms = chunk_length * 60 * 1000
    chunks = []
    for i in range(0, len(audio), chunk_length_ms):
        chunk = audio[i:i + chunk_length_ms]
        chunk_filename = f"{os.path.splitext(wav_file)[0]}_chunk_{i // (chunk_length_ms)}.wav"
        chunk.export(chunk_filename, format='wav')
        chunks.append(chunk_filename)
    return chunks


def process_input(source: str) ->list:
    if source.startswith("http://") or source.startswith("https://"):
        print(" Detected YouTube URL. Downloading audio...")
        wav_file = download_youtube_audio(source)
    else:
        print ("Detected local file. Converting to WAV...")
        wav_file = convert_to_wav(source)

    print ("Chunking audio...")
    chunks = chunk_audio(wav_file)
    print(f"Audio ready - {len(chunks)} chunk(s) created.")
    return chunks
