# auto-reddit-youtube-shorts
Automatically shares reddit videos on youtube as shorts

# Installition

Create conda environment
```bash
conda env create -f monetizer.yaml
```

# Usage
Set values on config.py as you wish and add it as cronjob to any system that you leave it active.
It will automatically download, re-render and upload the video to youtube.

In first time scenario, you will need to allow google cloud app to access your youtube account.

You can run as follows:
```bash
conda activate monetize
```


```bash
python main.py
```

