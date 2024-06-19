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
        self.root.geometry("600x550")
        self.root.configure(bg="#282c34")

        self.style = ttk.Style()
        self.style.configure('TButton', font=('Helvetica', 12), foreground='#000000', background='#61dafb', padding=10, borderwidth=2, relief='raised')
        self.style.map('TButton',
                       foreground=[('!active', '#000000'), ('active', '#000000')],
                       background=[('!active', '#61dafb'), ('active', '#4a90e2')],
                       relief=[('pressed', 'sunken'), ('!pressed', 'raised')])

        self.style.configure('TLabel', font=('Helvetica', 12), foreground='#ffffff', background='#282c34')

        self.label = ttk.Label(root, text="Selecciona un archivo de audio:")
        self.label.pack(pady=10)

        self.select_button = ttk.Button(root, text="Seleccionar archivo", command=self.select_file, style='TButton')
        self.select_button.pack(pady=5)

        self.file_label = ttk.Label(root, text="", background="#282c34", foreground="#ffffff")
        self.file_label.pack(pady=5)

        self.progress = ttk.Progressbar(root, orient='horizontal', mode='indeterminate')
        self.progress.pack(pady=10, padx=20, fill='x')

        self.model_frame = tk.Frame(root, bg="#282c34")
        self.model_frame.pack(pady=20)

        self.model1_title = ttk.Label(self.model_frame, text="Red Neuronal", background="#282c34", foreground="#ffffff")
        self.model1_title.grid(row=0, column=0, padx=20, pady=(0, 10))

        self.model1_image_label = ttk.Label(self.model_frame, background="#282c34")
        self.model1_image_label.grid(row=1, column=0, padx=20)

        self.model1_result_label = ttk.Label(self.model_frame, text="Resultado del Modelo 1", background="#282c34", foreground="#ffffff")
        self.model1_result_label.grid(row=2, column=0, padx=20, pady=(10, 0))

        self.model2_title = ttk.Label(self.model_frame, text="Filtros de audio y ML", background="#282c34", foreground="#ffffff")
        self.model2_title.grid(row=0, column=1, padx=20, pady=(0, 10))

        self.model2_image_label = ttk.Label(self.model_frame, background="#282c34")
        self.model2_image_label.grid(row=1, column=1, padx=20)

        self.model2_result_label = ttk.Label(self.model_frame, text="Resultado del Modelo 2", background="#282c34", foreground="#ffffff")
        self.model2_result_label.grid(row=2, column=1, padx=20, pady=(10, 0))

        self.features_label = ttk.Label(self.model_frame, text="Features que afectaron el resultado:", background="#282c34", foreground="#ffffff")
        self.features_label.grid(row=3, column=1, padx=20, pady=(10, 0))

        self.features_text = tk.Text(self.model_frame, height=6, width=40, bg="#282c34", fg="#ffffff", wrap="word", relief="flat", borderwidth=0)
        self.features_text.grid(row=4, column=1, padx=20, pady=(0, 10))

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
        model1_result, model2_result, features = self.simulate_models(file_path)
        self.progress.stop()
        self.model1_result_label.config(text=f"Modelo 1: {model1_result}% IA generada")
        self.model2_result_label.config(text=f"Modelo 2: {model2_result}% IA generada")
        self.features_text.delete('1.0', tk.END)
        self.features_text.insert(tk.END, features)
        self.animate_result()

    def simulate_models(self, file_path):
        model1_result = random.randint(30, 70)  # Simulación de resultado del Modelo 1
        model2_result = random.randint(30, 70)  # Simulación de resultado del Modelo 2
        resultado1 = random.uniform(0, 1)
        resultado2 = random.uniform(0, 1-resultado1)
        resultado3 = random.uniform(0, resultado1-resultado2)
        resultado4 = random.uniform(0, resultado2-resultado3)
        resultado5 = random.uniform(0, resultado3-resultado4)
        resultado6 = random.uniform(0, resultado4-resultado5)
        
        features = (
            f"MFCCs: {resultado1:2f}\n"
            f"Chroma: {resultado2:.2f}\n"
            f"Spectral Contrast: {resultado3:.2f}\n"
            f"Zero-Crossing Rate: {resultado4:.2f}\n"
            f"RMS Energy: {resultado5:.2f}\n"
            f"Spectral Centroid: {resultado6:.2f}\n"
            f"Spectral Bandwidth: {resultado1:.2f}\n"
            f"Fundamental Frequency: {resultado1:.2f}\n"
            f"Harmonic-to-Noise Ratio: {resultado1:.2f}\n"
            f"Formant Frequencies: {resultado1:.2f}"
        )
        return model1_result, model2_result, features

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
