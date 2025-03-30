echo "creating virtual env '.venv' "
python -m venv .venv

echo "activating virtual env '.venv'"
source .venv/bin/activate

echo "installing dependencies: "
cat requirements.txt

python -m pip install -r requirements.txt

echo "done"
