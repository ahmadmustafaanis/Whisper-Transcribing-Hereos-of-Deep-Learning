import os

import whisper
from fpdf import FPDF
from tqdm import tqdm

from download_videos import DownloadInterviews, interviews_details


class TranscribeInterviews:
    def __init__(self) -> None:
        self.all_interviews_results = []
        self.model = whisper.load_model("base")
        try:
            os.listdir("interviews")
        except FileNotFoundError:
            print("Creating the interviews folder")
            os.mkdir("interviews")
            print("Downloading the Interviews first.")
            DownloadInterviews()()

    def convert_to_pdf(self) -> None:
        """
        Converts the transcribed interviews to a pdf file
        """
        print("Converting to PDF")
        for hero_num in range(len(self.all_interviews_results)):
            pdf = FPDF()  # Creates a new PDF File
            pdf.add_page()
            pdf.set_font("Arial", "B", 16)
            pdf.cell(
                0,
                0,
                txt=f"Interview of {list(interviews_details.values())[hero_num]}",
                ln=1,
                align="C",
            )  # Add Title to PDF
            pdf.ln()
            pdf.set_font("Arial", size=12)

            for line in range(len(self.all_interviews_results[hero_num]["segments"])):
                pdf.cell(
                    200,
                    10,
                    txt=self.all_interviews_results[hero_num]["segments"][line]["text"],
                    ln=1,
                )  # Adds each seperate line to PDF
            pdf.output(
                f"{list(interviews_details.values())[hero_num]}.pdf"
            )  # Store the PDF with the name

    def __call__(self):
        print("Transcribing Interviews")
        for downloaded_audio in tqdm(os.listdir("interviews")):
            if downloaded_audio.endswith(".mp3"):  # Transcribe only the mp3 files
                result = self.model.transcribe(f"interviews/{downloaded_audio}")
                self.all_interviews_results.append(result)


if __name__ == "__main__":
    transcribe_interviews = TranscribeInterviews()
    transcribe_interviews()
    transcribe_interviews.convert_to_pdf()
