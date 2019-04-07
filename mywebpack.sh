#!/bin/sh
register_path="template/register/pug/register.pug"
register_path_ouput="static/register/register.html"



pypugjs -c django $register_path $register_path_ouput