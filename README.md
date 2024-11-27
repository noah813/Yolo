# Start
1. Clone this repository

```bash
git clone https://github.com/noah813/Yolo.git
```

2. Install pytorch visit [pytorch install](https://pytorch.org/get-started/locally/)
3. Install the requirements

```bash
pip install -r requirements.txt
```
4. Put/install pretrained models/input videos into assets folder

[download sample assets](https://drive.google.com/drive/folders/1xtU5YQ5dqT_gsFislNT9TBftjY-ZTuKs?usp=share_link)

5. run

```bash
python main.py <args>
```

# Arguments
- ```path_ball_track_model```
- ```path_court_model```
- ```path_bounce_model```
- ```path_input_video```
- ```path_output_video```