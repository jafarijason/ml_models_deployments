# ml_models_deployments

## for windows please use [wsl](https://learn.microsoft.com/en-us/windows/wsl/install)

## general installation
```
curl https://pyenv.run | bash
# or
curl https://pyenv.run | zsh
```

## For zsh
```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```


## [pyenv on mac](https://github.com/pyenv/pyenv?tab=readme-ov-file#getting-pyenv)

## On ubuntu
```
# https://github.com/pyenv/pyenv/issues/2888
sudo apt install build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

```
pyenv install 3.12.3
pyenv install 3.10
```

```
pyenv versions
```

```
pyenv global 3.12.3
```

## How to install virtualenv

```
pip install virtualenv
```

## Use vireualevn
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Fast api development
```
fastapi dev main.py
```

##
```
uvicorn main:app --host=0.0.0.0 --port=${PORT:-9900}
```

## if you install new dependency run this command and commit your code
```
pip freeze > requirements.txt
```

## Run Jupyter notebooks
```
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
jupyter notebook \
        --notebook-dir="./notebooks" \
        --ip=0.0.0.0 --port=3225
```

# deploy serverless
```
# https://www.deadbear.io/simple-serverless-fastapi-with-aws-lambda/amp/

pip install mangum

```

## heroku
```
heroku login

git push heroku master
```
