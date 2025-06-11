#!/usr/bin/env python3
"""
Crea tutti i file necessari per OrtoIoT-AI
"""
import os
import json
from datetime import datetime
from pathlib import Path


def create_all_files():
    """Crea tutti i file necessari"""
    print("🌱 Creazione file OrtoIoT-AI...")

    # 1. requirements.txt
    requirements = """# OrtoIoT-AI Dependencies
Pillow>=10.0.0
pandas>=2.0.0
numpy>=1.24.0
tqdm>=4.65.0
"""

    # 2. config.json
    config = {
        "application": {
            "name": "OrtoIoT-AI Dataset Creator",
            "version": "1.0.0",
            "description": "Professional tool for creating plant disease datasets"
        },
        "window": {
            "title": "OrtoIoT-AI Dataset Creator",
            "width": 1200,
            "height": 800
        },
        "paths": {
            "diseases_db": "data/diseases/diseases.json",
            "images_dir": "data/images",
            "exports_dir": "data/exports"
        }
    }

    # 3. Database di esempio
    diseases_db = {
        "plant_diseases": {
            "PWM001": {
                "id": "PWM001",
                "name": "Powdery Mildew",
                "category": "Fungal Diseases",
                "description": "White powdery substance on leaf surfaces",
                "symptoms": ["White powder on leaves", "Yellowing", "Stunted growth"],
                "treatments": ["Baking soda solution", "Neem oil", "Improve air circulation"],
                "severity": "High",
                "image_count": 0
            },
            "SPM001": {
                "id": "SPM001",
                "name": "Spider Mites",
                "category": "Pests",
                "description": "Small pests that cause leaf damage",
                "symptoms": ["Small spots on leaves", "Webbing", "Yellowing"],
                "treatments": ["Neem oil", "Predatory mites", "Increase humidity"],
                "severity": "Very High",
                "image_count": 0
            },
            "HLT001": {
                "id": "HLT001",
                "name": "Healthy Plant",
                "category": "Healthy",
                "description": "No signs of disease",
                "symptoms": ["Green leaves", "No spots", "Healthy growth"],
                "treatments": ["Regular care", "Proper nutrition", "Good watering"],
                "severity": "None",
                "image_count": 0
            }
        },
        "metadata": {
            "version": "1.0.0",
            "created": datetime.now().isoformat(),
            "disease_count": 3
        }
    }

    # 4. App principale semplice
    app_code = '''"""
OrtoIoT-AI Dataset Creator - Versione Semplice
"""
import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime

class OrtoIoTApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("OrtoIoT-AI Dataset Creator")
        self.root.geometry("1000x700")
        
        # Carica configurazione
        self.load_config()
        self.load_database()
        
        # Crea interfaccia
        self.create_ui()
    
    def load_config(self):
        """Carica configurazione"""
        try:
            with open('config.json', 'r') as f:
                self.config = json.load(f)
        except:
            self.config = {"application": {"name": "OrtoIoT-AI"}}
    
    def load_database(self):
        """Carica database malattie"""
        try:
            with open('data/diseases/diseases.json', 'r') as f:
                data = json.load(f)
                self.diseases = data.get('plant_diseases', {})
        except:
            self.diseases = {}
    
    def create_ui(self):
        """Crea interfaccia utente"""
        # Titolo
        title = ttk.Label(self.root, text="🌱 OrtoIoT-AI Dataset Creator", 
                         font=("Helvetica", 18, "bold"))
        title.pack(pady=20)
        
        # Notebook per le schede
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Tab 1: Database Malattie
        self.create_diseases_tab()
        
        # Tab 2: Collezione Immagini  
        self.create_images_tab()
        
        # Tab 3: Export Dataset
        self.create_export_tab()
        
        # Tab 4: Info
        self.create_info_tab()
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready - OrtoIoT-AI Dataset Creator")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, 
                              relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(fill=tk.X, side=tk.BOTTOM, padx=5, pady=2)
    
    def create_diseases_tab(self):
        """Crea tab gestione malattie"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Disease Database")
        
        # Titolo
        ttk.Label(frame, text="Plant Disease Database", 
                 font=("Helvetica", 14, "bold")).pack(pady=10)
        
        # Lista malattie
        list_frame = ttk.LabelFrame(frame, text="Current Diseases")
        list_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Treeview per malattie
        columns = ("Name", "Category", "Severity", "Images")
        self.diseases_tree = ttk.Treeview(list_frame, columns=columns, show="headings")
        
        for col in columns:
            self.diseases_tree.heading(col, text=col)
            self.diseases_tree.column(col, width=150)
        
        self.diseases_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Carica malattie
        self.refresh_diseases_list()
        
        # Pulsanti
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(fill=tk.X, padx=20, pady=10)
        
        ttk.Button(btn_frame, text="Add Disease", 
                  command=self.add_disease).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Import JSON", 
                  command=self.import_json).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Refresh", 
                  command=self.refresh_diseases_list).pack(side=tk.LEFT, padx=5)
    
    def create_images_tab(self):
        """Crea tab collezione immagini"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Image Collection")
        
        ttk.Label(frame, text="Image Collection & Organization", 
                 font=("Helvetica", 14, "bold")).pack(pady=20)
        
        info_text = """
        📸 Image Collection Features:
        
        • Drag-and-drop image importing
        • Batch processing capabilities
        • Automatic organization by disease type
        • Image quality validation
        • Duplicate detection
        
        🔧 Coming Soon:
        • Advanced image tools
        • Annotation capabilities
        • Quality assessment
        """
        
        ttk.Label(frame, text=info_text, justify=tk.LEFT).pack(pady=20)
        
        # Statistiche
        stats_frame = ttk.LabelFrame(frame, text="Dataset Statistics")
        stats_frame.pack(fill=tk.X, padx=20, pady=10)
        
        stats_text = f"Total Diseases: {len(self.diseases)}\\nTotal Images: 0"
        ttk.Label(stats_frame, text=stats_text).pack(pady=10)
    
    def create_export_tab(self):
        """Crea tab export dataset"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Dataset Export")
        
        ttk.Label(frame, text="Dataset Export", 
                 font=("Helvetica", 14, "bold")).pack(pady=20)
        
        export_info = """
        📊 Export Formats Available:
        
        • COCO Format (JSON) - Standard for object detection
        • YOLO Format (TXT) - Popular for real-time detection  
        • Pascal VOC (XML) - Traditional annotation format
        • CSV Format - Tabular data export
        • Custom JSON - Flexible custom format
        
        🚀 Export your dataset for ML training!
        """
        
        ttk.Label(frame, text=export_info, justify=tk.LEFT).pack(pady=20)
        
        # Pulsanti export
        export_frame = ttk.LabelFrame(frame, text="Export Options")
        export_frame.pack(fill=tk.X, padx=20, pady=10)
        
        btn_frame = ttk.Frame(export_frame)
        btn_frame.pack(pady=10)
        
        ttk.Button(btn_frame, text="Export COCO", 
                  command=lambda: self.export_dataset("COCO")).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Export YOLO", 
                  command=lambda: self.export_dataset("YOLO")).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Export CSV", 
                  command=lambda: self.export_dataset("CSV")).pack(side=tk.LEFT, padx=5)
    
    def create_info_tab(self):
        """Crea tab informazioni"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Documentation")
        
        ttk.Label(frame, text="OrtoIoT-AI Documentation", 
                 font=("Helvetica", 14, "bold")).pack(pady=10)
        
        # Text widget con scroll
        text_frame = ttk.Frame(frame)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        text_widget = tk.Text(text_frame, wrap=tk.WORD, font=("Courier", 10))
        scrollbar = ttk.Scrollbar(text_frame, orient=tk.VERTICAL, command=text_widget.yview)
        text_widget.configure(yscrollcommand=scrollbar.set)
        
        documentation = """
ORTOIOT-AI DATASET CREATOR
==========================

Welcome to OrtoIoT-AI Dataset Creator - Professional tool for creating 
plant disease datasets for machine learning applications.

GETTING STARTED:
1. Disease Database: Add and manage plant diseases
2. Image Collection: Import and organize disease images
3. Dataset Export: Export in ML-ready formats

KEY FEATURES:
• Professional disease database management
• Multiple export formats (COCO, YOLO, Pascal VOC)
• Dataset statistics and validation
• Extensible architecture

WORKFLOW:
1. Add diseases with detailed information
2. Collect images for each disease category  
3. Validate dataset quality
4. Export in preferred ML format

EXPORT FORMATS:
• COCO: Standard JSON format for object detection
• YOLO: Text-based format for real-time detection
• Pascal VOC: XML annotation format
• CSV: Tabular data for analysis

COMMUNITY:
• Website: www.ortoiot.com
• Discord: https://discord.gg/nYakDDmE5s
• GitHub: https://github.com/ortoiot/ortoiot-ai

This tool is designed for researchers, developers, and agricultural 
professionals working on AI-powered plant disease detection.

Built with ❤️ by the OrtoIoT Team
        """
        
        text_widget.insert(tk.END, documentation)
        text_widget.config(state=tk.DISABLED)
        
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    def refresh_diseases_list(self):
        """Aggiorna lista malattie"""
        # Pulisci lista
        for item in self.diseases_tree.get_children():
            self.diseases_tree.delete(item)
        
        # Aggiungi malattie
        for disease_id, disease in self.diseases.items():
            self.diseases_tree.insert("", tk.END, values=(
                disease.get("name", ""),
                disease.get("category", ""),
                disease.get("severity", ""),
                disease.get("image_count", 0)
            ))
    
    def add_disease(self):
        """Aggiungi malattia"""
        messagebox.showinfo("Add Disease", "Add disease feature coming soon!\\n\\nFor now, you can import diseases from JSON files.")
    
    def import_json(self):
        """Importa da JSON"""
        messagebox.showinfo("Import JSON", "JSON import feature coming soon!\\n\\nYou can manually place JSON files in data/diseases/")
    
    def export_dataset(self, format_type):
        """Export dataset"""
        messagebox.showinfo("Export Dataset", f"{format_type} export feature coming soon!\\n\\nThis will export your dataset in {format_type} format.")
    
    def run(self):
        """Avvia applicazione"""
        self.root.mainloop()

def main():
    """Main entry point"""
    print("🌱 Starting OrtoIoT-AI Dataset Creator...")
    try:
        app = OrtoIoTApp()
        app.run()
    except Exception as e:
        print(f"Error: {e}")
        messagebox.showerror("Error", f"Application error: {str(e)}")

if __name__ == "__main__":
    main()
'''

    # 5. Launcher Windows
    launcher_bat = '''@echo off
echo.
echo ================================
echo   OrtoIoT-AI Dataset Creator
echo ================================
echo.

if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

echo Activating virtual environment...
call venv\\Scripts\\activate

echo Installing/updating dependencies...
pip install -r requirements.txt

echo.
echo Starting OrtoIoT-AI...
python app.py

echo.
echo Application closed.
pause
'''

    # Scrivi tutti i file
    files = {
        'requirements.txt': requirements,
        'config.json': json.dumps(config, indent=2),
        'app.py': app_code,
        'launch.bat': launcher_bat
    }

    print("📝 Creazione file...")
    for filename, content in files.items():
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ {filename}")

    # Crea database
    os.makedirs('data/diseases', exist_ok=True)
    with open('data/diseases/diseases.json', 'w', encoding='utf-8') as f:
        json.dump(diseases_db, f, indent=2, ensure_ascii=False)
    print(f"  ✓ data/diseases/diseases.json")

    # Crea directories vuote
    dirs = ['data/images', 'data/exports', 'data/backups', 'logs', 'temp']
    for directory in dirs:
        os.makedirs(directory, exist_ok=True)
        Path(f"{directory}/.gitkeep").touch()

    print("\n" + "="*50)
    print("✅ ORTOIOT-AI PRONTO!")
    print("="*50)
    print("\n🚀 PER AVVIARE:")
    print("1. Doppio click su: launch.bat")
    print("2. Oppure: python app.py")
    print("\n🌟 CARATTERISTICHE:")
    print("• 3 malattie di esempio")
    print("• Interfaccia professionale")
    print("• 4 tab funzionali")
    print("• Pronto per lo sviluppo")
    print("\n🔗 COMMUNITY:")
    print("• Website: www.ortoiot.com")
    print("• Discord: discord.gg/nYakDDmE5s")
    print("\nBuon lavoro! 🌱🤖")


if __name__ == "__main__":
    create_all_files()
