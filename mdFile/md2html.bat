@echo off
for /f  %%a in ('dir /a /b E:\github\icesdy115.github.io\mdFile\*.md') do ( 
    python md2html.py E:\github\icesdy115.github.io\mdFile\%%a  .\html\%%a.html
)
