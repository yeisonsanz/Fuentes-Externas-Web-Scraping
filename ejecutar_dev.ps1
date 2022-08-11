# ejecutar desde cualquier ubicacion ya que tiene rutas absolutas
$locationdir = $MyInvocation.MyCommand.Path
$dir = Split-Path $locationdir

Push-Location $dir

venv\Scripts\Activate.ps1

Set-Location externalSources\projects\sancionesejec\scrapyEjecutariadas\

scrapyrt -i 0.0.0.0 -p 80

Pop-Location