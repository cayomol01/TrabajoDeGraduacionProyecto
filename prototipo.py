import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import random
import threading
import time
from PIL import Image, ImageTk

class VoiceAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Analyzer")
        self.root.geometry("600x400")
        self.root.configure(bg="#282c34")

        self.style = ttk.Style()
        self.style.configure('TButton', font=('Helvetica', 12), foreground='#61dafb', background='#282c34')
        self.style.configure('TLabel', font=('Helvetica', 12), foreground='#ffffff', background='#282c34')

        self.label = ttk.Label(root, text="Selecciona un archivo de audio:")
        self.label.pack(pady=20)

        self.select_button = ttk.Button(root, text="Seleccionar archivo", command=self.select_file)
        self.select_button.pack(pady=10)

        self.progress = ttk.Progressbar(root, orient='horizontal', mode='indeterminate')
        self.progress.pack(pady=20, padx=20, fill='x')

        self.model_frame = ttk.Frame(root)
        self.model_frame.pack(pady=20)

        self.model1_image_label = ttk.Label(self.model_frame)
        self.model1_image_label.grid(row=0, column=0, padx=20)

        self.model1_result_label = ttk.Label(self.model_frame, text="Resultado del Modelo 1")
        self.model1_result_label.grid(row=1, column=0, padx=20)

        self.model2_image_label = ttk.Label(self.model_frame)
        self.model2_image_label.grid(row=0, column=1, padx=20)

        self.model2_result_label = ttk.Label(self.model_frame, text="Resultado del Modelo 2")
        self.model2_result_label.grid(row=1, column=1, padx=20)

        self.load_images()

    def load_images(self):
        model1_image = Image.open("RedLSTM.png")
        model1_image = model1_image.resize((100, 100), Image.ANTIALIAS)
        self.model1_image = ImageTk.PhotoImage(model1_image)
        self.model1_image_label.config(image=self.model1_image)

        model2_image = Image.open("FiltrosDeSonido.jpg")
        model2_image = model2_image.resize((100, 100), Image.ANTIALIAS)
        self.model2_image = ImageTk.PhotoImage(model2_image)
        self.model2_image_label.config(image=self.model2_image)

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3")])
        if file_path:
            self.start_processing(file_path)

    def start_processing(self, file_path):
        self.progress.start()
        threading.Thread(target=self.process_file, args=(file_path,)).start()

    def process_file(self, file_path):
        time.sleep(2)  # Simulando tiempo de procesamiento
        model1_result, model2_result = self.simulate_models(file_path)
        self.progress.stop()
        self.model1_result_label.config(text=f"Modelo 1: {model1_result}")
        self.model2_result_label.config(text=f"Modelo 2: {model2_result}")
        self.animate_result()

    def simulate_models(self, file_path):
        model1_result = random.choice(["Voz generada por IA", "Voz humana"])  # Modelo 1
        model2_result = random.choice(["Voz generada por IA", "Voz humana"])  # Modelo 2
        return model1_result, model2_result

    def animate_result(self):
        for i in range(10):
            self.model1_result_label.config(foreground=random.choice(['#ff5555', '#50fa7b', '#f1fa8c', '#bd93f9']))
            self.model2_result_label.config(foreground=random.choice(['#ff5555', '#50fa7b', '#f1fa8c', '#bd93f9']))
            self.root.update_idletasks()
            time.sleep(0.1)

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceAnalyzerApp(root)
    root.mainloop()
