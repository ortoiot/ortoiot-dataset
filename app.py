"""
OrtoIoT-AI Dataset Creator - VERSIONE DEFINITIVA CORRETTA
Applicazione completa con tutte le malattie e sistema facile per aggiungere foto
"""
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import os
import shutil
import uuid
from datetime import datetime
from pathlib import Path


class OrtoIoTApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("OrtoIoT-AI Dataset Creator")
        self.root.geometry("1200x800")

        # Inizializza attributi
        self.selected_photos = []
        self.disease_combo = None  # Inizializza per evitare errori
        self.diseases_tree = None
        self.disease_details = None

        # Carica configurazione e database
        self.load_config()
        self.load_database()

        # Crea interfaccia
        self.create_ui()

        # Aggiorna liste DOPO che tutti i componenti sono stati creati
        self.refresh_diseases_list()

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
            # Se non esiste, crea database completo
            self.create_complete_database()

    def create_complete_database(self):
        """Crea database completo con TUTTE le malattie dal tuo JSON originale"""
        print("📊 Creating complete disease database...")

        # Database completo con tutte le malattie dal tuo JSON originale
        self.diseases = {
            "OID001": {
                "id": "OID001",
                "name": "Powdery Mildew",
                "category": "Fungal Diseases",
                "description": "Powdery mildew is one of the most common fungal diseases in cannabis. It appears as a white powdery substance on leaf surfaces and can spread rapidly under high humidity and poor air circulation conditions.",
                "symptoms": [
                    "White powdery substance on leaf surfaces",
                    "Circular white spots that expand and merge",
                    "Progressive yellowing",
                    "Stunted growth",
                    "Possible leaf deformation"
                ],
                "treatments": [
                    "Baking soda solution (1 tsp per liter with soap drops)",
                    "Neem oil spray (diluted according to instructions)",
                    "Diluted milk (1 part milk, 9 parts water) sprayed on leaves",
                    "Improve air circulation",
                    "Reduce environmental humidity"
                ],
                "severity": "High",
                "reversibility": "Good if treated early",
                "image_count": 0
            },
            "BOT001": {
                "id": "BOT001",
                "name": "Gray Mold (Botrytis)",
                "category": "Fungal Diseases",
                "description": "Gray mold or Botrytis is a particularly dangerous fungus during flowering. It mainly affects dense buds and develops from inside out, making early detection difficult.",
                "symptoms": [
                    "Grayish or brown buds",
                    "Decaying plant tissue",
                    "Wet rot",
                    "Gray spores",
                    "Soft, dark stems",
                    "Moldy odor"
                ],
                "treatments": [
                    "Remove all infected parts immediately",
                    "Drastically reduce environmental humidity",
                    "Increase ventilation",
                    "Isolate affected plants",
                    "Biological treatments with Bacillus subtilis"
                ],
                "severity": "Very High",
                "reversibility": "Low - infected parts not recoverable",
                "image_count": 0
            },
            "SPM001": {
                "id": "SPM001",
                "name": "Spider Mites",
                "category": "Pests",
                "description": "Spider mites are small arachnids that cause significant damage to cannabis plants by sucking sap from leaves, causing yellowing spots and discoloration. They multiply rapidly and can cause serious damage in a short time.",
                "symptoms": [
                    "Small white/yellow spots on leaves (stippling)",
                    "Fine webbing on undersides of leaves or between branches",
                    "Small moving dots visible with magnification",
                    "Progressive yellowing",
                    "Bronzing",
                    "Premature leaf drop"
                ],
                "treatments": [
                    "Neem oil spray",
                    "Natural predators like predatory mites",
                    "Maintain high humidity (mites prefer dry conditions)",
                    "Isolate infected plants",
                    "High-pressure water spray on leaf undersides",
                    "Specific acaricides in severe cases"
                ],
                "severity": "Very High",
                "reversibility": "Medium - damaged leaves don't recover",
                "image_count": 0
            },
            "ND001": {
                "id": "ND001",
                "name": "Nitrogen Deficiency",
                "category": "Nutritional Deficiencies",
                "description": "Nitrogen is an essential macronutrient for cannabis plant growth. It's necessary for chlorophyll formation, proteins and amino acids. Nitrogen deficiency limits vegetative growth and reduces final yield.",
                "symptoms": [
                    "Yellowing of older/lower leaves",
                    "Stunted growth",
                    "Light green coloration",
                    "Premature leaf drop",
                    "Thin, weak stems",
                    "Possible reddish stems"
                ],
                "treatments": [
                    "Nitrogen-rich fertilizers",
                    "Organic compost or manure",
                    "Blood meal or fish emulsion",
                    "Liquid fish-based fertilizers",
                    "Correct soil pH (ideally 6.0-7.0)"
                ],
                "severity": "Medium",
                "reversibility": "Good - new growth normal after correction",
                "image_count": 0
            },
            "APH001": {
                "id": "APH001",
                "name": "Aphid Infestation",
                "category": "Pests",
                "description": "Aphids are small sucking insects that feed on cannabis plant sap. They reproduce rapidly and can form large colonies, weakening the plant and potentially transmitting viral diseases.",
                "symptoms": [
                    "Visible insects on stems and leaves",
                    "Sticky honeydew",
                    "Curled leaves",
                    "Stunted growth",
                    "Yellowing leaves",
                    "Black sooty mold",
                    "Presence of ants"
                ],
                "treatments": [
                    "High-pressure water spray to remove aphids",
                    "Insecticidal soap",
                    "Neem oil",
                    "Natural predators like ladybugs or lacewings",
                    "Systemic insecticides in severe cases (vegetative stage only)"
                ],
                "severity": "Medium-High",
                "reversibility": "Good if treated early",
                "image_count": 0
            },
            "CAT001": {
                "id": "CAT001",
                "name": "Caterpillar Infestation",
                "category": "Pests",
                "description": "Caterpillars are larvae of butterflies and moths that feed on leaves and can cause significant damage to cannabis crops.",
                "symptoms": [
                    "Holes in leaves",
                    "Eaten leaf margins",
                    "Dark droppings on leaves (frass)",
                    "Visible caterpillars",
                    "Damage to buds during flowering",
                    "Skeletonized leaves"
                ],
                "treatments": [
                    "Manual removal of caterpillars",
                    "Bacillus thuringiensis (Bt)",
                    "Natural predators like parasitoid wasps",
                    "Moth traps for adults",
                    "Biological insecticides in extreme cases"
                ],
                "severity": "Medium-High",
                "reversibility": "Good if treated early",
                "image_count": 0
            },
            "BLR001": {
                "id": "BLR001",
                "name": "Black Rot",
                "category": "Fungal Diseases",
                "description": "Black rot is a fungal disease that causes black spots on leaves and can spread to stems and roots, leading to plant death.",
                "symptoms": [
                    "Black or dark brown spots on leaves",
                    "Lesions that expand and merge",
                    "Wilting and dying leaves",
                    "Stems turning black",
                    "Root rot",
                    "Unpleasant odor"
                ],
                "treatments": [
                    "Improve drainage",
                    "Avoid excessive watering",
                    "Remove and destroy infected parts",
                    "Copper-based fungicides",
                    "Increase air circulation"
                ],
                "severity": "High",
                "reversibility": "Low - infected parts not recoverable",
                "image_count": 0
            },
            "HLT001": {
                "id": "HLT001",
                "name": "Healthy Plant",
                "category": "Healthy State",
                "description": "Healthy plant with no visible signs of disease, pests, or nutritional deficiencies.",
                "symptoms": [
                    "Uniform green coloration",
                    "No spots or discoloration",
                    "Intact leaf structure",
                    "Vigorous growth",
                    "Regular leaf margins",
                    "No visible pests"
                ],
                "treatments": [
                    "Maintain balanced nutrition",
                    "Proper watering schedule",
                    "Optimal lighting conditions",
                    "Preventive pest monitoring",
                    "Regular plant inspection",
                    "Good air circulation"
                ],
                "severity": "None",
                "reversibility": "Optimal",
                "image_count": 0
            },
            "RR001": {
                "id": "RR001",
                "name": "Root Rot",
                "category": "Fungal Diseases",
                "description": "Root rot is a condition caused by various fungal pathogens that attack the cannabis root system, preventing water and nutrient absorption. It's often associated with excessive substrate moisture.",
                "symptoms": [
                    "Wilting despite adequate watering",
                    "Stunted growth",
                    "Yellowing leaves",
                    "Dark, mushy roots",
                    "Leaves dying from bottom up",
                    "Unpleasant odor from roots"
                ],
                "treatments": [
                    "Immediately reduce watering",
                    "Improve drainage",
                    "Apply Trichoderma or other biological agents",
                    "Transplant to fresh soil in severe cases",
                    "Avoid water stagnation"
                ],
                "severity": "Very High",
                "reversibility": "Low in advanced cases",
                "image_count": 0
            },
            "NB001": {
                "id": "NB001",
                "name": "Nutrient Burn",
                "category": "Cultivation Errors",
                "description": "Nutrient burn occurs when plants receive excess fertilizers, causing salt buildup in substrate. This leads to reduced ability to absorb water and nutrients through osmotic stress.",
                "symptoms": [
                    "Brown leaf tips",
                    "Burned leaf edges",
                    "Claw-shaped leaves",
                    "Very dark leaves",
                    "Stunted growth",
                    "Salt accumulation in soil"
                ],
                "treatments": [
                    "Flush thoroughly with pH-corrected pure water",
                    "Stop nutrient administration",
                    "Reduce nutrient concentration when resuming",
                    "Monitor solution EC",
                    "Maintain regular flushing schedule"
                ],
                "severity": "Medium-High",
                "reversibility": "Good if treated early",
                "image_count": 0
            },
            "THR001": {
                "id": "THR001",
                "name": "Thrips",
                "category": "Pests",
                "description": "Thrips are small sucking insects that damage cannabis plants by scraping leaf and flower surfaces to feed on cellular fluids. They're particularly harmful during flowering as they can directly infest buds.",
                "symptoms": [
                    "Silver spots on leaves",
                    "Black droppings on leaves",
                    "Deformed leaves",
                    "Small yellow or brown insects",
                    "Damage to buds",
                    "Stunted growth"
                ],
                "treatments": [
                    "Natural predators like Orius insidiosus",
                    "Neem oil spray",
                    "Insecticidal soap solution",
                    "Spinosad",
                    "Blue sticky traps for monitoring and capture"
                ],
                "severity": "High",
                "reversibility": "Medium - flower damage not recoverable",
                "image_count": 0
            },
            "NL001": {
                "id": "NL001",
                "name": "Nutrient Lockout (pH Error)",
                "category": "Cultivation Errors",
                "description": "Nutrient lockout occurs when nutrient uptake is compromised due to inadequate pH in the root zone. Each nutrient has an optimal pH range for absorption.",
                "symptoms": [
                    "Multiple simultaneous deficiencies",
                    "Stunted growth",
                    "Various yellowing patterns",
                    "Leaf necrosis",
                    "Burned tips",
                    "Deformed leaves"
                ],
                "treatments": [
                    "Flush with pH-corrected water",
                    "Measure and correct irrigation water pH",
                    "Use natural or chemical pH regulators",
                    "Reintroduce nutrients only after pH stabilization",
                    "Regularly monitor runoff pH"
                ],
                "severity": "High",
                "reversibility": "Good if corrected quickly",
                "image_count": 0
            },
            "CA001": {
                "id": "CA001",
                "name": "Calcium Deficiency",
                "category": "Nutritional Deficiencies",
                "description": "Calcium is an essential nutrient for cannabis, fundamental for cell structure, cell division and cell wall stability. Calcium deficiency can cause significant problems in plant structure and growth.",
                "symptoms": [
                    "Brown spots on new leaves",
                    "Deformed or curled leaves",
                    "Damaged growth tips",
                    "Burned leaf edges",
                    "Weak stems",
                    "Stunted growth"
                ],
                "treatments": [
                    "Apply calcium supplements (Cal-Mag)",
                    "Correct pH to 6.2-7.0 in soil, 5.5-6.5 in hydroponics",
                    "Foliar calcium sprays for quick results",
                    "Avoid excess potassium and magnesium",
                    "Add dolomitic lime to soil"
                ],
                "severity": "High",
                "reversibility": "Medium - existing damage permanent",
                "image_count": 0
            },
            "MG001": {
                "id": "MG001",
                "name": "Magnesium Deficiency",
                "category": "Nutritional Deficiencies",
                "description": "Magnesium is an essential component of chlorophyll and enzyme activator. Its deficiency is common in cannabis and manifests with characteristic interveinal yellowing in older leaves.",
                "symptoms": [
                    "Interveinal yellowing (veins remain green)",
                    "Starts from older/lower leaves",
                    "Progression from edge to center of leaf",
                    "Possible purple or reddish tints",
                    "Leaf edges may dry out",
                    "Leaves become brittle and break easily"
                ],
                "treatments": [
                    "Apply magnesium supplement (Epsom salt)",
                    "Dilute 1-2 grams Epsom salt per liter water",
                    "Correct pH to 6.0-6.5 in soil, 5.5-6.0 in hydroponics",
                    "Use complete Cal-Mag supplement",
                    "Apply foliar spray for faster absorption",
                    "Avoid excess potassium and calcium"
                ],
                "severity": "Medium",
                "reversibility": "Good - responds quickly to treatment",
                "image_count": 0
            },
            "OVW001": {
                "id": "OVW001",
                "name": "Overwatering",
                "category": "Cultivation Errors",
                "description": "Overwatering is one of the most common problems in cannabis cultivation. It causes substrate saturation, reducing oxygen available to roots and promoting fungal diseases.",
                "symptoms": [
                    "Leaves become swollen and droop downward",
                    "Slow or stagnant growth",
                    "General yellowing of plant",
                    "Soil remains constantly wet",
                    "Possible algae formation on soil surface",
                    "Moldy or stagnant soil odor"
                ],
                "treatments": [
                    "Immediately reduce watering frequency",
                    "Ensure pots have good drainage",
                    "Allow soil to dry between waterings",
                    "Transplant to fresh, well-draining soil in severe cases",
                    "Add perlite to soil to improve drainage",
                    "Avoid saucers with standing water"
                ],
                "severity": "Medium",
                "reversibility": "Good if corrected quickly",
                "image_count": 0
            }
        }

        # Salva database
        self.save_database()
        print(
            f"✅ Created complete database with {len(self.diseases)} diseases")

    def save_database(self):
        """Salva database"""
        try:
            os.makedirs('data/diseases', exist_ok=True)
            data = {
                'plant_diseases': self.diseases,
                'metadata': {
                    'version': '1.0.0',
                    'updated': datetime.now().isoformat(),
                    'disease_count': len(self.diseases)
                }
            }
            with open('data/diseases/diseases.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save database: {str(e)}")
            return False

    def create_ui(self):
        """Crea interfaccia utente"""
        # Titolo
        title = ttk.Label(self.root, text="🌱 OrtoIoT-AI Dataset Creator",
                          font=("Helvetica", 18, "bold"))
        title.pack(pady=10)

        # Notebook
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Crea tutti i tab
        self.create_diseases_tab()
        self.create_photos_tab()
        self.create_export_tab()
        self.create_info_tab()

        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set(f"Ready - {len(self.diseases)} diseases loaded!")
        status_bar = ttk.Label(self.root, textvariable=self.status_var,
                               relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(fill=tk.X, side=tk.BOTTOM, padx=5, pady=2)

    def create_diseases_tab(self):
        """Tab gestione malattie"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="🗃️ Disease Database")

        # Pannello principale
        paned = ttk.PanedWindow(frame, orient=tk.HORIZONTAL)
        paned.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Lista malattie (sinistra)
        left_frame = ttk.LabelFrame(paned, text="Diseases List")
        paned.add(left_frame, weight=1)

        columns = ("Name", "Category", "Images")
        self.diseases_tree = ttk.Treeview(
            left_frame, columns=columns, show="headings", height=15)

        for col in columns:
            self.diseases_tree.heading(col, text=col)
            self.diseases_tree.column(col, width=120)

        tree_scroll = ttk.Scrollbar(
            left_frame, orient=tk.VERTICAL, command=self.diseases_tree.yview)
        self.diseases_tree.configure(yscrollcommand=tree_scroll.set)

        self.diseases_tree.pack(
            side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.diseases_tree.bind('<<TreeviewSelect>>', self.on_disease_select)

        # Dettagli malattia (destra)
        right_frame = ttk.LabelFrame(paned, text="Disease Details")
        paned.add(right_frame, weight=1)

        self.disease_details = tk.Text(
            right_frame, wrap=tk.WORD, height=20, width=40)
        details_scroll = ttk.Scrollbar(
            right_frame, orient=tk.VERTICAL, command=self.disease_details.yview)
        self.disease_details.configure(yscrollcommand=details_scroll.set)

        self.disease_details.pack(
            side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        details_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        # Pulsanti
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(fill=tk.X, padx=10, pady=5)

        ttk.Button(btn_frame, text="📊 Update Counts",
                   command=self.update_image_counts).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="🔄 Refresh",
                   command=self.refresh_diseases_list).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="📁 Open Folder",
                   command=self.open_disease_folder).pack(side=tk.LEFT, padx=5)

        # NON chiamare refresh qui - lo faremo dopo che tutto è inizializzato

    def create_photos_tab(self):
        """Tab per aggiungere foto - SUPER FACILE"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="📸 Add Photos")

        # Istruzioni
        instructions = ttk.LabelFrame(
            frame, text="📋 How to Add Photos (Super Easy!)")
        instructions.pack(fill=tk.X, padx=10, pady=5)

        instruction_text = """
        1️⃣ Click "Browse Photos" to select your image files
        2️⃣ Choose the disease from the dropdown menu  
        3️⃣ Click "Save Photos" → Done! Photos automatically organized! ✅
        """
        ttk.Label(instructions, text=instruction_text, font=(
            "Helvetica", 10)).pack(padx=10, pady=10)

        # Selezione foto
        photo_frame = ttk.LabelFrame(frame, text="📷 Select Your Photos")
        photo_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Pulsanti browse
        btn_frame = ttk.Frame(photo_frame)
        btn_frame.pack(fill=tk.X, padx=10, pady=10)

        ttk.Button(btn_frame, text="📁 Browse Single Photo",
                   command=self.browse_single_photo, width=20).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="📂 Browse Multiple Photos",
                   command=self.browse_multiple_photos, width=20).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="🗑️ Clear Selection",
                   command=self.clear_selection, width=15).pack(side=tk.LEFT, padx=5)

        # Lista foto selezionate
        list_frame = ttk.Frame(photo_frame)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        ttk.Label(list_frame, text="Selected Photos:", font=(
            "Helvetica", 10, "bold")).pack(anchor=tk.W)

        self.photos_listbox = tk.Listbox(list_frame, height=8)
        photos_scroll = ttk.Scrollbar(
            list_frame, orient=tk.VERTICAL, command=self.photos_listbox.yview)
        self.photos_listbox.configure(yscrollcommand=photos_scroll.set)

        self.photos_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        photos_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        # Selezione malattia e salvataggio
        action_frame = ttk.LabelFrame(frame, text="🏷️ Choose Disease & Save")
        action_frame.pack(fill=tk.X, padx=10, pady=5)

        select_frame = ttk.Frame(action_frame)
        select_frame.pack(fill=tk.X, padx=10, pady=10)

        ttk.Label(select_frame, text="Disease:", font=(
            "Helvetica", 10, "bold")).pack(side=tk.LEFT, padx=5)

        self.disease_combo = ttk.Combobox(
            select_frame, width=30, state="readonly", font=("Helvetica", 10))
        self.disease_combo.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

        self.save_btn = ttk.Button(select_frame, text="💾 Save Photos",
                                   command=self.save_photos, state=tk.DISABLED)
        self.save_btn.pack(side=tk.RIGHT, padx=5)

        # Statistiche
        self.stats_label = ttk.Label(
            action_frame, text="No photos selected", font=("Helvetica", 9))
        self.stats_label.pack(padx=10, pady=5)

    def create_export_tab(self):
        """Tab export dataset"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="📊 Export Dataset")

        ttk.Label(frame, text="Dataset Export & Statistics",
                  font=("Helvetica", 14, "bold")).pack(pady=10)

        # Statistiche
        stats_frame = ttk.LabelFrame(frame, text="📈 Dataset Statistics")
        stats_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        self.stats_text = tk.Text(
            stats_frame, height=20, width=80, font=("Courier", 9))
        stats_scroll = ttk.Scrollbar(
            stats_frame, orient=tk.VERTICAL, command=self.stats_text.yview)
        self.stats_text.configure(yscrollcommand=stats_scroll.set)

        self.stats_text.pack(side=tk.LEFT, fill=tk.BOTH,
                             expand=True, padx=5, pady=5)
        stats_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        # Pulsanti
        btn_frame = ttk.Frame(stats_frame)
        btn_frame.pack(fill=tk.X, padx=5, pady=5)

        ttk.Button(btn_frame, text="🔄 Update Statistics",
                   command=self.update_statistics).pack(side=tk.LEFT, padx=5)

        # Export
        export_frame = ttk.LabelFrame(frame, text="📋 Export Formats")
        export_frame.pack(fill=tk.X, padx=20, pady=10)

        export_btn_frame = ttk.Frame(export_frame)
        export_btn_frame.pack(pady=10)

        ttk.Button(export_btn_frame, text="📄 Export CSV",
                   command=self.export_csv).pack(side=tk.LEFT, padx=5)
        ttk.Button(export_btn_frame, text="📄 Export JSON",
                   command=self.export_json).pack(side=tk.LEFT, padx=5)

        # Aggiorna statistiche iniziali
        # Ritarda per permettere inizializzazione completa
        self.root.after(1000, self.update_statistics)

    def create_info_tab(self):
        """Tab informazioni"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="📚 Documentation")

        ttk.Label(frame, text="OrtoIoT-AI Documentation",
                  font=("Helvetica", 14, "bold")).pack(pady=10)

        text_frame = ttk.Frame(frame)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        text_widget = tk.Text(text_frame, wrap=tk.WORD, font=("Courier", 10))
        scrollbar = ttk.Scrollbar(
            text_frame, orient=tk.VERTICAL, command=text_widget.yview)
        text_widget.configure(yscrollcommand=scrollbar.set)

        documentation = f"""
ORTOIOT-AI DATASET CREATOR
==========================

🚀 QUICK START:
The app is loaded with {len(self.diseases)} professional plant diseases!

📸 ADDING PHOTOS (SUPER EASY):
1. Go to "Add Photos" tab
2. Click "Browse Multiple Photos" 
3. Select your photos
4. Choose disease from dropdown
5. Click "Save Photos" - Done! ✅

🗃️ DISEASES INCLUDED:
• Powdery Mildew
• Gray Mold (Botrytis) 
• Spider Mites
• Nitrogen Deficiency
• Aphid Infestation
• Caterpillar Infestation
• Black Rot
• Root Rot
• Nutrient Burn
• Thrips
• Nutrient Lockout
• Calcium Deficiency
• Magnesium Deficiency
• Overwatering
• Healthy Plant (reference)

📊 DATASET EXPORT:
• CSV format with all data
• JSON summary format
• Professional ML-ready datasets

💡 TIPS:
• Photos are automatically organized by disease
• Each disease gets its own folder
• Use good quality photos for best results
• Aim for 20+ photos per disease

🔗 COMMUNITY:
• Website: www.ortoiot.com
• Discord: https://discord.gg/nYakDDmE5s

Built with ❤️ by the OrtoIoT Team
Perfect for AI plant disease detection research!
        """

        text_widget.insert(tk.END, documentation)
        text_widget.config(state=tk.DISABLED)

        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Funzioni per gestione foto
    def browse_single_photo(self):
        """Seleziona una singola foto"""
        file_path = filedialog.askopenfilename(
            title="Select Photo",
            filetypes=[
                ("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff *.tif"), ("All files", "*.*")]
        )

        if file_path:
            self.selected_photos = [file_path]
            self.update_photo_display()
            self.status_var.set(
                f"Selected 1 photo: {os.path.basename(file_path)}")

    def browse_multiple_photos(self):
        """Seleziona più foto"""
        file_paths = filedialog.askopenfilenames(
            title="Select Multiple Photos",
            filetypes=[
                ("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff *.tif"), ("All files", "*.*")]
        )

        if file_paths:
            self.selected_photos = list(file_paths)
            self.update_photo_display()
            self.status_var.set(f"Selected {len(file_paths)} photos")

    def update_photo_display(self):
        """Aggiorna visualizzazione foto"""
        # Pulisci lista
        self.photos_listbox.delete(0, tk.END)

        # Aggiungi foto
        for photo_path in self.selected_photos:
            filename = os.path.basename(photo_path)
            self.photos_listbox.insert(tk.END, filename)

        # Abilita pulsante salva
        if self.selected_photos:
            self.save_btn.config(state=tk.NORMAL)
        else:
            self.save_btn.config(state=tk.DISABLED)

        # Aggiorna statistiche
        self.update_photo_stats()

    def update_photo_stats(self):
        """Aggiorna statistiche foto"""
        if not self.selected_photos:
            self.stats_label.config(text="No photos selected")
            return

        total_size = 0
        formats = {}

        for photo_path in self.selected_photos:
            try:
                total_size += os.path.getsize(photo_path)
                ext = os.path.splitext(photo_path)[1].lower()
                formats[ext] = formats.get(ext, 0) + 1
            except:
                pass

        size_mb = total_size / (1024 * 1024)
        formats_str = ", ".join(
            [f"{ext}({count})" for ext, count in formats.items()])

        self.stats_label.config(
            text=f"📊 {len(self.selected_photos)} photos | {size_mb:.2f} MB | {formats_str}")

    def clear_selection(self):
        """Pulisci selezione"""
        self.selected_photos = []
        self.update_photo_display()
        self.status_var.set("Selection cleared")

    def save_photos(self):
        """Salva foto nella malattia selezionata"""
        if not self.selected_photos:
            messagebox.showwarning("No Photos", "Please select photos first!")
            return

        disease_name = self.disease_combo.get()
        if not disease_name:
            messagebox.showwarning("No Disease", "Please select a disease!")
            return

        try:
            # Crea cartella malattia
            disease_dir = Path("data/images") / disease_name
            disease_dir.mkdir(parents=True, exist_ok=True)

            # Copia foto
            copied = 0
            for photo_path in self.selected_photos:
                try:
                    # Nome unico
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    unique_id = str(uuid.uuid4())[:8]
                    original_name = Path(photo_path).stem
                    extension = Path(photo_path).suffix

                    new_name = f"{original_name}_{timestamp}_{unique_id}{extension}"
                    dest_path = disease_dir / new_name

                    # Copia file
                    shutil.copy2(photo_path, dest_path)
                    copied += 1

                except Exception as e:
                    print(f"Error copying {photo_path}: {e}")

            # Aggiorna database
            self.update_disease_image_count(disease_name)

            # Feedback
            messagebox.showinfo("Success!",
                                f"✅ Successfully added {copied} photos to '{disease_name}'\\n\\n"
                                f"📁 Photos saved in: data/images/{disease_name}/")

            # Pulisci e aggiorna
            self.clear_selection()
            self.refresh_diseases_list()
            self.status_var.set(f"✅ Added {copied} photos to {disease_name}")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to save photos: {str(e)}")

    # Funzioni per gestione database
    def update_disease_combo(self):
        """Aggiorna dropdown malattie"""
        if self.disease_combo is None:  # Controllo di sicurezza
            return

        names = sorted([d.get('name', '') for d in self.diseases.values()])
        self.disease_combo['values'] = names
        if names:
            self.disease_combo.current(0)

    def refresh_diseases_list(self):
        """Aggiorna lista malattie"""
        if self.diseases_tree is None:  # Controllo di sicurezza
            return

        # Pulisci
        for item in self.diseases_tree.get_children():
            self.diseases_tree.delete(item)

        # Ricarica
        for disease in self.diseases.values():
            name = disease.get("name", "")
            category = disease.get("category", "")
            image_count = self.count_images(name)

            self.diseases_tree.insert(
                "", tk.END, values=(name, category, image_count))

        # Aggiorna combo solo se esiste
        self.update_disease_combo()

    def count_images(self, disease_name):
        """Conta immagini per malattia"""
        disease_dir = Path("data/images") / disease_name
        if not disease_dir.exists():
            return 0

        extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif'}
        count = 0

        try:
            for file_path in disease_dir.iterdir():
                if file_path.suffix.lower() in extensions:
                    count += 1
        except:
            pass

        return count

    def update_disease_image_count(self, disease_name):
        """Aggiorna conteggio nel database"""
        for disease in self.diseases.values():
            if disease.get('name') == disease_name:
                disease['image_count'] = self.count_images(disease_name)
                break
        self.save_database()

    def update_image_counts(self):
        """Aggiorna tutti i conteggi"""
        updated = 0
        for disease in self.diseases.values():
            name = disease.get('name', '')
            if name:
                old_count = disease.get('image_count', 0)
                new_count = self.count_images(name)
                disease['image_count'] = new_count
                if old_count != new_count:
                    updated += 1

        self.save_database()
        self.refresh_diseases_list()
        messagebox.showinfo(
            "Updated", f"Updated {updated} disease image counts")

    def on_disease_select(self, event):
        """Mostra dettagli malattia selezionata"""
        if self.diseases_tree is None or self.disease_details is None:
            return

        selection = self.diseases_tree.selection()
        if not selection:
            return

        item = self.diseases_tree.item(selection[0])
        disease_name = item['values'][0]

        for disease in self.diseases.values():
            if disease.get('name') == disease_name:
                self.show_disease_details(disease)
                break

    def show_disease_details(self, disease):
        """Mostra dettagli completi malattia"""
        if self.disease_details is None:
            return

        self.disease_details.config(state=tk.NORMAL)
        self.disease_details.delete(1.0, tk.END)

        details = f"""🏷️ NAME: {disease.get('name', 'N/A')}

📂 CATEGORY: {disease.get('category', 'N/A')}

📝 DESCRIPTION:
{disease.get('description', 'No description')}

⚠️ SYMPTOMS:
"""

        for symptom in disease.get('symptoms', [])[:7]:
            details += f"• {symptom}\\n"

        details += f"""
💊 TREATMENTS:
"""

        for treatment in disease.get('treatments', [])[:5]:
            details += f"• {treatment}\\n"

        details += f"""
🔺 SEVERITY: {disease.get('severity', 'N/A')}
🔄 REVERSIBILITY: {disease.get('reversibility', 'N/A')}
📸 IMAGES: {disease.get('image_count', 0)} photos
"""

        self.disease_details.insert(1.0, details)
        self.disease_details.config(state=tk.DISABLED)

    def open_disease_folder(self):
        """Apri cartella malattia in Explorer"""
        if self.diseases_tree is None:
            return

        selection = self.diseases_tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a disease!")
            return

        item = self.diseases_tree.item(selection[0])
        disease_name = item['values'][0]

        disease_dir = Path("data/images") / disease_name
        disease_dir.mkdir(parents=True, exist_ok=True)

        if os.name == 'nt':
            os.startfile(str(disease_dir))
        else:
            os.system(f'xdg-open "{disease_dir}"')

        self.status_var.set(f"📁 Opened folder: {disease_name}")

    # Funzioni export e statistiche
    def update_statistics(self):
        """Aggiorna statistiche complete"""
        if self.stats_text is None:
            return

        self.stats_text.delete(1.0, tk.END)

        total_diseases = len(self.diseases)
        total_images = sum(self.count_images(d.get('name', ''))
                           for d in self.diseases.values())

        # Raggruppa per categoria
        categories = {}
        images_per_disease = {}

        for disease in self.diseases.values():
            name = disease.get('name', '')
            category = disease.get('category', 'Unknown')
            image_count = self.count_images(name)

            categories[category] = categories.get(category, 0) + 1
            images_per_disease[name] = image_count

        stats = f"""📊 ORTOIOT-AI DATASET STATISTICS
{'='*60}

📈 OVERVIEW:
Total Diseases: {total_diseases}
Total Images: {total_images}
Average Images per Disease: {total_images/max(total_diseases, 1):.1f}

📂 BY CATEGORY:
"""

        for category, count in sorted(categories.items()):
            stats += f"{category}: {count} diseases\\n"

        stats += f"""
📸 IMAGES PER DISEASE:
"""

        for name, count in sorted(images_per_disease.items(), key=lambda x: x[1], reverse=True):
            stats += f"{name}: {count} images\\n"

        stats += f"""
✅ DATASET QUALITY ASSESSMENT:
"""

        with_images = sum(1 for c in images_per_disease.values() if c > 0)
        well_represented = sum(
            1 for c in images_per_disease.values() if c >= 10)
        excellent = sum(1 for c in images_per_disease.values() if c >= 20)

        stats += f"Diseases with images: {with_images}/{total_diseases}\\n"
        stats += f"Well-represented (10+ images): {well_represented}/{total_diseases}\\n"
        stats += f"Excellent (20+ images): {excellent}/{total_diseases}\\n\\n"

        if total_images >= 200:
            stats += "🟢 EXCELLENT dataset size for ML training!\\n"
        elif total_images >= 100:
            stats += "🟡 GOOD dataset size for ML training\\n"
        elif total_images >= 50:
            stats += "🟡 DECENT dataset, consider adding more images\\n"
        else:
            stats += "🔴 SMALL dataset, add more images for better results\\n"

        stats += f"""
💡 RECOMMENDATIONS:
• Add more images to diseases with < 10 photos
• Aim for 20+ images per disease for best results
• Include variety: different lighting, angles, stages
• Good quality photos improve ML performance

🚀 READY FOR EXPORT: {'YES' if total_images >= 50 else 'Add more images first'}
"""

        self.stats_text.insert(1.0, stats)

    def export_csv(self):
        """Export dataset in CSV"""
        try:
            import csv

            export_dir = Path("data/exports")
            export_dir.mkdir(parents=True, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            csv_file = export_dir / f"ortoiot_dataset_{timestamp}.csv"

            with open(csv_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['image_path', 'disease_name',
                                'category', 'severity', 'description'])

                for disease in self.diseases.values():
                    name = disease.get('name', '')
                    category = disease.get('category', '')
                    severity = disease.get('severity', '')
                    description = disease.get('description', '')

                    disease_dir = Path("data/images") / name
                    if disease_dir.exists():
                        for img_file in disease_dir.iterdir():
                            if img_file.suffix.lower() in {'.jpg', '.jpeg', '.png', '.bmp'}:
                                writer.writerow(
                                    [str(img_file), name, category, severity, description])

            messagebox.showinfo("Export Complete",
                                f"✅ CSV exported to:\\n{csv_file}")
            self.status_var.set("✅ CSV export completed")

        except Exception as e:
            messagebox.showerror(
                "Export Error", f"Failed to export CSV: {str(e)}")

    def export_json(self):
        """Export dataset summary in JSON"""
        try:
            export_dir = Path("data/exports")
            export_dir.mkdir(parents=True, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            summary = {
                "dataset_info": {
                    "name": "OrtoIoT-AI Plant Disease Dataset",
                    "version": "1.0",
                    "created": datetime.now().isoformat(),
                    "total_diseases": len(self.diseases),
                    "total_images": sum(self.count_images(d.get('name', '')) for d in self.diseases.values())
                },
                "diseases": []
            }

            for disease in self.diseases.values():
                name = disease.get('name', '')
                summary["diseases"].append({
                    "name": name,
                    "category": disease.get('category', ''),
                    "description": disease.get('description', ''),
                    "severity": disease.get('severity', ''),
                    "image_count": self.count_images(name),
                    "symptoms": disease.get('symptoms', []),
                    "treatments": disease.get('treatments', [])
                })

            json_file = export_dir / f"ortoiot_summary_{timestamp}.json"
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(summary, f, indent=2, ensure_ascii=False)

            messagebox.showinfo("Export Complete",
                                f"✅ JSON exported to:\\n{json_file}")
            self.status_var.set("✅ JSON export completed")

        except Exception as e:
            messagebox.showerror(
                "Export Error", f"Failed to export JSON: {str(e)}")

    def run(self):
        """Avvia applicazione"""
        self.root.mainloop()


def main():
    """Entry point"""
    print("🌱 Starting OrtoIoT-AI Dataset Creator...")
    print("✅ Loading complete disease database...")

    try:
        app = OrtoIoTApp()
        app.run()
    except Exception as e:
        print(f"❌ Error: {e}")
        messagebox.showerror("Error", f"Application error: {str(e)}")


if __name__ == "__main__":
    main()
