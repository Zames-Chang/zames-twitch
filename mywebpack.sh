#!/bin/sh
# use js please
# index.pug -> index.html
index_path="template/index/pug/index.pug"
index_path_ouput="static/index/index.html"
# register.pug -> register.html
register_path="template/registration/pug/register.pug"
register_path_ouput="static/registration/register.html"



pypugjs -c django $register_path $register_path_ouput
pypugjs -c django $index_path $index_path_ouput
