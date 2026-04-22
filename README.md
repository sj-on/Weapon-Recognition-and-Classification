# Weapon Recognition and Classification

**A Darknet & YOLO-based tool for real-time security and law enforcement.**

This tool is designed to assist law enforcement and security personnel in identifying potentially dangerous situations by detecting firearms in images and video feeds. While initially developed for manual image processing, the open-source nature of the project allows it to be extended for real-time CCTV integration.

### Key Features

  * **Optimized for Low-Res:** Specially trained to handle low-resolution input, making it ideal for standard CCTV footage.
  * **YOLO & Darknet Powered:** Utilizes a custom-trained model for high-speed, accurate detection.
  * **Open Source:** Fully customizable source code for real-time weapon classification updates.

-----

### 🚀 Getting Started

#### 1\. Prerequisites

Ensure you have the latest version of **Python** installed on your system.

#### 2\. Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/sj-on/Weapon-Recognition-and-Classification
    ```
2.  **Download the Model Weights:**
    The `.weights` file generated during training is required for the tool to function.
      * [Download `yolo_weapon_weights.weights` here]([https://drive.google.com/file/d/17z3LOJDlKkTxkcryidLWWZ3DeIRtTlXc/view%3Fusp%3Dsharing](https://drive.google.com/file/d/17z3LOJDlKkTxkcryidLWWZ3DeIRtTlXc/view?usp=sharing))
      * Place the downloaded file in the root directory of the project.

#### 3\. Usage

1.  Open your Terminal or Command Prompt in the project directory.
2.  Run the main script:
    ```bash
    python main.py
    ```
3.  **Important:** When the program prompts for file locations, you must provide **absolute paths**. Relative paths are not supported.

-----

### 📺 Video Guides

| Content | Video Link |
| :--- | :--- |
| **Model Training & Building** | [Training](https://youtu.be/RPXL25qcutw) |
| **Testing & Results** | [Testing](https://youtu.be/KkErB0YqrEA) |
| **How to Use This Tool** | [Tutorial Guide](https://youtu.be/ngtDlQcDhfw) |

-----

### Contributing

We welcome contributions\! If you have ideas for improving the detection accuracy or porting this to a real-time streaming framework, feel free to fork the repo and submit a PR.

**Thanks and Regards,**  
*sj-on and The Team*
