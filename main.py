import customtkinter as ctk
from clicker import AutoClicker
import threading

# Paramètres de base de CustomTkinter
ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuration de la fenêtre principale
        self.title("Auto Clicker Premium")
        self.geometry("400x350")
        self.resizable(False, False)
        
        # Initialisation de l'intervalle par défaut (30 secondes)
        self.delay = 30.0
        
        # Initialisation du thread du clicker
        self.click_thread = AutoClicker(self.delay)
        self.click_thread.start()
        
        # UI Elements
        self.setup_ui()

    def setup_ui(self):
        # Titre
        self.title_label = ctk.CTkLabel(
            self, 
            text="AUTO CLICKER", 
            font=ctk.CTkFont(family="Inter", size=32, weight="bold")
        )
        self.title_label.pack(pady=(30, 10))

        # Sous-titre / Statut
        self.status_label = ctk.CTkLabel(
            self, 
            text="Prêt. En attente...", 
            font=ctk.CTkFont(size=14),
            text_color="gray"
        )
        self.status_label.pack(pady=(0, 20))

        # Frame pour l'intervalle
        self.interval_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.interval_frame.pack(pady=10)

        self.interval_label = ctk.CTkLabel(
            self.interval_frame, 
            text="Intervalle (secondes) :", 
            font=ctk.CTkFont(size=16)
        )
        self.interval_label.pack(side="left", padx=(0, 10))

        # Champ de saisie pour l'intervalle
        self.interval_entry = ctk.CTkEntry(
            self.interval_frame, 
            width=80,
            justify="center",
            font=ctk.CTkFont(size=16)
        )
        self.interval_entry.insert(0, str(int(self.delay)))
        self.interval_entry.pack(side="left")

        # Bouton principal Start/Stop
        self.action_button = ctk.CTkButton(
            self,
            text="▶ DÉMARRER",
            command=self.toggle_clicking,
            font=ctk.CTkFont(size=20, weight="bold"),
            height=60,
            width=250,
            corner_radius=30,
            fg_color="#2E8B57", # Beau vert doux
            hover_color="#226B42"
        )
        self.action_button.pack(pady=30)
        
    def get_delay_from_entry(self):
        try:
            val = float(self.interval_entry.get())
            if val <= 0:
                val = 0.1 # Minimum sécurité
            return val
        except ValueError:
            # Si invalide, on remet l'affichage à la dernière valeur correcte
            self.interval_entry.delete(0, 'end')
            self.interval_entry.insert(0, str(int(self.delay)))
            return self.delay

    def toggle_clicking(self):
        if not self.click_thread.running:
            # Démarrer
            self.delay = self.get_delay_from_entry()
            self.click_thread.set_delay(self.delay)
            self.click_thread.start_clicking()
            
            # Update UI
            self.action_button.configure(
                text="⏹ ARRÊTER",
                fg_color="#CD5C5C", # Beau rouge doux
                hover_color="#A52A2A"
            )
            self.status_label.configure(
                text=f"En cours : Clic toutes les {self.delay} s",
                text_color="#2E8B57" # Vert
            )
            self.interval_entry.configure(state="disabled")
        else:
            # Arrêter
            self.click_thread.stop_clicking()
            
            # Update UI
            self.action_button.configure(
                text="▶ DÉMARRER",
                fg_color="#2E8B57", # Beau vert doux
                hover_color="#226B42"
            )
            self.status_label.configure(
                text="En pause.",
                text_color="gray"
            )
            self.interval_entry.configure(state="normal")
            
    def on_closing(self):
        # Gérer la fermeture de l'application proprement
        self.click_thread.exit()
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
