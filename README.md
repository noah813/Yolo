# YOLO Tennis Ball Tracker

This repository provides a YOLO-based model for tracking tennis balls in videos, with pre-trained models and sample videos to get started quickly.

<center><img src="https://github.com/noah813/Yolo/blob/main/.github/images/Processed_Match.gif" width="100%"></center>

## Getting Started

Follow these steps to set up and run the project:

### 1. Clone the Repository

```bash
git clone https://github.com/noah813/Yolo.git
```

### 2. Install PyTorch

For installation instructions tailored to your environment, visit the official PyTorch installation guide:  
[PyTorch Installation Guide](https://pytorch.org/get-started/locally/)

<center><img src="https://raw.githubusercontent.com/noah813/Yolo/refs/heads/main/.github/images/Screenshot%202024-10-23%20at%203.02.41%E2%80%AFPM.png"></center>

### 3. Install Dependencies

Once PyTorch is set up, install the required dependencies by running:

```bash
pip install -r requirements.txt
```

### 4. Add Assets

Download the sample assets, including pretrained models and input videos, and place them in the `assets` folder:

[Download Sample Assets](https://drive.google.com/drive/folders/1xtU5YQ5dqT_gsFislNT9TBftjY-ZTuKs?usp=share_link)

### 5. Run the Tracker

Execute the following command to start the tracker:

```bash
python main.py <args>
```

## Arguments

You can specify the following arguments when running the script:

- `path_ball_track_model`: Path to the pretrained ball tracking model.
- `path_court_model`: Path to the pretrained court detection model.
- `path_bounce_model`: Path to the pretrained bounce detection model.
- `path_input_video`: Path to the input video file.
- `path_output_video`: Path to save the output video.