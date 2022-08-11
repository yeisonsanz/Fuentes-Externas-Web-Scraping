# primero ubicarse en la carpeta principal del proyecto
$locationdir = $MyInvocation.MyCommand.Path
$dir = Split-Path $locationdir

Push-Location $dir

python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
xcopy .\resources.py .\venv\Lib\site-packages\scrapyrt\
xcopy .\default_settings.py .\venv\Lib\site-packages\scrapyrt\conf\

Get-Location

Pop-Location
