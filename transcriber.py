import whisper
import pytube

def download_youtube_audio(url, output_path='audio.mp4'):
    """
    Downloads the audio from a YouTube video.
    
    Args:
        url (str): URL of the YouTube video.
        output_path (str): Path to save the audio file.
    
    Returns:
        str: Path to the downloaded audio file.
    """
    yt = pytube.YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(filename=output_path)
    return output_path

def transcribe_audio(file_path, model_size="large"):
    """
    Transcribes audio using the Whisper ASR model.
    
    Args:
        file_path (str): Path to the audio file.
        model_size (str): Size of the Whisper model to use (tiny, base, small, medium, large).
    
    Returns:
        str: The transcription of the audio.
    """
    model = whisper.load_model(model_size)
    result = model.transcribe(file_path)
    return result['text']

def transcribe_youtube_video(url, model_size="large"):
    """
    Transcribes a YouTube video by first downloading the audio and then transcribing it.
    
    Args:
        url (str): URL of the YouTube video.
        model_size (str): Size of the Whisper model to use (tiny, base, small, medium, large).
    
    Returns:
        str: The transcription of the YouTube video.
    """
    audio_path = download_youtube_audio(url)
    transcription = transcribe_audio(audio_path, model_size)
    return transcription

# Example usage:
youtube_url = "https://www.youtube.com/watch?v=-JH5d0Mpcbk&t=3855s"
transcription = transcribe_youtube_video(youtube_url, model_size="large")
print(transcription)
