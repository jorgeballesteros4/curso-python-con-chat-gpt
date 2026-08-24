@echo off
title Iniciando Cristian AI...
echo =========================================
echo Preparando el entorno para Cristian AI
echo Instalando librerias necesarias...
echo =========================================

pip install -r requirements.txt

echo.
echo =========================================
echo Abriendo la aplicacion en el navegador...
echo =========================================

python -m streamlit run app.py

pause