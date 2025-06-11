# OrtoIoT-AI Dataset Creator

Professional tool for creating high-quality plant disease datasets for machine learning applications.

![License](https://img.shields.io/badge/license-MIT-green.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Status](https://img.shields.io/badge/status-stable-brightgreen.svg)

## Features

### Easy Dataset Creation
- **Zero external dependencies** - Works with Python built-in libraries only
- **15+ pre-loaded diseases** with professional descriptions
- **Simple photo management** - Browse, select, save workflow
- **Automatic organization** - Photos sorted by disease type
- **Professional export formats** - CSV, JSON ready for ML training

### Complete Disease Database
Pre-loaded with **15 professionally documented plant diseases**:

#### Fungal Diseases
- **Powdery Mildew** - White powdery substance on leaves
- **Gray Mold (Botrytis)** - Dangerous flowering stage fungus
- **Root Rot** - Fungal root system damage
- **Black Rot** - Black spots spreading to stems and roots

#### Pests
- **Spider Mites** - Small arachnids causing leaf damage
- **Aphid Infestation** - Sap-sucking insects forming colonies
- **Caterpillar Infestation** - Larvae eating leaves and buds
- **Thrips** - Tiny insects scraping leaf surfaces

#### Nutritional Deficiencies
- **Nitrogen Deficiency** - Essential growth nutrient shortage
- **Calcium Deficiency** - Cell structure nutrient problems
- **Magnesium Deficiency** - Chlorophyll component shortage

#### Cultivation Errors
- **Nutrient Burn** - Excess fertilizer damage
- **Nutrient Lockout** - pH-related absorption problems
- **Overwatering** - Root oxygen deprivation

#### Reference
- **Healthy Plant** - Disease-free reference state

Each disease includes:
- Professional description
- Detailed symptoms list (5-7 symptoms each)
- Treatment recommendations (5+ treatments each)
- Severity assessment
- Recovery potential

### Photo Management

#### Simple 3-Step Process:
1. **Browse Photos** - Single or multiple selection
2. **Choose Disease** - Select from dropdown menu
3. **Save Photos** - Automatic organization and naming

#### Advanced Features:
- **Automatic file naming** with timestamps and unique IDs
- **Duplicate handling** - No overwrites
- **Format support** - JPG, PNG, BMP, TIFF
- **Size statistics** - Track file sizes and formats
- **One-click folder access** - Open disease folders in Explorer

### Professional Export & Statistics

#### Export Formats:
- **CSV Export** - Complete dataset with metadata
- **JSON Summary** - Structured data with all disease info
- **Statistics Dashboard** - Dataset quality assessment

#### Quality Metrics:
- **Dataset completeness** - Images per disease tracking
- **Quality assessment** - Automatic recommendations
- **Category distribution** - Balanced dataset insights
- **Export readiness** - ML training preparation status

## Quick Start

### Prerequisites
- **Python 3.8+** (that's it!)
- **Windows, macOS, or Linux**

### Installation & Setup

#### Option 1: Simple Download & Run
```bash
# Download/clone the repository
git clone https://github.com/ortoiot/ortoiot-ai.git
cd ortoiot-ai

# Run directly (no dependencies needed!)
python app.py
```

#### Option 2: With Virtual Environment (Recommended)
```bash
# Clone repository
git clone https://github.com/ortoiot/ortoiot-ai.git
cd ortoiot-ai

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Unix/Linux/Mac:
source venv/bin/activate

# Run application
python app.py
```

#### Option 3: Windows Launcher
```bash
# Double-click
launch.bat
```

### First Run
1. **Launch the app** - 15 diseases are automatically loaded
2. **Go to "Add Photos" tab**
3. **Click "Browse Multiple Photos"**
4. **Select your images**
5. **Choose disease from dropdown**
6. **Click "Save Photos"** - Done!

## User Guide

### Disease Database Tab
- **Browse diseases** - Click any disease to see full details
- **View statistics** - See image counts per disease
- **Update counts** - Refresh image statistics
- **Open folders** - Direct access to image directories

### Add Photos Tab
- **Browse Single Photo** - Add one image at a time
- **Browse Multiple Photos** - Bulk image import
- **Photo preview** - See selected files and statistics
- **Disease selection** - Choose target disease from dropdown
- **Save photos** - Automatic organization and renaming

### Export Dataset Tab
- **View statistics** - Complete dataset overview
- **Quality assessment** - Readiness for ML training
- **Export CSV** - Complete dataset with metadata
- **Export JSON** - Structured summary format

### Documentation Tab
- **User guide** - How to use the application
- **Disease reference** - Complete disease list
- **Tips & tricks** - Best practices for dataset creation

## Project Structure

```
ortoiot-ai/
├── app.py                  # Main application (single file!)
├── requirements.txt        # Dependencies (minimal)
├── config.json            # Configuration
├── launch.bat             # Windows launcher
├── README.md              # This documentation
├── data/
│   ├── diseases/          # Disease database
│   │   └── diseases.json  # Complete disease information
│   ├── images/            # Training images (organized by disease)
│   │   ├── Powdery_Mildew/
│   │   ├── Spider_Mites/
│   │   ├── Nitrogen_Deficiency/
│   │   └── ... (15 disease folders)
│   └── exports/           # Dataset exports
│       ├── ortoiot_dataset_YYYYMMDD_HHMMSS.csv
│       └── ortoiot_summary_YYYYMMDD_HHMMSS.json
└── logs/                  # Application logs
```

## Workflow Example

### Creating Your First Dataset:

1. **Start the application**
   ```bash
   python app.py
   ```

2. **Add photos for Powdery Mildew**
   - Go to "Add Photos" tab
   - Click "Browse Multiple Photos"
   - Select 20 powdery mildew photos
   - Choose "Powdery Mildew" from dropdown
   - Click "Save Photos"

3. **Repeat for other diseases**
   - Spider Mites, Aphids, etc.
   - Aim for 10-20+ photos per disease

4. **Check your progress**
   - Go to "Disease Database" tab
   - See image counts updated automatically

5. **Export your dataset**
   - Go to "Export Dataset" tab
   - Click "Update Statistics"
   - When ready, click "Export CSV"

## Dataset Quality Guidelines

### Recommended Image Counts:
- **20+ images per disease** - Excellent for ML training
- **10-19 images per disease** - Good for basic training
- **<10 images per disease** - Add more for better results

### Photo Quality Tips:
- **Good lighting** - Clear, well-lit images
- **Multiple angles** - Different perspectives of symptoms
- **Various stages** - Early, mid, and late stage symptoms
- **Clean backgrounds** - Focus on the plant/disease
- **High resolution** - At least 224x224 pixels for ML

## Technical Details

### Dependencies
- **Core**: Python 3.8+ built-in libraries only
- **GUI**: tkinter (included with Python)
- **File Operations**: os, shutil, pathlib (built-in)
- **Data**: json, uuid, datetime (built-in)

### Supported Image Formats
- **JPEG** (.jpg, .jpeg)
- **PNG** (.png)
- **BMP** (.bmp)
- **TIFF** (.tiff, .tif)

### Export Formats
- **CSV**: Complete dataset with image paths and metadata
- **JSON**: Structured summary with disease information
- **COCO**: Coming soon
- **YOLO**: Coming soon

## Community & Support

- **Website**: [www.ortoiot.com](https://www.ortoiot.com)
- **Discord**: [Join our community](https://discord.gg/nYakDDmE5s)
- **Email**: info@ortoiot.com
- **Issues**: [GitHub Issues](https://github.com/ortoiot/ortoiot-ai/issues)

## Contributing

We welcome contributions! Here's how to get started:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
4. **Test thoroughly**
5. **Commit your changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```
6. **Push to your branch**
   ```bash
   git push origin feature/amazing-feature
   ```
7. **Open a Pull Request**

### Development Setup
```bash
git clone https://github.com/ortoiot/ortoiot-ai.git
cd ortoiot-ai
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
python app.py
```

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## Citation

If you use OrtoIoT-AI Dataset Creator in your research, please cite:

```bibtex
@software{ortoiot_ai_2025,
  title={OrtoIoT-AI Dataset Creator},
  author={OrtoIoT Team},
  year={2025},
  url={https://github.com/ortoiot/ortoiot-ai},
  version={1.0.0},
  license={MIT}
}
```

## Roadmap

### Current Version (v1.0.0)
- 15 pre-loaded diseases
- Easy photo management
- CSV/JSON export
- Professional UI
- Zero external dependencies

### Coming Soon (v1.1.0)
- COCO format export
- YOLO format export
- Image annotation tools
- Batch image processing
- Quality validation

### Future (v2.0.0)
- Web-based interface
- Cloud storage integration
- Real-time collaboration
- ML model training integration
- Mobile app companion

## Statistics

- **Purpose**: Plant disease dataset creation for AI/ML
- **Target**: Researchers, developers, agricultural professionals
- **Scope**: 15+ plant diseases with comprehensive information
- **Platform**: Cross-platform (Windows, macOS, Linux)
- **Performance**: Lightweight, fast, zero external dependencies

## Acknowledgments

- **OrtoIoT Team** - Core development
- **Plant pathology experts** - Disease information validation
- **Open source community** - Inspiration and feedback
- **Agricultural researchers** - Use cases and requirements

---

**Built with care by the OrtoIoT Team**

*Advancing precision agriculture through AI innovation*

**Ready to create professional plant disease datasets for machine learning research.**