#This code required python 3

virtualenv -p python3 myenv
source myenv/bin/activate
pip install -r ./requirments.txt

# for playing game needs to run server first:
    python api.py
# then:
    python play_hangman.py